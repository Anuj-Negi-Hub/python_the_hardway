# DITA Technical Reference Setup

This document provides a comprehensive overview of the DITA Technical Reference project, focusing on the implementation of **Indirect Addressing** (Keys) and the use of the **DitaCraft** VS Code extension for advanced documentation management.

## 1. Project Architecture

The project is structured to support scalable, modular documentation using DITA 1.3 standards.

### Key Files
- **[tech-reference.bookmap](file:///d:/editors_vault/starting_dita/tech-reference.bookmap)**: The main entry point that defines the hierarchy and book structure.
- **[keys.ditamap](file:///d:/editors_vault/starting_dita/keys.ditamap)**: The central registry for all topic keys.
- **[tech_ref/](file:///d:/editors_vault/starting_dita/tech_ref/)**: Contains the source DITA topics (Concepts, Tasks, References).

---

## 2. Reference Tags & Addressing
The project has been refactored to use **Indirect Addressing**, which decouples the navigation hierarchy from physical file paths.

### The Problem Solved: Maintenance & Portability
Without keys, every file path is hardcoded into the bookmap. If you move a file or rename a folder, your entire project breaks. 
By moving paths to the **Keys Map**, you create a "Redirect Table."
*   **Decoupling**: The Bookmap defines the *Structure*. The Keysmap defines the *Location*.
*   **Version Control**: You can point the same key (`intro`) to `v1/intro.dita` or `v2/intro.dita` just by changing one line in the map.

---

## 3. How DITA Works: Meaning vs. Appearance
A common question is: *How does a tag like `<title>` turn into a bold heading in English?*

### Structure (What it is)
In DITA, you focus on the **meaning** of the content, not how it looks. When you use a tag like `<section>` or `<note type="tip">`, you are labeling the data. 

### Transformation (How it looks)
To see the final result, the XML goes through a **Publishing Engine** (like the DITA Open Toolkit). This engine uses a set of rules to "translate" the tags:
1.  **Rule 1**: Take any `<title>` inside a `<chapter>` and make it a large, bold header.
2.  **Rule 2**: Take any `<note>` and add a specific icon (like a lightbulb or warning sign) based on the "type" attribute.
3.  **Rule 3**: Take the `<shortdesc>` and use it for the hover-preview in the table of contents.

### The Benefit: Instant Re-styling
Because the "Look" is separate from the "Meaning," you can change the design of your entire 500-page manual by updating just one style file. You never have to manually format a heading again.

**Project Implementation**: 
I have added a [custom_style.css](file:///d:/editors_vault/starting_dita/custom_style.css) to this project. It specifically targets IDs like `#semantic_tagging` and tags like `<keyword>` to change their color and layout without touching the XML content.

---

### Core Attributes
- **`keyref`**: Used in maps/topics to point to a resource.
- **`href`**: The actual physical path (now isolated in the keysmap).

---

## 4. Content Reuse (Transclusion)
DITA allows you to "pull" pieces of content from one file into another. This is called **Content Referencing**.

### Conref (Direct)
Pulls content from a specific file path.
```xml
<!-- Hardcoded path -->
<note conref="warehouse.dita#warehouse/voltage_warning"/>
```

### Conkeyref (Indirect - Best Practice)
Pulls content using a Key. If the "warehouse" file changes location, you only update the key definition.
```xml
<!-- Symbolic key 'warehouse' -->
<note conkeyref="warehouse/voltage_warning"/>
```

---

## 5. DitaCraft Integration
The **DitaCraft** VS Code extension is utilized to provide IDE-like features for this XML project:

- **Smart Navigation**: `Ctrl + Click` on any `keyref` or `href` to jump directly to the target.
- **Key Space Explorer**: Automatically indexes the `keys.ditamap` to provide autocomplete and validation for keys.
- **Peek Definition**: Allows viewing the content of a `conref` or `keyref` target in a small overlay window.
- **Real-time Validation**: Ensures all references are resolved and compliant with DITA schemas.

---

## 6. Topics Catalog

| Topic Key | File Path | Type | Description |
| :--- | :--- | :--- | :--- |
| `dita_briefing` | `tech_ref/dita_briefing.dita` | Concept | Guide to DITA addressing and reference tags. |
| `preface` | `tech_ref/preface.dita` | Topic | Introduction and target audience details. |
| `intro` | `tech_ref/getting_started_intro.dita` | Concept | Foundation for the Technical Reference. |
| `requirements` | `tech_ref/requirements.dita` | Reference | System hardware and software specs. |
| `advanced_config` | `tech_ref/advanced_config.dita` | Task | Steps for modifying system parameters. |
| `error_codes` | `tech_ref/error_codes.dita` | Reference | Troubleshooting and resolution table. |

---

## 7. Usage Example (Bookmap)
The following snippet shows how the bookmap leverages the keys map:

```xml
<frontmatter>
    <mapref href="keys.ditamap" processing-role="resource-only"/>
    <preface keyref="preface"/>
</frontmatter>

<chapter keyref="dita_briefing"/>
<chapter keyref="intro">
    <topicref keyref="requirements"/>
</chapter>
```

---

## 8. AI-Assisted Generation
Integrating AI into DITA helps bridge the gap between "rough ideas" and "perfectly structured code."

### Turning Notes into Topics
Instead of writing XML from scratch, you can feed an AI (like Claude or GPT) your raw notes or a transcript. 
*   **The Workflow**: Give the AI a template for a DITA "Task" or "Concept."
*   **The Result**: The AI generates a valid `.dita` file with the correct tags (`<steps>`, `<context>`, etc.), saving you from manual tagging.

### Automated Summaries (`shortdesc`)
DITA relies heavily on the "Short Description" tag for hover-previews and SEO.
*   **AI Speed**: AI can read your entire topic and write a one-sentence summary that fits perfectly in the `<shortdesc>` tag. This ensures consistency across hundreds of files.

### Smart Tagging (Keywords)
Adding metadata (keywords and categories) is often skipped because it's tedious.
*   **The Solution**: AI can analyze your text and suggest specific "Keywords" to add to the topic's metadata, making your documentation much easier to search.

---

## 9. Increasing Code Creation Speed
Writing DITA XML can be slow because of its strict rules. Here is how to speed it up:

### Map-Driven Boilerplates
Instead of creating files one-by-one, use a script or AI to look at your **Bookmap**.
*   **Instant Setup**: If your Bookmap says you need 10 new chapters, the system can automatically create those 10 empty `.dita` files with the correct headers, so you can start writing immediately.

### Custom Code Snippets (Shortcuts)
In VS Code, you can set up "Snippets."
*   **How it works**: You type a short word like `dnote` and hit `Tab`. 
*   **The Result**: It expands into a full, complex piece of code: `<note type="important">Your text here</note>`. This eliminates the need to remember exact tag names.

### AI-Powered "Content Discovery"
The biggest time-sink in DITA is finding content you've already written to reuse it.
*   **Dynamic Suggestions**: While you are typing, an AI co-pilot can look through your "Warehouse" (reusable parts) and say: *"Hey, you already wrote a safety warning for high voltage. Would you like to pull it in here?"* 
*   **Technique**: This uses **Conkeyref** (see Section 3) automatically so you never write the same warning twice.

---

## 10. Choosing the Right Tool: DITA Topic Types
In DITA, you don't just write "pages." You choose a specific **Topic Type** based on what the user needs to achieve. This solves the problem of "cluttered" documentation where instructions and definitions are mixed together.

### 1. Concept (`<concept>`)
*   **The Problem**: Users often don't understand the "Why" behind a feature before they try to use it.
*   **The Solution**: Use a Concept for background information, definitions, and theory. It answers the question: *"What is this?"*
*   **Example**: [ai_generation.dita](file:///d:/editors_vault/starting_dita/tech_ref/ai_generation.dita) is a concept because it explains how AI works in DITA.

### 2. Task (`<task>`)
*   **The Problem**: Users get lost in long paragraphs when they just want to know how to finish a job.
*   **The Solution**: A Task provides numbered steps (`<steps>`), commands (`<cmd>`), and expected results. It answers the question: *"How do I do this?"*
*   **Example**: [speed_optimization.dita](file:///d:/editors_vault/starting_dita/tech_ref/speed_optimization.dita) is a task because it gives you steps to set up snippets.

### 3. Reference (`<reference>`)
*   **The Problem**: Technical data (like error codes or hardware specs) should be easy to scan, not buried in sentences.
*   **The Solution**: A Reference topic is designed for tables, lists, and properties. It answers the question: *"What are the facts?"*
*   **Example**: [requirements.dita](file:///d:/editors_vault/starting_dita/tech_ref/requirements.dita) is a reference topic focusing on hardware specifications.

---

## 11. Advanced Concepts to Explore
Once you master the basics, these "Pro" features help you manage massive amounts of content.

### Conditional Processing (Filtering)
*   **The Problem**: You have two versions of a product (Basic and Pro), but you don't want to maintain two separate manuals.
*   **The Solution**: You can tag content with attributes like `audience="pro"` or `product="basic"`. When you publish, you use a **DITAVAL file** to tell DITA: *"Hide anything tagged for 'pro' in this version."*

### Relationship Tables (`reltable`)
*   **The Problem**: Manual "See Also" links at the bottom of pages are hard to maintain. If a file moves, the link breaks.
*   **The Solution**: You create a table in your Map that says: *"These three topics are related."* DITA will automatically add links between them at the bottom of the pages during publishing.

### Specialization
*   **The Problem**: Standard DITA tags aren't specific enough for your industry (e.g., Medical or Aerospace).
*   **The Solution**: DITA allows you to create your own tags (like `<surgical-step>` or `<flight-check>`) that still follow the core DITA rules. This is called Specialization.

---

## 12. Troubleshooting: Why didn't my PDF change?
A common point of confusion is seeing a beautiful layout in the VS Code preview but a plain-looking PDF. 

*   **Preview vs. Print**: The `custom_style.css` file we created is for the **Live Preview** (the web-based view). 
*   **The PDF Engine**: PDF generation uses the **DITA Open Toolkit**. It doesn't look at your editor's CSS. To style a PDF, you would need to create a "PDF Plugin" or a specialized print stylesheet.
*   **The Takeaway**: In DITA, you can have one look for your website and a completely different look for your printed books, all from the same XML files.

---

## 13. DITA as a Universal Standard
DITA is not "owned" by any one company. It is an international standard.
*   **Tool Independence**: You can write a file in VS Code today, and a colleague can open and edit it in **Adobe FrameMaker** or **Oxygen XML** tomorrow. 
*   **FrameMaker**: FrameMaker is a powerful tool used for high-end DITA publishing. It "speaks" the same DITA language as VS Code, but offers more advanced features for professional book layout.
*   **Investment Protection**: Because you are using a standard, your documentation is never "locked" into a specific piece of software.

---

## 14. Standard DITA Topic Types
You don't need to invent tags for most scenarios. DITA comes with these "Standard" types pre-installed:
*   **Topic**: The generic starting point.
*   **Concept**: For explanations ("What is...?").
*   **Task**: For instructions ("How to...?").
*   **Reference**: For technical facts (Tables, Specs).
*   **Troubleshooting**: For resolving issues (Condition, Cause, Remedy).
*   **Glossary**: For defining industry terms.

---

## 15. The Process: Creating Your Own "Custom Tags"
Since you cannot simply "make up" a new tag in DITA without complex technical setup, we use a process called **Attribute-Based Specialization**. This allows you to create a custom identity while following the standard rules.

### Step 1: Choose the "Base Block"
Identify the standard DITA tag that behaves most like your new idea.
*   If you want a **Callout Box** -> use `<note>`.
*   If you want a **Badge** or **Colored Text** -> use `<ph>` (phrase).
*   If you want a **Custom Section** -> use `<section>`.

### Step 2: Give it a "Identity" (The Sticker)
Use the `outputclass` attribute to give your tag a unique nickname.
```xml
<!-- This is now an "AI Label" instead of just a note -->
<note outputclass="ai-label">This is the content.</note>

<!-- This is now a "New Badge" instead of just a phrase -->
<ph outputclass="badge-new">V2.0</ph>
```

### Step 3: Define the "Look"
Open your `custom_style.css` and create a rule for that specific nickname. 
*   **Selector Tip**: Use a period before the nickname (e.g., `.ai-label`).
*   **Automatic Text**: Use the `:before` rule to add text or icons automatically so you don't have to type them every time.

### Why this works:
*   **Validation**: Your file remains "Valid DITA." Every tool in the world will understand it as a `<note>`.
*   **Searchability**: You can search your entire project for every instance of `outputclass="ai-label"` to review your AI-drafted content.
*   **Compatibility**: This content can be opened in Adobe FrameMaker or Oxygen XML without any errors.

---

---

## 16. The "Old Way": Structural Specialization (DTD)
Before the simplified `outputclass` method became popular, the only way to create custom tags was to modify the **Document Type Definition (DTD)**. This is a more technical approach used for strict enforcement.

### The Component Files
To create a real tag like `<ai-warning>`, you need three files:
1.  **Entity File (`.ent`)**: Names the tag and registers it in the system.
2.  **Module File (`.mod`)**: Defines the rules (e.g., what can go inside the tag) and its **Heritage**.
3.  **Heritage (The `class` attribute)**: Every specialized tag must have a hidden `class` attribute. For example, an `<ai-warning>` based on a `<note>` would have: `class="- topic/note ai-d/ai-warning "`. This ensures that any DITA tool in the world knows it is "a type of note."

### Comparison: Which should you use?

| Feature | `outputclass` (Sticker) | DTD Specialization (DNA) |
| :--- | :--- | :--- |
| **Setup Time** | 1 Minute | 1 Hour+ |
| **Enforcement** | Loose (can misspell) | **Strict** (Editor shows error) |
| **Autocomplete** | No | **Yes** (Appears in dropdown) |
| **Learning Curve** | Low | High |

---

## 17. Common DITA Validation Pitfalls (Debugging DOTJ088E)
When building a DITA project, you will often encounter "Parsing Errors" (Error Code `DOTJ088E`). These happen because DITA enforces very strict rules about the order of information.

### 1. The Bookmap Order Rule
*   **The Rule**: In a `bookmap`, all `<chapter>` elements must be listed **before** any `<part>` elements.
*   **The Trap**: If you add a "Reference" chapter at the very end of your book after an "Advanced" part, the validator will fail.

### 2. The `conbody` Nesting Rule
*   **The Rule**: In a Concept topic, all basic blocks (like `<p>`, `<ul>`, or `<image>`) must come at the top of the body. Once you start a `<section>`, you cannot add a "loose" paragraph afterward.
*   **The Trap**: Adding a "Next Steps" paragraph at the bottom of a topic that already contains sections. 
*   **The Fix**: Wrap that final paragraph in its own `<section>`.

### 3. The Table Placeholder Rule
*   **The Rule**: A `<table>` tag is considered "incomplete" if it doesn't contain at least one `<tgroup>` (the grid definition).
*   **The Trap**: Using `<table conkeyref="..."/>` as an empty tag. Some validators will error before they even try to pull in the content.
*   **The Fix**: Always include a "stub" or placeholder `<tgroup>` inside the table, even if it will be replaced later.

---

## 18. Final Best Practices for Modern DITA
1.  **AI is a Co-Pilot**: Always check AI-generated XML for "validity" (DitaCraft will highlight any errors in red).
2.  **Keep it Modular**: Write small, focused topics. AI handles small chunks of information much better than massive documents.
3.  **Centralize Everything**: Keep your keys in `keys.ditamap`. This allows AI and scripts to easily find where files are located without getting lost in folders.
4.  **Use the Right Type**: Don't put steps in a Concept or definitions in a Task. Keeping them separate makes your content easier for AI to digest and for users to scan.
5.  **Tag for Meaning**: Use `outputclass` to label *what* the content is (e.g., `ai-label`), not how it looks (e.g., `purple-box`). This makes your data "smarter" for the future.
6.  **Follow the Order**: Respect the content models (like `blocks before sections`). DITA is a data standard, not a word processor, so the sequence matters.

---

## 19. Extending DITA-OT: The Plugin Ecosystem
The **DITA Open Toolkit (DITA-OT)** is designed to be extensible. If the standard output (like the default PDF) doesn't meet your needs, you use **Plugins**.

### How Plugins Work
A plugin is a folder in the `DITA-OT/plugins/` directory containing:
- **`plugin.xml`**: The manifest that tells DITA-OT what "Extension Points" to hook into.
- **XSLT/CSS/Ant scripts**: The actual logic that overrides the default behavior.

### Case Study: `com.acolad.imagemap-pdf`
Standard DITA-OT often struggles to render "hotspots" (clickable areas) in PDFs. 
- **The Solution**: This plugin (developed by Acolad/Amplexor) intercepts the PDF generation and overlays an **SVG layer** with the clickable links. 
- **Usage**: You install it via the CLI: `dita --install com.acolad.imagemap-pdf`.

---

## 20. DITA-OT vs. Adobe FrameMaker: Choosing Your Pipeline
Moving from FrameMaker to DITA-OT is a shift from **Desktop Publishing** to **Content Engineering**.

| Feature | DITA-OT (Code-Driven) | Adobe FrameMaker (GUI-Driven) |
| :--- | :--- | :--- |
| **Philosophy** | "Docs-as-Code". You write XSLT/CSS. | Visual Layout. You use menus and templates. |
| **Automation** | Perfect for CI/CD (GitHub/GitLab). | Harder to automate headless builds. |
| **Customization** | Infinite, but requires technical skill. | Deep, but within the "Adobe way." |
| **Cost** | Free (Open Source). | High (Subscription). |

### The Verdict:
Use **DITA-OT** if you have a developer on the team and want automated, standard-based builds. Use **FrameMaker** if your writers need a "What You See Is What You Get" (WYSIWYG) environment and professional print layouts out of the box.

---

## 21. The "Open Source Gap"
There is currently no direct, open-source, GUI-based equivalent to Adobe FrameMaker. 
- **The Reason**: Developing a professional XML editor that "renders" a book visually is incredibly complex and expensive to maintain.
- **The Industry Shift**: Most open-source innovation has moved toward **Docs-as-Code** (writing in plain text) rather than building complex XML editors.

---

## 22. AsciiDoc: The Modern Open-Source Alternative
If DITA feels too "drastic" and FrameMaker is too expensive, **AsciiDoc** is the recommended middle ground. It offers the same single-sourcing power as DITA but uses human-readable plain text.

### Why AsciiDoc?
- **Human-Readable**: You write in text (like Markdown) but have professional features like "Includes" (snippets) and "Attributes" (variables).
- **No XML Pain**: No tags to close, no DTDs to learn.
- **Built for Books**: Specifically designed for technical manuals, unlike standard Markdown.

### Getting Started with AsciiDoc
**1. Download & Install:**
- **CLI**: Install the Ruby-based implementation: `gem install asciidoctor` (requires Ruby).
- **Node.js**: `npm install @asciidoctor/core`.
- **Official Site**: [asciidoctor.org](https://asciidoctor.org/)

**2. VS Code Setup (Recommended):**
- Install the **"AsciiDoc"** extension (by João Pinto).
- This provides a **Live Preview** just like DitaCraft, so you see your document as you type.

**3. For Large Projects:**
- Use **[Antora](https://antora.org/)**. It is the "DITA-OT for AsciiDoc." It looks at your Git folders and builds a professional multi-version documentation portal automatically.


---

## 23. AsciiDoc Editors: Beyond VS Code
While any text editor works, these tools provide a more professional "authoring" experience:

- **AsciidocFX (Free/OS)**: A dedicated editor specifically built for technical books. It includes built-in PDF/Ebook generation and a project tree view. (Best "standalone" choice).
- **adoc Studio (Mac/iPad)**: A polished, premium app that feels more like a modern word processor.
- **IntelliJ IDEA (with plugin)**: The most powerful editor for huge, enterprise-scale AsciiDoc projects.
- **Asciidoctor Live Preview**: A browser extension (Chrome/Firefox) that renders `.adoc` files as web pages in real-time as you save them.

---

## 24. The "Oxygen Gap": Are there Free Alternatives?
There is **no 1:1 open-source clone** of Oxygen XML Editor's "Author Mode" (visual WYSIWYG).

### Why the Gap Exists
Building a "Visual XML Editor" is technically brutal. The software must live-render XML tags based on complex DTD/Schemas and CSS rules simultaneously. Because the market for this is small (only pro tech writers), it is rarely a priority for open-source communities.

### The Best "Free" Options:
1.  **DitaCraft (VS Code)**: The best free tool for **Source Editing** (seeing the tags).
2.  **XMLmind (Personal Edition)**: The best free tool for **Visual Editing** (hiding the tags). It is free for personal use but is not open source.
3.  **XML Notepad (Microsoft OS)**: A simple **Tree View** editor. Good for seeing structure, but has no "DITA intelligence."

---
