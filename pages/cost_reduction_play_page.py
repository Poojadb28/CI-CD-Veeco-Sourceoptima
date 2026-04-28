# import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# class CostReductionPage:

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 120)

#     # LOCATORS (Stable)
#     dropdown = (By.XPATH, "//select")
#     option = (By.XPATH, "//option[contains(.,'Cost Reduction')]")
#     run_button = (By.XPATH, "//button[contains(.,'Run')]")
#     view_results = (By.XPATH, "//button[contains(.,'View Results')]")
#     view_details = (By.XPATH, "//button[contains(.,'View Details')]")
#     report_tab = (By.XPATH,"//div[contains(@class,'fixed')]//button[normalize-space()='Cost Reduction']")
#     active_report_tab = (By.XPATH,"//div[contains(@class,'fixed')]//button[contains(@class,'border-green-800') and normalize-space()='Cost Reduction']")
#     popup_overlay = (By.XPATH, "//div[contains(@class,'fixed')]")
#     close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

#     # ACTIONS

#     # def select_cost_reduction(self):
#     #     dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown))
#     #     dropdown.click()

#     #     self.wait.until(lambda d: len(dropdown.find_elements(By.TAG_NAME, "option")) > 1)

#     #     # self.wait.until(EC.element_to_be_clickable(self.option)).click()
#     #     element = self.wait.until(EC.presence_of_element_located(self.option))

#     #     # Wait until visible
#     #     self.wait.until(EC.visibility_of(element))

#     #     # Scroll into view (important for headless)
#     #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

#     #     # Try normal click first
#     #     try:
#     #         element.click()
#     #     except:
#     #         # Fallback to JS click (very common CI fix)
#     #         self.driver.execute_script("arguments[0].click();", element)

#     # def select_cost_reduction(self):

#     #     # Step 1: Wait for page load
#     #     self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#     #     # Step 2: Wait until loader/spinner disappears (VERY IMPORTANT)
#     #     try:
#     #         self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'loader')]")))
#     #     except:
#     #         pass  # if no loader, continue

#     #     # Step 3: Wait until files are actually stable
#     #     self.wait.until(lambda d: len(d.find_elements(By.XPATH, "//input[@type='checkbox']")) > 0)

#     #     # Step 4: Now wait for Cost Reduction tab
#     #     cost_tab = (By.XPATH, "//button[normalize-space()='Cost Reduction']")

#     #     element = self.wait.until(EC.presence_of_element_located(cost_tab))
#     #     self.wait.until(EC.visibility_of(element))

#     #     # Scroll (important in headless)
#     #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

#     #     # Click safely
#     #     try:
#     #         element.click()
#     #     except:
#     #         self.driver.execute_script("arguments[0].click();", element)

#     def select_cost_reduction(self):

#         cost_tab = (By.XPATH, "//button[normalize-space()='Cost Reduction']")

#         # Step 1: Try to find element safely (no immediate failure)
#         elements = self.driver.find_elements(*cost_tab)

#         if not elements:
#             # Debug info (VERY IMPORTANT)
#             print("Cost Reduction tab NOT found in UI")
#             self.driver.save_screenshot("screenshots/cost_tab_missing.png")

#             raise Exception("Cost Reduction tab not available - processing incomplete or feature not loaded")

#         element = elements[0]

#         # Step 2: Wait for visibility
#         self.wait.until(EC.visibility_of(element))

#         # Step 3: Scroll (headless fix)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

#         # Step 4: Safe click
#         try:
#             element.click()
#         except:
#             self.driver.execute_script("arguments[0].click();", element)
        
#     def click_run(self):
#         run_btn = self.wait.until(EC.element_to_be_clickable(self.run_button))
#         self.wait.until(lambda d: run_btn.is_enabled())

#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", run_btn)
#         self.driver.execute_script("arguments[0].click();", run_btn)

#     def wait_for_processing(self):
#         self.wait.until(EC.element_to_be_clickable(self.view_results))

#     def click_view_results(self):
#         btn = self.wait.until(EC.element_to_be_clickable(self.view_results))
#         self.driver.execute_script("arguments[0].click();", btn)

#     def click_view_details(self):
#         btn = self.wait.until(EC.element_to_be_clickable(self.view_details))
#         self.driver.execute_script("arguments[0].click();", btn)

#     # def open_report_tab(self):

#     #     # Handle optional popup safely
#     #     try:
#     #         self.wait.until(EC.presence_of_element_located(self.popup_overlay))
#     #     except:
#     #         pass

#     #     element = self.wait.until(EC.element_to_be_clickable(self.report_tab))
#     #     self.driver.execute_script("arguments[0].click();", element)

