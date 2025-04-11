Level 2 Capstone: Band/Music Website
This project is a Django-based full-stack application designed for a fictional band/music website. It includes features such as user authentication, event listing, and more. The app is a great example of a full Django application, utilizing database models, templates, and views to provide dynamic content.

Features
User Authentication: Login and registration functionality.

Home Page: Displays basic information about the band.
About Page: Information about the band members.
Contact Page: Form to contact the band.
Events Page: Shows upcoming events for the band.
Responsive Design: Built with Bootstrap to ensure the app looks great on all devices.

Technologies Used
Django: Web framework used for building the app.
Bootstrap: Front-end framework used for responsive design.
SQLite: Default database used for this project (you can switch to another database like PostgreSQL if needed).
Git: Version control for managing the project's source code.

Installation
Follow these steps to get your development environment set up:
Prerequisites

Make sure you have the following installed:
Python
Pip (Python's package installer)
Git (for version control)
Virtualenv (for managing dependencies in isolated environments)

Step 1: Clone the repository
Clone the repository to your local machine:
bash
git clone git@github.com:lipholo-dev/level-2-capstone.git

Step 2: Navigate to the project directory
bash
cd level-2-capstone

Step 3: Set up a virtual environment
Create a virtual environment and activate it:
bash
python -m venv venv

On Windows:
bash
venv\Scripts\activate

On Mac/Linux:
bash
source venv/bin/activate

Step 4: Install the required dependencies
Install all the necessary dependencies listed in requirements.txt:
bash
pip install -r requirements.txt

Step 5: Apply database migrations
Run the following command to set up your database:
bash
python manage.py migrate

Step 6: Create a superuser (optional, for admin access)
To access the Django admin panel, create a superuser:
bash
python manage.py createsuperuser
Follow the prompts to set a username, email, and password.

Step 7: Run the server
Start the Django development server:
bash
python manage.py runserver
The app should now be running at http://127.0.0.1:8000/.

Usage
1. User Registration and Login
Navigate to /accounts/register/ to create a new account.

Use /accounts/login/ to log in.
Upon successful login, you will be redirected to the Home Page.

2. Pages
Home: Displays basic information about the band, including an introduction and upcoming events.
About: Learn about the band members with images and short bios.
Contact: A form for users to contact the band.
Events: List of upcoming events the band is performing at.

3. Admin Access
Access the Django admin panel at /admin/ (requires superuser credentials : username: admin, password: admin1234).
The admin panel allows you to manage band members, events, and other data.
