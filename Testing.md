

# Testing home page

## Link tracking 

### Home Page
|Link|Location  |Pass/Fail|
|--|--|--|
|  Logo | index.html |Pass|
|Home|index.html|Pass|
|Destinations/All Tours|products.html|Pass|
|Destinations/K'gari(Fraser Island)|products.html with filter for K'gari products|Pass|
|Destinations/Whitsundays|products.html with filter for whitsundays products|Pass|
Destinations/Great Barrier Reef|products.html with filter for Great Barrier Reef products|Pass|
|Contact Us|contact.html|Pass|
|About Us|about.html|Pass|

- When a user is not logged in they can still click the "My account" drop down menu. This will provide two seperate links: Register and Log in.

  |Link|Location  |Pass/Fail|
|--|--|--|
|  Register|all auth registration page|Pass|
|Log in | all auth log in page| Pass


- The Register link will take them to the following page
    ![Register](docs/testing/register.png)
- The log in link will take them to the following page
    ![LogIn](docs/testing/login.png)

- When a user creates an account they will be brought to an email confirmation page. Users will then be sent an email to the email address provided. This takes the user back to the site where they can confirm their email.
    ![LoginEmail](docs/testing/NewAccEmail%20.png)
- 

- When a user succesfully signs in they will be presented with the below toast message
    ![SigninToast](docs/testing/signinToast.png)


- When a user clicks the destinations images on the homepage they will be taken to a different location
|Destinations Link|Location  |Pass/Fail|
|--|--|--|
|Destinations/All Tours|products.html|Pass|
|Destinations/K'gari(Fraser Island)|products.html with filter for K'gari products|Pass|
|Destinations/Whitsundays|products.html with filter for whitsundays products|Pass|
|Destinations/Great Barrier Reef|products.html with filter for Great Barrier Reef products|Pass|

###  Footer

![Footer](docs/features/footer.png)

 - The footer is comprised of three sections. The first section is a brief synopsis of the company. The second section is a list of links to different "Destinations" and the different products associated with those regions.


|Destinations Link|Location  |Pass/Fail|
|--|--|--|
|Destinations/All Tours|products.html|Pass|
|Destinations/K'gari(Fraser Island)|products.html with filter for K'gari products|Pass|
|Destinations/Whitsundays|products.html with filter for whitsundays products|Pass|
|Destinations/Great Barrier Reef|products.html with filter for Great Barrier Reef products|Pass|


- There is another section of links that will take you to "Your Account", "Contact Us", "About Us" and "Privacy Policy".

|Destinations Link|Location  |Pass/Fail|
|--|--|--|
|Contact Us|contact.html|Pass|
|About Us|about.html|Pass|
|My Profile|Profile.html|Pass|
|Privacy Policy|privacy.html|Pass|

- There is also a Contact section in the footer that allows users to contact the company directly via phone or email.

|Action|Application  |Pass/Fail|
|--|--|--|
|Send Email|Open Email Client|Pass|
|Phone company|Open facetime on desktop|Pass|





### Toasts

- Toasts have been introduced to keep users informed of different progress and activities on the site. Toasts have been included with a timer that they should only last for 5 seconds


- When a user signs in they will be sent the following Toast.
   ![SigninToast](docs/testing//toasts/signinToast.png)

- When a user creates a new account they should be greeted with this Toast

### Email confirmation

- When a user creates an account they will be brought to an email confirmation page. Users will then be sent an email to the email address provided.
    ![LoginEmail](docs/testing/emails/NewAccEmail.png)