# import time
# import os

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains


# class ProjectPage:

#     # upload_popup_locator = (By.XPATH, "//button[normalize-space()='New Upload']")
#     # file_upload_input = (By.XPATH, "//input[@type='file']")
#     upload_popup_locator = (By.XPATH, "//button[normalize-space()='New Upload']")
#     file_upload_input = (By.XPATH, "//input[@type='file']")

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 30)

#     def wait_for_page_load(self):
#         self.wait.until(
#             lambda d: d.execute_script("return document.readyState") == "complete"
#         )

#     def click_projects(self):
#         # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Projects']"))).click()
#         projects = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Projects']")))
#         self.driver.execute_script("arguments[0].click();", projects)
#         self.wait_for_page_load()
#         # self.wait.until(
#         #     lambda d: "Organization Structure" in d.find_element(By.TAG_NAME, "body").text
#         # )
#         self.wait.until(
#             lambda d: "OrgChart" in d.current_url
#             or "Organization Structure" in d.find_element(By.TAG_NAME, "body").text
#         )
#         # self.wait.until(
#         #     lambda d: "Loading" not in d.find_element(By.TAG_NAME, "body").text
#         # )
#         self.wait.until(
#             lambda d: "Loading" not in d.find_element(By.TAG_NAME, "body").text
#         )

#     # def right_click_on_canvas(self):
#     #     page_body = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'flex-1 overflow-auto p-8 relative')]")))
#     #     ActionChains(self.driver).move_to_element(page_body).context_click(page_body).perform()

#     def right_click_on_canvas(self):

#         # canvas = self.wait.until(EC.visibility_of_element_located(
#         #     (By.XPATH, "//div[contains(@class,'flex-1')]")
#         # ))
#         #
#         # self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", canvas)
#         #
#         # ActionChains(self.driver)\
#         #     .move_to_element(canvas)\
#         #     .pause(1)\
#         #     .context_click(canvas)\
#         #     .perform()

#         canvas_locators = [
#             (By.XPATH, "//div[contains(@class,'react-flow')]"),
#             (By.XPATH, "//div[contains(@class,'overflow-auto') and contains(@class,'relative')]"),
#             (By.XPATH, "//div[contains(@class,'flex-1') and contains(@class,'relative')]"),
#             (By.XPATH, "//main"),
#         ]

#         canvas = None
#         for locator in canvas_locators:
#             elements = self.driver.find_elements(*locator)
#             visible = [element for element in elements if element.is_displayed()]
#             if visible:
#                 canvas = visible[-1]
#                 break

#         if canvas is None:
#             canvas = self.wait.until(EC.visibility_of_element_located(
#                 (By.XPATH, "//div[contains(@class,'flex-1')]")
#             ))

#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", canvas)

#         rect = canvas.rect
#         try:
#             ActionChains(self.driver)\
#                 .move_to_element_with_offset(canvas, int(rect["width"] * 0.65), int(rect["height"] * 0.25))\
#                 .pause(1)\
#                 .context_click()\
#                 .perform()
#         except Exception:
#             self.driver.execute_script(
#                 """
#                 const el = arguments[0];
#                 const rect = el.getBoundingClientRect();
#                 const x = rect.left + rect.width * 0.65;
#                 const y = rect.top + rect.height * 0.25;
#                 el.dispatchEvent(new MouseEvent('contextmenu', {
#                     bubbles: true,
#                     cancelable: true,
#                     view: window,
#                     clientX: x,
#                     clientY: y
#                 }));
#                 """,
#                 canvas
#             )

#         # VERY IMPORTANT: wait for menu to appear
#         self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//*[contains(text(),'New Root Space')]")
#         ))

#     # def right_click_on_canvas(self):

#     #     canvas = self.wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH, "//div[contains(@class,'react-flow')]")
#     #         )
#     #     )

#     #     # scroll to canvas
#     #     self.driver.execute_script(
#     #         "arguments[0].scrollIntoView({block:'center'});", canvas
#     #     )

