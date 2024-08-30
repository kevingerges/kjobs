# from datetime import datetime
# from airtable import initializeWebdriver, navigateToPage, scrollAndFetchData, printTableData
#
# def main():
#     todayDate = datetime.today().strftime('%Y-%m-%d')
#     print(f"Today's date: {todayDate}")
#
#     driver = initializeWebdriver()
#
#     try:
#         url = "https://airtable.com/embed/appjDG7vmPOm1pO7S/shrS1OCRlsl1hkXqC/tblLP4AtskrLA8Aw1?viewControls=on"
#         navigateToPage(driver, url)
#
#         allData = scrollAndFetchData(driver, todayDate)
#
#         printTableData(allData)
#
#     finally:
#         driver.quit()
#
# if __name__ == "__main__":
#     main()