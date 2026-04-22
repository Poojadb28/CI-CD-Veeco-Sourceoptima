from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProjectPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_projects(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Projects']"))).click()

    # def right_click_on_canvas(self):
    #     page_body = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'flex-1 overflow-auto p-8 relative')]")))
    #     ActionChains(self.driver).move_to_element(page_body).context_click(page_body).perform()

    def right_click_on_canvas(self):

        canvas = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'flex-1')]")
        ))

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", canvas)

        ActionChains(self.driver)\
            .move_to_element(canvas)\
            .pause(1)\
            .context_click(canvas)\
            .perform()

        # VERY IMPORTANT: wait for menu to appear
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'New Root Space')]")
        ))

    # def click_new_root_space(self):
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='New Root Space']"))).click()

    # def click_new_root_space(self):
    #     import time
    #     time.sleep(2)

    #     elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'New Root Space')]")

    #     for el in elements:
    #         if el.is_displayed():
    #             self.driver.execute_script("arguments[0].click();", el)
    #             return

    #     raise Exception("New Root Space option not found")

    def click_new_root_space(self):
        # Wait until context menu is visible
        menu = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//*[contains(text(),'New Root Space')]")
        ))

        for el in menu:
            if el.is_displayed():
                self.driver.execute_script("arguments[0].click();", el)
                return

        raise Exception("New Root Space option not found")

    def enter_space_name(self, name):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='e.g. Finance, Project Alpha...']"))).send_keys(name)

    def open_icon_selector(self):
        icon_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//*[name()='svg' and contains(@class,'w-5')]]")))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", icon_button)
        self.driver.execute_script("arguments[0].click();", icon_button)

    def select_color(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Blue']"))).click()

    def click_create_space(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Space']"))).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Space created successfully')]"))).text
    
   # ================= SUB SPACE ================= #

    def right_click_root_space(self, name):
        from selenium.webdriver.common.action_chains import ActionChains

        locator = (By.XPATH, f"//h4[normalize-space()='{name}']")

        element = self.wait.until(EC.visibility_of_element_located(locator))

        # scroll to element
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

        # re-fetch (avoid stale element)
        element = self.driver.find_element(*locator)

        # right click
        ActionChains(self.driver).move_to_element(element).pause(1).context_click(element).perform()


    def click_add_sub_space(self):
        import time
        time.sleep(2)  # wait for context menu

        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Add Sub')]")

        for el in elements:
            if el.is_displayed():
                self.driver.execute_script("arguments[0].click();", el)
                return

        raise Exception("Add Sub Space option not found")


    def enter_sub_space_name(self, name):
        field = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='e.g. Finance, Project Alpha...']")
        ))
        field.clear()
        field.send_keys(name)


    def choose_icon(self):
        icon = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[.//*[name()='svg']]")
        ))
        self.driver.execute_script("arguments[0].click();", icon)


    def select_color(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@title='Blue']")
        )).click()


    def click_create_space(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Create Space']")
        ))
        self.driver.execute_script("arguments[0].click();", btn)


    def verify_sub_space_created(self, name):
        locator = (By.XPATH, f"//h4[normalize-space()='{name}']")
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
    
    # ================= DELETE ROOT SPACE ================= #

    # def right_click_root_space(self, name):
    #     from selenium.webdriver.common.action_chains import ActionChains

    #     locator = (By.XPATH, f"//h4[normalize-space()='{name}']")

    #     element = self.wait.until(EC.visibility_of_element_located(locator))

    #     self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

    #     element = self.driver.find_element(*locator)

    #     ActionChains(self.driver).move_to_element(element).pause(1).context_click(element).perform()


    def click_delete_space(self):
        import time
        time.sleep(2)

        elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Delete')]")

        for el in elements:
            if el.is_displayed():
                self.driver.execute_script("arguments[0].click();", el)
                return

        raise Exception("Delete option not found")


    def confirm_delete_space(self):
        from selenium.webdriver.common.alert import Alert

        # wait for alert
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        print("Alert text:", alert.text)  

        alert.accept()  # click OK

    def verify_space_deleted(self, name):
        return self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//div[contains(text(),'Space \"{name}\" deleted successfully')]")
        )).is_displayed()