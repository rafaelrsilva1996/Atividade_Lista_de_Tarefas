from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import time


def get_token_list_per_wallet(wallet_address):    
    # options = Options()
    # browser = webdriver.Chrome(executable_path='../bin/chromedriver', options=options)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME, options=chrome_options)

    url = f'https://bscscan.com/address/{wallet_address}'
    browser.get(url=url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    table = soup.find('table')
    lines = table.find_all('tr')
    hashs = []
    values = []
    tokens = []

    for index in range(1, len(lines)):
        line = lines[index].find_all('td')
        hashs.append(line[1].get_text())
        values.append(line[9].get_text().split(" ")[0])
        tokens.append(line[9].get_text().split(" ")[1])
    
    df = pd.DataFrame(data={'hash_transaction': hashs, 'value': values, 'token': tokens})
    browser.quit()
    return df

    # time.sleep(5)


if __name__ == "__main__":
    
    print(get_token_list_per_wallet('0x29a97c6effb8a411dabc6adeefaa84f5067c8bbe'))
