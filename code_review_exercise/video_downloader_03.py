import json
import re
import subprocess
import requests
import traceback
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def run():
    base_url = input("Your Course Link: ")
    
    url_match = re.search(r'/community/learning/(?:courses|tutorials)/([^/]+)', base_url)
    if not url_match:
        print("Invalid URL format")
        return
        
    course_id = url_match.group(1)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        try:
            print("Navigating to base URL...")
            page.goto(base_url, timeout=60000)
            page.wait_for_timeout(10000)
        except PlaywrightTimeoutError as e:
            print(f"Failed to load base URL: {e}")
            return
        except Exception as e:
            print(f"Error loading base URL: {e}")
            return
        
        anchors = page.query_selector_all("a")
        module_links = []
        
        for a in anchors:
            href = a.get_attribute("href")
            if href and f"/{course_id}/" in href and not href.endswith("/new"):
                full_url = href if href.startswith("http") else "https://dev.epicgames.com" + href
                if full_url not in module_links:
                    module_links.append(full_url)
                    
        print("**********Module Links**********")
        for link in module_links:
            print(link)
        print("********************************")
        # Get the video index
        start_link = int(input("From which video you want to download: "))

        for link in module_links[start_link:]:
            try:
                module_name = link.rstrip('/').split('/')[-1]
                print(f"\n--- Processing: {module_name} ---")
                print(f"Navigating to module page: {link}")
                
                page.goto(link, timeout=60000)
                page.wait_for_timeout(10000)
                
                iframe_element = page.query_selector("iframe[src*='embed']")
                if not iframe_element:
                    print(f"Error: Unable to locate iframe element on page for {module_name}. Moving to next module.")
                    continue
                    
                embed_src = iframe_element.get_attribute("src")
                print(f"Found Embed source: {embed_src}")
                print(f"Navigating to Embed source...")

                page.goto(embed_src, timeout=60000)
                page.wait_for_load_state("networkidle", timeout=60000)
                page.wait_for_timeout(5000)

                content = page.content()
                
                qsep_match = re.search(r'(qsep://[^"\'\s]+)', content)
                
                if qsep_match:
                    print(f"Match found for qsep stream.")
                    raw_url = qsep_match.group(1)
                    http_url = raw_url.replace("qsep://", "https://")
                    
                    print(f"Requesting JSON payload from: {http_url}")
                    response = requests.get(http_url, timeout=15)
                    if response.status_code == 200:
                        try:
                            data = response.json()
                            video_hash = data.get("playlist", "")
                            
                            if video_hash:
                                dash_url = f"data:application/dash+xml;base64,{video_hash}"
                                print(f"Hash successfully extracted. Initializing yt-dlp download...")
                                subprocess.run([
                                    "yt-dlp",
                                    dash_url,
                                    "-o", f"{module_name}.mp4",
                                    "--progress",
                                    "--console-title"
                                ])
                            else:
                                print(f"Error: Hash missing from JSON response for {module_name}")
                        except json.JSONDecodeError:
                            print(f"Error: Failed to parse JSON response for {module_name}")
                    else:
                        print(f"Error: Failed to fetch CDN URL, HTTP Status {response.status_code}")
                else:
                    print(f"Error: Could not find qsep:// link in embed HTML for {module_name}")
                    
            except PlaywrightTimeoutError:
                print(f"Timeout Error during {module_name} processing. Skipping to next.")
            except Exception as e:
                print(f"Unhandled Exception during {module_name} processing:")
                traceback.print_exc()
                
        print("Closing browser context...")
        browser.close()

if __name__ == "__main__":
    run()