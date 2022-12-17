#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import xlsxwriter

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[ ]:


#  KATADATA.CO.ID


# In[12]:


options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://katadata.co.id/tags/pasar-modal')

while True:
    try:
        time.sleep(1)
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "btn-loadmore"))))
    except NoSuchElementException:
        break


# In[14]:


doc = driver.page_source
html = doc
soup = bs(html, 'html.parser')

file=open('data0.txt','w', encoding = 'utf-8')

for word in soup.find_all('h3'):
    find_all_title = word.get_text()
    file.write(find_all_title + '\n')

file.close()


# In[ ]:


# BAREKSA.COM


# In[6]:


options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.bareksa.com/berita/pasar-modal')

while True:
    try:
        time.sleep(4)
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > main > div > section > section > section > main > div.sc-jzJRlG.jWsbSn > button > div"))))
    except NoSuchElementException:
        break


# In[9]:


doc = driver.page_source
html = doc
soup = bs(html, 'html.parser')

file=open("data1.txt","w",encoding='utf-8')

for word in soup.find_all('h6'):
    find_all_title = word.get_text()
    file.write(find_all_title + '\n')
    
file.close()


# In[ ]:


# KUMPARAN


# In[42]:


options = Options()

driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe")
driver.get('https://kumparan.com/topic/pasar-modal')

while True:
    try:
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except NoSuchElementException:
        break


# In[43]:


doc = driver.page_source
html = doc
soup = bs(html, 'html.parser')

file=open("data2.txt","w",encoding='utf-8')

for word in soup.find_all("span", {"class": "Textweb__StyledText-sc-1uxddwr-0 eSSwLt CardContentweb__CustomText-sc-1gsg7ct-0 grhZrk"}):
    find_all_title = word.get_text()
    file.write(find_all_title + '\n')
    
file.close()


# In[ ]:


# IDNTIMES


# In[73]:


options = Options()

driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe")
driver.get('https://www.idntimes.com/tag/investasi-saham')

while True:
    try:
        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except NoSuchElementException:
        break


# In[74]:


doc = driver.page_source
html = doc
soup = bs(html, 'html.parser')

file=open("data3.txt","w",encoding='utf-8')

for word in soup.find_all("h2"):
    find_all_title = word.get_text()
    file.write(find_all_title + '\n')
    
file.close()


# In[ ]:


# CNBCINDONESIA


# In[17]:


options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
  
element_list = []
  
for page in range(1,88, 1):
    
    page_url = "https://www.cnbcindonesia.com/tag/pasar-modal/" + str(page)
    driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options)
    driver.get(page_url)
    title = driver.find_elements(By.TAG_NAME, 'h2')
  
    for i in range(len(title)):
        element_list.append([title[i].text])
  
with xlsxwriter.Workbook('result.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)
  
driver.close()


# In[ ]:


# CNNINDONESIA


# In[19]:


options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
  
element_list = []
  
for page in range(1,62, 1):
    
    page_url = "https://www.cnnindonesia.com/tag/pasar-modal/" + str(page)
    driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options,)
    driver.get(page_url)
    title = driver.find_elements(By.TAG_NAME, 'h2')
  
    for i in range(len(title)):
        element_list.append([title[i].text])
  
with xlsxwriter.Workbook('result2.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)
  
driver.close()


# In[ ]:


# MARKET.BISNIS.COM


# In[16]:


options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options,)
  
element_list = []
#nextbtn
page_url = "https://market.bisnis.com/bursa-saham/"
driver.get(page_url)
css = '#nextbtn'


while True:
    
    try:
        time.sleep(2)
        title = driver.find_elements(By.TAG_NAME, 'h2')
  
        for i in range(len(title)):
            element_list.append([title[i].text])
    
        next_button = driver.find_element(By.CSS_SELECTOR, css)
        next_button.click()
        WebDriverWait(driver, 30).until(EC.staleness_of(next_button))
        
    except NoSuchElementException:
        break
  
driver.close()


# In[17]:


with xlsxwriter.Workbook('result3.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


# In[ ]:


# MEDCOM


# In[2]:


options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options,)
  
element_list = []
#nextbtn
page_url = "https://www.medcom.id/tag/3662/bei"
driver.get(page_url)
css = 'body > div.master_wrapper.theme_2019 > div.w100fl > div > div.mid_content.mt40 > div.lc_col > div > ul.pagination > li:nth-child(5) > a'


while True:
    
    try:
        time.sleep(1)
        title = driver.find_elements(By.TAG_NAME, 'h4')
  
        for i in range(len(title)):
            element_list.append([title[i].text])
    
        next_button = driver.find_element(By.CSS_SELECTOR, css)
        next_button.click()
        WebDriverWait(driver, 30).until(EC.staleness_of(next_button))
        
    except NoSuchElementException:
        break
  
driver.close()


# In[3]:


with xlsxwriter.Workbook('result4.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


# In[ ]:


# WARTAEKONOMI


# In[7]:


options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
  
element_list = []
  
for page in range(1,71, 1):
    
    page_url = "https://wartaekonomi.co.id/category-283/bursa?page=" + str(page)
    driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options,)
    driver.get(page_url)
    title = driver.find_elements(By.TAG_NAME, 'h3')
  
    for i in range(len(title)):
        element_list.append([title[i].text])
  
with xlsxwriter.Workbook('result5.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)
  
driver.close()


# In[8]:


with xlsxwriter.Workbook('result5.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


# In[ ]:


# OKEZONE


# In[9]:


options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options,)
  
element_list = []
#nextbtn
page_url = "https://www.okezone.com/tag/bei"
driver.get(page_url)
css = 'body > div > div.container.container-body-home > div > div.col-md-7.col-sm-7.right > div.btn-pagination > div > ul > li.next.pagination-list__item > a > i'


while True:
    
    try:
        time.sleep(1)
        title = driver.find_elements(By.CLASS_NAME, 'ga_BreakingMore')
  
        for i in range(len(title)):
            element_list.append([title[i].text])
    
        next_button = driver.find_element(By.CSS_SELECTOR, css)
        next_button.click()
        WebDriverWait(driver, 30).until(EC.staleness_of(next_button))
        
    except NoSuchElementException:
        break
  
driver.close()


# In[10]:


with xlsxwriter.Workbook('result6.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


# In[ ]:


# SINDONEWS


# In[9]:


options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
  
element_list = []
  
for page in range(0,1035, 15):
    
    page_url = "https://www.sindonews.com/topic/2340/bursa-efek-indonesia-bei/" + str(page)
    driver = webdriver.Chrome("C:/Users/krish/Desktop/chromedriver_win32/chromedriver.exe", chrome_options=options,)
    driver.get(page_url)
    title = driver.find_elements(By.TAG_NAME, 'a')
  
    for i in range(len(title)):
        element_list.append([title[i].text])
  
with xlsxwriter.Workbook('result7.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)
  
driver.close()


# In[10]:


with xlsxwriter.Workbook('result7.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


# In[ ]:




