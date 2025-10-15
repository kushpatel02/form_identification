# import pandas as pd
# import numpy as np
# import pytesseract

# # main_processor.py
# import fitz
# import pytesseract
# from PIL import Image

# pdf_path='Documents/ML/forms_data'

# def extract_images_from_pdf(pdf_path, dpi=300):
#     import fitz  # PyMuPDF
# from PIL import Image

# def extract_images_from_pdf(pdf_path, dpi=300):
    
#     try:
#         pdf_document = fitz.open(pdf_path)
#         images = []
#         for page_num in range(len(pdf_document)):
#             page = pdf_document.load_page(page_num)
#             pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
            
#             # Create a Pillow Image from the pixmap
#             img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#             images.append(img)
            
#         pdf_document.close()
#         return images
#     except Exception as e:
#         print(f"Error processing PDF: {e}")
#         return []

# def extract_text_from_image(image):
#     import pytesseract
# from PIL import Image

# def extract_text_from_image(image):
    
#     try:
#         text = pytesseract.image_to_string(image)
#         return text
#     except pytesseract.TesseractNotFoundError:
#         print("Tesseract is not installed or not in your PATH. Please install it.")
#         return ""
#     except Exception as e:
#         print(f"Error during OCR: {e}")
#         return ""

# def identify_form_type(text):
#     text = text.lower()
    
#     # Define your keywords for each form type
#     form_keywords = [
#         "Form A", "Form B", "Form C", "Form D", "Form E"
#     ]

#     for form_type, keywords in form_keywords:
#         for keyword in keywords:
#             if keyword in text:
#                 return form_type

#     form_keywords = [
#         ("Form A", ["form a", "type a"]),
#         ("Form B", ["form b", "type b"]),
#         ("Form C", ["form c", "type c"]),
#         ("Form D", ["form d", "type d"]),
#         ("Form E", ["form e", "type e"])
#     ]
    
#     # for form_type, keywords in form_keywords:
#     #     for keyword in keywords:
#     #         if keyword in text:
#     #             return form_type
    
#     return "Unknown Form"

# def process_pdf(pdf_path):
    
#     print(f"Processing '{pdf_path}'...")
#     pdf_pages = extract_images_from_pdf(pdf_path)
    
#     if not pdf_pages:
#         return "Could not process PDF."
    
#     # We'll only use the first page for quick identification
#     first_page_image = pdf_pages[0]
    
#     # Optional: Save the extracted image to verify it
#     # first_page_image.save("extracted_first_page.png")

#     text = extract_text_from_image(first_page_image)
    
#     if not text:
#         return "No text found on the first page."
        
#     form_type = identify_form_type(text)
    
#     return f"The form type is: {form_type}"

# # Example of how to run the script
# if __name__ == "__main__":
#     pdf_file = "Documents/ML/forms_data/00068790.pdf" # Replace with your PDF file
#     result = process_pdf(pdf_file)
#     print(result)


import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def extract_first_page_as_image(pdf_path, dpi=300):
    """
    Extracts the first page of a PDF file as a PIL Image.
    """
    try:
        pdf_document = fitz.open(pdf_path)
        if len(pdf_document) > 0:
            # Load only the first page (index 0)
            page = pdf_document.load_page(0)
            # Render page to an image (pixmap)
            pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))
            # Convert the pixmap to a PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            pdf_document.close()
            return img
        else:
            pdf_document.close()
            print(f"Warning: PDF '{pdf_path}' is empty and was skipped.")
            return None
    except Exception as e:
        print(f"Error processing PDF '{pdf_path}': {e}")
        return None

def extract_text_from_image(image):
    """
    Extracts text from a PIL Image using Tesseract OCR.
    """
    if image is None:
        return ""
    try:
        text = pytesseract.image_to_string(image)
        return text
    except pytesseract.TesseractNotFoundError:
        print("Tesseract Error: Tesseract is not installed or not in your PATH. Please install it.")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred during OCR: {e}")
        return ""

def identify_form_type(text):
    """
    Identifies the form type from extracted text based on keywords.
    """
    text = text.lower()
    
    # Define keywords for each form type in a (Name, [keywords]) format
    form_keywords = [
        ("Form A", ["form a", "type a"]),
        ("Form B", ["form b", "type b"]),
        ("Form C", ["form c", "type c"]),
        ("Form D", ["form d", "type d"]),
        ("Form E", ["form e", "type e"])
    ]
    
    for form_type, keywords in form_keywords:
        for keyword in keywords:
            if keyword in text:
                return form_type  # Return the first match found
    
    return "Unknown Form"

def process_pdf(pdf_path):
    """
    Main processing function for a single PDF file.
    """
    print(f"--- Processing '{os.path.basename(pdf_path)}' ---")
    
    first_page_image = extract_first_page_as_image(pdf_path)
    
    if first_page_image is None:
        return "Could not extract image from PDF."
    
    # For debugging: save the extracted image to verify it's correct
    # first_page_image.save(f"debug_{os.path.basename(pdf_path)}.png")

    text = extract_text_from_image(first_page_image)
    
    if not text.strip():
        return "No text could be extracted from the first page."
        
    form_type = identify_form_type(text)
    
    return f"Result: The identified form type is: {form_type}"

if __name__ == "__main__":
    # Define the path to the directory containing your PDF files
    pdf_directory = "/Users/kush/Documents/ML/forms_data" 

    if not os.path.isdir(pdf_directory):
        print(f"Error: Directory not found at '{pdf_directory}'")
    else:
        # Loop through all files in the specified directory
        for filename in sorted(os.listdir(pdf_directory)):
            # Check if the file is a PDF before processing
            if filename.lower().endswith(".pdf"):
                full_pdf_path = os.path.join(pdf_directory, filename)
                result = process_pdf(full_pdf_path)
                print(result)
                print("-" * 20) # Separator for clarity