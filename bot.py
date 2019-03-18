from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init
from termcolor import colored
import time
import os
from dotenv import load_dotenv

init()
#usernameStr = os.getenv('USERNAME_STR')
#passwordStr = os.getenv('PASSWORD_STR')

print(colored('Please enter URL of site to be created e.g https://dev-blogs.manchester.ac.uk/yoururl :  ', 'white', 'on_magenta'))
url = input()
print(colored('Please enter the title of the site : ', 'white', 'on_magenta'))
title = input()
print(colored('Please type the faculty the site belongs to. Choice: humanities/fse/non-faculty/non-branded (default is BMH)', 'white', 'on_magenta'))
style = input().lower()
if style == "bmh": 
    style = ""
else: stylesheet = f'<link rel="stylesheet" type="text/css" href="//blogs.manchester.ac.uk/wp-content/themes/UoMDiviChild/{style}.css">'
print(colored('What platform do you want to create this site on (dev, uat, prod)? ', 'white', 'on_magenta'))
plat = input().lower()

if plat == "dev":
    plat = "dev-blogs"
elif  plat == "uat":
    plat="uat-blogs"
else: 
    plat == "sites"

usernameStr = 'oliver.burge@manchester.ac.uk'
passwordStr = ''

#Create site
browser = webdriver.Chrome()
browser.get((f'https://{plat}.manchester.ac.uk/wp-admin/'))

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
addSite = browser.find_element_by_id('add-site').click()
print(colored('Site Created', 'cyan','on_white'))

#Changing the site tagline
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/options-general.php')
tagline = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'blogdescription')))
tagline.clear()
tagline.send_keys('The University Of Manchester')
submitbtn = browser.find_element_by_id('submit')
submitbtn.click()
print('Changed site tagline')

#Choosing Theme
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/themes.php')
selectTheme = browser.find_element_by_xpath("//a[@aria-label='Activate UoM Divi Child']")
selectTheme.click()
print('Theme activated')

#Fixed nav
# browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/admin.php?page=et_divi_options')
# browser.find_element_by_xpath(".//input[@name='divi_fixed_nav']//span[@class='et_pb_button_slider']").click()
# browser.find_element_by_id('epanel-save').click()

#Creating primary menu
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/nav-menus.php')
menuName = browser.find_element_by_id('menu-name')
menuName.send_keys('primary menu')
browser.find_element_by_id('save_menu_header').click()
browser.find_element_by_id('locations-primary-menu').click()
browser.find_element_by_xpath("//h3[contains(text(), 'Custom Links')]").click()
browser.find_element_by_id('add-custom-links').click()
customURL = browser.find_element_by_xpath("//input[@class='code menu-item-textbox']").clear()
site = f'https://dev-blogs.manchester.ac.uk/{url}'
browser.find_element_by_xpath("//input[@class='code menu-item-textbox']").send_keys(site)
linkText = browser.find_element_by_id('custom-menu-item-name')
linkText.send_keys(title)
addToMenu = browser.find_element_by_id('submit-customlinkdiv').click()
saveMenu = browser.find_element_by_id('save_menu_header').click()
print('Primary menu created')

#Editor Menu and widget access
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/themes.php?page=editorMenuWidgetAccess')
browser.find_element_by_name('emwa_settings[emwa_chk_custom]').click()
browser.find_element_by_name('emwa_settings[emwa_chk_widgets]').click()
print('Menu and Widget boxes checked')

#Widgets LeftNavArea
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/widgets.php')
widgetName = browser.find_element_by_id('et_pb_new_widget_area_name')
widgetName.send_keys('LeftNavArea')
browser.find_element_by_xpath("//button[contains(text(), 'Create')]").click()
time.sleep(2)
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/widgets.php')
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Navigation Menu')]")))
navMenu = browser.find_element_by_xpath("//h3[contains(text(), 'Navigation Menu')]")
leftNavArea = browser.find_element_by_id('et_pb_widget_area_1')
ActionChains(browser).click_and_hold(navMenu).move_to_element(leftNavArea).release(leftNavArea).perform()
#browser.find_element_by_xpath("//button[@class='widget-action hide-if-no-js']").click()
# select = Select(browser.find_element_by_xpath("//select[@id='widget-nav_menu-2-nav_menu']"))
# select.select_by_value('2').click()
# browser.find_element_by_xpath("//select[@id='widget_nav_menu-2-nav_menu']/option[text()='primary menu']").click()
# browser.find_element_by_xpath("//input[@value='Save']").click()
#browser.find_element_by_class_name('widget-control-save').click()
print('LeftNavArea widget created, Please choose the menu you want.')

#Home Page
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/post-new.php?post_type=page')
browser.find_element_by_xpath("//input[@name='post_title']").send_keys('Home')
# diviBuilder = browser.find_element_by_xpath("//a[@id='et_pb_toggle_builder']")
# diviBuilder.click()
# browser.find_element_by_xpath("//a[@class='et-pb-layout-buttons et-pb-layout-buttons-load']").click()
# browser.find_element_by_xpath("//a[contains(text(), 'Your Saved Layouts')]").click()
# time.sleep(2)
# browser.find_element_by_xpath("//a[@class='et-dlib-layouts-grid-item et-dlib-home-page-final et-dlib-animate']").click()
# time.sleep(3)
browser.find_element_by_id('publish').click()
print('Home page created')

#Settings > Reading
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/options-reading.php')
browser.find_element_by_xpath("//input[@name='show_on_front']").click()
browser.find_element_by_xpath("//select[@id='page_on_front']/option[text()='Home']").click()
browser.find_element_by_id('blog_public').click()
browser.find_element_by_xpath("//input[@name='submit']").click()
print('Search engine visibility disabled')

#Body and Head code paste
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/admin.php?page=et_divi_options')
browser.find_element_by_xpath("//a[contains(text(), 'Integration')]").click()
body = browser.find_element_by_xpath("//textarea[@name='divi_integration_head']//pre[@class='CodeMirror-line']")
with open('data.txt', 'r') as myfile:
    data = myfile.read()
body.send_keys(data)

#head = browser.find_element_by_id
#To be finished 

#Enabling breadcrumbs
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/admin.php?page=wpseo_titles')
browser.find_element_by_id('breadcrumbs-tab').click()
browser.find_element_by_xpath("//input[@id='breadcrumbs-enable']").click()
sep = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'breadcrumbs-sep'))).clear()
sep.send_keys('/')
browser.find_element_by_id('breadcrumbs-home').send_keys(title)
browser.find_element_by_id('submit').click()
print('Breadcrumbs enabled')

#Set search page
browser.get(f'https://dev-blogs.manchester.ac.uk/{url}/wp-admin/options-general.php?page=sb_et_search_li')
browser.find_element_by_xpath("//select[@name='sb_et_search_li_layout']/option[text()='Search Results']").click()
browser.find_element_by_xpath("//input[@name='sb_et_search_li_edit_submit']")
print('Set Search page successfully')

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
print(colored('The site is now set up, a few things to do before the site is complete:\n1. Import layouts JSON file.\n2. Add About page.\n3. Use the theme customizer to adjust Blog post settings.\n ', 'white', 'on_magenta'))

