from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Specify the path to the downloaded chromedriver.exe
driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

# Create a new instance of the Chrome driver using ChromeService
# Create ChromeOptions object
chrome_options = Options()

# Enable headless mode
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--enable-logging")
# chrome_options.add_argument("--v=1")

driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)

# Navigate to the Text Box page
driver.get("https://demoqa.com/text-box")

# Fill in the text box fields
driver.find_element(By.ID, "userName").send_keys("John Doe")
driver.find_element(By.ID, "userEmail").send_keys("johndoe@example.com")
driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street")
driver.find_element(By.ID, "permanentAddress").send_keys("456 Park Avenue")

# Submit the form
driver.find_element(By.ID, "submit").click()

# Wait for a few seconds to see the result
driver.implicitly_wait(3)

# Get values from the output
# Get values from the output using XPath

output_name = driver.find_element(By.ID, "name").text
output_email = driver.find_element(By.ID, "email").text
output_current_address = driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
output_permanent_address = driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text


# Verify the values
print (f"Output", output_name, output_email, output_current_address, output_permanent_address)

assert output_name == "Name:John Doe1"

# Close the browser
driver.quit()
