import os
from PIL import Image

def combine_tif_files(input_folder, output_file):
    # Get list of all files in the input folder
    files = [f for f in os.listdir(input_folder) if "c2" in f and f.endswith('.tif')]
    
    # Sort files to ensure they are in order
    files.sort()
    
    # List to hold the individual images (slices)
    all_slices = []

    # Load each tif file and add all its slices to the list
    for file in files:
        file_path = os.path.join(input_folder, file)
        img = Image.open(file_path)
        
        # Check if the image has multiple slices
        try:
            while True:
                all_slices.append(img.copy())
                img.seek(img.tell() + 1)
        except EOFError:
            pass  # End of sequence
    
    # Save all slices as a single multi-slice tif file
    if all_slices:
        all_slices[0].save(output_file, save_all=True, append_images=all_slices[1:], compression="tiff_deflate")
        print(f"Combined {len(all_slices)} slices into {output_file}")
    else:
        print("No images found to combine.")

input_folder = "/Users/anuraagaravindan/Documents/testcombine.py/new stretch"
output_file = "/Users/anuraagaravindan/Documents/testcombine.py/complete.tif"

combine_tif_files(input_folder, output_file)
