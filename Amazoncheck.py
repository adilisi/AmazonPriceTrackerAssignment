#IMPORTING PACKAGES THAT ARE NEEDED.
import requests
from bs4 import BeautifulSoup
import smtplib
import time
#SETTING OUR PRODUCT THAT WILL BE USED
URL = "https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=zg_bs_electronics_home_2?_encoding=UTF8&psc=1&refRID=ZKZCJY3YZ1S5QC96CS6J"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
Wanted_Price = 45
#CREATED FUNCTION TO TRACK THE PRICE OF OUR PRODUCT AND PRINTING IF ITS TO EXPENSIVE OR IF ITS ON SALE.
def Price_track():
    price = check_price()
    if price > Wanted_Price:
        diff = price - Wanted_Price
        print("The Product is still {:.2f} too expensive for me.".format(diff))
    else:
        print("The Product is now on sale. Go purchase it fast before its gone!")

#CREATING THE CHECK_PRICE FUNCTIONT TO CHECK THE PRICE OF THE PRODUCT AND SEND EMAIL DEPENDING ON THE PRICE.
def check_price():
    page = requests.get(URL, headers=HEADERS)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
#GETTING PRODUCT WITH BEAUTIFULSOUP AND THE PRICE. THEN PASSING IT THROUGH CONVERTED_PRICE
    title = soup2.find(id="productTitle").get_text().strip()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])
    #CHECKING IF THE PRICE IS LESS THAN 30 AND IF IT IS SEND AN EMAIL.
    if(converted_price < 30):
	    send_mail()
#PRINTING THE PRICE AND TITLE OF OUR PRODUCT.
    print(converted_price)
    print(title)
 #CHECKING IF PRICE IS LESS THAN 30 STILL AND SENDING EMAIL.
# IF YOU WOULD LIKE TO TEST THE PROGRAM CHANGE THE < TO A > AND RUN THE PROGRAM TO RECEIVE THE EMAIL AND MAKE SURE IT WORKS.
    if(converted_price < 30):
	    send_mail()


#CREATING THE SEND MAIL FUNCTION.
def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	#LOGGING INTO THE YOUR GMAIL AND USING APP PASSWORD (CHECK THE README) TO LOGIN IN TO SERVER.
	server.login('FILL YOUR EMAIL HERE','FILL YOUR APP PASSWORD HERE')
	#THE MESSAGES THAT WILL BE SENT IF YOUR PRODUCT HAS BEEN DETECTED TO BE CHEAPER AND WILL ME EMAILED OUT.
	subject = 'THE PRICE HAS BEEN DECREASED! YOU ITEM IS NOW CHEAPER GO FAST!'
	body = 'YOU CAN CHECK YOUR AMAZON LINK HERE  https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=zg_bs_electronics_home_2?_encoding=UTF8&psc=1&refRID=ZKZCJY3YZ1S5QC96CS6J'
	msg = "Subject: YOUR PRODUCT IS ON SALE \n\n PRICE HAS FELL ON YOUR PRODUCT GO GO FAST AND PURCHASE IT at \n https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=zg_bs_electronics_home_2?_encoding=UTF8&psc=1&refRID=ZKZCJY3YZ1S5QC96CS6J"
	#SETTING THE EMAIL YOU ARE USING AND THE EMAIL YOU WANT TO SEND THE MESSAGE TO.
	server.sendmail(
	'FILL THE EMAIL FROM SERVERLOGIN HERE',
	'ENTER THE EMAIL YOU WANT TO SEND TO',
	msg
	)
	#PRINTING OUT THE RESPONSE IN CONSOLE ONCE THE EMAIL GETS SENT.
	print('The Email has been sent. Please check your email to get the link to the updated listing and product.')
	server.quit()
	#RUNNING CHECK_PRICE FUNCTION AND DOING IT EVERY HOUR. READ THE README FILE TO CHANGE THE TIME IT CHECKS THE PRODUCT.
while(True):
    check_price()
    time.sleep(60 * 60)
