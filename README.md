# LegalDocketExtractor
Automation for downloading docket PDF information from Delco Court systems. This was a request for someone who needed a tool to pull all of the foreclosure documents.

Extracting Mortgage Foreclosure Complaints in Delaware County using Selenium
This code extracts Mortgage Foreclosure Complaints in Delaware County using Selenium. The script navigates to the Delaware County Public Access website, searches for Mortgage Foreclosure cases, selects and downloads the initial complaint document, and extracts information from the complaint.

The code uses the following Python modules:

time: to add delays between browser operations
selenium: to automate browser actions
pdfExtract: to extract text from the downloaded PDF file
os: to rename and manipulate files
How to use the code
Install the necessary packages - selenium and pdfminer.
Update the URL variable to match the Delaware County Public Access website.
Set the pdf_dir variable to the directory in which to save downloaded PDF files.
Set the path_to_images variable to the directory in which to save extracted images.
Set the pattern variable to match the information to extract from the complaint.
Set the download_folder variable to the path of the folder to download files.
Run the script to download and extract information from the complaint.

Outside of the requirements, you also need to install tessarct for using OCR to read the PDF documents. PDF files are initially encrypted which prevents direct OCR. To bypass this issue I created a module that will use poppler to convert each PDF page into an image file. The tesseract OCR will read the image files which you can then search, or export text from the documents.
