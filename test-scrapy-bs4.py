from bs4 import BeautifulSoup
import urllib.request as urllib

url = "https://mobile.facebook.com/groups/2005484523039969"

content = urllib.urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')

for link in soup.find_all('a'):
    if "photo.php" in str(link.get('href')):
    	suburl = 'https://mobile.facebook.com' + link.get('href')
    	print(suburl)
    	subcontent = urllib.urlopen(suburl).read()
    	subsoup = BeautifulSoup(subcontent, 'html.parser')
    	for sublink in subsoup.find_all('a'):
    		print(sublink.get_text())
    		if "View full size" in sublink.get_text():
    			print('=================================================')
    			print('https://mobile.facebook.com' + sublink.get('href'))