#     #     import time
#     #     time.sleep(2)  

#     #     ActionChains(self.driver).move_to_element(canvas).context_click().perform()

#     #     # wait for menu
#     #     self.wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH, "//span[contains(text(),'New Root Space')]")
#     #         )
#     #     )

#     # def click_new_root_space(self):
#     #     self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='New Root Space']"))).click()

#     # def click_new_root_space(self):
#     #     import time
#     #     time.sleep(2)

#     #     elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'New Root Space')]")

#     #     for el in elements:
#     #         if el.is_displayed():
#     #             self.driver.execute_script("arguments[0].click();", el)
#     #             return

#     #     raise Exception("New Root Space option not found")

#     def click_new_root_space(self):
#         # Wait until context menu is visible
#         menu = self.wait.until(EC.visibility_of_all_elements_located(
#             (By.XPATH, "//*[contains(text(),'New Root Space')]")
#         ))

#         for el in menu:
#             if el.is_displayed():
#                 self.driver.execute_script("arguments[0].click();", el)
#                 return

#         raise Exception("New Root Space option not found")

#     # def enter_space_name(self, name):
#     #     self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='e.g. Finance, Project Alpha...']"))).send_keys(name)

#     def enter_space_name(self, name):
#         field = self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//input[@placeholder='e.g. Finance, Project Alpha...']")
#             )
#         )
#         field.clear()
#         field.send_keys(name)

#     def open_icon_selector(self):
#         icon_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[.//*[name()='svg' and contains(@class,'w-5')]]")))
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", icon_button)
#         self.driver.execute_script("arguments[0].click();", icon_button)

#     def select_color(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Blue']"))).click()

#     def click_create_space(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Space']"))).click()

#     def get_success_message(self):
#         return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Space created successfully')]"))).text
    
#    # ================= SUB SPACE ================= #

#     # def right_click_root_space(self, name):
#     #     from selenium.webdriver.common.action_chains import ActionChains

#     #     locator = (By.XPATH, f"//h4[normalize-space()='{name}']")

#     #     element = self.wait.until(EC.visibility_of_element_located(locator))

#     #     # scroll to element
#     #     self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

#     #     # re-fetch (avoid stale element)
#     #     element = self.driver.find_element(*locator)

#     #     # right click
#     #     ActionChains(self.driver).move_to_element(element).pause(1).context_click(element).perform()

#     # from selenium.webdriver import ActionChains

#     # def right_click_root_space(self, name):
#     #     element = self.wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH, f"//*[text()='{name}']")
#     #         )
#     #     )

#     #     ActionChains(self.driver).context_click(element).perform()

#     def right_click_root_space(self, name):

#         element = self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, f"//*[text()='{name}']")
#             )
#         )

#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

#         from selenium.webdriver.common.action_chains import ActionChains
#         ActionChains(self.driver).move_to_element(element).pause(1).context_click(element).perform()

#         # IMPORTANT: wait for menu
#         self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//*[contains(text(),'Edit')]")
#             )
#         )


#     def click_add_sub_space(self):
#         import time
#         time.sleep(2)  # wait for context menu

#         elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Add Sub')]")

#         for el in elements:
#             if el.is_displayed():
#                 self.driver.execute_script("arguments[0].click();", el)
#                 return

#         raise Exception("Add Sub Space option not found")


#     def enter_sub_space_name(self, name):
#         field = self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//input[@placeholder='e.g. Finance, Project Alpha...']")
#         ))
#         field.clear()
#         field.send_keys(name)


#     def choose_icon(self):
#         icon = self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//button[.//*[name()='svg']]")
#         ))
#         self.driver.execute_script("arguments[0].click();", icon)


#     def select_color(self):
#         self.wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[@title='Blue']")
#         )).click()


#     def click_create_space(self):
#         btn = self.wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[normalize-space()='Create Space']")
#         ))
#         self.driver.execute_script("arguments[0].click();", btn)


