import os
import re

directories = ["c:/Users/Sanjay Kumar/Documents/miraclewealth"]
files_to_update = [
    "retirement-planning.html",
    "lamf.html",
    "maternity-insurance-service.html",
    "comprehensive-health-insurance.html",
    "term-insurance.html",
    "claim-settlement.html"
]

for filename in files_to_update:
    path = os.path.join(directories[0], filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply TidyCal Updates
    content = re.sub(r'https://tidycal\.com/miraclewealthin/[^"\s>]+', 'https://tidycal.com/miraclewealthin/investmentadvisory', content)
    
    # Apply Whatsapp Updates (ensure it uses 917972053045)
    content = re.sub(r'https://wa\.me/\d+', 'https://wa.me/917972053045', content)
    
    # Apply Tel link updates
    content = re.sub(r'tel:\d+', 'tel:+917972053045', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links in all services files.")
