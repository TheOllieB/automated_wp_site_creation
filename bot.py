from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

usernameStr = os.getenv('USERNAME_STR')
passwordStr = os.getenv('Oliver2010!')
url = input("Please enter URL of site to be created e.g https://dev-blogs.manchester.ac.uk/yoururl :  ")
title = input("Please enter the title of the site : ")

#Create site
browser = webdriver.Chrome()
browser.get(('https://dev-blogs.manchester.ac.uk/wp-admin/'))

time.sleep(15)

browser.get('https://dev-blogs.manchester.ac.uk/wp-admin/network/sites.php')
newSite = browser.find_element_by_class_name('page-title-action')
newSite.click()
siteAddress =  WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'site-address')))
siteAddress.send_keys(url)
siteTitle = browser.find_element_by_id('site-title')
siteTitle.send_keys(title)
adminEmail = browser.find_element_by_id('admin-email')
adminEmail.send_keys(usernameStr)

#Changing the site tagline
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/options-general.php')
tagline = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'blogdescription')))
tagline.send_keys("The University Of Manchester")
submitbtn = browser.find_element_by_id('submit')

#Choosing Theme
#Importing layouts
# browser.get(('https://dev-blogs.manchester.ac.uk/ollie-test/wp-admin/edit.php?post_type=et_pb_layout'))
# layout = browser.find_element_by_class_name('page-title-action')
# pick = browser.find_element_by_class_name('et-pb-portability-button').click()
# time.sleep(9)


#For login page
# username = browser.find_element_by_id('username')
# username.send_keys(usernameStr)
# password = browser.find_element_by_id('password')
# password.send_keys(passwordStr)
# nextButton = browser.find_element_by_class_name('btn-submit')
# nextButton.click()



# #password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.class_name, 'whsOnd')))
# password.send_keys(passwordStr)

# signInButton = browser.find_element_by_id('passwordNext')
# #signInButton.click()

