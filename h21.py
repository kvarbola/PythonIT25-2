import os
from PIL import Image, ImageOps

def create_thumbnails(source_dir, thumb_dir, size=(350, 350)):
    # Kontrolli, kas thumb kataloog on olemas, kui ei ole, siis loo see
    if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)

    nr = 1
    # Kõikide JPG failide leidmine kataloogis
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(source_dir, filename)
            img = Image.open(img_path)
            img = img.rotate(90)
            img = img.convert("L")
           
            # Pisipildi loomine
            thumb_img = ImageOps.fit(img, size, centering=(0.5, 0.5))
            img.close()
           
            filename = str(nr)+".jpg"
            # Pisipildi salvestamine
            thumb_path = os.path.join(thumb_dir, filename)
            thumb_img.save(thumb_path, "JPEG")
           
            print(f"Pisipilt salvestatud: {thumb_path}")
            nr+=1

# Kasuta funktsiooni
source_directory = 'yl_pildid'
thumb_directory = 'yl_pildid/thumb'
create_thumbnails(source_directory, thumb_directory)