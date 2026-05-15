# Level 2: Intermediate File Handling - Data Processing and Appending
# This script reads a file, counts the frequency of each word, and appends the result to another file.

input_file = "level2_data.txt"
output_file = "level2_summary.txt"

word_counts = {}

print(f"--- Processing {input_file} ---")
with open(input_file, 'r') as file:
    for line in file:
        word = line.strip().lower() # Remove whitespace and convert to lowercase
        # print(word)
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        print(word_counts)

print(f"--- Appending results to {output_file} ---")
# Using 'a' mode to append to the file instead of overwriting
with open(output_file, 'a') as file:
    file.write("\n--- New Word Count Summary ---\n")
    for word, count in word_counts.items():
        file.write(f"{word.capitalize()}: {count}\n")
        print(f"{word.capitalize()}: {count}")

print("Done!")
