# form_identification

Automated PDF Form Recognition using OCR

Image Processing on PDFs to understand the type of form/document it is.

This project is a Python script that automates the identification of different form types from a directory of PDF files. It processes each PDF by converting its first page into an image, performing Optical Character Recognition (OCR) to extract the text, and then classifying the form based on predefined keywords.

📜 Project Overview
The goal of this tool is to quickly and automatically sort or identify various forms without manual inspection. For example, it can distinguish between "Form A," "Form B," and "Form C" by reading the text on the first page. This is particularly useful for batch processing large volumes of scanned documents.

✨ Core Features
PDF to Image Conversion: Extracts the first page of a PDF and converts it into a high-resolution image for analysis.

OCR Text Extraction: Uses the Tesseract OCR engine to accurately read and extract text from the page image.

Keyword-Based Classification: Identifies the form type by searching the extracted text for specific, user-defined keywords.

Batch Processing: Automatically scans a specified directory and processes all PDF files within it.

⚙️ How It Works
The script follows a simple and effective workflow:

Scan Directory: The script begins by looking for all .pdf files in a target directory.

Extract First Page: For each PDF, PyMuPDF (fitz) is used to render the first page as a high-quality image object. The script is optimized to only process the first page to save time.

Perform OCR: The powerful Tesseract OCR engine, via the pytesseract library, scans the image and converts any text into a machine-readable string.

Identify Form: The extracted text is converted to lowercase and checked against a predefined list of keywords. If a keyword (e.g., "form a") is found, the script classifies the document and reports the result. If no keywords match, it's labeled as "Unknown Form."

