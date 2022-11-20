# import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

chromedriver= "chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.get("https://dermnetnz.org/image-library")

# imgResults = browser.find_elements(By.XPATH,"//img")

# # Access and store the scr list of image url's.
# src = []
# for img in imgResults[:293]:
#     src.append(img.get_attribute('src'))

# opener = urllib.request.build_opener()
# opener.addheaders = [('User-Agent', 'MyApp/1.0')]
# urllib.request.install_opener(opener)

# # Retrieve and download the images.
# for i in range(len(src)):    
#     urllib.request.urlretrieve(str(src[i]),"sample_data/derm{}.jpg".format(i+1))

# list of name of disease, url links, icon
dis = []
names = browser.find_elements(By.XPATH,"//h6")
for name in names:
    dis.append(name.text)
# print(len(dis))

# dst = {}
# for i,j in zip(dis, src):
#     dst[i] = j

# print(dst)    
