from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

import time
import json

#FUNCTION GET IMAGES
def getImageFromGroup(driver):
	imgs = []
	try:
		myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'pagelet_pinned_posts')))

		soup = BeautifulSoup(driver.page_source, 'html.parser')

		for link in soup.findAll("a"):
			if "t1.0-9" in str(link.get('data-ploi')):
				imgs.append({ "img" : link.get('data-ploi') })

		return imgs
	except TimeoutException:
	    return 0

#open the first window
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://facebook.com")

#LOGIN TO FACEBOOK
search_form = driver.find_element_by_id('login_form')

email = driver.find_element_by_id('email')
email.send_keys('argap13@gmail.com')

passwd = driver.find_element_by_id('pass')
passwd.send_keys('pepong12345')

search_form.submit()

try:
	WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'fb_stories_card_root')))
except TimeoutException:
	print ("Loading took too much time!")

#CURRY FB POSTS GAMBAR
urls = { "datas" : [
	{
		"url" : "https://www.facebook.com/groups/NonsenseTaDeVolta/",
		"type" : "group"
	}
]}

results = []

for i in urls["datas"]:
	driver.get(i["url"])
	tmpResult = getImageFromGroup(driver)
	if(tmpResult):
		results.extend(tmpResult)

print(json.dumps(results))
driver.quit()