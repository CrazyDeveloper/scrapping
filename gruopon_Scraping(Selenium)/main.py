import requests
import csv, time
import xlsxwriter

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
def url_move(url, state, worksheet, row): 
    driver.get(url)
    time.sleep(3)    
    driver.find_element_by_id('topcategory|category|subcategory|subcategory2|subcategory3|subcategory4-filter-box').click()
    child_list = driver.find_elements_by_class_name('children-list')
    category_list = child_list[state].find_elements_by_tag_name('a')
    tree2 = [item.get_attribute('href') for item in category_list]    
    for item2 in tree2:
        print('step2')
        driver.get(item2)       
        time.sleep(3)
        child_body = driver.find_element_by_id('pull-results')
        child_figures = child_body.find_elements_by_tag_name('figure')
        tree3 = [figure.find_element_by_tag_name('a').get_attribute('href') for figure in child_figures]
        for item3 in tree3:
            print('step3')
            driver.get(item3)
            time.sleep(5)   
            row += 1         
            article = driver.find_element_by_tag_name('article')
            try:
                falg = article.find_element_by_class_name('address-area')
                neighborhood = True
            except:
                neighborhood = False
            if neighborhood == True:
                try:
                    # print(article.find_element_by_class_name('address-bottom').text+"--------")
                    # print(article.find_element_by_id('website-url').get_attribute('href')+"========")
                    article_content = article.find_element_by_class_name('carousel-content')
                    links = article_content.find_elements_by_tag_name('a')
                    print(len(links))
                    print("=====================")
                    tree4 = [item.get_attribute('href') for item in links]
                    for item4 in tree4:
                        driver.get(item4)
                        time.sleep(5)
                        print('step4')
                        try:
                            worksheet.write(row, 0, driver.find_element_by_class_name('address-bottom').text)
                            contact_info = driver.find_element_by_class_name('contact-info')
                            worksheet.write(row, 1, contact_info.find_element_by_tag_name('a').get_attribute('href'))
                        except:
                            pass
                except:
                    print('error')
                    try:
                        worksheet.write(row, 0, article.find_element_by_class_name('address-bottom').text)
                        contact_info = article.find_element_by_class_name('contact-info')
                        print(article.find_element_by_id('website-url').get_attribute('href'))
                        worksheet.write(row, 1, contact_info.find_element_by_tag_name('a').get_attribute('href'))
                    except:
                        pass
            else:
                print('false')
                print(article.find_element_by_class_name('merchant-website').get_attribute('href'))
                worksheet.write(row, 1, article.find_element_by_class_name('merchant-website').get_attribute('href'))
workbook = xlsxwriter.Workbook('scrapResult.xlsx')
worksheet = workbook.add_worksheet('result')
row = 1
driver = webdriver.Chrome(r"C:\Users\116\.wdm\drivers\chromedriver\win32\90.0.4430.24\chromedriver.exe")

## ---------------------------------
driver.get("https://www.groupon.com/")
driver.find_element_by_id('nothx').click()
time.sleep(5)
categoris = driver.find_elements_by_class_name('subcategories-link')
tree1 = [item.get_attribute('href') for item in categoris]
# for item in tree1:
#     print(item.get_attribute('href'))
print('step1')
url_move(categoris[0].get_attribute('href'), 1, worksheet, row)
workbook.close()



    
