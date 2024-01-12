# Top Destinations

**This is a Django-based Travel Blog project where users can create posts about favourite destinations**

![Homepage](static/images/homepage.jpg)

***[Live website](https://dcigic92-pp4-top-destinations-a65b10a6448e.herokuapp.com/)*** created by **Dino Cigic**.

***

## Table of Contents

- [User experience](#user-experience)
    - [Project goals](#project-goals)
    - [User stories](#user-stories)
- [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
- [Features](#features)
    - [Existing features](#existing-features)
    - [Features left to implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Agile Development Process](#agile-development-process)
- [Setup](#setup)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Testing](#testing)
    - [Automated Testing](#automated-testing)
    - [Validation](#validation)
    - [Manual Testing](#manual-testing)
        - [Account Registration](#account-registration)
        - [Navigation](#navigation)
        - [Pagination](#pagination)
        - [CRUD](#crud)
- [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
- [Acknowledgements](#acknowledgements)

## User experience

### Project goals
- Project goal was to inspire and encourage travel by showcasing the beauty and uniqueness of different locations.

### User stories

- As a Site Admin I can create draft posts so that I can finish writing my posts later.
- As a Site admin I can remove comments and posts so that I can filter out bad behavior on my site.
- As a Site User / Admin I can create, read, update and delete posts so that I can manage my content.
- As a Site User I can use site navbar so that I can easily navigate different pages and find relevant informations.
- As a Site User I can view a paginated list of posts so that I can easily select which post I want to view.
- As a Site User I can click on a post so that I can view the full post.
- As a Site User I can search posts so that I can find a specific post.
- As a Site User I can register an account so that I can interact with the site content.
- As a Site user I can login to the site so that I can access my account.
- As a Site user I can logout from the site so that my account is kept secure.
- As a Site User I can choose post categories so that I can easier find relevant posts.
- As a Site User / Admin I can view comments on an individual post so that I can read the conversation.
- As a Site User I can leave comments on a post so that I can be involved in the conversation.
- As a Site User I can edit my comments so that I can fix typos.
- As a Site user I can delete my comments so that I don't have to be involved in the conversation anymore.


## Design

### Colours
Used only black and white color, and Bootstrap's dark class.

### Typography
In this project I used google's font ***Montserrat***.


## Features

### Existing features

- Paginated view of all posts on the homepage.
- Paginated view of posts from the chosen country.
- Paginated view of posts from the search result.
- Detailed view of each post.
- Reading comments.
- Account registration, login and logout.
- Option to comment on posts for registered users.
- Option to edit and delete comments for registered users.
- Option to add posts for registered users.
- Option to edit and delete posts for registered users.
- Improved admin panel.

### Features left to implement

- User profile (update and delete).
- Star rating and sorting posts by rating.

## Technologies Used
- Python
- Django
- PostgreSQL
- HTML
- CSS
- Javascript
- Bootstrap
- [Elephant SQL](https://www.elephantsql.com/)
- [Cloudinary](https://cloudinary.com/)
- [Heroku](https://heroku.com/)
- [Git](https://git-scm.com/)
- [Github](https://github.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Favicon](https://favicon.io/favicon-converter/)


## Agile Development Process

I followed Agile methodology for this project, fostering flexibility and regular progress updates. This approach allowed me to deliver increments efficiently. I used Github Kanban board for this project and created Kanban board with four columns: "To Do" "In Progress" "Done" and "Left to implement". Project contains 20 user stories. Link to project's user stories [here](https://github.com/users/dcigic92/projects/4).

## Setup

1. **Clone the repository:**

   ```bash
   git clone git@github.com:dcigic92/pp4-top-destinations.git
   ```

2. **Install dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Generate migrations:**

   ```bash
   python3 manage.py makemigrrations
   ```

4. **Apply migrations:**

   ```bash
   python3 manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python3 manage.py createsuperuser
   ```

   Follow the prompts to create an admin account.

6. **Run the development server:**

   ```bash
   python3 manage.py runserver
   ```

   The project should now be accessible at http://127.0.0.1:8000/.

## Deployment

### Heroku:

1. **Create Heroku App:**
   - Create a new Heroku app and link it to the Git repository for the project.

2. **Heroku Configurations:**
   - In Heroku's settings set up config vars such as the Database URL, Cloudinary URL and the Secret Key.

3. **Deployment:**
   - Deploy the project to Heroku by pushing the code to the Heroku remote repository, set Debug=False before final deployment.

## Testing

### Automated Testing

As part of my project I decided to implement some automated testing into my project. I tested forms, models and views using Python unittest modul. Tests can be found in /website/tests folder.

Coverage report showed 78%.

![Coverage](static/images/coverage_report.jpg)

### Validation

- CSS validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
- HTML validated with [W3C HTML5 Validator](https://validator.w3.org/).
- JavaScript was tested with [JSHint](https://jshint.com/).
- Python has been validated using the [PEP8 Python Checker](https://www.pythonchecker.com/).

### Manual Testing

#### Account Registration
| Test |Result |
|--|--|
| User can register account|Pass|
| User can log in|Pass|
| User can log out|Pass|
---

#### Navigation
| Test |Result |
|--|--|
|User can sort by countries|Pass|
|User can open add new post|Pass|
|User can use search bar|Pass|
|User can open post detail|Pass|
|User can open go back to homepage|Pass|
---

#### Pagination
| Test |Result |
|--|--|
|Pagination on homepage|Pass|
|Pagination on sorted by countries page|Pass|
|Pagination on search results page|Pass|
---

#### CRUD
| Test |Result |
|--|--|
|User can view posts|Pass|
|User can add new post|Pass|
|User can edit post|Pass|
|User can delete post|Pass|
|User can view comments|Pass|
|User can add new comment|Pass|
|User can edit comment|Pass|
|User can delete comment|Pass|
---


## Credits

### Content

- All content text taken from [Wikipedia](https://wikipedia.org/).

### Images 

- [Pexels](https://www.pexels.com/)
    - [Photo](https://www.pexels.com/photo/person-with-toy-airplane-on-world-map-3769138/) by Andrea Piacquadio - Default image
    - [Photo](https://www.pexels.com/photo/view-of-the-coast-in-split-croatia-18759978/) by Jan Tang - Split, Croatia
    - [Photo](https://www.pexels.com/photo/colosseum-rome-italy-2064827/) by Davi Pimentel - Rome, Italy
    - [Photo](https://www.pexels.com/photo/illuminated-eiffel-tower-at-night-19738542/) by Ali Burak - Paris, France

- [Unsplash](https://unsplash.com/)
    - [Photo](https://unsplash.com/photos/aerial-view-of-city-buildings-during-daytime-zTiYT7HHzAE) by Geio Tischler - Hvar, Croatia
    - [Photo](https://unsplash.com/photos/silhouette-of-trees-near-body-of-water-during-sunset-FjCKt9WGxcI) by Cauayan Island Resort - El Nido, Philippines
    - [Photo](https://unsplash.com/photos/green-and-brown-mountain-beside-body-of-water-during-sunset-AEallbg9q_A) by Federico Beccari - Cliffs of Moher, Ireland
    - [Photo](https://unsplash.com/photos/a-body-of-water-with-boats-and-buildings-along-it-ov5S-3erSlY) by Francesco Dondi - Galway, Ireland
    - [Photo](https://unsplash.com/photos/island-under-white-sky-exFdOWkYBQw) by Alfiano Sutianto - Nusa Penida, Indonesia

- [Flaticon](https://www.flaticon.com/)
    -[Photo](https://www.flaticon.com/free-icons/world) World icons created by Freepik - Flaticon


### Code
  
- Found out about context processors on [Stackoverflow](https://stackoverflow.com/).
- Some parts of the code were inspired by Django Blog Project from [Code institute](https://learn.codeinstitute.net/dashboard).


## Acknowledgements

- My mentor **Akshat Garg** for his feedback and advice.
- Our cohort facilitator **Alan Bushell** and slack community.
- My wife and friends for help with testing.