#     def verify_sub_space_created(self, name):
#         locator = (By.XPATH, f"//h4[normalize-space()='{name}']")
#         return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
    
#     # ================= DELETE ROOT SPACE ================= #

#     # def right_click_root_space(self, name):
#     #     from selenium.webdriver.common.action_chains import ActionChains

#     #     locator = (By.XPATH, f"//h4[normalize-space()='{name}']")

#     #     element = self.wait.until(EC.visibility_of_element_located(locator))

#     #     self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

#     #     element = self.driver.find_element(*locator)

#     #     ActionChains(self.driver).move_to_element(element).pause(1).context_click(element).perform()


#     def click_delete_space(self):
#         import time
#         time.sleep(2)

#         elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Delete')]")

#         for el in elements:
#             if el.is_displayed():
#                 self.driver.execute_script("arguments[0].click();", el)
#                 return

#         raise Exception("Delete option not found")


#     def confirm_delete_space(self):
#         from selenium.webdriver.common.alert import Alert

#         # wait for alert
#         alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())

#         print("Alert text:", alert.text)  

#         alert.accept()  # click OK

#     def verify_space_deleted(self, name):
#         return self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, f"//div[contains(text(),'Space \"{name}\" deleted successfully')]")
#         )).is_displayed()
    
#     # ================= PROJECT ================= #

#     def open_root_space(self, name):
#         locator = (By.XPATH, f"//h4[normalize-space()='{name}']")
#         element = self.wait.until(EC.visibility_of_element_located(locator))

#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
#         self.driver.execute_script("arguments[0].click();", element)


#     def click_new_upload(self):
#         btn = self.wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[normalize-space()='New Upload']")
#         ))
#         self.driver.execute_script("arguments[0].click();", btn)


#     def enter_project_name(self, name):
#         # field = self.wait.until(EC.visibility_of_element_located(
#         #     (By.XPATH, "//input[@placeholder='Enter project name']")
#         # ))
#         # field.clear()
#         # field.send_keys(name)
#         if not self.driver.find_elements(By.XPATH, "//input[@placeholder='Enter project name']"):
#             self.click_new_upload()

#         field = self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//input[@placeholder='Enter project name']")
#         ))
#         field.clear()
#         field.send_keys(name)


#     # def upload_file(self, file_path):
#     #     import os

#     #     file_path = os.path.abspath(file_path)

#     #     upload = self.wait.until(EC.visibility_of_element_located(
#     #         (By.XPATH, "//input[@type='file']")
#     #     ))

#     #     # IMPORTANT for hidden input
#     #     self.driver.execute_script("arguments[0].style.display='block';", upload)

#     #     upload.send_keys(file_path)

#     def upload_file(self, file_path):
#         self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

#         file_path = os.path.abspath(file_path)
#         upload = self.wait.until(
#             EC.presence_of_element_located(self.file_upload_input)
#         )

#         self.driver.execute_script(
#             "arguments[0].style.display='block'; arguments[0].style.visibility='visible'; arguments[0].style.opacity=1;",
#             upload
#         )

#         upload.send_keys(file_path)

#         print("File uploaded successfully")


#     def click_upload(self):
#         btn = self.wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[normalize-space()='Upload']")
#         ))
#         self.driver.execute_script("arguments[0].click();", btn)
#         self.wait_for_processing_complete()


#     def create_project(self, name, file_path):
#         self.click_new_upload()
#         self.enter_project_name(name)
#         self.upload_file(file_path)
#         self.click_upload()


#     def verify_project_created(self, name):
#         locator = (By.XPATH, f"//h3[normalize-space()='{name}']")
#         return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
    
#     # ================= FILE UPLOAD ================= #

#     # def open_project(self, project_name):

#     #     locator = (By.XPATH, f"//h3[normalize-space()='{project_name}']")

#     #     element = self.wait.until(EC.visibility_of_element_located(locator))

