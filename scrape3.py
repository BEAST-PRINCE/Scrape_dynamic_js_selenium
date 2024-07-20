import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def save_to_csv(data):
    csv_file = 'output.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Data saved to {csv_file}")



chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(options=chrome_options)



url = 'https://hprera.nic.in/PublicDashboard'
driver.get(url)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'reg-Projects')))
print("Page loaded successfully.")

project_blocks = driver.find_elements(By.CSS_SELECTOR, "a[onclick*='tab_project_main_ApplicationPreview']")[:6]

scraped_project_data = []

for project_url in project_blocks:
    project_url.click()

    modal = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'project-menu-html')))
    modal_contents = driver.page_source

    if modal:
        name = driver.find_element(By.XPATH, "//td[text()='Name']/following-sibling::td").text
        permanent_addr = driver.find_element(By.XPATH, "//td[text()='Permanent Address']/following-sibling::td/span").text
        pan = driver.find_element(By.XPATH, "//td[text()='PAN No.']/following-sibling::td/span").text
        gstin = driver.find_element(By.XPATH, "//td[text()='GSTIN No.']/following-sibling::td/span").text

        # name_css = driver.find_element(By.CSS_SELECTOR, "table.table-borderless.table-sm.table-responsive-lg.table-striped.font-sm tr:nth-child(1) td:nth-child(2)").text
            
        scraped_project_data.append({'name': name, 'permanent_addr': permanent_addr, 'pan': pan, 'gstin': gstin})

            
        closebtn = driver.find_element(By.XPATH, "//button[text()='Close']")
        if closebtn:
            closebtn.click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'reg-Projects')))

        else:
            driver.back()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'reg-Projects')))
            


    

save_to_csv(scraped_project_data)
            



driver.quit()