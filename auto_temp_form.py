from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driverPath = 'D:\python project\程式設計\chromedriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'https://docs.google.com/forms/d/e/1FAIpQLSc9mhTWQ3CKj0dzViSA15Nqci555Z2pAXpjxKg0wT9jNU86CQ/viewform'
browser.get(url)

name_wait = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'quantumWizTextinputPaperinputInput')))
name = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
name[0].send_keys("891137")
name[1].send_keys('36.6')

yorn = browser.find_elements_by_class_name('appsMaterialWizToggleRadiogroupOffRadio')
yorn[1].click()

nextpg = browser.find_element_by_class_name('appsMaterialWizButtonPaperbuttonLabel')
nextpg.click()

submit_wait = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,"//span[contains(text(),'提交')]")))
submit_wait.click()

