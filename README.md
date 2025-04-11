Django Capstone Project
This repository contains the Django Capstone Project for Level 2. This README provides instructions on how to set up and run the application using both virtual environment and Docker.
Prerequisites

Python 3.8 or higher
pip (Python package installer)
Docker (for container deployment)
Git

Setup using Virtual Environment
1. Clone the repository
bash
git clone git@github.com:lipholo-dev/level-2-capstone.git
cd level-2-capstone

2. Create and activate a virtual environment
bash#
On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
bash
pip install -r requirements.txt

4. Configure environment variables
Create a .env file in the project root directory with the following content:
SECRET_KEY=your_secret_key_here
DEBUG=True
Note: Replace your_secret_key_here with a secure random string.
5. Run migrations
bash
python manage.py migrate

6. Create a superuser (optional)
bash
python manage.py createsuperuser

8. Run the development server
bash
python manage.py runserver

The application will be available at http://127.0.0.1:8000/

Setup using Docker
1. Clone the repository
bash
git clone git@github.com:lipholo-dev/django-capstone-level-2.git
cd django-capstone-level-2

3. Configure environment variables
Create a .env file as described in the previous section.

4. Build the Docker image
bash
docker build -t django-capstone .

6. Run the Docker container
bash
docker run -p 8000:8000 django-capstone

The application will be available at http://localhost:8000/

Documentation
Project documentation is available in the docs/ directory. 
To view the documentation:

Navigate to the docs/ directory
Open _build/html/index.html in your web browser