#     #     self.driver.execute_script(
#     #         "arguments[0].scrollIntoView({block:'center'});", element
#     #     )
#     #     element.click()

#     def open_project(self, project_name):
        
#         locator = (By.XPATH, f"//h3[contains(text(),'{project_name}')]")

#         element = self.wait.until(EC.visibility_of_element_located(locator))

#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", element
#         )

#         self.driver.execute_script("arguments[0].click();", element)

#     # def upload_new_file(self, file_path):

#     #     # locator inside method
#     #     upload = self.wait.until(EC.visibility_of_element_located(
#     #         (By.XPATH, "//input[@type='file']")
#     #     ))

#     #     # scroll (important for visibility)
#     #     self.driver.execute_script("arguments[0].scrollIntoView(true);", upload)

#     #     # make visible (CRITICAL for hidden inputs)
#     #     self.driver.execute_script("arguments[0].style.display='block';", upload)

#     #     # upload file
#     #     upload.send_keys(file_path)

#     # def wait_for_processing_complete(self):
#     #     # wait until modal disappears
#     #     self.wait.until(EC.invisibility_of_element_located(
#     #         (By.XPATH, "//div[contains(text(),'Processing')]")
#     #     ))

#     def verify_file_uploaded(self, file_name):

#         self.wait.until(lambda driver: len(
#             driver.find_elements(By.XPATH, f"//*[contains(text(),'{file_name}')]")
#         ) > 0)

#         elements = self.driver.find_elements(
#             By.XPATH,
#             f"//*[contains(text(),'{file_name}')]"
#         )

#         return any(el.is_displayed() for el in elements)
    
#     # ================= EDIT DETAILS ================= #

#     # def click_edit_details(self):
#     #     elements = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Edit')]")

#     #     for el in elements:
#     #         if el.is_displayed():
#     #             self.driver.execute_script("arguments[0].click();", el)
#     #             return

#     #     raise Exception("Edit Details option not found")

#     def click_edit_details(self):

#         # wait for menu items
#         elements = self.wait.until(
#             EC.visibility_of_all_elements_located(
#                 (By.XPATH, "//*[contains(text(),'Edit')]")
#             )
#         )

#         for el in elements:
#             if el.is_displayed():
#                 self.driver.execute_script("arguments[0].click();", el)
#                 return

#         raise Exception("Edit Details option not found")


#     def edit_space_name(self, new_name):
#         from selenium.webdriver.common.keys import Keys

#         field = self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//div[contains(@class,'z-50')]//input")
#         ))

#         field.click()
#         field.clear()
#         field.send_keys(Keys.CONTROL + "a")
#         field.send_keys(Keys.DELETE)
#         field.send_keys(new_name)


#     def change_icon(self):
#         icon = self.wait.until(EC.visibility_of_element_located(
#             (By.XPATH, "//button[.//*[name()='svg']]")
#         ))
#         self.driver.execute_script("arguments[0].click();", icon)


#     def select_purple_color(self):
#         self.wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//button[@title='Purple']")
#         )).click()


#     def save_changes(self):
        
#         # try multiple locators
#         locators = [
#             "//button[contains(text(),'Save')]",
#             "//button[contains(text(),'Update')]",
#             "//div[contains(@class,'z-50')]//button"
#         ]

#         for xpath in locators:
#             buttons = self.driver.find_elements(By.XPATH, xpath)

#             for btn in buttons:
#                 if btn.is_displayed():
#                     self.driver.execute_script("arguments[0].click();", btn)

#                     # wait for modal close
#                     try:
#                         self.wait.until(EC.invisibility_of_element_located(
#                             (By.XPATH, "//div[contains(@class,'z-50')]")
#                         ))
#                     except:
#                         pass

#                     return

#         raise Exception("Save button not found")

#     def verify_space_updated(self, name):
#         locator = (By.XPATH, f"//h4[normalize-space()='{name}']")
#         return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
    
