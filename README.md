# Jane - Backend Coding Challenge


Your job is to build a small cannabis marketplace that allows users to find products based on a search term. The scope is limited so you can focus on building an app that could be deployed tomorrow in a real production environment. The instructions below capture all the product requirements. Everything that isn’t explicitly specified is up to you to decide; use your best judgement.

If you have any questions, feel free to contact your sponsor at Jane. Good luck and have fun!
____________________________________________________________________________

The app is split into two separate pages: 'Data Collection' and 'Products'.

The flow is as follows:

### Data Collection Page

1.    The user enters her/his name (first and last), email address, phone number, home address, and search term.

2.    Email and phone are checked for validity. If invalid, display a suitable error message and don't proceed until fixed.

3.    Next, the user enters her/his home address. Home addresses should be auto-completed using the Google Maps API. If that address cannot be located, display a suitable error message and don't proceed until fixed.

4.    Finally, the user enters a search term.

5.    Once all fields have been completed and are valid, display a 'Next' button somewhere on the page. This button should navigate the user to a 'products' page displaying all of the products relevant to the user's search term.

6.    The search term will search against the following fields in the provided `products.json` file:
  - `name`
  - `brand`
  - `category`
  - `kind`
  - `kind_subtype`
  - `description`


### Products Page

7.    Display the products in a grid of 'product cards'.

8.    Each product card should include the following information.

  - `name`
  - `brand`
  - `category`
  - `kind_subtype` (if not available, display `kind`)
  - `photo`

9.    In certain cases, some of the fields aren't available. In those cases, simply ignore the missing fields. However, if the product **_photo_** is missing, please use this default image: https://s3-us-west-1.amazonaws.com/iheartjane/images/stock_photos/general/indica.png

10.    Each card should display an 'Add to cart' button. No need to implement any functionality for this button.

11.    Somewhere on the page, display the user's address.

12.    Somewhere on the page, display a search field and a button to allow the user to perform additional searches.

 
### Summarizing the features for each page:

1.    Data Collection Page
  - Form with the following fields:                                    
    - Name                                         
    - Email address                                       
    - Phone number                                       
    - Address                                         
    - Search term
  - Next button                                         
    - only clickable when above fields are valid                                           
    - should take the user to the products page

2.    Products Page
  - Grid of product cards, each with the following information:
    - `name`                                          
    - `brand`                                          
    - `category`                                       
    - `kind_subtype`                                    
    - `photo` (use default photo when one is not available)                                        
    - 'Add to Cart' button (non-functional)
  - Search field with a button to allow the user to perform additional searches
  - User's address

 
### Notes and instructions

1.    We use React and Typescript, and we'd love to see you use them too.

2.    The products to search and display are contained in the provided `products.json` file.

3.    We appreciate beautiful and readable code.

4.    Your design should be mobile friendly (i.e. responsive).

5.    Bonus points if you deploy the project to a live environment.

6.    When you're done, submit all code and files to github and send us the link (and if deployed live, the URL).
