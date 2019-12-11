LIVE DEMO LINK
==============



BACKGROUND:
==========
* More than 80% of Singapore families are dual income family. Most of these families employ Foreign Domestic Workder (FDW) to take care of their household and look after young children and elderly.
* These Foreign Domestic Workders (FDWs) comes from Philipine, Indonesia, Myanmar and India.
* Currently, there are about 200,000 FDWs working in Singapore.  They are paid a fixed monthly salary and stay with employers.
* At the same time, there are more than 600 service providers (Maid Agencies) that help to source these FDWs from neighbouring countries to meet the demand in Singapore.
* There are families who opt for Part Time Helper to come in once or twice a week to clean the house.  Part time helpers are charged by hourly.
* With this platform, Maid Agencies are able to list their FDWs biodata and generate sales lead through eqnuiries from potential employers.
* For employer, they can view more than a few thousands FDWs biodata at this platform at their devices instead of visiting Maid Agencies to make enquiry or collect FDWs biodata.
 


BUSINESS MODEL
==============
* This platform generate its revenue from monthly subscription paid by employment agencies.  
* By subscription to one of the three plans, agencies are able to post details of their FDWs on this platform, and thus generate enquiries from potential employers. Some of this enquiries will resulted in sales.



A) User Stories - Employment Agency:
==================================
* As agencies, we want to be able to list my FDW's biodata online to generate enquiries.
* As agencies, in order to provide better service, we would prefer potential employer to shortlist the FDW and email me. This will shorten the sales cycle.
* Alternatively, potential employer can also send in general enquiry with their selection criteria for us to match their requirements.


B) User Stories - Potential Employer:
==================================
* As potential employers,  we want to be able to send our enquiries/ requirements to all the agencies, and for them to match my requirements. This will shorten our time and effort in sourcing for our preferred FDWs.
* As potential employers,  we want to be able to view all the FDWs profiles on any of our devices at any time, 24 hours x 7 days.
* As potential employers,  we want to be able to interview the FDWs at our conventient place instead of at agencies office.
* As potential employers, we do not want to waste time calling/ visiting agencies office to make enquires or view helpers' profile. 


UX DESIGN
=========
* This website is designed in an orderly and logical manner. It aims to allow users have an easy time navigating for informations .  User are not required to go beyong 3 click to get to their destination.
* Orange and blue is the main colour theme for this website. It gives a trendy yet professional look. 


FEATURED 
========
* This website is makeup of 4 parts:
    * A) Website (consits of "Home" page, "Search Maid" page, "Shortlisted" page and "Enquiry" page)
    * B) Employer and agency "Sign up" and "Log in".
    * C) Agency Admin Page (consists of "General Enquiry" page, "Shortlisted Enquiry" page,, "Maid List" page, "Product" page and "Shopping Cart" page )
    * D) Super Admin Page (consists of "Agency Detail" page, "Employer Detail" page, "Subscription receivable" page, "All Shortlisted Enquiry" page, "Maid List" page and "Product" page )


A) Web Site
===========
* On the navibar, there are "Home" Page, "Search Maid" page, "Shortlisted" page and "Enquiry" page. 
    * Home Page - It consists of 5 sections
        * The banner is a search box which has dropped down option for users to do a quick search for their prefered FDWS. This is very useful for user who prefer to "go straight to the point". 
        * Next is the "Steps" section which provide guidance for users who need help to navigate this website. 
        * Followed by is "Preference" section which provide users a quick search option for the top 6 choices (Full time maid, Part Time Maid, Confinement Nanny, Care for Infant/ Children, Care for Elderly/Disable, General Housework and Cooking).
        * Due to time constrain, i have not done up the webpage for Part Time Maid and Confinement Nanny.  Therefore, these two links is not working.
        * After this is the "Testimonial" section, xontributed by happy and satisfied users of the website.
        * The last part is a banner with enquiry button, which allow users to send in their enquiries. This last parts appeared at the end of every webpage.
        
    * Seach Maid Page - It consists of 2 sections
        * This page has a "filter" option which allow users to custom their searches based on "Nationality", "Type of Maid", "Main Responsibility", "Language Ability", "Marital Status" and "Age".
        * When user clicked on the "shortlisted" button at the end of the FDW's biodata, It will lead them to "Employer Sign Up" page.  Users must sign up in order to shortlist the maid, and it provide them the benefit to view their shortlisted cart at any device.
        * The last part is is a banner with enquiry button.
        
    * Shortlisted Page - It consists of 3 sections
        * This sections consist of the FDWs the the users has selected.  At the end OF each biodata, they is a "remove" button for users to unselect their choice.
        * Next is the "Shortlisted Enquiry Form", which require users to provide their contact informations.
        * The last part is is a banner with enquiry button.
        
    * Enquiry Page - It consists of 2 sections
        * The first part is an enquiry form. It has dropdown options for employer to select their requirements such as "Maid Nationality", "Maid Responsibility", "Type of Maid" and "Age."
        * The last part is is a banner with enquiry button.
         

B) Employer and Agency "Sign Up" and "Log In"
============================================
* This platform have "sign up" and "log in" function for both potential employers and agencies. 
    * Employer "sign up" and "log in" button is at the right of the navibar.
    * This is only required from employers who have shortlisted FDWs.  Thus, allow them to view their shortlisted cart from any devices.

* Agency "sign up" and "log in" button is at right of the footer.
    * Once agency log in, it will lead them to their admin account. From there, agency are able to:
    * View general enquiry and shortlisted enquiry send by potential employers. 
    * Manage FDW biodatas.  Agencies are able to create new biodata, edit current biodata as well as delete unwanted biodata.
    * View the different type of subscription plans and select the plan they want to subscribe.
    * Make online payment to the platform vendor using Stripe.
    

c) Agency Admin
===============
* On the Agency Admin navibar, there are "General Enquiry" page, "Shortlisted Enquiry" page, "Maid List" page, "Product" page and "Cart" page.
    * General enquiry page - For general enquiry, employers do not have any prefered FDWs in mind. Therefore, agencies have to recommend FDWs based on emplyoyer requirements.
    * Shortlisted enquiry page - Employers have selected their prefered maid and agencies need to revert back to employers on their selection.
    * Maid List page - It showed all the FDWs that belongs to this agency. In the page, agency is also able create, read, edit and delete any biodata.
    * Product page - It showed the subscrib









  
 
    
    




TECHNOLOGIES
============
* Bootstrap, HTML and CSS
* HTML
* CSS
* Javascript
* Jquery
* Python
* Django
* PostgreSQL



TESTING
=======
* Testing was done across multiple viewports sizes to ensure responsiveness. HTMLHint were used to check the HTML code and CSSLint were also used to check the CSS code. JSHint was used to check the Javascript code.
* Manual testing was employed to check this project to check all the button and link is functioning properly.



DEPLOYMENT
==========
* This site is hosted using Heroku.