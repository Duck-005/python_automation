from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
import pandas as pd

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://exam.msrit.edu')

time.sleep(10)
# Manually solve the Captcha
captcha_element = driver.find_element(By.ID, 'osolCatchaTxt0')
captcha_element.send_keys(Keys.CONTROL, 'a')
captcha_element.send_keys(Keys.CONTROL, 'c')
captcha = pyperclip.paste()

input_element = driver.find_element(By.ID, 'usn')
input_element.clear()
prefix = '1MS23'
postfix = '-T'

# last usn for each CSE branch ( need to check it manually TᴖT)
branchCodeDict = {'CI': 143, 'CS': 229, 'CY': 75, 'IS': 160}
# branchCodeDict = {'CI': 143}

# XPATH details of the elements you want to locate
sgpaXPATH = '/html/body/div[2]/div/div/div[4]/div/div/div[1]/div/div[3]/div/p'
cgpaXPATH = '/html/body/div[2]/div/div/div[4]/div/div/div[1]/div/div[4]/div/p'
nameXPATH = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/h3'

names = []
sgpa = []
cgpa = []
usn = []

for branchCode in branchCodeDict:
    sno = '1'
    i = int(sno)
    for i in range(branchCodeDict[branchCode]):
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'usn'))
        )

        # Enter the usn and click go ( automatically )
        input_element.clear()
        USN = prefix + branchCode + sno.zfill(3) + postfix
        input_element.send_keys(USN)
        go_element = driver.find_element(By.CLASS_NAME, 'buttongo')
        go_element.click()

        try:
            # locating the element and converting the text to strings
            name = driver.find_element(By.XPATH, nameXPATH).text
            CGPA = driver.find_element(By.XPATH, cgpaXPATH).text
            SGPA = driver.find_element(By.XPATH, sgpaXPATH).text

            names.append(name)
            usn.append(USN)
            sgpa.append(SGPA)
            cgpa.append(CGPA)

        except NoSuchElementException:
            pass

        sno = str(int(sno) + 1)
        driver.execute_script("window.history.go(-1)")
        # driver.back()  another method of undo

# convert the extracted data to Excel sheets
df_dict = {'names': names, 'usn': usn, 'sgpa': sgpa, 'cgpa': cgpa}
df = pd.DataFrame(df_dict)
df.to_csv('student_GPA_ISEM.csv', mode = 'a')

driver.quit()
