import os
from PIL import Image, ImageOps

def create_thumbnails(source_dir, thumb_dir, size=(300, 300)):
    # Kontrolli, kas thumb kataloog on olemas, kui ei ole, siis loo see
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    # Kõikide JPG failide leidmine kataloogis
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(source_dir, filename)
            img = Image.open(img_path)
           
            # Pisipildi loomine
            thumb_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
            img.close()
           
            # Pisipildi salvestamine
            thumb_path = os.path.join(thumb_dir, filename)
            thumb_img.save(thumb_path, "JPEG")
           
            print(f"Pisipilt salvestatud: {thumb_path}")

# Kasuta funktsiooni
source_directory = 'yl_pildid'
thumb_directory = 'yl_pildid/thumb'
create_thumbnails(source_directory, thumb_directory)