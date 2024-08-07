# Cafitio Corner

Welcome to Cafitio Corner. The place where you can buy coffee, coffee machines, and accessories to have a professional coffee experience at your home. Whether you're a casual coffee drinker or a connoisseur, this website caters to all types of coffee enthusiasts.

The purpose of the website is to offer high-quality coffee products and accessories. It provides a convenient platform for purchasing coffee-related items. Additionally, it aims to educate and inspire coffee enthusiasts to enhance their at-home coffee experience.

![responsive image with the website](assets/responsive_white.png)

[Live Website](https://cafitio-corner-5f01d0c35567.herokuapp.com/)

[GitHub Repository](https://github.com/terintealexandrin18/cafitiocorner)

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
    3. [Structure](#structure)
        1. [Database Model](#database-model)
    4. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    5. [Surface](#surface)
        1. [Color Scheme](#color-scheme)
        2. [Typography](#typography)
2. [Marketing](#marketing)
    1. [Search Engine Optimization (SEO)](#search-engine-optimization-seo)
    2. [Business Model](#business-model)
3. [Features](#features)
    1. [General](#general)
    2. [Header](#header)
    3. [Search Bar](#search-bar)
    4. [Footer](#footer)
    5. [Home Page](#home-page)
    6. [Products](#products)
        1. [Products Page](#products-page)
        2. [Product Informations Page](#product-informations-page)
    7. [Products Admin](#products-admin)
        1. [Add Product](#add-product)
        2. [Edit Product](#edit-product)
    8. [Shopping Cart Page](#shopping-cart-page)
    9. [Checkout Page](#checkout-page)
    10. [Checkout Success Page](#checkout-success-page)
    11. [Profile Page](#profile-page)
    12. [Wishlist Page](#wishlist-page)
    13. [Contact Us Page](#contact-us-page)
    14. [About Us Page](#about-us-page)
    15. [Accounts Pages](#accounts-pages)
    16. [404 Error Page](#404-error-page)
4. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#libraries-and-frameworks)
    3. [Packages / Dependencies Installed](#packages--dependencies-installed)
    4. [Database Management](#database-management)
    5. [Payment Service](#payment-service)
    6. [Cloud Storage](#cloud-storage)
    7. [Tools and Programs](#tools-and-programs)
5. [Testing](#testing)
6. [Deployment to Heroku](#deployment-to-heroku)
7. [Finished Product](#finished-product)
8. [Credits](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Code](#code)
    4. [Resources and References](#resources-and-references)
9. [Known Bugs](#known-bugs)
10. [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Strategy

#### Project Goals

- Provide a Seamless User Experience: Ensure the website is user-friendly, intuitive, and accessible on all devices.
- Showcase Products Effectively: Highlight coffee products, machines, and accessories with high-quality images, detailed descriptions, and user reviews.
- Streamline the Purchase Process: Simplify the shopping cart and checkout process to reduce cart abandonment and increase conversions.
- Engage and Retain Customers: Implement features like user accounts, wishlists, and newsletters to foster customer loyalty.
- Optimize for Search Engines: Use SEO best practices to increase visibility and attract more potential customers.

#### User Goals

- Epic 1 - User Account Management
  - Access and Edit User Profile
    - As a site user, I want to maintain my profile information to ensure it is current and accurate.

  - Account Management
    - As a site user, I want to set up an account to enable order placements and access additional features.
    - As a site user, I want to efficiently log in and out for seamless access to my profile.
    - As a site user, I want to review my order history to keep track of my previous purchases.
    - As a site user, I want to restore access to my account by resetting my password if needed.

- Epic 2 - Product Management
  - Product Management for Site Owner
    - As a site owner, I want to remove unavailable products to keep the store offerings relevant.
    - As a site owner, I want to update product details to ensure customers have accurate information.
    - As a site owner, I want to add new products to broaden the store's inventory.

  - Product Interaction for Site Users
    - As a site user, I want to browse through all products to find items that suit my needs.
    - As a site user, I want to view larger images and detailed descriptions to make informed purchasing decisions.
    - As a site user, I want to filter products by categories to easily find what I am looking for.
    - As a site user, I want to search for specific products quickly by name or description.

- Epic 3 - Shopping Experience
  - Order Confirmation
    - As a shopper, I want to receive an email confirmation to verify that my order was successfully placed.
    - As a shopper, I want to review my order details after checkout for accuracy and records.

  - Basket and Checkout
    - As a user, I want to add multiple items to my basket to facilitate a single transaction.
    - As a shopper, I want my personal details to be saved during checkout for faster future purchases.
    - As a shopper, I want my personal and payment information to be securely processed to protect my data.
    - As a shopper, I want to see the total cost of items in my basket at any time to manage my spending.
    - As a shopper, I want to adjust the quantity of items in my basket for accurate order fulfillment.
    - As a site user, I want to add multiple units of the same product to my basket to simplify bulk purchases.

- Epic 4 - Product Reviews and Ratings
  - Product Reviews and Ratings
    - As a shopper, I want to give ratings to products to share my experience with other shoppers.
    - As a site user, I want to manage my reviews by editing or deleting them to ensure they reflect my current opinions.
    - As a site user, I want to read reviews from others to help inform my buying decisions.
    - As a shopper, I want to sort reviews to quickly find the most relevant or recent feedback.

- Epic 5 - Newsletter Subscription
  - Newsletter Subscription
    - As a site owner, I want to provide a newsletter subscription to keep users informed about new products and offers.

- Epic 6 - Miscellaneous
  - Category and Search
    - As a shopper, I want to compare products across different categories to find the best options for my needs.

- Additional Features
  - The following feature was added after the initial user stories were completed:
    - As a site user, I want to add items to a wishlist to save them for future consideration.
    - As a site user, I want to view my wishlist to see the items I have saved.
    - As a site user, I want to remove items from my wishlist to manage my saved products effectively.

#### Strategy Table

| Opportunity / Problem / Feature                  | Importance | Viability / Feasibility |
|--------------------------------------------------|------------|-------------------------|
| Account signup                                   | 5          | 5                       |
| User profile                                     | 5          | 5                       |
| Responsive design                                | 5          | 5                       |
| Add products to the basket                       | 5          | 5                       |
| Make payment for selected products               | 5          | 5                       |
| Rate products                                    | 5          | 4                       |
| Add, edit, and delete reviews                    | 5          | 5                       |
| View product reviews                             | 5          | 5                       |
| Search for products                              | 5          | 5                       |
| View product details                             | 5          | 5                       |
| View order confirmation after checkout           | 5          | 5                       |
| Newsletter subscription                          | 5          | 5                       |
| Add products to wishlist                         | 5          | 5                       |
| View wishlist                                    | 5          | 3                       |
| Remove products from wishlist                    | 5          | 3                       |
| **Total**                                        | **75**     | **70**

### Scope

The project aims to develop an e-commerce website, Cafitio Corner, offering a wide range of coffee products, machines, and accessories to customers. The website will be responsive and user-friendly, providing users with the ability to:

- User Authentication:
  - Register and create a user account
  - Login and logout seamlessly
  - Reset passwords

- Product Browsing and Management:
  - Browse and search for products by name or description
  - View detailed product information including images, descriptions, prices, and stock levels
  - Sort products by different criteria such as price, ratings, and categories
  - Add products to a shopping cart and manage quantities
  - Add products to a wishlist for future reference

- User Profile Management:
  - Access and edit user profile information
  - View past orders and order history
  - Save personal details for a streamlined checkout experience

- Reviews and Ratings:
  - Leave, edit, and delete product reviews
  - Rate products to provide feedback based on user experience
  - View product reviews from other users to make informed purchasing decisions

- Checkout and Payments:
  - Securely pay for products using integrated payment systems
  - Receive order confirmation via email after successful checkout

- Wishlist Management:
  - Add products to a wishlist for future reference
  - View and manage wishlist items, including the ability to remove products from the wishlist

- Newsletter Subscription:
  - Subscribe to a newsletter to stay updated with the latest products, offers, and coffee-related content

- Admin Functionality:
  - Add, edit, and delete products to maintain up-to-date offerings
  - Manage product stock levels
  - Access and update order statuses
  - Sort orders by status (In Progress, Completed, Cancelled)

### Structure

- The header, footer, and navigation bar are consistent across all pages, ensuring a seamless user experience.
- Links and forms provide clear feedback to the user, enhancing usability and interaction.
- Additional content features become available to shoppers once they register an account, providing a more personalized experience.
- A 404-error page is in place to handle any incorrect or broken links, guiding users back to the main content.

#### Database Model

The database model has been designed using [dbdiagram.io](https://dbdiagram.io). A relational database is used for the project, managed with SQLite3 during development and deployed using [PostgreSQL](https://www.postgresql.org/) in the production environment.

![Entity Relationship Diagram](assets/readme/entity-relationship-diagram.png)

### Skeleton

The wireframes for the project were created using [Balsamiq](https://balsamiq.com). These wireframes helped in planning the layout and user interface of the website effectively.

#### Wireframes

| Page              | Desktop Version                                                   | Mobile Version                                                   |
|-------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
| **Home**          | ![Home Desktop](assets/wireframes/home_desktop.png)               | ![Home Mobile](assets/wireframes/home_mobile.png)                |
| **Products**      | ![Products Desktop](assets/wireframes/products_desktop.png)       | ![Products Mobile](assets/wireframes/products_mobile.png)        |
| **Product Details** | ![Product Details Desktop](assets/wireframes/products_informations_desktop.png) | ![Product Details Mobile](assets/wireframes/products_informations_mobile.png) |
| **Bag**           | ![Bag Desktop](assets/wireframes/bag_desktop.png)                 | ![Bag Mobile](assets/wireframes/bag_mobile.png)                  |
| **Checkout**      | ![Checkout Desktop](assets/wireframes/checkout_desktop.png)       | ![Checkout Mobile](assets/wireframes/checkout_mobile.png)        |
| **Checkout Success** | ![Checkout Success Desktop](assets/wireframes/checkout_success_desktop.png) | ![Checkout Success Mobile](assets/wireframes/checkout_success_mobile.png) |
| **Contact**       | ![Contact Desktop](assets/wireframes/contact_desktop.png)         | ![Contact Mobile](assets/wireframes/contact_mobile.png)          |
| **About**         | ![About Desktop](assets/wireframes/about_desktop.png)             | ![About Mobile](assets/wireframes/about_mobile.png)              |

### Surface

#### Color Scheme

![Color Scheme](assets/readme/colorscheme.png)

- The colors used in the website have been carefully selected to create a warm, inviting, and sophisticated aesthetic, enhancing the user experience and making the shopping process enjoyable.

- We use Cream (#D1CBB8) for the main background. This light, neutral color provides a clean and welcoming canvas, ensuring readability and reducing eye strain for users browsing the site.

- Green (#809671) is used for primary buttons, links, and call-to-action sections. Green evokes feelings of tranquility and nature, which aligns with the organic and comforting atmosphere we aim to create. It effectively draws attention to important interactive elements without overwhelming the user.

- Brown (#725C3A) serves as a secondary accent color for elements such as secondary buttons, headers, and borders. This earthy tone complements the cream background and green accents, adding warmth and a sense of reliability to the design.

- Muted Red (#AB706D) is utilized for alerts, notifications, and error messages. This color highlights urgent information that requires user attention, providing a subtle yet effective way to convey critical messages without causing alarm.

- Beige (#D2AB80) is used to highlight specific content areas such as product cards, testimonials, and feature sections. This soft neutral color offers a gentle contrast to the cream background, making these sections stand out without disrupting the overall harmony of the design.

By incorporating these colors, the website achieves a harmonious balance that guides the user's attention intuitively while maintaining a cohesive and aesthetically pleasing appearance throughout.

#### Typography

The typography for this project has been carefully selected to enhance readability and create a visually appealing hierarchy. Google Fonts are used specifically for titles, providing a unique and stylish appearance, while the body text uses default system fonts for simplicity and faster loading times.

Titles
- The Google Font 'Roboto' is used for all titles (h1, h2, h3, h4, h5, h6). This ensures that headings stand out and contribute to a cohesive visual identity.

Body Text
- Default system fonts like Arial and Helvetica are used for the body text. These fonts are reliable and widely supported, ensuring good readability and performance.

By combining 'Roboto' for titles with standard fonts for body text, the website maintains a clean and professional look while ensuring optimal performance and readability.

## Marketing

### Search Engine Optimization (SEO)

To improve the search index rating on Google, extensive research was conducted using various tools such as Google Keyword Planner and SEMrush. These tools helped identify relevant keywords to use in meta tags, content, and other strategic areas of the website.

The implemented meta tags include a description and keywords that focus on capturing the primary search queries related to our business:

- Description: "Cafitio Corner - Top coffee products, accessories, and more. Free delivery on orders over £40. Sign in for exclusive deals."
- Keywords: "Cafitio Corner, coffee shop, coffee accessories, online coffee store, free delivery, coffee products, coffee deals, coffee beans, coffee machines"

These keywords are strategically chosen to align with the products and services offered by Cafitio Corner, ensuring that potential customers can easily find the website through search engines.

Continuous Monitoring and Improvement

- SEO is an ongoing process. To ensure the effectiveness of the selected keywords, they are regularly monitored using tools like Google Analytics. This allows us to:
    - Track the performance of each keyword.
    - Determine which terms are driving traffic to the site.
    - Refine and adjust the keywords based on performance data.

- Additional SEO Strategies

    - Sitemap: A sitemap was generated using [xml-sitemaps](https://www.xml-sitemaps.com/) and is included in the root level of the project. This helps search engines crawl and index the website more efficiently.
    - Robots.txt: A `robots.txt` file was created at the root level of the project. This file instructs search engine crawlers on which URLs they can access on the website, improving crawl efficiency and ensuring important pages are indexed.

By implementing these SEO strategies, Cafitio Corner aims to increase its online visibility, attract more visitors, and provide an enhanced user experience.

### Business Model

#### Company Description

- Cafitio Corner Overview:
  - Cafitio Corner operates a B2C (Business-to-Consumer) ecommerce model, providing an innovative online platform specializing in the retail of premium coffee products, accessories, and a diverse range of coffee machines. Our mission is to curate a comprehensive selection of high-quality coffee items, offering enthusiasts and beginners alike a one-stop-shop for all their coffee-related needs.

- Values:
  - Commitment to Quality:
    - Cafitio Corner prioritizes offering products of superior quality to ensure customer satisfaction and loyalty.
  - Customer-Centric Approach:
    - Our main focus is on delivering exceptional customer service, creating a seamless shopping experience.
  - Diversity and Inclusivity:
    - We celebrate the diversity of coffee culture, catering to a wide audience with varied preferences.
  - Innovation:
    - We embrace the latest trends and technologies to stay at the forefront of the coffee industry.

#### Customers

##### Target Audience:

- Coffee Enthusiasts:
  - Experienced coffee drinkers seeking premium products and unique flavors.

- Beginners:
  - Individuals entering the world of coffee, requiring guidance and starter kits.

- Home Baristas:
  - Coffee lovers looking to create professional-quality coffee at home with specialized equipment and accessories.

#### Customer Needs:

- Quality Products:
  - Customers seek top-notch coffee beans, genuine accessories, and a diverse range of high-quality coffee machines.

- Convenience:
  - A user-friendly platform with easy navigation and secure transactions.

- Expert Advice:
  - Access to informative content and customer support for guidance on product selection and usage.

#### Competitors

##### Primary Competitors:

Cafitio Corner competes with established online coffee retailers, such as:
- Blue Bottle Coffee
- Stumptown Coffee Roasters
- Intelligentsia Coffee
- Peet’s Coffee

### SWOT Analysis

##### Strengths

- Diverse Product Range:
  - Cafitio Corner offers a comprehensive selection of premium coffee products, accessories, and machines, providing customers with a wide array of choices in one place.

- Community Engagement:
  - Fostering an online community where coffee enthusiasts can connect, share experiences, and contribute to a vibrant and engaged user base.

##### Weaknesses

- New Brand:
  - As a new entrant, Cafitio Corner may face challenges in establishing brand recognition and trust in the competitive market.

- Limited Marketing Budget:
  - Initial budget constraints may limit the reach and awareness of Cafitio Corner compared to more established competitors.

##### Opportunities

- Market Niche:
  - Cafitio Corner has the opportunity to fill a niche in the market by providing a diverse and curated selection of coffee-related products on one platform, a unique offering not widely available.

- Collaborations:
  - Potential collaborations with prominent coffee brands, influencers, and organizations can enhance brand visibility and credibility.

##### Threats

- Supply Chain Disruptions:
  - Challenges in shipping and supply chain disruptions, particularly for products produced in other countries, may impact inventory and lead to delays.

- Variable Shipping Costs:
  - Fluctuations in shipping costs can impact the overall pricing structure and potentially affect customer satisfaction.

- Competitive Landscape:
  - Larger companies with the ability to change product supply and smaller eco-friendly competitors expanding their product range may pose threats to market share.

- Public Relations and Market Share:
  - Other similar companies gaining more PR and a larger market share may pose a threat to Cafitio Corner's growth.

#### Marketing Strategy

Given our resource constraints, we are strategically focusing on cost-effective yet impactful marketing initiatives to establish and grow Cafitio Corner. Our marketing strategy is designed to create brand awareness, foster customer loyalty, and attract a wider audience:

##### Engaging Social Media Presence

- Facebook Community Building:
  - Actively manage our Facebook page, engaging with our audience through regular posts, updates, and responding promptly to customer inquiries. This platform serves as a hub for coffee enthusiasts to share experiences and connect.

##### Newsletter Loyalty Program

- Customer Loyalty through Newsletters:
  - Encourage visitors to sign up for our newsletter by offering exclusive discounts, early access to new products, and valuable coffee-related content. This not only builds customer loyalty but also provides a direct communication channel.

##### Word of Mouth Marketing

- Customer Referral Program:
  - Implement a customer referral program, incentivizing existing customers to refer friends and family to Cafitio Corner. This taps into the power of word of mouth, expanding our customer base organically.

#### Facebook Business page

![Facebook Page](assets/readme/facebook_cafitio_corner.png)

The Business Facebook [LIVE](https://www.facebook.com/p/Cafitio-Corner-61563015151538/)

## Features

### General

- The website has been designed from a mobile-first perspective.
- Responsive design across all device sizes.
- Validation messages for various actions such as adding a product to the bag, logging in/logging out, updating the bag quantity, removing an item from the bag, adding a new item and many more. These messages can be closed manually or will disappear after 5 seconds.

### Header

- The header contains the main logo, navigation links, and search product functionality.
- The main logo works as a link to the home page.
- The navigation links allow the shopper access to all sections to facilitate navigation across the website.
- The shopping bag icon changes the color reflecting the current status. If no items are in the cart the icon color is black; if items are in the cart the icon color changes to green. Also, the current shopping amount is displayed for the shopper.

![Header](assets/readme/nav_bar.png)

### Search Bar

- The search bar allows the user to search the website for products using specific keywords.

![Search Bar](assets/readme/search_bar.png)

### Footer

- The footer contains contact details and business social media links, including Facebook Business page, Instagram, and LinkedIn. It also includes links to the owner's GitHub page and the Privacy Policy.
- A newsletter registration form has been located in the footer allowing the shopper to subscribe across the whole website.

![Footer](assets/readme/footer.png)

### Home Page

- Display the discount for free delivery on all orders. The text bar moves left to right and right to left to ensure users are aware of the offer.
- Button that redirects to the "All Products" page, helping users easily navigate to the product pages. The background image visually represents the website's offerings.

![Home Page](assets/readme/home_page.png)

### Products

#### Products Page

- Display all the products currently available or filtered on a specific category.
- Display an image of the products as well as their main information such as name, price, rating, and whether they are added to the wishlist or not.
- Users can see only 8 items per page and can navigate to the first page, last page, next, and previous pages.
- The user can add items to the wishlist and remove items from the wishlist without having to click on the product details.
- Provides sorting functionality to sort products by price, rating, name, or category.
- A back-to-the-top button is available so the shopper can easily return to the top of the page.
- As a superuser, the admin can see the edit and delete buttons, allowing quick access to the product admin.

![Products Page](assets/readme/products_page.png)

#### Product Informations Page

- The product navigation bar is present in case the shopper wants to go back to the products.
- Provide a larger image of the product and display its detailed information.
- A heart icon is available to easily add/remove the product to the shopper's wishlist.
- Allow the user to select the quantity of products to be added to the shopping bag.
- An "Add to Bag" button is available to add the desired quantity of the product to the shopping bag.
- Logged-in users can leave a rating and review for products, providing valuable feedback to other shoppers and the site owner.
- Any shopper can view customer reviews, with the total number of reviews displayed. The reviews section can be toggled to show or hide customer feedback, helping shoppers make informed decisions.
- All reviews the product has received are displayed in the reviews section at the bottom of the page.
- Only the user who left the review can update or delete their reviews and ratings.
- Edit and delete buttons are displayed only for admins to update or delete the product.

![Product Informations Page](assets/readme/products_informations_page.png)
![Product Informations Page](assets/readme/products_informations_page_with_review.png)

### Products Admin

#### Add Product

- Provide a form for the site admin to add new products to the store.

![Add Product](assets/readme/admin_add_product.png)

#### Edit Product

- Provide a prefilled form for the site admin to update products in the store.

![Edit Product](assets/readme/admin_edit_product.png)

### Shopping Cart Page

- A message alerts the user if the free delivery threshold has not been reached, displaying the amount left.
- Display all products currently in the shopping cart and their information.
- Allow the user to update the product quantity or remove the product from the shopping cart.
- Display the current total cost including the cart total and delivery costs.
- Provide a "Keep Shopping" link to go back to the products.
- A button to checkout is provided for the shopper to complete the purchase.

![Shopping Cart Page](assets/readme/shoping_cart.png)

### Checkout Page

- Provide a checkout form for the shopper to complete the purchase and provide the necessary contact, shipping, and payment information.
- Display an order summary listing all the products to be purchased and their total cost including the bag total and delivery costs.
- Provide a button back to the shopping bag if the shopper would like to adjust the products in the shopping cart.
- A message informs the shopper of the amount to be charged on the provided card.
- Descriptive error messages are displayed if there is any issue with the payment information provided.
- A button is clearly available for the shopper to complete the order.
- Stripe webhook handler is created in the backend to pass the order information if the browser crashes after checkout completion.

![Checkout Page](assets/readme/checkout_page.png)

### Checkout Success Page

- Display the order details and shopper information to allow the shopper to confirm that the information provided is correct.
- Additionally, inform the shopper that an email has been sent to the email address provided with the same information.
- A button to continue shopping is provided at the bottom of the page.

![Checkout Success Page](assets/readme/checkout_success_page.png)

### Profile Page

- Provide a form for the registered shopper to update their default information.
- An order history section is present with all registered shopper's past orders information.

![Profile Page](assets/readme/profile_page.png)

### Wishlist Page

- Display the registered shopper's wishlist products and provide a picture, name, and price for each product.
- A remove button is present for the registered shopper to remove products they no longer want to keep on the list.

![Wishlist Page](assets/readme/wishlist_page.png)

### Contact Us Page

- Provide a form where the user can get in touch with the business regarding different topics.

![Contact Us Page](assets/readme/contact_page.png)

### About Us Page

- Provides an overview of Cafitio Corner's mission, story, values, and ways to connect with us.
- Includes an engaging image representing our coffee-centric focus.

![About Us Page](assets/readme/about_page.png)

### Accounts Pages

| Page            | Purpose                                                                                 | Image                                      |
|-----------------|-----------------------------------------------------------------------------------------|--------------------------------------------|
| Sign Up         | Allow the shopper to sign up for an account on the website.                             | ![Sign Up](assets/readme/sign_up.png)      |
| Sign In         | Allow the registered shopper to sign in with their account.                             | ![Sign In](assets/readme/sign_in.png)      |
| Sign Out        | Allow the registered shopper to sign out from their account.                            | ![Sign Out](assets/readme/sign_out.png)    |
| Reset Password  | Allow the registered shopper to reset their password.                                   | ![Reset Password](assets/readme/password_reset.png) |

### 404 Error Page

- Provide information to the shopper if the address entered cannot be found.
- A link to return to the products page is present.

![404 Error Page](assets/readme/404_page.png)

## Technologies Used

### Languages Used

- HTML5
- CSS3
- JavaScript
- Python

### Libraries and Frameworks

- Django: Utilized as the primary web framework.
- Django Template: Employed as a templating language to render backend data into HTML.
- Bootstrap 4: Implemented for styling and ensuring responsiveness across the website.
- Google Fonts: Integrated to import fonts used across the entire site.
- Font Awesome: Applied to enhance aesthetics and user experience with icons.
- jQuery 3.6.0: Utilized as a JavaScript library to simplify code writing.

### Packages / Dependencies Installed

- Django Allauth: Facilitated user authentication, registration, and account management.
- Django Crispy Forms: Managed the rendering of forms.
- Django Countries: Provided country choices for forms and country fields for models.
- Pillow: Enabled image processing capabilities.
- Gunicorn: Served as the WSGI HTTP Server for UNIX to support the Django application deployment.
- Django Summernote: Integrated as a text editor to manage content easily within the Django admin.
- psycopg2: Used as the PostgreSQL adapter for Python.
- dj-database-url: Allowed the configuration of the database via a URL.
- django-heroku: Simplified the configuration of the Django application for Heroku deployment.
- django-storages: Managed storage of static and media files on AWS S3.
- boto3: Allowed interaction with AWS services.
- whitenoise: Simplified the serving of static files.

### Database Management

- SQLite: Used as the single-file database during development.
- Heroku Postgres: Database was used in production, as a service based on PostgreSQL provided by Heroku.

### Payment Service

- Stripe: Managed all online payment transactions.

### Cloud Storage

- Amazon Web Services (AWS) S3: Used to store all static and media files in the production environment.

### Tools and Programs

- [Git](https://git-scm.com/): Employed for version control, using the Gitpod terminal to commit and push code to GitHub.
- [GitPod](https://www.gitpod.io/): Used for code writing, committing, and pushing to GitHub.
- [GitHub](https://github.com/): Hosted the project's code repository.
- [Heroku](https://www.heroku.com/): Deployed the website.
- [Coolors](http://colormind.io/): Utilized to create the website's color scheme.
- [Balsamiq](https://balsamiq.com/): Used for creating wireframes during the design phase.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): Employed during development for code review and responsiveness testing.
- [W3C Markup Validator](https://validator.w3.org/): Validated HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): Validated CSS code.
- [JSHint](https://jshint.com/): Used to validate the site's JavaScript code quality.
- [Font Awesome](https://fontawesome.com/): Applied to enhance aesthetics and user experience with icons.
- [PEP8 CI](https://pep8ci.herokuapp.com/): Used to validate the site's Python code quality.

### Testing

The testing documentation can be found [here](TESTING.md)

## Deployment to Heroku

This project is deployed on Heroku for production, with all static and media files stored on AWS S3. Here are the steps to deploy on Heroku:

1. **Create Heroku App**
   - Navigate to [Heroku](https://heroku.com), create a new account or log in.
   - On the dashboard page, click the "Create New App" button.
   - Give the app a unique name (with hyphens between words) and select the region closest to you.
   - Click "Create App".

2. **Provision Heroku Postgres Database**
   - On the Resources tab, add a new Heroku Postgres database.

3. **Configure Environment Variables**
   - Navigate to the Settings tab and click "Reveal Config Vars".
   - Add the following variables:

     | Variable               | Key                                     |
     |------------------------|-----------------------------------------|
     | AWS_ACCESS_KEY_ID      | your_access_key_id_from_AWS             |
     | AWS_SECRET_ACCESS_KEY  | your_secret_access_key_from_AWS         |
     | DATABASE_URL           | your_database_url                       |
     | EMAIL_HOST_PASS        | your_app_password_from_your_email       |
     | EMAIL_HOST_USER        | your_email_address                      |
     | SECRET_KEY             | your_secret_key                         |
     | STRIPE_PUBLIC_KEY      | your_stripe_public_key                  |
     | STRIPE_SECRET_KEY      | your_stripe_secret_key                  |
     | USE_AWS                | True                                    |

4. **Install Required Packages**
   - If not already installed, install `dj_database_url` and `psycopg2`:

     ```bash
     pip3 install dj_database_url psycopg2-binary
     ```

5. **Database Configuration**
   - In `settings.py`, import `dj_database_url`.
   - Replace the default database configuration with:

     ```python
     DATABASES = {
       'default': dj_database_url.parse('YOUR_DATABASE_URL_FROM_HEROKU')
     }
     ```

6. **Run Migrations**
   ```bash
   python3 manage.py migrate
   ```

7. **Import Data to Database**
   - Backup the current database and load it into a JSON file:

     ```bash
     ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
     ```

   - Connect to the Postgres database and load the data:

     ```bash
     ./manage.py loaddata db.json
     ```

8. **Create Superuser**

   - Create a superuser for your Django application by running the following command in your terminal:

     ```bash
     python3 manage.py createsuperuser
     ```

   - Follow the prompts to enter the username, email address, and password for the superuser account.

9. **Update Database Configuration**

   - Add conditional statements in `settings.py` to switch between Postgres and SQLite:

     ```python
     import dj_database_url
     import os

     if 'DATABASE_URL' in os.environ:
         DATABASES = {
             'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
         }
     else:
         DATABASES = {
             'default': {
                 'ENGINE': 'django.db.backends.sqlite3',
                 'NAME': BASE_DIR / 'db.sqlite3',
             }
         }
     ```
10. **Install Gunicorn**

    - Install Gunicorn, which will act as the web server for your Django application:

      ```bash
      pip3 install gunicorn
      ```

    - Freeze the installed packages into `requirements.txt`:

      ```bash
      pip3 freeze > requirements.txt
      ```

11. **Create Procfile**
    - In the project's root directory, create a `Procfile` to tell Heroku to create a web dyno that will run Gunicorn and serve the Django app:

      ```text
      web: gunicorn your_project_name.wsgi:application
      ```

12. **Deploy to Heroku**
    - Login to Heroku CLI:

      ```bash
      heroku login
      ```

    - Disable collectstatic temporarily so that Heroku won't try to collect static files when it deploys:

      ```bash
      heroku config:set DISABLE_COLLECTSTATIC=1 --app your_app_name
      ```

    - Add your Heroku app to `ALLOWED_HOSTS` in `settings.py`:

      ```python
      ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost']
      ```

    - Add, commit, and push to GitHub, then to Heroku:

      ```bash
      git add .
      git commit -m "Prepare for Heroku deployment"
      git push origin main
      heroku git:remote -a your_app_name
      git push heroku main
      ```

    - Connect the Heroku app to GitHub and enable automatic deploys:

      - Go to the app's dashboard on Heroku.
      - Navigate to the Deploy tab.
      - Connect the app to GitHub by clicking "GitHub" and search for the repository.
      - Click "Connect".
      - Enable automatic deploys by clicking "Enable Automatic Deploys".

13. **Update Settings for Secret Key and Debug**

    - In `settings.py`, replace the secret key setting with a call to get it from the environment and use an empty string as a default:

      ```python
      SECRET_KEY = os.environ.get('SECRET_KEY', '')
      ```

    - Set debug to be true only if there's a variable called development in the environment:

      ```python
      DEBUG = 'DEVELOPMENT' in os.environ
      ```

### AWS Bucket Creation

All static and media files are stored in an AWS S3 bucket. Follow these steps to create your own bucket:

1. **Create AWS Account**
   - Go to [Amazon Web Services](https://aws.amazon.com) and create an account or log in.

2. **Create S3 Bucket**
   - Go to the S3 service and click "Create Bucket".
   - Name the bucket (e.g., your Heroku app name) and select the closest region.
   - Enable ACLs (Access Control Lists) and choose "Bucket Owner Preferred".
   - Uncheck "Block All Public Access" and acknowledge the warning.
   - Enable Static Website Hosting in the Properties tab.
   - Set the Index and Error documents to `index.html` and `error.html`.

3. **Configure Bucket Policies**
   - Add the following CORS (Cross-Origin Resource Sharing) configuration in the Permissions tab:

     ```json
     [
         {
             "AllowedHeaders": ["Authorization"],
             "AllowedMethods": ["GET"],
             "AllowedOrigins": ["*"],
             "ExposeHeaders": []
         }
     ]
     ```

   - Set up a Bucket Policy to allow public read access:

     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Principal": "*",
                 "Action": "s3:GetObject",
                 "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
             }
         ]
     }
     ```

4. **Create IAM User and Group**
   - Create a user group with appropriate policies.
   - Create a user with programmatic access, attach it to the group, and save the access keys.

5. **Connect Django to AWS**
   - Install `boto3` and `django-storages`:

     ```bash
     pip3 install boto3 django-storages
     pip3 freeze > requirements.txt
     ```

   - Add `storages` to `INSTALLED_APPS` in `settings.py`.
   - Configure AWS settings in `settings.py`:

     ```python
     if 'USE_AWS' in os.environ:
         AWS_S3_OBJECT_PARAMETERS = {
             'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
             'CacheControl': 'max-age=94608000',
         }

         AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
         AWS_S3_REGION_NAME = 'YOUR_REGION'
         AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
         AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
         AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

         STATICFILES_STORAGE = 'custom_storages.StaticStorage'
         STATICFILES_LOCATION = 'static'
         DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
         MEDIAFILES_LOCATION = 'media'

         STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
         MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
     ```

   - Set the following Config Vars on Heroku:

     | Variable              | Value                           |
     |-----------------------|---------------------------------|
     | AWS_ACCESS_KEY_ID     | your_access_key_id              |
     | AWS_SECRET_ACCESS_KEY | your_secret_access_key          |
     | USE_AWS               | True                            |

   - Create `custom_storages.py` in the project root:

     ```python
     from django.conf import settings
     from storages.backends.s3boto3 import S3Boto3Storage

     class StaticStorage(S3Boto3Storage):
         location = settings.STATICFILES_LOCATION

     class MediaStorage(S3Boto3Storage):
         location = settings.MEDIAFILES_LOCATION
     ```

   - Push changes to GitHub:

     ```bash
     git add .
     git commit -m "Connect to AWS S3"
     git push
     ```

That's it! Your project should now be successfully deployed to Heroku with static and media files stored on AWS S3.


## Finished Product

| Page               | Desktop                                                  | Mobile                                                   |
|--------------------|----------------------------------------------------------|----------------------------------------------------------|
| Home               | ![home_page_d](assets/readme/home_page_d.png)            | ![home_page_m](assets/readme/home_page_m.png)            |
| Products           | ![product_page_d](assets/readme/product_page_d.png)      | ![product_page_m1](assets/readme/product_page_m1.png) <br> ![product_page_m2](assets/readme/product_page_m2.png) |
| Product Details    | ![product_informations_d](assets/readme/product_informations_d.png) | ![product_informations_m](assets/readme/product_informations_m.png) |
| Add Product        | ![add_product_d](assets/readme/add_product_d.png)        | ![add_product_m](assets/readme/add_product_m.png)        |
| Edit Product       | ![edit_product_d](assets/readme/edit_product_d.png)      | ![edit_product_m](assets/readme/edit_product_m.png)      |
| Shopping Bag       | ![shopping_bag_d](assets/readme/shoping_bag_d.png)       | ![shopping_bag_m](assets/readme/shoping_bag_m.png)       |
| Checkout           | ![checkout_d](assets/readme/checkout_d.png)              | ![checkout_m](assets/readme/checkout_m.png)              |
| Checkout Success   | ![checkout_success_d](assets/readme/checkout_success_d.png) | ![checkout_success_m](assets/readme/checkout_success_m.png) |
| Profile            | ![profile_d](assets/readme/profile_d.png)                | ![profile_m](assets/readme/profile_m.png)                |
| Wishlist           | ![wishlist_d](assets/readme/wishlist_d.png)              | ![wishlist_m](assets/readme/wishlist_m.png)              |
| Contact Us         | ![contact_d](assets/readme/contact_d.png)                | ![contact_m](assets/readme/contact_m.png)                |
| About Us           | ![about_d](assets/readme/about_d.png)                    | ![about_m](assets/readme/about_m.png)                    |
| Sign Up            | ![sign_up_d](assets/readme/sign_up_d.png)                | ![sign_up_m](assets/readme/sign_up_m.png)                |
| Sign In            | ![sign_in_d](assets/readme/sign_in_d.png)                | ![sign_in_m](assets/readme/sign_in_m.png)                |
| Sign Out           | ![sign_out_d](assets/readme/sign_out_d.png)              | ![sign_out_m](assets/readme/sign_out_m.png)              |
| Password Reset     | ![password_reset_d](assets/readme/password_reset_d.png)  | ![password_reset_m](assets/readme/password_reset_m.png)  |
| 404 Page           | ![404_d](assets/readme/404_d.png)                        | ![404_m](assets/readme/404_m.png)                        |

## Credits

### Content
- Product examples were taken from the following website: [Amazon](https://www.amazon.com)
- Content for the individual products was taken from the following page: [Amazon](https://www.amazon.com)
- All other content was written by the developer.

### Media
- Home page image and About Us page image were taken from [Pixabay](https://www.pixabay.com)
- Product images were taken from [Amazon](https://www.amazon.com)

## Code

The code in Code Institute's video on the Boutique Ado project was used as the main reference point to set up an e-commerce/online store project using HTML, CSS, JS, Python+Django, PostgreSQL database, Stripe, and AWS S3 as storage.

### Resources and References

- Stack Overflow - Used to search for solutions to various issues encountered during development.
- Slack - Utilized for seeking help and discussing issues with peers and mentors.
- Crispy Forms Documentation - Used for implementing and styling Django forms.
- Django Documentation - Followed step-by-step to ensure proper setup and implementation of Django features.
- Code Institute Template - This repository was created using the template provided by Code Institute.
- W3Schools - Consulted regularly for inspiration and to better understand the implementation of various code snippets.

## Known Bugs

There are 2 issues in the project that have been identified and need to be resolved. However, they remain unsolved due to a lack of my current skills and time. Both issues do not impact the functionality of the website:

1. Gitpod Configuration Warnings
   - Warning: `ms-toolsai.vscode-jupyter-cell-tags extension is not synced, but not added in .gitpod.yml`
   - Warning: `ms-toolsai.vscode-jupyter-slideshow extension is not synced, but not added in .gitpod.yml`
   - ![terminal error](assets/readme/terminal.png) 

   These warnings indicate that certain VS Code extensions are not synced and not added to the `.gitpod.yml` configuration file. This does not affect the core functionality of the website but needs to be addressed to ensure a clean development environment setup.

2. Console Errors
   - Error: There is an unspecified error appearing in the browser console that needs to be addressed. The exact details of the error are not currently available, but it does not impact the overall functionality of the website.
   - Error: A 404 error appears when navigating to certain pages. This needs further investigation to determine the cause and to implement a solution. This does not significantly impact the website's functionality but is noted for future resolution.
   - ![console error](assets/readme/console.png)

   Despite these issues, the website functions correctly, and these warnings and errors can be addressed as needed in the future.

## Acknowledgements

I would like to thank my mentor, Marcel, the Slack community, and everyone at the Code Institute for their help and support.

I also want to extend my gratitude to my wife for her unwavering support throughout this journey.





