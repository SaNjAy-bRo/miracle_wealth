import os
import glob
import re

html_files = glob.glob('c:/Users/Sanjay Kumar/Documents/miraclewealth/*.html')

print('--- CHECKING MOBILE MENU SCRIPT ---')
missing_script = []
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        if 'mobileMenuBtn.addEventListener' not in content:
            missing_script.append(os.path.basename(file_path))

if missing_script:
    print('Failed: Missing script in:', missing_script)
else:
    print('Passed: All files have the mobileMenuBtn event listener.')

print('\\n--- CHECKING LINK VALIDITY ---')
valid_endpoints = [os.path.basename(f) for f in html_files] + [
    'https://tidycal.com/miraclewealthin/investmentdiscovery-3qd7z0g',
    'https://wa.me/+917972053045',
    'tel:+917972053045',
    'mailto:miraclewealth.in@gmail.com',
    'https://www.linkedin.com/in/swapnil-asati/',
    'https://www.instagram.com/simplifywithswapnil/',
    'https://www.youtube.com/@SimplifyWithSwapnil'
]

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find href values
    hrefs = re.findall(r'href=["\'](.*?)["\']', content)
    invalid_internal = []
    
    for href in hrefs:
        # Ignore external links we aren't directly checking
        if href.startswith('http') and href not in valid_endpoints:
            pass # external site
        elif href.startswith('mailto:') or href.startswith('tel:'):
            if href not in valid_endpoints:
                 pass
        elif href.endswith('.css') or href.endswith('.js') or href.endswith('.png') or href.endswith('.jpg') or href.endswith('.webp'):
            pass # static asset
        elif href not in valid_endpoints:
            # check if it contains a fragment
            if '#' in href:
               base = href.split('#')[0]
               if base and base not in valid_endpoints:
                   invalid_internal.append(href)
            elif href == '':
               pass # empty link
            else:
               invalid_internal.append(href)
            
    if invalid_internal:
        print(f'Warning in {os.path.basename(file_path)}: Unknown internal links -> {set(invalid_internal)}')

print('Verification complete.')
