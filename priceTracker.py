import requests
from bs4 import BeautifulSoup
import smtplib
from re import sub
from decimal import Decimal

def checkPrice():
    # need to find the product link and id for the price (it may change)
    URL = 'https://www.ebay.com.au/itm/Sony-75-X95G-Full-Array-LED-4K-Ultra-HD-Smart-Android-TV-Box-Damaged/283668292759?epid=23034117006&hash=item420bf2a497%3Ag%3Aj1wAAOSwqIldxP1Z&_trkparms=%2526rpp_cid%253D5dc15db70f926b2ecea2adef'
    ID = 'prcIsum'
    # put your target price here
    PRICE_TARGET = 500

    headers = {
        "User-Agent":
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36' }

    page = requests.get(URL, headers = headers) 

    soup = BeautifulSoup(page.content, 'html.parser')

    price= soup.find(id=ID).get_text()
    converted_price = Decimal(sub(r'[^\d.]', '', price[3:]))

    print(converted_price)

    if (converted_price < PRICE_TARGET):
        send_email(converted_price)

def send_email(price):
    EMAIL_ADDRESS = 'username@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 857)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL_ADDRESS, '2-step authentication generated password')
    subject = 'Price Reached Ideal Range'
    body = 'Check the link https://www.amazon.com.au/Soniq-N65UX17A-AU-Google-Chromecast-Built/dp/B07JHYD5R4?smid=ANEGB3WVEVKZB&pf_rd_p=407520f4-63f9-4772-91bf-5ffe50123934&pf_rd_r=HEBK96XGBHD7J5E6S743'

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        EMAIL_ADDRESS,
        EMAIL_ADDRESS,
        msg
    )
    
    print('price Drop has dropped to: ', price)
    print('email has been sent to,')
    server.quit()

checkPrice()