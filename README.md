# About Ecommerce shoes
Hello everyone! This is E-commerce shoes that sell most shoes ranging from trainers and other types. All you just need to do is to check the foot wears online and choose one. Pick the one that is good for you and check out the product online. Although these are what we have right now, there are more shoes that will be introduced in the future.
This project is my final one that will complete the Full Stack Software Developing Course in Code Institute. 
I treasure this project very much because of its challenging areas that are close to my heart. This is because I am fascinated with several kinds of shoes especially trainers that are new and “shiny” as I call it. This is something most Black British young men do like. Back in my younger days I would take old and worn-out trainers from the streets or waste and patch them into a useful foot ware. This is one of my ways of loving trainers. As technology is becoming part of our daily life, I developed the idea of making online shoe business that can be very appealing to customers. So therefore I developed the Ecommerce Shoe website.

# Website
[Visit the website](https://ecommerce-shoes-website.herokuapp.com/)

---

<a></a>

# Table of contents 
* UX
    * The objectives of the website
    * User Stories
        * As a user I want
        * As a user I want to
    * Necessities and expectations of the user
        * Necessities
        * Expectations
    * How to use the site
    * Choice of design in the site
    * Fonts
    * Structure of the site
* Wireframes and Flowcharts
    * Wireframes
    * Flowcharts
* Features of the website
    * Features that are already implemented
    * Features that need to be created on the site
    * Technologies used in this site
        * Software languages
        * Libraries
        * Framework tools
        * External deployment tools
        * Flake8
* Testing
    * Google Chrome DeVop
    * All Dev Emulated Devices
    * Validating tools
    * Lighthouse
* BUGS IDENTIFIED
    * Errors identified with Heroku push
* STRIPE and EMAIL
    * Setting up and using Stripe
    * Email
    * Social media
* Deployment
    * Git deployment
    * These are the steps to clone the project
    * Further work on the requirements.txt
* Credits

--- 

<a name="ux"></a>
# UX

<a name="user-goals"></a>
## The objectives of the website

- Upon going to the site, the user must have a good viewing experience so much that he/she will explore other areas in the site. The site must have an appealing feeling to the user. 
- The site must work well on all devices such as desktop, laptops, tablets, and mobile phones.
- The site must have the ability to be able make sure that the viewer can clearly see all shoe products on most desired page.
- The products on the site must have their specific information
- The site must have an access in a way that the products must be easily checked out and allow for more additional products in the products pack.
- There must be an ability to sign in or sign up on the page where the user is able to view the accounts and details
[Back to Top](#table-of-contents)

<a name="user_stories"></a>
## User Stories

<a name="i-want"></a>
### As a user I want:
- the website to be very appealing to me in terms of design and feeling
- the website to have varieties of shoe products ranging from trainers to casual shoes
- The shoes to have descriptive information on the site
- The site to have the price available to me easily
- To make sure that the site is easy to pay for each product chosen
- To make it easy to sign up or sign off my account page
- To make sure that each shoe has the kind that I need
- To make sure that it is easy for me to see the product price and compare the products that fit me in terms of my product style choice.

<a name="i-want-to"></a>
### As owner of the site, I want to:
- promote my site in a way that will keep existing customers and attract new customers
- make the checkout process easy and straight forward
- make it easy for customers to sign in and sign up 
- make sure that customers can easily browse through the site and view the shoe items
- make separate sites for specific type of shoes (e.g. trainer sections, casual shoes)
- I want to make it easy to add shoes in the future.

<a name="needs-of-the-user"></a>
## Necessities and expectations of the user

<a name="necessities"></a>
### Necessities
- The easy way for the site to be navigated using the navigation bar and other types of links that leads to other pages inside the website
- Attractive pages that has a good view to the user
- The site is easy for the shoes to be viewed when landing on the site
- The site is easy to select shoes and reserve them in a product pack
- There is an availability to store information via sign up in the account
- The images of the shoes can be easily viewed on the site
- The information of each item.

<a name="expectations"></a>
### Expectations
- When clicking on to a shoe product, it should give me the page centred based on the product information
- I expect the links in the navigation area to properly direct me to wherever I want to go
- I expect the prices of the products to be correct based on their information

<a name="how-to-use-site"></a>
## How to use the site
- Pick a shoe product and click "Put to Pack". 
- Click on the shopping bag icon on the top to check out.
- Then click "Checkout" to checkout the purchase
- After filling in the details to finalise the purchase it will produce a checkout confirmation.

<a name="choice-of-design"></a>
## Choice of design in the site
The background of the website on the Home Page is made of different trainers such as Nike, Addidas, Puma, etc. This gives the background a good appeal in how users view the shoe website. The background image is gotten from Google Images. 
The colours used in other pages are used to design some pages on the sites:
- Darkgreen
- Wheat
- Cornsilk
- Darkslategrey
- Beige
- Darkorange
- Black

<a name="fonts"></a>
## Fonts
Most of the font families are gotten from Google Fonts. They are:
- Segoe UI
- Roboto
- Oxygen
- Ubuntu
- Cantarell
- Open Sans
- Helvetica Neue
- Sans-serif

<a name="structure-of-site"></a>
## Structure of the site
- Home page: this is more of a “welcoming” page is aimed at attracting the viewer in an attractive way. The welcoming feeling of the page is designed with various shoes trainers background dyed with red colour and has a “buy now” clickable link with a reddish colour. 
- Shoe pages: contains all the shoe pages including casual shoes and trainers
- Trainers page: this contain the shoes that are considered trainers 
- Casual shoes page: this contain shoes that are not trainers
- Account page: the user account page after signing in
- Sign up page: contains empty slots for fillings by the user 

[Back to Top](#table-of-contents)

<a name="wireframes-and-flowcharts"></a>
# WIREFRAMES AND FLOWCHARTS

<a name="wireframes"></a>
## Wireframes 
I used Mockflow tools to design the website. For each page, I made 2 forms of wireframes: laptop/desktop, and mobile.
- Home page
- shoe pages
- Account page

<a href="">
        <img src="/wireframes/wireframe_fullstack-3.png" alt="Webhooks successful">
    </a>

<a name="flowcharts"></a>
## Flowcharts 
I then made a flowchart for the site in terms of check out. (I decided to this by using Microsoft Word to design it). 
    <a href="">
        <img src="/wireframes/wireframe_MS_Fullstack-1.png" alt="Webhooks successful">
    </a>

<a name="features-of-the-website"></a>
# FEATURES OF THE WEBSITE

<a name="features-implemented"></a>
## Features that are already implemented
- Registeration and signin ability using allauth platform from Django.
- The ability for the user to check out products 
- Ability for the user to click and view different shoes
- View the existing shoes that are already established on the site

<a name="features-needed"></a>
## Features that need to be created on the site
- Future shoe webpage design that can be attract new users and give a better feel
- More and expansive information on each shoe products 
- Introduction to new various shoes that are about to break into the shoe market

<a name="technologies-used"></a>
## Technologies used in this site

<a name="software-languages"></a>
### Software languages
- HTML/CSS
- JAVASCRIPT
- PYTHON
<a name="library"></a>
### Libraries
- Font Awesome
- Bootstrap
- Google Fonts
- jQuery
- 
<a name="framework-tools"></a>
### Framework tools
- Allauth
- Django
- Gunicorn
- Pillow
- Psycopg
- Unicorn
- Gitpod
- Pip3
- Django-heroku 

<a name="external-deployment"></a>
### External deployment tools
- Heroku

<a name="flake8"></a>
### Flake8
Flake8 is a very useful tool in making your python codes tidy. 
It tells you where exactly in a python file there should be some arrangements and tidiness that need to be done.
However there are some information that it will provide that do not need attention. 
For examplesuch as some useful variables that are needed in the codes which will signify that it is not useful. However if you remove these
variables it can lead to certain errors. Other issues that it will prompt up that do not need attention are the migration files.

[Back to Top](#table-of-contents)

<a name="testing"></a>
# Testing
Using DeVop technologies can be browsed using these platforms:

<a name="google-chrome"></a>
## Google Chrome DeVop

<a name="emulated-devices"></a>
## All Dev Emulated Devices
- All Samsung Galaxy series
- All iPhone series
- All Blackberry series
- All Galaxy series
- All Nexus series
- All Pixel series
- All IPad series

<a name="validating-tools"></a>
## Validating tools
There were validating tools used to validate the CSS/HTML codes to verify for errors.
One of them is the [validator](https://validator.w3.org/) which is used for HTML. The other for CSS is [jigsaw](https://jigsaw.w3.org/css-validator/)

<a name="lighthouse"></a>
## Lighthouse
To use Lighthouse, since it is Chrome based, you can easily download the Chrome and make it as an extension to the page.
The Lighthouse should be next to the searchbar. Go on the website and click on Lighthouse and get a result.

[Back to Top](#table-of-contents)

<a name="bugs-identified"></a>
# BUGS IDENTIFIED

<a name="errors-identified"></a>
## Errors identified with Heroku push
There were series of persistent errors encountered when trying to deploy to Heroku through Gitpod. One of the most common errors encountered are that the python version (Python 3.6.8) installed into Git do not support the version for pushing into Heroku. The version is needed to be upgraded to Python 3.8.8 for the stack Heroku-20 allowing the push to be successfully built. This is in addition when the required packages for Django to be successful where installed and validated them on requirements.txt. 
Another error encountered here is when the DISABLE_COLLECTSTATIC and the HEROKU_HOSTNAME config vars in Heroku were removed while running manage.py collectstatic. AWS Secret and Access keys were then added which made the build-up push to Heroku successful. 
Other problems encountered
The most common and enduring problem is the background image not showing (# THIS NEEDS TO BE EXPANDED).

[Back to Top](#table-of-contents)

<a name="stripe-email-social_media"></a>
# STRIPE, EMAIL and SOCIAL MEDIA

<a name="setting-up-stripe"></a>
## Setting up and using Stripe
- On the Gitpod workspace, with pip3 installed, pip3 install stripe was typed. This links Stripe with Django.
- On the Stripe website, a personal account was made.
- The Stripe secret key and Stripe public key details were set up in the settings.py and env.py. Both keys are available on the API
    section under the Developers section. 
- Test the stripe payment on the account site by making a purchase on the E-commerce website. This will send an alert on how successful
    transaction went. 
- Based on the history logs, the payments should be successful based on the transaction. So here is a sample below:
    <a href="">
        <img src="/wireframes/Log_Payment_success_1.png" alt="Webhooks successful">
    </a>
    <a href="">
        <img src="/wireframes/Log_payment_success_2.png" alt="Webhooks successful">
    </a>
- If the payment is successful it should view a HTTP status as 200(OK).
    <a href="">
        <img src="/wireframes/Webhooks_review.png" alt="Webhooks successful">
    </a>

- If unsuccessful it will display the HTTP status as 404.
    <a href="">
        <img src="/wireframes/Webhook_fail_404.png" alt="Webhooks successful">
    </a>
- Or a HTTP status code 500 status error.
    <a href="">
        <img src="/wireframes/Webhook_fail_500.png" alt="Webhooks successful">
    </a>
- In addition, the events of financial activities can be found on the Events area under the Developers tab.

<a name="email"></a>
## Email
- First you must install allauth using:

        pip3 install django-allauth==0.41.0

And then use

        pip3 freeze > requirements.txt

- Then obtain the passcode from your gmail account and paste it into Heroku Config vars. 
- Test the email functionality by signing up. 
Please note that the email used must be the email created from gmail. (i.e my gmail created.). Also note
that the phone details as well the ecommerceshoes@example.com email are dummy/test contact details; they are not created
or real. 

The only real contacts are the social media links in the footer section.

<a name="social-media"></a>
## Social media
- The website social links are already created such as Facebook, Twitter, Instagram, and Telegram. All can be found on the footer. 

[Back to Top](#table-of-contents)

<a name="deploment"></a>
# DEPLOYMENT

<a name="git-deployment"></a>
## Git deployment
The project is written using Github and there Gitpod is used to write the code. The work is then committed to git repository. The git repository page was linked to Heroku which means that pushing the work automatically pushes to Heroku even after not installing Heroku into workspace. This means in contrary to popular suggestion, there was no need to use “git push heroku master”. Gitpod was used for project development. The methods to install packages using pip3 and other virtual environments is [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Moreover depending on how a certain Django might be installed individually, here is how it can be installed manually [here](https://bennettgarner.medium.com/deploying-django-to-heroku-procfile-static-root-other-pitfalls-e7ab8b2ba33b)

These are the steps to clone the project:
-	While in the user git repository page, the “code” button in order to download the particular zip repository. This is cloning the project. The other method of doing this is typing the command line:

        git clone “LINK”
-	The required folder needs to be installed using the command which will install the necessary folder requirements that allow the Django to work effectively.

        pip3 install –r requirements.txt
-	There has to be a file that called the env.py which contains the environmental variables which is at the what is known to be the root of the application. It must look like this

        import os
        os.environ[“ SECRET KEY”]=”the secret key”

The secret key is the unique key set in the settings.py. The purpose of the secret key is to keep the file secure by using a cryptographic signing. The env.py is still added to .gitignore file so as to push this application public.
-	The command 

        “python3 manage.py migrate” 
is used to move models in the database in the process called migration. alternatively the files can be manually migrated from the database. For example the shoes details on my database were migrated to my Django administration account manually. 
-	A superuser must be created using the following command

        “python3 manage.py createsuperuser”

- In order to run the app live from the server the foolowing comad must be typed:

        “python manage.py runserver”

- In addition, the website can be accessed on the admin account for other activities. 

<a name="ways-to-clone-project"></a>
## These are the steps to clone the project
- While in the user git repository page, the “code” button in order to download the particular zip repository. This is cloning the project. The other method of doing this is typing the command line:

        git clone “LINK”
- The required folder needs to be installed using the command which will install the necessary folder requirements that allow the Django to work effectively.
pip3 install –r requirements.txt
- There has to be a file that called the env.py which contains the environmental variables which is at the what is known to be the root of the application. It must look like this
import os

        os.environ[“ SECRET KEY”]=”the secret key”

The secret key is the unique key set in the settings.py. The purpose of the secret key is to keep the file secure by using a cryptographic signing. The env.py is still added to .gitignore file so as to push this application public.
- The command 

    “python3 manage.py migrate” 
is used to move models in the database in the process called migration. alternatively the files can be manually migrated from the database. For example the shoes details on my database were migrated to my Django administration account manually. 
- A superuser must be created using the following command

        “python3 manage.py createsuperuser”

- In order to run the app live from the server the foolowing comad must be typed:

        “python manage.py runserver”

- In addition, the website can be accessed on the admin account for other activities. 

<a name="further-work-requirements"></a>
## Further work on the requirements.txt
- After the superuser has been created, the procfile must be created so as to declare an application process and the site entry points. It can be created by just using the file tab or created using the command in the workspace:

        “echo web: python app.py > profile”

And must freeze the requirements by using this command:

    “pip3 freeze –local > requirements.txt”

The procfile must require a Gunicorn for it to work. If it is not present then it can be installed using the command:

    “web: gunicorn <name of the project>.wsgi:application”
- Committing the files should be done as follows:

        “git add . (or git add –A)”
        “git commit –m <write your commit message>”
        “git push”

Alternatively you can you can deploy the app to Heroku through using:

    “git push heroku master”

- Then it can be deployed in the Heroku account by going to the “Deploy” tab and then clicking “enable automatic deployment”.  Beneath it then the “Deploy branch” should be clicked which will build the app and can be viewed by just clicking the “Open app” at the top right. 

[Back to Top](#table-of-contents)

# CREDITS
I want to especially thank majority of the Code Institute members including the tutors and my mentor for their vast amount of help despite my family difficulties I faced during much of the pandemic/COVID season. The season especially was a very difficult period not just for me but for a lot of people who have undertaken this project. Despite this it was a worthwhile of counter battle against such problems and victory was finally achieved. 