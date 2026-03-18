import os
import re
import glob

directory = "c:/Users/Sanjay Kumar/Documents/miraclewealth"
files_to_update = [
    "wealth-management.html",
    "services.html",
    "privacy-policy.html"
]

header_snippet = """
  <header id="header" class="fixed top-0 z-50 w-full transition-all duration-300 bg-[#1A1506]/95 backdrop-blur-md border-b border-zinc-800">
    <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-2 lg:px-8">
      <a href="index.html" class="flex items-center gap-3">
        <img src="images/logo.png" alt="Miracle Wealth" class="h-16 w-auto md:h-20 lg:h-24" />
      </a>

      <nav class="hidden items-center gap-8 text-sm text-zinc-200 lg:flex">
        <a href="index.html" class="nav-link font-['Inter']">Home</a>
        <a href="about.html" class="nav-link font-['Inter']">About</a>
        <div class="relative group">
          <button class="nav-link flex items-center gap-1 cursor-pointer font-['Inter']">Services <ion-icon name="chevron-down-outline"></ion-icon></button>
          <div class="absolute left-0 top-full mt-2 hidden w-64 flex-col rounded-xl border border-zinc-800 bg-[#0F0D04] p-2 shadow-xl group-hover:flex">
            <a href="wealth-management.html" class="block rounded-lg px-4 py-2 hover:bg-zinc-800 transition-colors font-['Inter']">Wealth Management</a>
            <a href="retirement-planning.html" class="block rounded-lg px-4 py-2 hover:bg-zinc-800 transition-colors font-['Inter']">Retirement Planning</a>
            <a href="lamf.html" class="block rounded-lg px-4 py-2 hover:bg-zinc-800 transition-colors font-['Inter']">Loan Against Mutual Funds</a>
            <a href="maternity-insurance-service.html" class="block rounded-lg px-4 py-2 hover:bg-zinc-800 transition-colors font-['Inter']">Maternity Health Insurance</a>
            <a href="comprehensive-health-insurance.html" class="block rounded-lg px-4 py-2 hover:bg-zinc-800 transition-colors font-['Inter']">Comprehensive Health Insurance</a>
            <a href="term-insurance.html" class="block rounded-lg px-4 py-2 hover:bg-zinc-800 transition-colors font-['Inter']">Term Insurance</a>
            <a href="claim-settlement.html" class="block rounded-lg px-4 py-2 hover:bg-zinc-800 transition-colors font-['Inter']">Claim Settlement Assistance</a>
          </div>
        </div>
        <a href="calculators.html" class="nav-link font-['Inter']">Calculators</a>
        <a href="contact.html" class="nav-link font-['Inter']">Contact</a>
      </nav>

      <div class="hidden items-center gap-3 lg:flex">
        <a href="tel:+917972053045" class="btn-secondary rounded-lg px-4 py-2 border border-zinc-700 font-['Inter']">+91 7972053045</a>
        <a href="https://tidycal.com/miraclewealthin/investmentdiscovery-3qd7z0g" class="btn-primary rounded-lg px-4 py-2 bg-purple-600 text-white font-['Inter']" target="_blank">Book a Call</a>
      </div>

      <button id="mobileMenuBtn"
        class="inline-flex items-center justify-center rounded-md border border-zinc-700 p-2 text-zinc-100 lg:hidden"
        aria-label="Toggle menu" aria-expanded="false" aria-controls="mobileMenu">
        <svg id="menuIconOpen" class="h-5 w-5 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        <svg id="menuIconClose" class="h-5 w-5 hidden transition-transform duration-300 rotate-90" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <div id="mobileMenu"
      class="mobile-menu hidden absolute top-full left-0 w-full border-t border-zinc-800 bg-[#0F0D04] shadow-2xl lg:hidden">
      <nav class="mx-auto flex max-w-7xl flex-col space-y-4 px-6 py-6 text-base">
        <a href="index.html" class="mobile-link block font-medium font-['Inter'] text-zinc-100">Home</a>
        <a href="about.html" class="mobile-link block font-medium font-['Inter'] text-zinc-100">About</a>
        <div class="space-y-3">
          <div class="font-medium text-zinc-100 font-['Inter']">Services</div>
          <div class="ml-4 flex flex-col space-y-3 text-sm border-l border-zinc-700 pl-4">
            <a href="wealth-management.html" class="mobile-link font-normal text-zinc-300 font-['Inter']">Wealth Management</a>
            <a href="retirement-planning.html" class="mobile-link font-normal text-zinc-300 font-['Inter']">Retirement Planning</a>
            <a href="lamf.html" class="mobile-link font-normal text-zinc-300 font-['Inter']">Loan Against Mutual Funds</a>
            <a href="maternity-insurance-service.html" class="mobile-link font-normal text-zinc-300 font-['Inter']">Maternity Health Insurance</a>
            <a href="comprehensive-health-insurance.html" class="mobile-link font-normal text-zinc-300 font-['Inter']">Comprehensive Health Insurance</a>
            <a href="term-insurance.html" class="mobile-link font-normal text-zinc-300 font-['Inter']">Term Insurance</a>
            <a href="claim-settlement.html" class="mobile-link font-normal text-zinc-300 font-['Inter']">Claim Settlement Assistance</a>
          </div>
        </div>
        <a href="calculators.html" class="mobile-link block font-medium font-['Inter'] text-zinc-100">Calculators</a>
        <a href="contact.html" class="mobile-link block font-medium font-['Inter'] text-zinc-100">Contact</a>
        <div class="mt-2 flex flex-col gap-3 border-t border-zinc-800 pt-6 font-['Inter']">
          <a href="tel:+917972053045" class="btn-secondary text-center rounded-lg px-4 py-2 border border-zinc-700 text-zinc-100">+91 7972053045</a>
          <a href="https://tidycal.com/miraclewealthin/investmentdiscovery-3qd7z0g" class="btn-primary text-center rounded-lg px-4 py-2 bg-purple-600 text-white" target="_blank">Book a Call</a>
        </div>
      </nav>
    </div>
  </header>
"""

