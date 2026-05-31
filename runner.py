from pathlib import Path
from PIL import Image

FILE_NAME = "snake"
FILE_NAME_2 = "puppy"
FILE_NAME_3 = "sunset"
FILE_NAME_4 = "tree"
IMAGE_MODE = "RGB"
EXERCISES_DIR = Path(__file__).resolve().parent / "exercises"
OUTPUTS_DIR = Path(__file__).resolve().parent / "outputs"
INPUT_IMG_NAME = FILE_NAME + ".png"
INPUT_IMG_NAME_2 = FILE_NAME_2 + ".png"
INPUT_IMG_NAME_3 = FILE_NAME_3 + ".png"
INPUT_IMG_NAME_4 = FILE_NAME_4 + ".png"
OUTPUT_IMG_NAME = INPUT_IMG_NAME.replace(".png", "_output.png")
INPUT_IMG_PATH = EXERCISES_DIR / INPUT_IMG_NAME
INPUT_IMG_PATH_2 = EXERCISES_DIR / INPUT_IMG_NAME_2
INPUT_IMG_PATH_3 = EXERCISES_DIR / INPUT_IMG_NAME_3
INPUT_IMG_PATH_4 = EXERCISES_DIR / INPUT_IMG_NAME_4
OUTPUT_IMG_PATH = OUTPUTS_DIR / OUTPUT_IMG_NAME

def negative_image(img):
    # Get the pixel data as a stream (list of tuples) and the size of the image
    in_stream = img.get_flattened_data()
    size = img.size
    
    # Create a new image with the same size and mode as the input image
    negative_img = Image.new(IMAGE_MODE, size)
    
    out_stream = []
    for (r,g,b) in in_stream:
        out_stream.append((255-r,255-g,255-b))
    negative_img.putdata(out_stream)
    
    return negative_img

def mirror_image(img):
    in_grid = img.load()
    size = img.size
        
    # Create a new image with the same size and mode as the input image
    mirror_img = Image.new(IMAGE_MODE, size)
    
    width, height = size
    out_grid = mirror_img.load()
    for y in range(height):
        for x in range(width):
            out_grid[x, y] = in_grid[width-1-x, y]
    
    return mirror_img

# TODO: Verify
def grayscale_average_conversion(img):
    in_stream = img.get_flattened_data()
    size = img.size
        
    # Create a new image with the same size and mode as the input image
    grayscale_img = Image.new(IMAGE_MODE, size)
    
    width, height = size
    out_stream_1 = []
    out_stream_2 = []
    for (r,g,b) in in_stream:
        # avg = (R+G+B)/3
        luma = int((r + g + b) / 3)
        out_stream_1.append(luma)
    grayscale_img.putdata(out_stream_1)
          
    return grayscale_img

# TODO: Verify
def grayscale_luma_conversion(img):
    in_stream = img.get_flattened_data()
    size = img.size
        
    # Create a new image with the same size and mode as the input image
    grayscale_img = Image.new(IMAGE_MODE, size)
    
    width, height = size
    out_stream_1 = []
    out_stream_2 = []
    for (r,g,b) in in_stream:
        # calculate lumen - Y=int(0.299R+0.587G+0.114B)
        luma = int(0.299 * r + 0.587 * g + 0.114 * b)
        out_stream_2.append(luma)
    grayscale_img.putdata(out_stream_2)
          
    return grayscale_img

# Convert an image to purely black and white depending on intensity
def binarization(img):
    # Assume T (comparator) of 130
    t_comparator = 130
    in_stream = img.get_flattened_data()
    size = img.size
        
    # Create a new image with the same size and mode as the input image
    # NOTE: "1" mode is a binary image (black and white)
    binarized_img = Image.new("1", size)
    
    out_stream = []
    # Since the green channel often carries the most structural information for the human eye, 
    # it serves as a reliable proxy for overall brightness.
    for (_,g,_) in in_stream:
        if (g >= t_comparator):
            out_stream.append(1)
        else:
            out_stream.append(0)
    binarized_img.putdata(out_stream)
          
    return binarized_img

# Hidding a secret message in the least significant bits of the image
def steganography(img):
    size = img.size
    in_stream = img.get_flattened_data()
    
    # Create a new image with the same size and mode as the input image
    # NOTE: "1" mode is a binary image (black and white)
    secret_img = Image.new("1", size)
    
    out_stream = []
    for (_,g,_) in in_stream:
        # Get the least significant bit of the green channel
        lsb = 0 if g % 2 == 0 else 1
        out_stream.append(lsb)
    # Contruct images with just the leasts significant bits of the green channel
    secret_img.putdata(out_stream)

    return secret_img

