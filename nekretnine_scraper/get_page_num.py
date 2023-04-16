from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

def get_ad_number(url):
    driver = webdriver.Chrome(options=options, executable_path='../chromedriver.exe')
    driver.get(url)

    htmlSource = driver.find_element(By.TAG_NAME, 'em')
    ad_number = int(htmlSource.text)
    driver.quit()
    
    return ad_number