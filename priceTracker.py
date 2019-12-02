import requests
from bs4 import BeautifulSoup
import smtplib
from re import sub
from decimal import Decimal

def checkPrice():
    # put to find the product link here
    URL = 'https://www.ebay.com.au/itm/Sony-75-X95G-Full-Array-LED-4K-Ultra-HD-Smart-Android-TV-Box-Damaged/283668292759?epid=23034117006&hash=item420bf2a497%3Ag%3Aj1wAAOSwqIldxP1Z&_trkparms=%2526rpp_cid%253D5dc15db70f926b2ecea2adef'
    # inspect mode to retrieve the ID of the price you wish to scrape
    ID = 'prcIsum'
    # put your target price here
    PRICE_TARGET = 500
    # google user agent to get your browser info and paste it here
    headers = {
        "User-Agent":
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36' }

    # this part does most of the magic
    page = requests.get(URL, headers = headers) 
    soup = BeautifulSoup(page.content, 'html.parser')
    price= soup.find(id=ID).get_text()
    # here you should set the price[] range according to how it is displayed when you inspect the price, get rid of 
    # all characters before but not include $ sign (leave the dollar sign there)
    converted_price = Decimal(sub(r'[^\d.]', '', price[3:]))

    if (converted_price < PRICE_TARGET):
        send_email(price)

def send_email(price):
    # assume everybody uses gmail
    EMAIL_ADDRESS = 'username@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 857)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # check 2-step authentication and put the generated password here
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
    print('email has been sent to: ', EMAIL_ADDRESS)
    server.quit()

checkPrice()