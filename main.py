import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pdfExtract import download_wait

pdf_dir = "pdf_files"
path_to_images = 'pages/'
pattern = r'Address ofMortgaged Property\s(.*\n.*\d{5})'  # Example pattern to extract social security numbers
download_folder = "C:\\Users\\rmwen\\PycharmProjects\\Extractor\\pdf_files"

# Set up the Selenium webdriver and the necessary options
profile = {"plugins.plugins_list": [{"enabled": False,
                                     "name": "Chrome PDF Viewer"}],
           "download.default_directory": download_folder,
           "download.extensions_to_open": "",
           "plugins.always_open_pdf_externally": True}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)

# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Define constants
URL = "https://delcopublicaccess.co.delaware.pa.us/login"

# Load Delco Public Access
driver.get(URL)

# Click TOS Agreement
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='app']/div/main/div/div/div[2]/div/div/div/div[2]/button/div"))).click()

# Click Party Search
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='app']/div[3]/main/div/div/div[2]/div[2]/div/div[5]/div/div[3]/a/div"))).click()

# Input Party Search Term
# input_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
# "//*[@id='app']/div[3]/main/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[1]/input")))
# input_text = "a"
# input_box.send_keys(input_text)

# Click Party Search
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='app']/div[3]/main/div/div/div[1]/div[2]/div/div/div[2]/div[2]/button[1]/div"))).click()
time.sleep(1)

# Activate Real Property Check Box
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='app']/div[3]/main/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div/div"))).click()
time.sleep(1)

# Activate Year filter *2023
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='app']/div[3]/main/div/div/div[2]/div/div[1]/div/div[2]/div[19]/div/div"))).click()
time.sleep(1)

# Locate the table using its XPath
table_xpath = "//*[@id='results-table']/div[1]/table/tbody"

# Find all rows in the table
rows_xpath = f"{table_xpath}/tr"
rows = driver.find_elements(By.XPATH, rows_xpath)

# Iterate through the rows and search for the text "Mortgage Foreclosure: Residential"
for row in rows:
    if "Mortgage Foreclosure: Residential" in row.text:
        # Find the table data with the href, replace the XPath expression accordingly
        link_element = row.find_element(By.XPATH, ".//td/a")
        case_num = row.text.split()[3]
        print('Case Number: {}\n'.format(case_num))

        # Open the href attached to the table data
        link = link_element.get_attribute("href")
        print('Case Link: {}\n'.format(link))
        driver.get(link)

        # Click Docket Tab
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='app']/div[3]/main/div/div/div/div[3]/div/div[1]/div/div/div/div[3]/a"))).click()

        time.sleep(1)

        # Locate the docket table using its XPath
        d_table_xpath = "//*[@id='app']/div[3]/main/div/div/div/div[3]/div/div[2]/div/div[1]/div[1]/table/tbody"

        # Find all rows in the table
        d_rows_xpath = f"{d_table_xpath}/tr"
        d_rows = driver.find_elements(By.XPATH, d_rows_xpath)
        d_rc = 1

        for d_row in d_rows:
            if "Complaint" in d_row.text:

                # Xpath to Document View
                d_xpath = "//*[@id='app']/div[3]/main/div/div/div/div[3]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[" \
                          "{}]/td[5]/button/div".format(d_rc)

                # Open Document View
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, d_xpath))).click()

                time.sleep(2)

                v_rows = driver.find_elements(By.XPATH, "//*[@id='app']/div[1]/div/div/div[1]/div/div/table/tbody/tr")

                for v_row in v_rows:
                    # if "Complaint" in v_row.text: //removing loop for now, might not need.

                    v_link_element = v_row.find_element(By.XPATH, ".//td/a")
                    v_link = v_link_element.get_attribute("href")
                    print('Document Link: {}\n'.format(v_link))
                    # hash_num = random.getrandbits(128)

                    if v_link:
                        # old_filename = 'pdf_files/Initial Filing - Complaint.pdf'
                        # new_filename = 'pdf_files/{}_{}_{}.pdf'.format(case_num, v_row.text.split()[3], hash_num)

                        driver.get(v_link)
                        dl = download_wait(download_folder, 30)

                        # if os.path.exists(old_filename):
                        #     os.rename(old_filename, new_filename)
                        # else:
                        #     print("File not found:", old_filename)

                        # Go back from Download
                        if dl is not None:
                            driver.back()

                time.sleep(2)
                # Go back from Document View
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='app']/div[1]/div/div/div[2]/div/div/div[2]/button/div"))).click()

        d_rc += 1

        # Return to the previous page
        driver.back()

# iterate_and_extract(pdf_dir)
# capture_and_extract_images(path_to_images)
