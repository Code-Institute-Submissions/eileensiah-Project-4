LIVE DEMO LINK
==============
https://project-4-maid-platform-django.herokuapp.com/


BACKGROUND:
==========
* More than 80% of Singapore families are dual income family. Most of these families employed Foreign Domestic Workders (FDWs) to take care of their households and look after young children and elderly.
* These Foreign Domestic Workders (FDWs) come from Philippines, Indonesia, Myanmar and India.
* Currently, there are about 200,000 FDWs working in Singapore.  They are paid a fixed monthly salary and stay with employers.
* At the same time, there are more than 600 service providers (Maid Agencies) that help to source these FDWs from neighbouring countries to meet the demand in Singapore.
* There are families who opt for Part Time Helpers to come in once or twice a week to clean the house.  Part time helpers are charged by hourly.
* With this platform, Maid Agencies are able to list their FDWs biodata and generate sales lead through enquiries from potential employers.
* For potential employers, they can view more than a few thousands FDWs biodata at this platform at their devices instead of visiting Maid Agencies to make enquiry or collect FDWs biodata.
 


BUSINESS MODEL
==============
* This platform generate its revenue from monthly subscription paid by employment agencies.  
* By subscribing to one of the three plans, agencies are able to post details of their FDWs on this platform, and thus generate enquiries from potential employers. Some of this enquiries will resulted in sales.



A) User Stories - Employment Agency:
==================================
* As agencies, we want to be able to list our FDW's biodata online to generate enquiries.
* As agencies, in order to provide better service, we would prefer potential employer to shortlist their preferred FDWs and email us. This will shorten the sales cycle.
* Alternatively, potential employers can also send in general enquiries with their selection criteria for us to match their requirements.


B) User Stories - Potential Employer:
==================================
* As potential employers,  we want to be able to send our enquiries/ requirements to all the agencies, and for them to match our requirements. This will shorten our time and effort in sourcing for our preferred FDWs.
* As potential employers,  we want to be able to view all the FDWs profiles on any of our devices at any time, 24 hours x 7 days.
* As potential employers,  we want to be able to interview the FDWs at places that are convenient to us instead of at agencies office.
* As potential employers, we do not want to waste time calling/ visiting agencies office to make enquires or view helpers' profile. 


UX DESIGN
=========
* This website is designed in an orderly and logical manner. It aims to allow users to have an easy time navigating for informations .  User are not required to go beyong 3 clicks to get to their destination.
* Orange and blue are the main colour theme for this website. It gives a trendy yet professional look. 


FEATURED 
========
* This website is makeup of 4 parts:
    * A) Website (consits of "Home" page, "Search Maid" page, "Shortlisted" page and "Enquiry" page)
    * B) Employer and agency "Sign up" and "Log in".
    * C) Agency Admin Page (consists of "General Enquiry" page, "Shortlisted Enquiry" page,, "Maid List" page, "Product" page and "Shopping Cart" page)
    * D) Super Admin Page (consists of "Agency Detail" page, "Employer Detail" page, "General Enquiry" page, "All Shortlisted Enquiry" page and "All Maid List" page )


A) Web Site
===========
* On the navibar, there are "Home" Page, "Search Maid" page, "Shortlisted" page and "Enquiry" page. 
    * Home Page - It consists of 5 sections
        * The banner has a search box with dropped down options for users to do a quick search for their preferred FDWS. This is very useful for user who prefer to "go straight to the point". 
        * Next is the "Steps" section which provide guidance for users who need help to navigate this website. 
        * Followed by is "Preference" section which provide users a quick search option for the top 6 choices (Full time maid, Part Time Maid, Confinement Nanny, Care for Infant/ Children, Care for Elderly/Disable, General Housework and Cooking).
        * Due to time constrain, i have not done up the webpage for Part Time Maid and Confinement Nanny.  Therefore, these two links are not working.
        * After this is the "Testimonial" section, contributed by happy and satisfied users of this website.
        * The last part is a banner with enquiry button, which allow users to send in their enquiries. This last parts appeared at the end of every webpage.
        
    * Seach Maid Page - It consists of 2 sections
        * This page has a "filter" option which allow users to custom their searches based on "Nationality", "Type of Maid", "Main Responsibility", "Language Ability", "Marital Status" and "Age".
        * When user clicked on the "shortlisted" button at the end of the FDW's biodata, It will lead them to "Employer Sign Up" page.  Users must sign up in order to shortlist the maids, and it provides them with the benefit of viewing their shortlisted cart at any devices.
        * The last part is a banner with enquiry button.
        
    * Shortlisted Page - It consists of 3 sections
        * This section consists of the FDWs the the users has selected.  At the end of each biodata, they is a "remove" button for users to unselect their choice.
        * Next is the "Shortlisted Enquiry Form", which require users to provide their contact informations.
        * The last part is is a banner with enquiry button.
        
    * Enquiry Page - It consists of 2 sections
        * The first part is an enquiry form. It has dropdown options for employer to select their requirements such as "Maid Nationality", "Maid Responsibility", "Type of Maid" and "Age."
        * The last part is is a banner with enquiry button.
         

