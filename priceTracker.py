import requests
from bs4 import BeautifulSoup
import smtplib

def checkPrice():
    # need to find the product link and id for the price (it may change)
    URL = 'https://www.amazon.com.au/Soniq-N65UX17A-AU-Google-Chromecast-Built/dp/B07JHYD5R4?smid=ANEGB3WVEVKZB&pf_rd_p=407520f4-63f9-4772-91bf-5ffe50123934&pf_rd_r=HEBK96XGBHD7J5E6S743'
    ID = 'priceblock_ourprice'

    headers = {
        "User-Agent":
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36' }

    page = requests.get(URL, headers = headers) 

    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

    price= soup2.find(id=ID).to_text()
    converted_price = float(price[1:])

    if (converted_price > 500):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 857)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('username@gmail.com', '2-step authentication generated password')
    subject = 'Price Reached Ideal Range'
    body = 'Check the link https://www.amazon.com.au/Soniq-N65UX17A-AU-Google-Chromecast-Built/dp/B07JHYD5R4?smid=ANEGB3WVEVKZB&pf_rd_p=407520f4-63f9-4772-91bf-5ffe50123934&pf_rd_r=HEBK96XGBHD7J5E6S743'

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'email1@gmail.com',
        'username@gmail.com',
        msg
    )
    
    print('price Drop and email has been sent')
    server.quit()

checkPrice()