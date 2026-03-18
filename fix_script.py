import os

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

    # Remove the dangling <script> before </body>
    content = content.replace("<script>\n</body>", "</body>")
    content = content.replace("<script>\r\n</body>", "</body>")
    content = content.replace("<script></body>", "</body>")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed dangling scripts.")