#     def open_report_tab(self):

#         # Wait for popup
#         self.wait.until(
#             EC.presence_of_element_located(self.popup_overlay)
#         )

#         # Click tab
#         tab = self.wait.until(
#             EC.element_to_be_clickable(self.report_tab)
#         )

#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", tab)
#         self.driver.execute_script("arguments[0].click();", tab)

#         # VERIFY TAB SWITCH (THIS FIXES YOUR ISSUE)
#         self.wait.until(
#             EC.presence_of_element_located(self.active_report_tab)
#         )

#     def take_screenshot(self):
#         os.makedirs("screenshots", exist_ok=True)
#         self.driver.save_screenshot("screenshots/Cost_Reduction_Report.png")

#     def close_popup(self):
#         element = self.wait.until(EC.element_to_be_clickable(self.close_icon))
#         self.driver.execute_script("arguments[0].click();", element)

#         self.wait.until(EC.element_to_be_clickable(self.dropdown))

import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CostReductionPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # LOCATORS
    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    option = (By.XPATH, "//option[normalize-space()='Cost Reduction']")
    # run_button = (By.XPATH, "//button[contains(text(),'Run Cost Reduction')]")
    run_button = (By.XPATH, "//button[contains(.,'Run')]")
    view_results = (By.XPATH, "//button[normalize-space()='View Results']")
    view_details = (By.XPATH, "//button[normalize-space()='View Details']")
    # report_tab = (By.XPATH, "//button[normalize-space()='Cost Reduction']")
    report_tab = (By.XPATH, "//button[contains(.,'Report') or contains(.,'Cost')]")
    popup_overlay = (By.XPATH, "//div[contains(@class,'fixed inset-0')]")
    close_icon = (By.XPATH, "//button[contains(@class,'p-2')]")

    # =========================
    # ACTIONS
    # =========================

    def select_cost_reduction(self):

        # Step 1: Wait for dropdown
        dropdown = self.wait.until(EC.presence_of_element_located(self.dropdown))
        self.wait.until(EC.visibility_of(dropdown))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)

        # Step 2: Wait until dropdown is enabled (IMPORTANT)
        self.wait.until(lambda d: dropdown.is_enabled())

        # Step 3: Click dropdown
        dropdown.click()

        # Step 4: WAIT until options are populated (STRONG FIX)
        self.wait.until(lambda d: any(
            opt.text.strip() != "" for opt in d.find_elements(By.XPATH, "//option")
        ))

        options = self.driver.find_elements(By.XPATH, "//option")

        print("Available options:", [opt.text for opt in options])

        # Step 5: Select correct option
        for opt in options:
            if "Cost Reduction" in opt.text:
                self.driver.execute_script("arguments[0].click();", opt)
                return

        # Step 6: Debug if not found
        self.driver.save_screenshot("screenshots/no_option.png")
        raise Exception("Cost Reduction option NOT found")

    def click_run(self):

        # Step 1: Wait until ANY Run button appears
        run_btn = self.wait.until(
            lambda d: d.find_element(By.XPATH, "//button[contains(.,'Run')]")
        )

        # Step 2: Wait until enabled
        self.wait.until(lambda d: run_btn.is_enabled())

        # Step 3: Scroll (headless fix)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", run_btn)

        # Step 4: Click safely
        try:
            run_btn.click()
        except:
            self.driver.execute_script("arguments[0].click();", run_btn)

    def wait_for_processing(self):
        self.wait.until(EC.element_to_be_clickable(self.view_results))

    def click_view_results(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.view_results))
        self.driver.execute_script("arguments[0].click();", btn)

    def click_view_details(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.view_details))
        self.driver.execute_script("arguments[0].click();", btn)

    def open_report_tab(self):

        # Wait for popup
        self.wait.until(EC.presence_of_element_located(self.popup_overlay))

        # Find all buttons in popup
        buttons = self.driver.find_elements(By.XPATH, "//button")

        print("Available popup buttons:", [b.text for b in buttons])

        target = None
        for b in buttons:
            if "Report" in b.text or "Cost" in b.text:
                target = b
                break

        if not target:
            self.driver.save_screenshot("screenshots/report_tab_missing.png")
            raise Exception("Report tab not found in popup")

        self.driver.execute_script("arguments[0].click();", target)

    def take_screenshot(self):
        os.makedirs("screenshots", exist_ok=True)

        file_path = os.path.abspath(f"screenshots/Cost_Reduction_{int(time.time())}.png")

        self.driver.save_screenshot(file_path)

        print(f"Screenshot saved at: {file_path}")

    def close_popup(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.close_icon))
        self.driver.execute_script("arguments[0].click();", btn)