#     #-------------------------Delete Project------------------------- #
#     # def wait_for_project_page(self, project_name):
#     #     self.wait.until(
#     #         EC.visibility_of_element_located(
#     #             (By.XPATH, f"//h3[contains(text(),'{project_name}')]")
#     #         )
#     #     )

#     def wait_for_processing_complete(self):

#         # wait for overlay to disappear
#         self.wait.until(
#             EC.invisibility_of_element_located(
#                 (By.XPATH, "//div[contains(@class,'fixed inset-0')]")
#             )
#         )

#     def click_delete_project(self):

#         # try multiple locators (VERY IMPORTANT)
#         locators = [
#             "//button[@title='Delete project']",
#             "//*[contains(@title,'Delete')]",
#             "//*[contains(text(),'Delete')]"
#         ]

#         for xpath in locators:
#             elements = self.driver.find_elements(By.XPATH, xpath)

#             for el in elements:
#                 if el.is_displayed():
#                     self.driver.execute_script(
#                         "arguments[0].scrollIntoView({block:'center'});", el
#                     )
        
#                     self.driver.execute_script("arguments[0].click();", el)
#                     return

#         raise Exception("Delete button not found")

#     def confirm_delete(self):
#         confirm_input = (By.XPATH, "//input[@placeholder='Type DELETE to confirm']")
#         delete_btn = (By.XPATH, "//button[normalize-space()='Delete']")

#         self.wait.until(EC.visibility_of_element_located(confirm_input)).send_keys("DELETE")
#         self.wait.until(EC.element_to_be_clickable(delete_btn)).click()

#     def wait_for_delete_complete(self):
#         self.wait.until(
#             EC.invisibility_of_element_located(
#                 (By.XPATH, "//div[contains(text(),'Deleting project')]")
#             )
#         )
#     def verify_project_deleted(self, project_name):
#         elements = self.driver.find_elements(
#             By.XPATH, f"//h3[contains(text(),'{project_name}')]"
#         )
#         return len(elements) == 0
    
# #---------------------------Search File Fumctionality-------------------------#
#     def search_file(self, name):
#         search_input = (By.XPATH, "//input[@placeholder='Search filename...']")
#         box = self.wait.until(
#             EC.visibility_of_element_located(search_input)
#         )
#         box.clear()
#         box.send_keys(name)


#     def verify_file_present(self, name):

#         locator = (By.XPATH, f"//*[contains(text(),'{name}')]")

#         return self.wait.until(
#             EC.visibility_of_element_located(locator)
#         ).is_displayed()
    
  
# #---------------------------Plays-------------------------#

#     def select_all_files(self):

#         select_all_btn = (By.XPATH, "//button[normalize-space()='Select All']")

#         element = self.wait.until(EC.element_to_be_clickable(select_all_btn))

#         # scroll for safety
#         self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

#         # click using JS (avoids overlay issues)
#         self.driver.execute_script("arguments[0].click();", element)

# # ================= DELETE FILE ================= #

# # ================= DELETE CONFIRMATION LOCATORS ================= #

#     confirm_delete_input = (By.XPATH, "//input[@placeholder='Type DELETE to confirm']")
#     delete_button = (By.XPATH, "//button[normalize-space()='Delete']")

#     def delete_file(self, file_name):

#         file_locator = (By.XPATH, f"//*[contains(text(),'{file_name}')]")

#         file_element = self.wait.until(
#             EC.visibility_of_element_located(file_locator)
#         )

#         ActionChains(self.driver).move_to_element(file_element).perform()

#         delete_icon = self.wait.until(
#             EC.element_to_be_clickable(
#                 (By.XPATH, f"//*[contains(text(),'{file_name}')]/ancestor::*//button[contains(@title,'Delete')]")
#             )
#         )

#         self.driver.execute_script("arguments[0].click();", delete_icon)

#         # Confirm delete
#         confirm = self.wait.until(
#             EC.visibility_of_element_located(self.confirm_delete_input)
#         )
#         confirm.clear()
#         confirm.send_keys("DELETE")

