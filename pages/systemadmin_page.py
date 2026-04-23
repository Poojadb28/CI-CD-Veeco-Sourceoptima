from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SystemAdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ================= LOCATORS ================= #

    # Navigation
    USER_ADMIN = (By.XPATH, "//button[normalize-space()='User Admin View']")
    CREATE_USER = (By.XPATH, "//button[normalize-space()='Create User']")

    # Available Plays
    AVAILABLE_PLAYS_SECTION = (By.XPATH, "//h2[normalize-space()='Available Plays']")
    DISABLE_MSG = (By.XPATH, "//div[contains(text(),'Play disabled successfully')]")
    ENABLE_MSG = (By.XPATH, "//div[contains(text(),'Play enabled successfully')]")

    # ================= GENERIC METHODS ================= #

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text.strip()

    # ================= NAVIGATION ================= #

    def open_user_admin(self):
        self.click(self.USER_ADMIN)
        self.wait.until(EC.visibility_of_element_located(self.CREATE_USER))

    # ================= AVAILABLE PLAYS ================= #

    def go_to_available_plays(self):
        section = self.wait.until(
            EC.visibility_of_element_located(self.AVAILABLE_PLAYS_SECTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", section)

    def toggle_play(self, play_name):

        print(f"Toggling: {play_name}")

        toggle = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//h3[normalize-space()='{play_name}']"
                f"/ancestor::div[contains(@class,'rounded-lg')]"
                f"//button[contains(@class,'inline-flex')]"
            ))
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", toggle)
        self.driver.execute_script("arguments[0].click();", toggle)

    def get_disable_message(self):
        return self.get_text(self.DISABLE_MSG)

    def get_enable_message(self):
        return self.get_text(self.ENABLE_MSG)