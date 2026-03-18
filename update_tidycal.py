import os
import re
import glob

directory = "c:/Users/Sanjay Kumar/Documents/miraclewealth"
html_files = glob.glob(os.path.join(directory, "*.html"))

new_link = "https://tidycal.com/miraclewealthin/investmentdiscovery-3qd7z0g"

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update TidyCal links anywhere
    updated_content = re.sub(r'https://tidycal\.com/miraclewealthin/[a-zA-Z0-9_-]+', new_link, content)

    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

print(f"Updated TidyCal links in {len(html_files)} files.")
