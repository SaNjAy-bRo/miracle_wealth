import fitz
import os

pdf_path = r"c:\Users\Sanjay Kumar\Documents\miraclewealth\Corrections\28.02.2025_Corrections\28.02.2026_Corrections.pdf"
output_dir = r"c:\Users\Sanjay Kumar\Documents\miraclewealth\Corrections\28.02.2025_Corrections\images_extracted"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    page = doc[i]
    image_list = page.get_images(full=True)
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {i}")
    else:
        print(f"[!] No images found on page {i}")
    
    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_name = f"page_{i}_img_{image_index}.{image_ext}"
        with open(os.path.join(output_dir, image_name), "wb") as f:
            f.write(image_bytes)
            print(f"Saved: {image_name}")