#         self.wait.until(
#             EC.element_to_be_clickable(self.delete_button)
#         ).click()

#         # IMPORTANT: WAIT UNTIL FILE DISAPPEARS
#         self.wait.until(
#             EC.invisibility_of_element_located(file_locator)
#         )


#     def is_file_deleted(self, file_name):

#         elements = self.driver.find_elements(
#             By.XPATH, f"//*[contains(text(),'{file_name}')]"
#         )

#         return len(elements) == 0
    
#     # ================= VERIFY BUTTONS ================= #
#     def deselect_all_files(self):

#         deselect_all_button = (By.XPATH, "//button[normalize-space()='Deselect All']")

#         element = self.wait.until(EC.element_to_be_clickable(deselect_all_button))

#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", element
#         )

#         self.driver.execute_script("arguments[0].click();", element)

#     def verify_deselect_visible(self):

#         return self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//button[normalize-space()='Deselect All']")
#             )
#         ).is_displayed()


#     def verify_select_visible(self):

#         return self.wait.until(
#             EC.visibility_of_element_located(
#                 (By.XPATH, "//button[normalize-space()='Select All']")
#             )
#         ).is_displayed()
    
#     # ================= FILTER ================= #

#     def get_filter_dropdown(self):

#         filter_dropdown = (By.XPATH, "//select[contains(@class,'text-sm')]")

#         return self.wait.until(
#             EC.visibility_of_element_located(filter_dropdown)
#         )


#     def apply_filter(self, label_text):

#         dropdown = self.get_filter_dropdown()

#         # wait until dropdown is enabled
#         self.wait.until(lambda d: dropdown.is_enabled())

#         self.driver.execute_script(
#             """
#             const select = arguments[0];
#             const label = arguments[1];

#             for (let option of select.options) {
#                 if (option.text.includes(label)) {
#                     select.value = option.value;
#                     select.dispatchEvent(new Event('change', { bubbles: true }));
#                     return;
#                 }
#             }
#             """,
#             dropdown,
#             label_text
#         )

#         # IMPORTANT: wait for filter effect (UI refresh)
#         self.wait.until(lambda d: dropdown.get_attribute("value") is not None)

#         # small stability wait (React rendering)
#         time.sleep(5)



#     def clear_filter(self):

#         try:
#             clear_btn = self.wait.until(
#                 EC.element_to_be_clickable(
#                     (By.XPATH, "//button[@title='Clear filter']")
#                 )
#             )

#             self.driver.execute_script("arguments[0].click();", clear_btn)

#             # wait until dropdown resets
#             dropdown = self.get_filter_dropdown()

#             self.wait.until(lambda d: dropdown.get_attribute("value") == "" or dropdown.get_attribute("value") is None)

#             time.sleep(2)

#         except:
#             pass

#     # ================= EXPORT CLASSIFICATION ================= #

#     export_classification_btn = (By.XPATH, "//button[contains(text(),'Export Classification')]")

#     def click_export_classification(self):

#         btn = self.wait.until(
#             EC.element_to_be_clickable(self.export_classification_btn)
#         )

#         self.driver.execute_script(
#             "arguments[0].scrollIntoView({block:'center'});", btn
#         )

#         import time
#         time.sleep(1)

#         self.driver.execute_script("arguments[0].click();", btn)


#     def wait_for_classification_download(self, download_dir, timeout=60):

#         import time
#         end_time = time.time() + timeout

#         while time.time() < end_time:

#             files = os.listdir(download_dir)

#             for f in files:
#                 file_lower = f.lower()

#                 if "classification" in file_lower and file_lower.endswith(".xlsx"):
#                     print("Downloaded:", f)
#                     return True

#             time.sleep(1)

