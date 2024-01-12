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
- [CI Python Linter](https://pep8ci.herokuapp.com/)

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


## Credits

### Text

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
    - [Photo](https://unsplash.com/photos/brown-and-white-concrete-houses-tnzzr8HpLhs) by Diogo Palhais - Galway, Ireland

### Code

- Found out about context processors on [Stackoverflow](https://stackoverflow.com/).
- Some parts of the code were inspired by Django Blog Project from [Code institute](https://learn.codeinstitute.net/dashboard).

## Acknowledgements

- My mentor **Akshat Garg** for his feedback and advice.
- Our cohort facilitator **Alan Bushell** and slack community.
- My wife and friends for help with testing.