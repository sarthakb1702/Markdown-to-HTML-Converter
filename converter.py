import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            text = md_file.read()

        # Convert markdown to HTML body
        body_html = markdown.markdown(text, extensions=['extra', 'codehilite', 'toc'])

        # Wrap with full HTML template
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{input_file} - Converted Markdown</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
            background-color: #f9f9f9;
        }}
        h1, h2, h3, h4 {{
            color: #333;
        }}
        pre {{
            background: #272822;
            color: #f8f8f2;
            padding: 10px;
            overflow-x: auto;
            border-radius: 5px;
        }}
        code {{
            
            padding: 2px 4px;
            border-radius: 3px;
        }}
        a {{
            color: #007acc;
        }}
        ul {{
            padding-left: 20px;
        }}
        blockquote {{
            
            padding-left: 10px;
            color: #555;
        }}
    </style>
</head>
<body>
{body_html}
</body>
</html>
"""

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(full_html)

        print(f"✅ Successfully converted {input_file} to {output_file}")
    except FileNotFoundError:
        print(f"❌ Error: File {input_file} not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input.md> <output.html>")
    else:
        convert_markdown_to_html(sys.argv[1], sys.argv[2])
