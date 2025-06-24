# Markdown to HTML Converter

This is a simple Python command-line tool that converts a `.md` (Markdown) file into a clean, well-formatted `.html` file.  
It supports standard Markdown syntax including headers, bold, italics, lists, links, inline code, code blocks, and more.

---

## 🚀 Features
- Converts standard Markdown elements to HTML
- Generates a complete HTML file (with `<html>`, `<head>`, `<body>`)
- Clean layout with built-in CSS for better readability
- Styled code blocks with black background and light text

---

## 📂 Example

### Input (`script.md`)
```markdown
# Python Basics
```

You can print a message using:

```python
print("Hello, World!")
```


### Output (`output.html`)
✅ A clean HTML file with styled text and code blocks.

---

## 💻 How to Run

### 1️⃣ Clone this repo
```bash
git clone <your-repo-url>
cd markdown-to-html-converter
```
### 2️⃣ Install dependencies
```bash
pip install markdown
```
### 3️⃣ Run the tool
```bash
python converter.py script.md output.html
```
script.md: Your input Markdown file

output.html: The generated HTML file

