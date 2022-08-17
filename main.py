from PIL import Image
from pathlib import Path 
import pillow_heif
import os


def main():
    valid_formats = [".heic"]
    folder = Path(r"C:\Users\jlmunoz\Downloads\visita_campo_elc\visita_campo_elc")
    file_list = os.listdir(folder)
    print(file_list)
    accepted_files = [file for file in file_list if file[-5:] in valid_formats]
    
    for archivo in accepted_files:
        filename = folder / archivo
        heif_file = pillow_heif.read_heif(filename)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw"
        )
        new_file_name = folder / "converted" / f"{archivo[:-4]}jpg"
        print(new_file_name)
        image.save(new_file_name)

if __name__ == "__main__":
    main()