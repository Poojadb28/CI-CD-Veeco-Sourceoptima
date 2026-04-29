# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# class UserAdminPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 120)

#     # def wait_for_page_load(self):
#     #     self.wait.until(
#     #         lambda d: d.execute_script("return document.readyState") == "complete"
#     #     )

#     def click_user_admin_view(self):
#         # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='User Admin View']"))).click()
#         button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='User Admin View']")))
#         self.driver.execute_script("arguments[0].click();", button)

#     def click_create_user(self):
#         # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create User']"))).click()
#         button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create User']")))
#         self.driver.execute_script("arguments[0].click();", button)
#         self.wait.until(
#             EC.visibility_of_element_located((By.XPATH, "//*[normalize-space()='Create New User' or normalize-space()='Cancel']"))
#         )

#     def click_cancel(self):
#         # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel']"))).click()
#         locators = [
#             (By.XPATH, "//button[normalize-space()='Cancel']"),
#             (By.XPATH, "//div[contains(@class,'fixed') or contains(@class,'z-50')]//button[normalize-space()='Cancel']"),
#             (By.XPATH, "//button[@type='button' and normalize-space()='Cancel']")
#         ]

#         self.wait.until(lambda d: any(
#             element.is_displayed()
#             for locator in locators
#             for element in d.find_elements(*locator)
#         ))

#         for locator in locators:
#             elements = self.driver.find_elements(*locator)
#             for element in elements:
#                 if element.is_displayed():
#                     self.driver.execute_script("arguments[0].click();", element)
#                     return

#     def enter_full_name(self, name):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter full name (e.g., John Doe)']"))).send_keys(name)

#     def enter_email(self, email):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='user@example.com']"))).send_keys(email)

#     def enter_password(self, password):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter secure password']"))).send_keys(password)

#     def enter_confirm_password(self, password):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Re-enter password']"))).send_keys(password)


#     def select_user_role(self, role_name):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'w-full')]"))).click()

#         self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[contains(text(),'{role_name}')]"))).click()

#     # def submit_user(self):
#     #     self.wait.until(EC.element_to_be_clickable(
#     #         (By.XPATH, "//button[@type='submit']")
#     #     )).click()
    
#     def submit_user(self):
#         import time

#         # wait until button is present
#         submit_btn = self.wait.until(EC.presence_of_element_located(
#             (By.XPATH, "//button[@type='submit']")
#         ))

#         # scroll into view
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)

#         # small wait for UI (VERY IMPORTANT)
#         time.sleep(2)

#         # force click using JavaScript (FINAL FIX)
#         self.driver.execute_script("arguments[0].click();", submit_btn)

#     # def get_success_message(self):
#     #     return self.wait.until(EC.visibility_of_element_located(
#     #         (By.XPATH, "//div[text()='User created successfully']")
#     #     )).text

#     def get_success_message(self):
#         return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'User created')]"))).text
    
#     def get_duplicate_error(self):
#         return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Failed to create user')]"))).text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserAdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # ================= COMMON ================= #

    def wait_for_page_load(self):
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_for_loader(self):
        try:
            self.wait.until(
                EC.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'fixed inset-0')]")
                )
            )
        except:
            pass

    def safe_click(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    # ================= NAVIGATION ================= #

    def click_user_admin_view(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='User Admin View']"))
        )
        self.safe_click(button)

        self.wait_for_page_load()
        self.wait_for_loader()

    # ================= CREATE USER ================= #

    def click_create_user(self):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create User']"))
        )
        self.safe_click(button)

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[normalize-space()='Create New User' or normalize-space()='Cancel']")
            )
        )

    def click_cancel(self):
        locators = [
            (By.XPATH, "//button[normalize-space()='Cancel']"),
            (By.XPATH, "//div[contains(@class,'fixed') or contains(@class,'z-50')]//button[normalize-space()='Cancel']"),
            (By.XPATH, "//button[@type='button' and normalize-space()='Cancel']")
        ]

        for locator in locators:
            elements = self.driver.find_elements(*locator)
            for el in elements:
                if el.is_displayed():
                    self.safe_click(el)
                    self.wait_for_loader()
                    return

        raise Exception("Cancel button not found")

    # ================= FORM INPUT ================= #

    def enter_full_name(self, name):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter full name (e.g., John Doe)']")
            )
        )
        field.clear()
        field.send_keys(name)

    def enter_email(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='user@example.com']")
            )
        )
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter secure password']")
            )
        )
        field.clear()
        field.send_keys(password)

    def enter_confirm_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Re-enter password']")
            )
        )
        field.clear()
        field.send_keys(password)

    def select_user_role(self, role_name):
        dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'w-full')]"))
        )
        self.safe_click(dropdown)

        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//option[contains(text(),'{role_name}')]"))
        )
        option.click()

    # ================= SUBMIT ================= #

    def submit_user(self):
        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

        self.safe_click(submit_btn)

        # wait for either success or error
        self.wait.until(
            lambda d: (
                len(d.find_elements(By.XPATH, "//div[contains(text(),'User created')]")) > 0
                or len(d.find_elements(By.XPATH, "//div[contains(text(),'Failed to create user')]")) > 0
            )
        )

        self.wait_for_loader()

    # ================= VALIDATION ================= #

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'User created')]")
            )
        ).text

    def get_duplicate_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Failed to create user')]")
            )
        ).text