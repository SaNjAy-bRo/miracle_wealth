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
        <a href="https://tidycal.com/miraclewealthin/investmentadvisory" class="btn-primary rounded-lg px-4 py-2 bg-purple-600 text-white font-['Inter']" target="_blank">Book a Call</a>
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
          <a href="https://tidycal.com/miraclewealthin/investmentadvisory" class="btn-primary text-center rounded-lg px-4 py-2 bg-purple-600 text-white" target="_blank">Book a Call</a>
        </div>
      </nav>
    </div>
  </header>
"""

footer_snippet = """
  <footer class="footer-dark border-t border-zinc-800 px-6 py-12 lg:px-8 bg-[#0F0D04]" style="margin-top:0;">
    <div class="mx-auto max-w-7xl rounded-2xl border border-zinc-800 footer-shell p-6 md:p-8 bg-[#1A1506]">
      <div class="grid gap-10 md:grid-cols-12">
        <div class="md:col-span-6 lg:col-span-5 flex flex-col md:flex-row items-start md:items-center gap-6">
          <img src="images/logo.png" alt="Miracle Wealth" class="h-24 md:h-32 w-auto" />
          <div class="flex flex-col gap-3 font-['Inter']">
            <a href="tel:+917972053045" class="social-pill w-fit pr-6 bg-zinc-800/50 rounded-full px-4 py-2 text-zinc-200 border border-zinc-700 flex items-center gap-2"><ion-icon name="call-outline"></ion-icon>+91 7972053045</a>
            <a href="https://tidycal.com/miraclewealthin/investmentadvisory" class="social-pill w-fit pr-6 bg-zinc-800/50 rounded-full px-4 py-2 text-zinc-200 border border-zinc-700 flex items-center gap-2" target="_blank"><ion-icon name="calendar-outline"></ion-icon>Book a Call</a>
          </div>
        </div>

        <div class="md:col-span-2 lg:col-span-3 font-['Inter']">
          <h4 class="font-semibold text-zinc-100">Quick Links</h4>
          <ul class="mt-4 space-y-2 text-sm text-zinc-300">
            <li><a class="footer-link hover:text-white" href="index.html">Home</a></li>
            <li><a class="footer-link hover:text-white" href="about.html">About</a></li>
            <li><a class="footer-link hover:text-white" href="services.html">Services</a></li>
            <li><a class="footer-link hover:text-white" href="calculators.html">Calculators</a></li>
            <li><a class="footer-link hover:text-white" href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="md:col-span-4 lg:col-span-4 font-['Inter']">
          <h4 class="font-semibold text-zinc-100">Connect</h4>
          <p class="mt-4 text-sm text-zinc-300">Email: miraclewealth.in@gmail.com</p>
          <p class="text-sm text-zinc-300">Location: Ensaara Metropark, Pipla-Kharsoli Road, Pipla, Nagpur, Maharashtra, India – 440034</p>
          <div class="mt-4 flex flex-wrap gap-2 text-sm text-zinc-300">
            <a href="https://www.youtube.com/@SimplifyWithSwapnil" target="_blank" rel="noopener" class="social-pill bg-zinc-800/50 rounded-full px-4 py-2 text-zinc-200 border border-zinc-700 flex items-center gap-2 hover:bg-zinc-700"><ion-icon name="logo-youtube"></ion-icon>YouTube</a>
            <a href="https://www.instagram.com/simplifywithswapnil/" target="_blank" rel="noopener" class="social-pill bg-zinc-800/50 rounded-full px-4 py-2 text-zinc-200 border border-zinc-700 flex items-center gap-2 hover:bg-zinc-700"><ion-icon name="logo-instagram"></ion-icon>Instagram</a>
            <a href="https://www.linkedin.com/in/swapnil-asati/" target="_blank" rel="noopener" class="social-pill bg-zinc-800/50 rounded-full px-4 py-2 text-zinc-200 border border-zinc-700 flex items-center gap-2 hover:bg-zinc-700"><ion-icon name="logo-linkedin"></ion-icon>LinkedIn</a>
          </div>
          <a href="privacy-policy.html" class="mt-6 inline-block text-sm text-zinc-400 hover:text-zinc-200">Privacy Policy</a>
        </div>
      </div>

      <div class="mt-8 grid gap-4 border-t border-zinc-800 pt-5 md:grid-cols-12 md:items-center font-['Inter']">
        <p class="md:col-span-9 text-xs leading-relaxed text-zinc-300">
          We are not a SEBI-registered investment advisor. We facilitate mutual funds (as per AMFI guidelines) &amp;
          insurance distribution services (as per IRDAI guidelines). Investments in mutual funds are subject to market
          risks, please read all scheme related documents carefully before investing.
        </p>
        <p class="md:col-span-3 text-xs text-zinc-500 md:text-right">© 2026 Miracle Wealth. All rights reserved.</p>
      </div>
    </div>
  </footer>
"""

for filename in files_to_update:
    path = os.path.join(directories[0], filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <header id="header"...>...</header>
    content = re.sub(r'<header id="header".*?</header>', header_snippet, content, flags=re.DOTALL)
    
    # Replace <footer class="footer-dark"...>...</footer>
    content = re.sub(r'<footer.*?</footer>', footer_snippet, content, flags=re.DOTALL)

    # Convert old conact.html to contact.html
    content = content.replace('conact.html', 'contact.html')

    # Update TidyCal links everywhere
    content = re.sub(r'https://tidycal\.com/miraclewealthin/[^"\s\'<>]+', 'https://tidycal.com/miraclewealthin/investmentadvisory', content)

    # Update whatsapp links
    content = re.sub(r'https://wa\.me/\d+', 'https://wa.me/+917972053045', content)

    # Update tel links
    content = re.sub(r'tel:\d+', 'tel:+917972053045', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links and layout elements in original service pages.")