#         raise Exception("Classification file not downloaded")

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProjectPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    # ================= COMMON UTILS ================= #

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

    def click_projects(self):
        projects = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Projects']"))
        )
        self.safe_click(projects)

        self.wait_for_page_load()

        self.wait.until(
            lambda d: "Loading" not in d.find_element(By.TAG_NAME, "body").text
        )

    # ================= RIGHT CLICK ================= #

    def right_click_on_canvas(self):

        canvas_locators = [
            "//div[contains(@class,'react-flow')]",
            "//div[contains(@class,'flex-1')]",
            "//main"
        ]

        canvas = None
        for xpath in canvas_locators:
            elements = self.driver.find_elements(By.XPATH, xpath)
            visible = [el for el in elements if el.is_displayed()]
            if visible:
                canvas = visible[-1]
                break

        if not canvas:
            raise Exception("Canvas not found")

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", canvas
        )

        try:
            ActionChains(self.driver)\
                .move_to_element(canvas)\
                .pause(1)\
                .context_click()\
                .perform()
        except:
            self.driver.execute_script("""
                arguments[0].dispatchEvent(new MouseEvent('contextmenu', {bubbles:true}));
            """, canvas)

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'New Root Space')]")
            )
        )

    # ================= ROOT SPACE ================= #

    def click_new_root_space(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//*[contains(text(),'New Root Space')]")
            )
        )

        for el in elements:
            if el.is_displayed():
                self.safe_click(el)
                return

        raise Exception("New Root Space not found")

    def create_root_space(self, name):

        self.click_new_root_space()

        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='e.g. Finance, Project Alpha...']")
            )
        )
        field.clear()
        field.send_keys(name)

        icon = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[.//*[name()='svg']]"))
        )
        self.safe_click(icon)

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Blue']"))
        ).click()

        create_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Space']"))
        )
        self.safe_click(create_btn)

        self.wait_for_loader()

    # ================= PROJECT ================= #

    def click_new_upload(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='New Upload']"))
        )
        self.safe_click(btn)

    def enter_project_name(self, name):
        field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter project name']")
            )
        )
        field.clear()
        field.send_keys(name)

    def upload_file(self, file_path):
        self.wait_for_page_load()

        upload = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        self.driver.execute_script(
            "arguments[0].style.display='block'; arguments[0].style.visibility='visible';",
            upload
        )

        upload.send_keys(os.path.abspath(file_path))

    def click_upload(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Upload']"))
        )
        self.safe_click(btn)

        self.wait_for_loader()

    def create_project(self, name, file_path):
        self.click_new_upload()
        self.enter_project_name(name)
        self.upload_file(file_path)
        self.click_upload()

    def verify_project_created(self, name):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//h3[contains(text(),'{name}')]")
            )
        ).is_displayed()

    def open_project(self, name):
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//h3[contains(text(),'{name}')]")
            )
        )
        self.safe_click(element)

    # ================= DELETE PROJECT ================= #

    def click_delete_project(self):

        locators = [
            "//button[@title='Delete project']",
            "//*[contains(text(),'Delete')]"
        ]

        for xpath in locators:
            elements = self.driver.find_elements(By.XPATH, xpath)
            for el in elements:
                if el.is_displayed():
                    self.safe_click(el)
                    return

        raise Exception("Delete button not found")

    def confirm_delete(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Type DELETE to confirm']")
            )
        ).send_keys("DELETE")

        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Delete']"))
        )
        self.safe_click(btn)

        self.wait_for_loader()

    def verify_project_deleted(self, name):
        elements = self.driver.find_elements(
            By.XPATH, f"//h3[contains(text(),'{name}')]"
        )
        return len(elements) == 0

    # ================= SEARCH ================= #

    def search_file(self, name):
        box = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Search filename...']")
            )
        )
        box.clear()
        box.send_keys(name)

    def verify_file_present(self, name):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//*[contains(text(),'{name}')]")
            )
        ).is_displayed()

    # ================= SELECT ================= #

    def select_all_files(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Select All']"))
        )
        self.safe_click(btn)

    def deselect_all_files(self):
        btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Deselect All']"))
        )
        self.safe_click(btn)


    


        