javascript_toggle_snippet = """
    const mobileMenuBtn = document.getElementById("mobileMenuBtn");
    const mobileMenu = document.getElementById("mobileMenu");
    const mobileLinks = mobileMenu.querySelectorAll("a");
    const menuIconOpen = document.getElementById("menuIconOpen");
    const menuIconClose = document.getElementById("menuIconClose");

    const toggleMenu = (forceClose = false) => {
      const isHidden = mobileMenu.classList.contains("hidden");
      if (forceClose && isHidden) return;

      const willBeHidden = forceClose ? true : !isHidden;

      if (willBeHidden) {
        mobileMenu.classList.add("hidden");
        mobileMenuBtn.setAttribute("aria-expanded", "false");
        menuIconClose.classList.add("hidden", "rotate-90");
        menuIconClose.classList.remove("rotate-0");
        menuIconOpen.classList.remove("hidden");
        menuIconOpen.classList.add("rotate-0");
      } else {
        mobileMenu.classList.remove("hidden");
        mobileMenuBtn.setAttribute("aria-expanded", "true");
        menuIconOpen.classList.add("hidden");
        menuIconOpen.classList.remove("rotate-0");
        menuIconClose.classList.remove("hidden", "rotate-90");
        menuIconClose.classList.add("rotate-0");
      }
    };

    mobileMenuBtn.addEventListener("click", () => toggleMenu());
    mobileLinks.forEach((link) => {
      link.addEventListener("click", () => toggleMenu(true));
    });
"""

for filename in files_to_update:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <header id="header"...>...</header>
    if '<header id="header"' in content:
        content = re.sub(r'<header id="header".*?</header>', header_snippet.strip(), content, flags=re.DOTALL)
    
    # ensure script has mobileMenuBtn initialization
    if 'mobileMenuBtn.addEventListener' not in content and 'const header = document.getElementById("header");' in content:
        content = content.replace('const header = document.getElementById("header");', 'const header = document.getElementById("header");\n' + javascript_toggle_snippet)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injected global header and mobile JS into missed files.")
