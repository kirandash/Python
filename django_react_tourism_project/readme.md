# Django React

## 1. Intro
### 1.1 Project overview
1. **Django Libraries**:
    - **Django** (web framework), `pip3 install django==3.0.4` (will install django and pytz library which provides timezone support). To upgrade pip: `sudo pip install --upgrade pip`
    - **Django REST Framework** (framework for creating REST APIs), `pip3 install djangorestframework`
    - **Django-filter** (dependency of Django REST: filtering of querysets and models), `pip3 install django-filter`
    - **Django OAuth Toolkit** (for OAuth2 authentication of the REST API)
2. **Front End Modules**:
    - **React.js** for building components
    - **React Router**: for navigating between React components
    - **Jest**: for unit testing
    - **Cypress**: for end-to-end testing
3. **Initial setup**:
    - Django models for packages, bookings, wishlist items
    - Methods for React to use Axios to interact with the Django API server
    - React components for displaying tour packages

### 1.2 Project creation and Run the Django server
- Create project: `django-admin.py startproject django_react_tourism`
- Rename root folder name to `django_react_tourism_project`</li>
- Create Virtual environment: `sudo pip install virtualenv` and `virtualenv python_env` or use an existing virtual environment if present.
- Activate vir env: `source django_restapi_ecom_env/bin/activate` (using venv of prev project)
- Run server: `python3 manage.py runserver`: available at http://localhost:8000/

## 2. Django and React Project Setup
### 2.1 Project Pre Requirement Setup
1. Install dependencies: `pip install django-oauth-toolkit`
2. Run `python3 manage.py makemigrations` and `python3 manage.py migrate`
3. Add initial react frontend code