# Convert and image to a poster
# "lmited" color pallete (e.g., 4 colors) to create a poster-like effect
# i.e.
    # Color Pallete
    # HIGHLIGHT = (255, 236, 209)
    # MIDTONE = (255, 125, 0)
    # DARKSHADOW = (120, 41, 15)
def posterization(img, highlight, midtone, darkshadow):
    # upper bounds for comparison
    t_upper = 130
    # lower bounds for comparison
    t_lower = 50
    
    in_stream = img.get_flattened_data()
    size = img.size
        
    # Create a new image with the same size and mode as the input image
    posterized_img = Image.new(IMAGE_MODE, size)
    
    out_stream = []
    # Since the green channel often carries the most structural information for the human eye, 
    # it serves as a reliable proxy for overall brightness.
    for (r,g,b) in in_stream:
        # average intensity at or above the upper threshold
        avg = int((r + g + b) // 3)
        
        # NOTE: Alternatively, we could also use the luma formula to calculate the intensity instead of the average
        # calculate lumen - Y=int(0.299R+0.587G+0.114B)
        #avg = int(0.299 * r + 0.587 * g + 0.114 * b)
        
        # Highlight at or above the upper threshold
        if (avg >= t_upper):
            out_stream.append(highlight)
        # Dark Shadows below the lower threshold
        elif (avg < t_lower):
            out_stream.append(darkshadow)
        # Midtones
        else:
            out_stream.append(midtone)
    posterized_img.putdata(out_stream)
          
    return posterized_img

# combine 4 images to one image by tiling
def place_tile(out_grid, file_path, position):
    with Image.open(file_path) as img:
        img = img.convert(IMAGE_MODE) 
        # Assuming all images have the same size
        width, height = img.size
        in_grid = img.load()
        
        out_x, out_y = position
        for y in range(height):
            for x in range(width):
                out_grid[out_x + x, out_y + y] = in_grid[x, y]

def run():
    # Open an image file from the exercises folder
    with Image.open(INPUT_IMG_PATH) as img:
        # safeguard to convert image to RGB mode
        img = img.convert(IMAGE_MODE)

        # TODO: Modify operation as needed (e.g., call negative_image or mirror_image)
        # Perform some operations on the image (e.g., convert to grayscale)
        #output_image = negative_image(img)
        output_image = posterization(img)
        
        # Save the processed image back to the exercises folder
        output_image.save(OUTPUT_IMG_PATH)

def run_tiling():
    with Image.open(INPUT_IMG_PATH) as img:
        width, height = img.size
        
    out_img = Image.new(IMAGE_MODE, (width*2, height*2))
    out_grid = out_img.load()
    place_tile(out_grid, INPUT_IMG_PATH, (0, 0))
    place_tile(out_grid, INPUT_IMG_PATH_2, (width, 0))
    place_tile(out_grid, INPUT_IMG_PATH_3, (0, height))
    place_tile(out_grid, INPUT_IMG_PATH_4, (width, height))
    
    out_img.save(OUTPUT_IMG_PATH)

def run_warhol_effect():
    with Image.open(INPUT_IMG_PATH) as img:
        width, height = img.size
    
        # Posterize original image 4 diff ways to create a Warhol-like effect
        img1 = posterization(img, (42,18,8), (196,72,24), (255,210,120))
        warhol1_output_path = OUTPUTS_DIR / "warhol1.png"
        img1.save(warhol1_output_path)
        img2 = posterization(img, (10, 6, 34), (88, 30, 180), (0, 240, 200))
        warhol2_output_path = OUTPUTS_DIR / "warhol2.png"
        img2.save(warhol2_output_path)
        img3 = posterization(img, (28, 24, 20), (112, 88, 56), (210, 192, 160))
        warhol3_output_path = OUTPUTS_DIR / "warhol3.png"
        img3.save(warhol3_output_path)
        img4 = posterization(img, (14, 40, 10), (220, 30, 90), (200, 255, 40))
        warhol4_output_path = OUTPUTS_DIR / "warhol4.png"
        img4.save(warhol4_output_path)

    # Construct tiling of the same image with different posterization parameters
    out_img = Image.new(IMAGE_MODE, (width*2, height*2))
    out_grid = out_img.load()
    place_tile(out_grid, warhol1_output_path, (0, 0))
    place_tile(out_grid, warhol2_output_path, (width, 0))
    place_tile(out_grid, warhol3_output_path, (0, height))
    place_tile(out_grid, warhol4_output_path, (width, height))
    
    out_img.save(OUTPUT_IMG_PATH)

if __name__ == "__main__":
    #run()
    #run_tiling()
    run_warhol_effect()