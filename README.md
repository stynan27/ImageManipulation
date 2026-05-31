# Image Manipulation

An educational Python project demonstrating core image processing techniques. These exercises were completed as part of a tutorial attended during **PyCon 2026**.

## Features

This project implements seven image manipulation techniques using Python and the Pillow (PIL) library:

- **Negative**: Color inversion (inverts RGB values to create a photographic negative)
- **Mirror**: Horizontal flip of an image
- **Grayscale (Average)**: Converts to grayscale using simple average of RGB channels
- **Grayscale (Luma)**: Converts to grayscale using weighted luma coefficients (0.299R + 0.587G + 0.114B)
- **Binarization**: Converts to pure black and white based on intensity threshold
- **Steganography**: Extracts least significant bits (LSB) from the green channel to reveal hidden patterns
- **Posterization**: Creates a poster-like effect using limited color palettes

## Requirements

- Python 3.x
- Pillow (PIL) library

Install dependencies:

```bash
pip install Pillow
```

## Usage

Run the main script to process sample images:

```bash
python runner.py
```

The script processes images from the `exercises/` folder and outputs results to the `outputs/` folder.

## Project Structure

```
ImageManipulation/
├── runner.py          # Main script with all image manipulation functions
├── exercises/         # Input images and credits
│   ├── puppy.png
│   ├── snake.png
│   ├── sunset.png
│   ├── tree.png
│   ├── woman.png
│   └── credits.txt    # Image attribution
└── outputs/           # Output images from processing
```

## Image Credits

All sample images are free-to-use photos sourced from [Pexels](https://www.pexels.com/):

- puppy.png by Сергей Сёмин
- snake.png by Pramod Giri
- sunset.png by musafirdost08
- tree.png by Johannes Plenio
- woman.png by bishenova
