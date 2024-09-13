SimpleSocialMediaProject - Django & React
Description
This is a simple social media project built with Django for the backend, Django REST Framework (DRF) for the API,
and React for the frontend. The project allows users to create profiles and blog posts. These functionalities are exposed through a REST API and can be consumed by the React frontend.

1.Table of Contents
2.Project Setup
2.Running the Project
4.API Endpoints
5.Features
6.Technologies Used

Project Setup
1. Clone the Repository

git clone https://github.com/kronera/SimpleSocialMediaProject.git
cd SimpleSocialMediaProject

2. Setting Up the Backend (Django)
Virtual Environment & Dependencies
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

Install the necessary dependencies:

pip install -r requirements.txt

Database Configuration
Ensure your database settings in settings.py are configured properly. The project currently uses MySQL. You may need to update the DATABASES section according to your database credentials.

Migrations
Run the following commands to apply the migrations:

python manage.py makemigrations
python manage.py migrate

Create a Superuser:

python manage.py createsuperuser

This will prompt you to enter a username, email, and password for the superuser.

Run the Django Development Server:
python manage.py runserver

This will start the server on http://127.0.0.1:8000.

3. Setting Up the Frontend (React)
Navigate to the frontend folder:
cd frontend

Install Dependencies
Make sure you have Node.js installed, then install the required packages:
npm install

Running the Frontend
Start the React development server:
npm start

This will start the React app on http://127.0.0.1:3000.

Building the Frontend for Production
If you need to build the app for production:
npm run build

API Endpoints
Blogs:
GET /api/blogs/ - Retrieve all blog posts
POST /api/blogs/ - Create a new blog post
GET /api/blogs/{id}/ - Retrieve a specific blog post
PUT /api/blogs/{id}/ - Update a blog post
DELETE /api/blogs/{id}/ - Delete a blog post
Profiles:
GET /api/profiles/ - Retrieve all profiles
POST /api/profiles/ - Create a new profile
GET /api/profiles/{id}/ - Retrieve a specific profile
PUT /api/profiles/{id}/ - Update a profile
DELETE /api/profiles/{id}/ - Delete a profile


Features
User Profiles: Users can create, view, and update their profiles, including uploading a profile picture.
Blog Posts: Users can create, view, and update their blog posts, with the option to publish or save them as drafts.
REST API: Exposes both blog posts and user profiles, fully integrated with Django REST Framework.


Technologies Used
Backend:
Django
Django REST Framework (DRF)
MySQL (or any configured database)
Frontend:
React
Node.js (with npm for package management)

Frontend-Backend Integration: Set up API calls in React to display blog posts and profiles.
Deployment: Deploy the project on platforms like Heroku (backend) and Netlify (frontend).
Authentication: Implement user authentication and authorization using Django's built-in tools or third-party solutions like django-rest-auth.
