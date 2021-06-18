# Our Website

Hello! We are the group, and our website goal is to make an easily accessable way to both review games and look at overviews of games to find ones to your liking. 
We also want to include a login system to show user's reviews and details.
- https://docs.google.com/document/d/1EFlapSLtudKA0r42AZ46T57u7ksnPDTYismk6XoxVEc/edit?usp=sharing
- Runtime link: http://76.176.48.196:5671/
- Crossover group: p4-fishes

### Features:
- 5 star based rating system for games, along with a written summary for the rating
- REST API used for searching game titles for a wide database of games to review
- User accounts that display their reviews
- Easy way to filter games based on genre

### How It's Made:
- Login System
  - [Create user table in site database](https://github.com/notkobalt/group-project/blob/main/bulkofproject/models.py) Lines 8-16
  - Create HTML Pages for [Login](https://github.com/notkobalt/group-project/blob/main/bulkofproject/templates/account/login.html) and [Sign Up](https://github.com/notkobalt/group-project/blob/main/bulkofproject/templates/account/signup.html)
  - Login: [Use Database to check user input](https://github.com/notkobalt/group-project/blob/main/bulkofproject/account/__init__.py) Lines 15-49
  - Sign Up: [Commit User Input to Database](https://github.com/notkobalt/group-project/blob/main/bulkofproject/account/__init__.py) Lines 52-74
  - Session Data in Every Route
  - [Log Out by Removing Session Data](https://github.com/notkobalt/group-project/blob/main/bulkofproject/account/__init__.py) Lines 76-83

- Rating System
  - [Database for User Reviews](https://github.com/notkobalt/group-project/blob/main/bulkofproject/models.py) Lines 18-28
  - [Scrape API With Games List](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/__init__.py) Lines 45-51
  - [Search Funciton Creates Session Based on User Data](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/__init__.py) Lines 35-77
  - [Get Search Results From Session Data](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/__init__.py) Lines 79-104
  - [Displayed Search Results Route to Review Page, Game Selected is Used For Review](https://github.com/notkobalt/group-project/blob/main/bulkofproject/templates/reviews/result.html) Lines 9-18 [Back End](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/__init__.py) Lines 70-104
  - [Write Review](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/__init__.py) Lines 107-129
  - [Display Existing Reviews](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/__init__.py) Lines 30-33 [Database Query Code](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/query.py)
  - [Filter Database Based on User Input](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/__init__.py) Lines 12-29 [Filter Database Code](https://github.com/notkobalt/group-project/blob/main/bulkofproject/reviews/filter.py)

## Crossover
Our original parter group was the fishies, however they finished a week early and collaborated with another group in period 3. We were not informed, and due to the miscommunication we needed to collaborate with the "Web Errors" group because they also needed a parter. We display the fishies' API as per our original agreement, however the "Web Errors" group displays our API instead of the fishies. 

# Progress 6/8
### Blueprints
- Instead of creating a blueprint for every person in the group we will use blueprints to split the project into categories of code for organization
  - ex: Game review code is in the "reviews" blueprint
- Mini-labs will each be in their seperate blueprints
- Splitting our project into blueprints corresponding to each group memeber would be inefficient for our project, it stops any chance for teamwork when coding our project. We have multiple tickets where group members work together, having individual folders for each group member's code would lead to one group member not recieving credit for their work, or duplicate dead code.

### Login
- One database stores usernames and passwords for login system
- One databse stores user reviews, connected to login database through "user_id" column and ForeignKey function
- Rating database has "game" column to store which game the rating is attached to (makes displaying proper review on proper game pages easier)

### API
- Using the RAWG game API to retrieve and search game titles https://rawg.io/apidocs
- Search system is completed, corresponding games returned from search query
- Games are displayed with clickable icons of screenshots

### Routing
- One single route in a for loop creates a route for every game in the database
- Single html file made completely with jinja allows for a smaller file size and prevents the creation of thousands of html files to accomodate for the api
- Routing and API query code in a "Blueprint" in order to keep project organized

### Rating Systen
- WIP

# Update 6/1
- A search system has been created using the API, along with a random game reccomendation function
- Front page, navbar, login page have finished CSS
- Website is deployed and accessable
- Rating system and the link from search result to review page is in development
- Login system is complete, user pages are in development


