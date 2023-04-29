# LegalDocketExtractor 
The LegalDocketExtractor is a tool for automating the download of docket PDF files from Delco Court systems. The main purpose of this tool is to extract Mortgage Foreclosure Complaints in Delaware County.

## Extracting Mortgage Foreclosure Complaints in Delaware County using Selenium 
This tool uses Python and the following modules: 
- time: to add delays between browser operations 
- selenium: to automate browser actions 
- pdfExtract: to extract text from the downloaded PDF file
- os: to rename and manipulate files 

### How to use the tool 
1. Install the necessary packages - selenium and pdfminer.
2. Update the URL variable to match the Delaware County Public Access website. 
3. Set the pdf_dir variable to the directory in which to save downloaded PDF files. 
4. Set the path_to_images variable to the directory in which to save extracted images. 
5. Set the pattern variable to match the information to extract from the complaint. 
6. Set the download_folder variable to the path of the folder to download files. 
7. Run the script to download and extract information from the complaint.

### Requirements
In addition to the necessary packages, tessarct must also be installed for using OCR to read the PDF documents. PDF files are initially encrypted which prevents direct OCR. To bypass this issue, a module has been created to use poppler to convert each PDF page into an image file. Then, the module will iterate through all of the image files and use tesseract OCR to read and extract the text from the documents as needed.
