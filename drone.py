import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChromeService())

# Open the initial page
initial_url = 'https://www.amazon.in'
driver.get(initial_url)
driver.maximize_window()

#search the for drone
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("drone")
driver.find_element(By.ID, "nav-search-submit-button").click()
#scrap page
def scrape_page():
    data_elements = driver.find_elements(By.XPATH, '//span[@class="a-size-base-plus a-color-base a-text-normal"]')
    review= driver.find_elements(By.XPATH, '//span[@class="a-size-base puis-normal-weight-text"]')
    data_price = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
    s=[]
    d=[]
    f=[]
    for i,j,k in zip( data_elements,review,data_price):
        d.append(i.text)
        s.append(j.text)
        f.append(k.text)
    print(s)
    print(d)
    print(f)

    # # convert data into csv fie
    # df = pd.DataFrame({'name': d, 'price': f, 'rating': s})
    # df.to_csv('t.csv', mode='a', header=False, index=False)


num_pages_to_scrape = 7


for page in range(num_pages_to_scrape):
    # Scraping logic for the current page
    scrape_page()

#scrapping for next page
    try:
        next_page_button = driver.find_element(By.XPATH, '//li[@class="a-last"]/a')
        if next_page_button.is_enabled():
            next_page_button.click()
        else:
            print("No more pages to scrape.")
            break
    except Exception as e:
        print(f'Error navigating to next page: {e}')




