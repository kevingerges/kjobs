from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def initializeWebdriver():
    """Initialize and return the Selenium WebDriver."""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver


def navigateToPage(driver, url):
    """Navigate to the specified URL."""
    driver.get(url)


def extractTableData(driver, todayDate):
    """Extract table data from the page."""
    parentDiv = driver.find_element(By.CSS_SELECTOR, '.dataRightPaneInnerContent.paneInnerContent')
    rows = parentDiv.find_elements(By.CSS_SELECTOR, '.dataRow.rightPane')

    tableData = []
    for row in rows:
        rowData = {}

        # Extract date
        dateCell = row.find_element(By.CSS_SELECTOR, '[data-columnindex="1"] .truncate')
        print(f"Date: {dateCell.text}")
        rowData['date'] = dateCell.text if dateCell else 'N/A'
        if dateCell.text < todayDate:
            break

        #apply link
        try:
            linkCell = row.find_element(By.CSS_SELECTOR, '[data-columnindex="2"] a')
            rowData['apply_link'] = linkCell.get_attribute('href')
        except:
            rowData['apply_link'] = 'N/A'

        #location
        try:
            locationCell = row.find_element(By.CSS_SELECTOR, '[data-columnindex="4"] .truncate')
            rowData['location'] = locationCell.text
        except:
            rowData['location'] = 'N/A'

        tableData.append(rowData)

    return tableData


def scrollAndFetchData(driver, todayDate, maxScrolls=1):
    """Scroll the page and fetch data iteratively."""
    allData = []
    scrollCount = 0

    while scrollCount < maxScrolls:
        print(f"Scroll attempt {scrollCount + 1}")
        tableData = extractTableData(driver, todayDate)
        allData.extend(tableData)

        if len(tableData) == 0:
            break

        driver.execute_script("window.scrollBy(0, 1000);")
        scrollCount += 1

    return allData


def printTableData(tableData):
    """Print extracted table data."""
    rowCount = len(tableData)
    print(f"Total number of rows: {rowCount}")
    rowCounter = 1
    for item in tableData:
        print(f"{rowCounter}: Date: {item['date']}, Apply Link: {item['apply_link']}, Location: {item['location']}")
        rowCounter += 1


def main():
    todayDate = datetime.today().strftime('%Y-%m-%d')
    print(f"Today's date: {todayDate}")

    driver = initializeWebdriver()

    try:
        url = "https://airtable.com/embed/appjDG7vmPOm1pO7S/shrS1OCRlsl1hkXqC/tblLP4AtskrLA8Aw1?viewControls=on"
        navigateToPage(driver, url)

        allData = scrollAndFetchData(driver, todayDate)
        printTableData(allData)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
