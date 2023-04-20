import time

from pdf2image import convert_from_path
import os
from PIL import Image
from pytesseract import pytesseract


def download_wait(directory, timeout, nfiles=None):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    nfiles : int, defaults to None
        If provided, also wait for the expected number of files.

    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True

        seconds += 1
    return seconds


def iterate_and_extract(pdf_dir):
    """
    Iterates through a directory of PDF files, extracts text patterns, and writes them to a CSV file.
    """
    v = 1
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(pdf_dir, filename)

            # Store Pdf with convert_from_path function
            images = convert_from_path(pdf_file_path)

            for i in range(len(images)):
                # Save pages as images in the pdf
                images[i].save('pages/' + filename.replace('.pdf', '') + '_page' + str(i) + '.jpg', 'JPEG')
        v += 1


def capture_and_extract_image(image):
    # Define path to tessaract.exe
    path_to_tesseract = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    # Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    # Open image with PIL
    img = Image.open(image)

    # Extract text from image
    text = pytesseract.image_to_string(img)

    print(text)


def capture_and_extract_images(images):
    # Define path to tessaract.exe
    path_to_tesseract = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    # Define path to images folder

    # Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    # Get the file names in the directory
    for root, dirs, file_names in os.walk(images):
        # Iterate over each file name in the folder
        for file_name in file_names:
            # Open image with PIL
            img = Image.open(images + file_name)

            # Extract text from image
            text = pytesseract.image_to_string(img)

            print(text)

