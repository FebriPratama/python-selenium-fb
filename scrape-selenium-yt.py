from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

import time

#open the first window
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.youtube.com")


current_url = driver.current_url

# search_form = driver.find_element_by_id('login_form')

# email = driver.find_element_by_id('email')
# email.send_keys('argap13@gmail.com')

# passwd = driver.find_element_by_id('pass')
# passwd.send_keys('pepong12345')

# search_form.submit()

# try:
# 	WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'fb_stories_card_root')))
# except TimeoutException:
# 	print ("Loading took too much time!")

# driver.get("https://www.facebook.com/groups/NonsenseTaDeVolta/")

try:
	myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'items')))

	soup = BeautifulSoup(driver.page_source, 'html.parser')

	for link in soup.find_all('a'):
		if "/watch?v=" in str(link.get('href')):
			print(link.get('href'))
	
	browser.quit()

except TimeoutException:
    print ("Loading took too much time!")