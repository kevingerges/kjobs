from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://airtable.com/embed/appjDG7vmPOm1pO7S/shrS1OCRlsl1hkXqC/tblLP4AtskrLA8Aw1?viewControls=on")
driver.implicitly_wait(5)

job_titles = driver.find_elements(By.CLASS_NAME, "cell.primary.read")
print("Job Titles:")
num = 0
for job in job_titles:
    print(f"{num}: {job.text}")
    num += 1

driver.quit()
