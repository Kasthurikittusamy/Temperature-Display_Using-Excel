from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import openpyxl
import time

# Set up Chrome WebDriver
service = Service("chromedriver.exe")  # Replace with the actual path to your chromedriver
driver = webdriver.Chrome(service=service)

# Open the HTML file
driver.get("file:///C:/Users/Admin/OneDrive/Desktop/Visual Studio/elgi/index.html")  # Update with the correct file path

# Create Excel report
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Test Results"
sheet.append(["Initial Temperature", "Updated Temperature", "Test Result"])

# Perform test
for _ in range(5):  # Perform multiple refreshes to see variations
    # Find the initial temperature
    initial_temp_element = driver.find_element(By.ID, "temperature-display")
    initial_temp = initial_temp_element.text

    # Click the refresh button
    refresh_button = driver.find_element(By.ID, "refresh-button")
    refresh_button.click()

    # Wait for the update
    time.sleep(1)

    # Find the updated temperature
    updated_temp_element = driver.find_element(By.ID, "temperature-display")
    updated_temp = updated_temp_element.text

    # Check if the temperature has changed
    result = "Pass" if initial_temp != updated_temp else "Fail"

    # Log results in Excel
    sheet.append([initial_temp, updated_temp, result])

# Save the Excel file
workbook.save("acceptance_criteria_results.xlsx")
print("Excel file 'acceptance_criteria_results.xlsx' created successfully.")

# Close the browser
driver.quit()
