import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=zg_bs_electronics_home_2?_encoding=UTF8&psc=1&refRID=ZKZCJY3YZ1S5QC96CS6J"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
Wanted_Price = 45

def Price_track():
    price = check_price()
    if price > Wanted_Price:
        diff = price - Wanted_Price
        print("The Product is still {:.2f} too expensive for me.".format(diff))
    else:
        print("The Product is now on sale. Go purchase it fast before its gone!")


def check_price():
    page = requests.get(URL, headers=HEADERS)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text().strip()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])
    
    if(converted_price < 30):
	    send_mail()

    print(converted_price)
    print(title)
    
    if(converted_price < 30):
	    send_mail()



def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('FILL YOUR EMAIL HERE','FILL YOUR APP PASSWORD HERE')
	subject = 'THE PRICE HAS BEEN DECREASED! YOU ITEM IS NOW CHEAPER GO FAST!'
	body = 'YOU CAN CHECK YOUR AMAZON LINK HERE  https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=zg_bs_electronics_home_2?_encoding=UTF8&psc=1&refRID=ZKZCJY3YZ1S5QC96CS6J'
	msg = "Subject: YOUR PRODUCT IS ON SALE \n\n PRICE HAS FELL ON YOUR PRODUCT GO GO FAST AND PURCHASE IT at \n https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=zg_bs_electronics_home_2?_encoding=UTF8&psc=1&refRID=ZKZCJY3YZ1S5QC96CS6J"
	server.sendmail(
	'FILL THE EMAIL FROM SERVERLOGIN HERE',
	'ENTER THE EMAIL YOU WANT TO SEND TO',
	msg
	)
	print('The Email has been sent. Please check your email to get the link to the updated listing and product.')
	server.quit()
while(True):
    check_price()
    time.sleep(60 * 60)
