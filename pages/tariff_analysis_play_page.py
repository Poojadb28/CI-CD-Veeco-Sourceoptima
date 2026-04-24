import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TariffPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # ---------------- LOCATORS ----------------

    dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")
    tariff_option = (By.XPATH, "//option[normalize-space()='Tariff Analysis']")
    treat_checkbox = (By.XPATH, "//input[contains(@class,'w-4 h-4')]")
    set_top = (By.XPATH, "//button[normalize-space()='Set as Top Level']")
    run_btn = (By.XPATH, "//button[contains(normalize-space(),'Run Tariff Analysis')]")

    # Separate export buttons
    bom_export_btn = (By.XPATH, "(//button[normalize-space()='Export to Excel'])[1]")
    tariff_export_btn = (By.XPATH, "(//button[normalize-space()='Export to Excel'])[2]")

    approve_bom_btn = (By.XPATH, "//span[normalize-space()='Approve BOM']")
    tariff_heading = (By.XPATH, "//h2[contains(text(),'Tariff Analysis')]")

    back_project = (By.XPATH, "//span[normalize-space()='Back to Project']")
    back_btn = (By.XPATH, "//span[normalize-space()='Back']")

    # ---------------- ACTIONS ----------------

    def select_tariff_analysis(self):
        self.wait.until(EC.element_to_be_clickable(self.dropdown)).click()
        self.wait.until(EC.element_to_be_clickable(self.tariff_option)).click()

    def treat_as_assembly(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.treat_checkbox))
        self.driver.execute_script("arguments[0].click();", checkbox)

    def set_top_level(self):
        elements = self.driver.find_elements(*self.set_top)
        if elements:
            self.driver.execute_script("arguments[0].click();", elements[0])

    def run_tariff_analysis(self):
        self.wait.until(EC.element_to_be_clickable(self.run_btn)).click()

    # ---------------- APPROVE BOM ----------------

    # def approve_bom(self):

    #     element = self.wait.until(EC.element_to_be_clickable(self.approve_bom_btn))
    #     self.driver.execute_script("arguments[0].click();", element)

    #     # Wait for tariff page to load
    #     self.wait.until(EC.element_to_be_clickable(self.tariff_export_btn))

    #     print("Tariff page loaded successfully")

    def approve_bom(self):

        element = self.wait.until(EC.element_to_be_clickable(self.approve_bom_btn))
        self.driver.execute_script("arguments[0].click();", element)

        # Wait until old element becomes stale (VERY IMPORTANT)
        old_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Export to Excel']")
        ))

        self.wait.until(EC.staleness_of(old_button))

        # Now wait for new export button
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Export to Excel']")
        ))

    # def export_bom(self, download_dir):

    #     before_files = set(os.listdir(download_dir))

    #     # WAIT until button is clickable (after processing)
    #     button = WebDriverWait(self.driver, 180).until(
    #         EC.element_to_be_clickable(self.bom_export_btn)
    #     )

    #     self.driver.execute_script("arguments[0].scrollIntoView();", button)
    #     self.driver.execute_script("arguments[0].click();", button)

    #     # Wait for download
    #     WebDriverWait(self.driver, 60).until(
    #         lambda d: len(set(os.listdir(download_dir)) - before_files) > 0
    #     )

    #     after_files = set(os.listdir(download_dir))
    #     new_files = after_files - before_files

    #     print("BOM Downloaded:", new_files)

    #     assert new_files, "BOM file not downloaded"

    def export_bom(self, download_dir):

        import time, os

        before_files = set(os.listdir(download_dir))

        button = self.wait.until(EC.element_to_be_clickable(self.bom_export_btn))
        self.driver.execute_script("arguments[0].click();", button)

        end_time = time.time() + 180

        while time.time() < end_time:

            after_files = set(os.listdir(download_dir))
            new_files = after_files - before_files

            # ONLY accept fully downloaded files
            completed = [
                f for f in new_files
                if f.endswith(".xlsx")
            ]

            # ignore .crdownload completely
            if completed:
                print("BOM Downloaded:", completed)
                return

            time.sleep(2)

        raise Exception("BOM download did not complete")


    # ---------------- TARIFF EXPORT ----------------

    # def export_tariff(self, download_dir):

    #     self.wait.until(EC.element_to_be_clickable(self.tariff_export_btn)).click()

    #     WebDriverWait(self.driver, 60).until(
    #         lambda d: any(
    #             f.lower().endswith(".xlsx") and "tariff" in f.lower()
    #             for f in os.listdir(download_dir)
    #         )
    #     )

    #     files = os.listdir(download_dir)

    #     print("Final Files:", files)

    #     assert any(
    #         "tariff" in f.lower() and f.endswith(".xlsx")
    #         for f in files
    #     ), "Tariff file not downloaded"

    def complete_hts_wizard(self):

        import time

        try:
            # Loop to handle multiple steps (important)
            for _ in range(5):

                # check if wizard present
                wizard = self.driver.find_elements(
                    By.XPATH, "//*[contains(text(),'nature of the imported good')]"
                )

                if not wizard:
                    print("Wizard completed fully")
                    return

                # click visible option (label is safer than input)
                options = self.driver.find_elements(
                    By.XPATH, "//label"
                )

                for opt in options:
                    if opt.is_displayed():
                        self.driver.execute_script("arguments[0].click();", opt)
                        break

                # click Continue
                continue_btn = self.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Continue']")
                ))
                self.driver.execute_script("arguments[0].click();", continue_btn)

                time.sleep(2)

        except Exception as e:
            print("Wizard handling skipped:", e)

        time.sleep(5)

    def wait_for_processing_complete(self):

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC

        try:
            # Wait until any loader disappears
            self.wait.until_not(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'animate-spin') or contains(text(),'Processing')]")
            ))
            print("Processing completed")

        except:
            print("No loader found, continuing")

    def export_tariff(self, download_dir):

        import time, os

        before_files = set(os.listdir(download_dir))

        # wait until button appears (after DOM refresh)
        button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(.,'Export to Excel')]")
        ))

        # wait until enabled (no disabled attribute)
        self.wait.until(lambda d: button.get_attribute("disabled") is None)

        # click using JS (safe)
        self.driver.execute_script("arguments[0].click();", button)

        end_time = time.time() + 120

        while time.time() < end_time:

            after_files = set(os.listdir(download_dir))
            new_files = after_files - before_files

            completed = [f for f in new_files if f.endswith(".xlsx")]

            if completed:
                print("Tariff Downloaded:", completed)
                return

            time.sleep(2)

        raise Exception("Tariff download failed")


    # ---------------- NAVIGATION ----------------
    def go_back(self):
        self.wait.until(EC.element_to_be_clickable(self.back_project)).click()
        self.wait.until(EC.element_to_be_clickable(self.back_btn)).click()
        