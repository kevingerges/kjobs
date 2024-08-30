# from datetime import datetime
# from airtable import initializeWebdriver, navigateToPage, scrollAndFetchData, printTableData
#
# def main():
#     # Today's date for comparison
#     todayDate = datetime.today().strftime('%Y-%m-%d')
#     print(f"Today's date: {todayDate}")
#
#     # Initialize WebDriver
#     driver = initializeWebdriver()
#
#     try:
#         # Navigate to the page
#         url = "https://airtable.com/embed/appjDG7vmPOm1pO7S/shrS1OCRlsl1hkXqC/tblLP4AtskrLA8Aw1?viewControls=on"
#         navigateToPage(driver, url)
#
#         # Scroll and fetch data
#         allData = scrollAndFetchData(driver, todayDate)
#
#         # Print extracted data
#         printTableData(allData)
#
#     finally:
#         # Close the WebDriver
#         driver.quit()
#
# if __name__ == "__main__":
#     main()

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver (Assuming you're using Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get('https://airtable.com/embed/appjDG7vmPOm1pO7S/shrS1OCRlsl1hkXqC/tblLP4AtskrLA8Aw1?viewControls=on')  # Replace with your actual URL

# Find all the rows in the table
rows = driver.find_elements(By.CSS_SELECTOR, '.dataRow.rightPane')

# Initialize an array to hold the extracted data
table_data = []

# Loop through each row to extract data
for row in rows:
    row_data = {}

    # Extract date
    date_cell = row.find_element(By.CSS_SELECTOR, '[data-columnindex="1"] .truncate')
    row_data['date'] = date_cell.text if date_cell else 'N/A'

    # Extract apply link
    try:
        link_cell = row.find_element(By.CSS_SELECTOR, '[data-columnindex="2"] a')
        row_data['apply_link'] = link_cell.get_attribute('href')
    except:
        row_data['apply_link'] = 'N/A'

    # Extract job type
    try:
        job_type_cell = row.find_element(By.CSS_SELECTOR, '[data-columnindex="3"] .truncate-pre')
        row_data['job_type'] = job_type_cell.text
    except:
        row_data['job_type'] = 'N/A'

    # Extract location
    try:
        location_cell = row.find_element(By.CSS_SELECTOR, '[data-columnindex="4"] .truncate')
        row_data['location'] = location_cell.text
    except:
        row_data['location'] = 'N/A'

    # Add the extracted data to the list
    table_data.append(row_data)

# Close the WebDriver
driver.quit()

# Print the extracted data
for item in table_data:
    print(item)
