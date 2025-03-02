Django + Vue.js Authentication Exploration

A deep dive into modern authentication methods using Django & Vue.js

Overview

This repository serves as a playground for implementing and testing various authentication methods using Django (backend) and Vue.js (frontend). The goal is to explore best practices, pros, and cons of different authentication mechanisms in modern web applications.

📌 Table of Contents
	•	✨ Features
	•	🔑 Authentication Methods To Be Explored
	•	🛠️ Technologies Used
	•	🚀 Setup and Installation
	•	📂 Project Structure
	•	🤝 Contributing
	•	📜 License

✨ Features

✅ Django REST Framework for robust backend API development.
✅ Vue.js for a dynamic and responsive frontend.
✅ Multiple authentication methods implemented and tested.
✅ SQLite (default) database, with easy configuration for PostgreSQL or MySQL.
✅ Docker support for consistent development and deployment environments.

🔑 Authentication Methods Explored

🔹 Token-Based Authentication
	•	Uses Django REST Framework’s built-in token authentication.
	•	Simple & stateless, ideal for Single Page Applications (SPAs).

🔹 JWT (JSON Web Tokens)
	•	Implements djangorestframework-simplejwt for secure, stateless authentication.
	•	Supports token refreshing and blacklisting.

🔹 Session-Based Authentication
	•	Traditional session-based authentication using Django’s session middleware.
	•	Suitable for server-rendered apps or hybrid applications.

🔹 OAuth2 / Social Authentication
	•	Integrates with third-party providers like Google, GitHub, etc.
	•	Uses django-allauth or drf-social-oauth2 for seamless authentication.

🔹 Custom Authentication
	•	Implements custom authentication logic, such as email/password + 2FA.

🛠️ Technologies Used

🔹 Backend
	•	Django – Web framework for the backend.
	•	Django REST Framework (DRF) – API development.
	•	Django REST Framework SimpleJWT – JWT-based authentication.
	•	Django Allauth – Social authentication.
	•	PostgreSQL (optional, default is SQLite) – Database management.

🔹 Frontend
	•	Vue.js – Frontend framework for building UI.
	•	Pinina – State management.
	•	Axios – HTTP client for API requests.
	•	Vue Router – Routing for Vue applications.

🔹 Other Tools
	•	Docker – Containerization for development & deployment.
	•	Redis – Caching and background tasks.
	•	Celery – Asynchronous task processing.

🚀 Setup and Installation

🔹 Backend Setup

# Clone the repository
git clone https://github.com/kinging1022/authy1
cd authy

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations and start the server
python manage.py migrate
python manage.py runserver

🔹 Frontend Setup

# Navigate to frontend directory
cd authy_frontend

# Install dependencies
npm install

# Start the development server
npm run dev

📂 Project Structure

/auth-exploration
│── authy_backend/               # Django backend  
│   ├── settings.py        # Project settings  
│   ├── urls.py            # API routes  
│   ├── authentication/    # Auth methods  
│   ├── models.py          # Database models  
│   ├── views.py           # API views  
│── authy_frontend/              # Vue.js frontend  
│   ├── src/               # Vue components  
│   ├── store/             # pinina state management  
│   ├── router.js          # Frontend routing  
│── README.md              # Project documentation  

🤝 Contributing

We welcome contributions! To get started:
	1.	Fork this repository.
	2.	Create a new branch (feature-new-auth-method).
	3.	Commit your changes and push to your fork.
	4.	Open a pull request 🚀.

📜 License

This project is licensed under the MIT License.