B) "Sign Up" and "Log In"
============================================
* This platform have "sign up" and "log in" function for both potential employers and agencies. 
* Employer "sign up" and "log in" buttons are at the right of the navibar.
    * Sign up is only required from employers who have shortlisted FDWs.  Thus, allowing them to view their shortlisted cart from any devices.

* Agency "sign up" and "log in" button are at right of the footer.
    * Once agency logged in, it will lead them to their admin account. From there, agency are able to:
    * View general enquiries and shortlisted enquiries send by potential employers. 
    * Manage FDW biodatas.  Agencies are able to create new biodata, edit current biodata as well as delete unwanted biodata.
    * View the different type of subscription plans and select the plan they want to subscribe.
    * Make online payment to the platform vendor using Stripe.
    

C) Agency Admin
===============
* On the Agency Admin navibar, there are "General Enquiry" page, "Shortlisted Enquiry" page, "Maid List" page, "Product" page and "Cart" page.
    * General enquiry page - It displays all the general enquiries send in by the potential employers. These group of employers do not have any preferred FDWs in mind. Therefore, agencies have to recommend FDWs based on emplyoyer requirements.
    * Shortlisted enquiry page - It displays all the shortlisted enquries send in by potential employers. Employers have selected their preferred maids and agencies need to revert back to employers as soon as possibel.
    * Maid List page - It displays all the FDWs that belongs to this agency. In this page, agency is also able create, view, edit and delete any biodata.
    * Product page - This page show information on subscription plan for agency to subscribe in order to use this platform.
    * Cart - It showed the subscription plan agency has selected as well as for them to make payment.
    
* I have created 3 agency accounts with following log in information for testing.
    * user name: cindy ; log in password : cindy123!@# ; Agency name: Nanyang Employment
    * user name: eric ; log in password : eric123!@# ; Agency name: Asia Care Consultancy
    * user name: Evon ; log in password : evon123!@# ; Agency Name: Wonderful Employment
    
    
    

D) Super Admin
==============
* I have created the the following app for this project.
    * Webfront app - It contains information regarding to website frontend, such as "Home", "Search Maid", "Shortlisted" and "Enquiry"
    * Accounts app - For creation of user account.  There are 2 types of accounts, agency account and employer account.
    * Agency app - For informations on general enquries, shortlisted enquries, FDWs biodata, and product plan.
    * Payment app - For payment using Stripe.
    * Product cart - It shows the product plans that agency has selected.
    * Shortlisted cart - It shows the FDWs that potential employers have selected.
    
* To log into into super admin account. Pls use the following
    * user name: admin2; password: 1234!@#$
    

FEATURES LEFT TO IMPLEMENT
=========================
* Due to insufficient time, the following features have yet to be implemented:
    * To be able to send a reset password email to the user when the user submits the form for forgot password.
    * I have not done up the webpage for Part Time Maid and Confinement Nanny.  Therefore, these two links is not working.



TECHNOLOGIES
============
* Bootstrap
* HTML
* CSS
* Javascript
* Jquery
* Python
* Django
* PostgreSQL
* Amazon S3



TESTING
=======
* Testing was done across multiple viewports sizes to ensure responsiveness. HTMLHint were used to check the HTML code and CSSLint were also used to check the CSS code. JSHint was used to check the Javascript code.
* Manual testing was employed to check all the buttons and links are functioning properly.



DEPLOYMENT
==========
* This site is hosted using Heroku.

