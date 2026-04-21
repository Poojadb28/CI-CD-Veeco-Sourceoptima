from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self):
        self.driver.get("https://testing.sourceoptima.com/")

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']"))).click()

    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)

    def click_submit(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()

    def login(self, email, password):
        self.open_url()
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()

    # invalid system admin login error message
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Error during login')]")
            )
        ).text