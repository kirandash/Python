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

### 2.4 Serving React code through Static Django Files
1. **settings.py**: Add `FRONTEND_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'django_react_tourism_ui', 'build'))`
2. **urls.py**: `from django.conf.urls.static import serve` and add `re_path(r'^(?P<path>.*)$', serve, { 'document_root': settings.FRONTEND_ROOT })` to urlpatterns
3. Run django server and site will be available at localhost:8000/index.html

### 2.5 Navigating between React Components using React Router
1. React only provides components. React router helps us navigate through the components and makes components behave like a page on the website.
2. To use react router: wrap our entire app in `<BrowserRouter>` and then use `<NavLink to="/">Explore our tours</NavLink>` to navigate through paths

### 2.6 Module 2 Quiz
1. Using React Router, define a Route that uses the DetailsPage component.\
Ans: `<Route path='/details' component='DetailsPage'/>`
2. In Django, there are how many ways to serve static files in the URL configuration?\
Ans: Two
3. For React, running `npm run-script build` will create a production build for the React App.
4. For a React project, which configuration key in package.json needs to be set so that API requests are proxied to a local REST API server?\
Ans: proxy

## 3. Filtering and Pagination with Django and React
### 3.1 Creating a ViewSet with Django
1. Create PublicPackageViewSet in views.py using existing serializer PackageSerializer.
2. Use Django REST Framework DefaultRouter in urls.py to navigate to PublicPackageViewSet: `router.register(r'public/packages', api.views.PublicPackageViewSet)`

### 3.2 Displaying List of items in React
1. Create a List class in List.js file.
2. Call API using retrieveList in ServiceAPI.js

### 3.3 Toggling an Item from Wishlist using React and Django
1. App.js: Delete or add an item to Wishlist by calling wishlistDelete or wishlistAdd API
2. wishlistDelete to be added in ServiceApi.js
3. In Django: Add the destroy method to WishlistItemViewSet in view.py file
4. Now run the server and check if it works in FE and BE
5. For BE, we will need an admin. So create a superuser: `python3 manage.py createsuperuser` username: kiran, password: mycommonpwd
6. Go to Admin at http://localhost:8000/admin/
7. Check wishlist at http://localhost:8000/admin/api/wishlistitem/. Toggling wishlist items on FE should reflect here on BE