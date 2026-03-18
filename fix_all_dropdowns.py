import os
import glob
import re

html_files = glob.glob('c:/Users/Sanjay Kumar/Documents/miraclewealth/*.html')

javascript_toggle_snippet = """
    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const mobileMenu = document.getElementById("mobileMenu");
    const mobileLinks = mobileMenu.querySelectorAll("a");
    const menuIconOpen = document.getElementById("menuIconOpen");
    const menuIconClose = document.getElementById("menuIconClose");

    const toggleMenu = (forceClose = false) => {
      if (!mobileMenu || !mobileMenuBtn) return;
      const isHidden = mobileMenu.classList.contains("hidden");
      if (forceClose && isHidden) return;

      const willBeHidden = forceClose ? true : !isHidden;

      if (willBeHidden) {
        mobileMenu.classList.add("hidden");
        mobileMenuBtn.setAttribute("aria-expanded", "false");
        if(menuIconClose) menuIconClose.classList.add("hidden", "rotate-90");
        if(menuIconClose) menuIconClose.classList.remove("rotate-0");
        if(menuIconOpen) menuIconOpen.classList.remove("hidden");
        if(menuIconOpen) menuIconOpen.classList.add("rotate-0");
      } else {
        mobileMenu.classList.remove("hidden");
        mobileMenuBtn.setAttribute("aria-expanded", "true");
        if(menuIconOpen) menuIconOpen.classList.add("hidden");
        if(menuIconOpen) menuIconOpen.classList.remove("rotate-0");
        if(menuIconClose) menuIconClose.classList.remove("hidden", "rotate-90");
        if(menuIconClose) menuIconClose.classList.add("rotate-0");
      }
    };

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener("click", () => toggleMenu());
    }
    if (mobileLinks) {
        mobileLinks.forEach((link) => {
          link.addEventListener("click", () => toggleMenu(true));
        });
    }
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check and inject mobile toggle JS if missing
    if 'mobileMenuBtn.addEventListener' not in content and 'const header = document.getElementById("header");' in content:
        content = content.replace(
            'const header = document.getElementById("header");', 
            'const header = document.getElementById("header");\n' + javascript_toggle_snippet
        )
    
    # Check and Fix the arbitrary bg-[#0F0D04] class, which isn't dynamically compiled by tailwind everywhere
    content = content.replace('bg-[#0F0D04]', 'bg-zinc-900')
    content = content.replace('bg-[#1A1506]', 'bg-zinc-950')
    
    # Just in case, replace the dropdown text colors from text-zinc-300 to explicitly ensure they don't get white-washed
    # (actually bg-zinc-900 will make white text look fine)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied strict JS toggles and fixed tailwind arbitrary hex classes in all files.")
