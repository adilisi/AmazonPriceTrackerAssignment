# AmazonPriceTrackerAssignment
AmazonPriceTracker Made with Python Final

# INTRODUCTION
The Amazon Price Tracker is used to track one product on Amazon US. It will scrape Amazon every hour and send an email to you if the product is on sale. This can be used to get your favorite items off of Amazon at a cheaper price. For this application it will show you the Amazon Echo as the product unless you edit the code yourself.

# PREREQUISTES
Before running the application please make sure to import the following items to python.
1.REQUESTS-  pipenv install requests or (MAC USERS) sudo  pipenv install requests 
2.BEAUTIFULSOUP
3.IMPORT SMPTLIB - pip install smtplib
4.IMPORT TIME
You also should have a basic understanding of Python and how to import those packages depending on your operating system.

# INSTALLATION
I have provided the entire code file below. All you need to do is download the code file and open it on your own machine. Please read below on how to use it.

# HOW TO USE IT
1. Before running the code you need to scroll down to line 45 and enter your email address and the APP PASSWORD where it tells you.
HOW TO GET THE APP PASSWORD- (https://myaccount.google.com/apppasswords)
2. In Line 6 where it shows URL = Paste your Amazon US link to monitor for this we will be using the Amazon Echo.
2. Look down to line 50 and 51 and follow the directions that it says. Enter the email you used above and the email you want to send the message of updated prices to.
3. If you would like it to refresh the product more than one time per hour please change the final line of code to your liking. For example just change it to 30 for it to refresh the product every 30 seconds.
4. RUN THE PROGRAM AND ENJOY!!

# TESTING THE PROGRAM
Due to this application relying on the market of specific items on Amazon you will not receive an email right away it may take days for the product to update. To test and make sure the application is working please go down to line 35 and change the < to > and run the program again. If everything is correct you should be receiving an email with the product link and it alerting a price drop.

# License
https://choosealicense.com/licenses/mit/


