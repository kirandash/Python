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

### 2.2 Run servers: FE and BE
1. activate venv: `source django_restapi_ecom_env/bin/activate`
2. `cd django_react_tourism_project`
3. `python3 manage.py runserver` will throw an error at 8000 port "Directory indexes are not allowed here." will handle later
4. Now for FE cd `dj_react_tourism_frontend`
5. `npm install`
6. `npm start` will start server at 3000

### 2.3 Preparing react code for production
1. **browserslist**: This is used by react, angular and other FE frameworks to allow JS libraries like babel and TS to know which JS features should be polyfilled or natively supported by browsers. Modern browsers build will be faster since no need of polyfils or transformation. (Defined in package.json file)
2. **>0.2%**: all browser versions above 0.2% global usage.
3. **Not Dead**: Targets new browser versions, not older browser versions viz IE6
4. **not op_mini all**: Does not support Opera mini, any version of the browser
5. Create a build: `npm run-script build`. It will create a prod ready build folder.
6. Once build is ready, project can be seen at http://localhost:8000/index.html