import os
import re
import glob

directory = "c:/Users/Sanjay Kumar/Documents/miraclewealth"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update TidyCal links anywhere
    content = re.sub(r'https://tidycal\.com/miraclewealthin/[a-zA-Z0-9_-]+', 'https://tidycal.com/miraclewealthin/investmentadvisory', content)

    # Update whatsapp links anywhere
    content = re.sub(r'https://wa\.me/(?:\+91)?\d+', 'https://wa.me/+917972053045', content)

    # Update tel links anywhere
    content = re.sub(r'tel:(?:\+91)?\d+', 'tel:+917972053045', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Global link consistency check applied to {len(html_files)} files.")
