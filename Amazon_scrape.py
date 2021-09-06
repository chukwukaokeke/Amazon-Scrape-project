from bs4 import BeautifulSoup  # pull the data out of HTML
import requests
import time
from datetime import date
import csv
import smtplib  # for sending emails




def check_price():
    # Pull the title and price of the amazon listing
    url = 'https://www.amazon.com/Sony-WH-1000XM4-Canceling-Headphones-Phone-Call/dp/B08MVGF24M/?_encoding=UTF8&pd_rd_w=aoAnS&pf_rd_p=1b1dfb25-2066-4d95-8e14-0250d0ca9656&pf_rd_r=H91HSE1E5GRE811EQKBV&pd_rd_r=2b3fc137-39b1-4786-80cc-3519b3331722&pd_rd_wg=VBww4&ref_=pd_gw_unk'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/92.0.4515.159 Safari/537.36",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"
    }

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    soup1 = BeautifulSoup(soup.prettify(), "html.parser")

    product_title = soup1.find(id="productTitle").get_text()
    product_price = soup1.find(id="priceblock_ourprice").get_text()

    title = product_title.strip()
    price = product_price.strip()[1:]

    # Get current date
    mydate = date.today()
    d1 = mydate.strftime("%m/%d/%y")
    print(d1)

    # Get current time
    mytime = time.localtime()
    t1 = time.strftime("%I:%M %p", mytime)
    print(t1)

    # Appending data to CSV file
    data = [title, price, d1, t1]
    with open('Amazondatafile.csv', 'a+', newline='', encoding='UTF8') as file1:
        writer = csv.writer(file1)
        writer.writerow(data)

#Creating and inserting header in CSV file
header = ['Title','Price','Date','Time']
with open('Amazondatafile.csv', 'w') as csvfile:
    headerwriter = csv.writer(csvfile)
    headerwriter.writerow(header)

# Schedule Loop
while True:
    check_price()
    time.sleep(1)
