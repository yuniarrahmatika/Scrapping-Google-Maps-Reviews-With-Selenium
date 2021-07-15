from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re #regular exp
import unicodecsv as csv 
import time
driver = webdriver.Chrome(executable_path="your-path-chromedriver/chromedriver.exe")
driver.get("your-link-google-maps")
time.sleep(5)
reviews = driver.find_elements_by_xpath("//button[@class='widget-pane-link']")
driver.execute_script(
    'var d = document.getElementsByClassName("section-layout section-scrollbox scrollable-y scrollable-show")[0];'
    'function sleep(ms){return new Promise(resolve => setTimeout(resolve, ms));}'+
    'var comment = document.getElementsByClassName("section-review-review-content");'+
    'async function scrolldown(){while(comment.length < 10){d.scrollTop += 10;await sleep(100)}}'+
    'scrolldown()'
)
time.sleep(5)
comment_text = driver.find_elements_by_xpath(".//div[@class='section-review-content']")
def writeTofile(data):
    with open('your-name-file.csv', mode='ab') as csv_file:
        fieldnames =['id', 'user','komentar']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,lineterminator='\n')
        writer.writerow(data)
for komen in comment_text:
    section = komen.find_element_by_xpath(".//div[@class='section-review-title']")
    id_r = section.find_element_by_xpath(".//span").text
    #bintang = komen.find_element_by_xpath(".//span[@class='section-review-stars']").get_attribute('aria-label')
    komentar = komen.find_element_by_xpath(".//span[@class='section-review-text']").text
    #r= re.search(r'\d+', bintang)
    #bintang = r.group(0) if r else ""
    data = {'id':20,'user':id_r,'komentar': komentar}
    print(data)
    writeTofile(data)
