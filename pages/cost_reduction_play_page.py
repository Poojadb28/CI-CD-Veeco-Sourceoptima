import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CostReductionPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # LOCATORS (Stable)
    dropdown = (By.XPATH, "//select")
    option = (By.XPATH, "//option[contains(.,'Cost Reduction')]")
    run_button = (By.XPATH, "//button[contains(.,'Run')]")
    view_results = (By.XPATH, "//button[contains(.,'View Results')]")
    view_details = (By.XPATH, "//button[contains(.,'View Details')]")
    report_tab = (By.XPATH,"//div[contains(@class,'fixed')]//button[normalize-space()='Cost Reduction']")
    active_report_tab = (By.XPATH,"//div[contains(@class,'fixed')]//button[contains(@class,'border-green-800') and normalize-space()='Cost Reduction']")
    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed')]")
    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    # ACTIONS

    def select_cost_reduction(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown))
        dropdown.click()

        self.wait.until(lambda d: len(dropdown.find_elements(By.TAG_NAME, "option")) > 1)

        self.wait.until(EC.element_to_be_clickable(self.option)).click()

    def click_run(self):
        run_btn = self.wait.until(EC.element_to_be_clickable(self.run_button))
        self.wait.until(lambda d: run_btn.is_enabled())

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", run_btn)
        self.driver.execute_script("arguments[0].click();", run_btn)

    def wait_for_processing(self):
        self.wait.until(EC.element_to_be_clickable(self.view_results))

    def click_view_results(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.view_results))
        self.driver.execute_script("arguments[0].click();", btn)

    def click_view_details(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.view_details))
        self.driver.execute_script("arguments[0].click();", btn)

    # def open_report_tab(self):

    #     # Handle optional popup safely
    #     try:
    #         self.wait.until(EC.presence_of_element_located(self.popup_overlay))
    #     except:
    #         pass

    #     element = self.wait.until(EC.element_to_be_clickable(self.report_tab))
    #     self.driver.execute_script("arguments[0].click();", element)

    def open_report_tab(self):

        # Wait for popup
        self.wait.until(
            EC.presence_of_element_located(self.popup_overlay)
        )

        # Click tab
        tab = self.wait.until(
            EC.element_to_be_clickable(self.report_tab)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", tab)
        self.driver.execute_script("arguments[0].click();", tab)

        # VERIFY TAB SWITCH (THIS FIXES YOUR ISSUE)
        self.wait.until(
            EC.presence_of_element_located(self.active_report_tab)
        )

    def take_screenshot(self):
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot("screenshots/Cost_Reduction_Report.png")

    def close_popup(self):
        element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
        self.driver.execute_script("arguments[0].click();", element)

        self.wait.until(EC.element_to_be_clickable(self.dropdown))