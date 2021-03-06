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

### 3.4 Partially updating an item using React
1. use `setOrderItem` and `clearOrderItem` in App.js to trigger when wishlist item added to cart or item removed from cart but stays on wishlist.
2. call the API in wishlistCartStatus method in file ServiceApi.js file.
3. Test by adding the packages to reserve on browser and then removing it.

### 3.5 Pagination with Django
3 Types of pagination:
1. **LimitOffset pagination**: Limits how many items are on a page and pages through by the offset number
2. **Cursor Pagination**: Relies on DB cursor to return pages of items. Good for large data sets.
3. **PagNumber Pagination**: Has a page size and a page number. Uses Django's default Paginator class. (Simpler approach)\
We are going to use PageNumber pagination.
1. In views.py file, apply PageNumber Pagination to PublicPackageViewSet

### 3.6 Pagination with React
1. Create pagination in Pagination.js
2. Modify List.js to implement pagination.
3. Modifer retrieveList to send pagination details (page number)
4. After changing FE/React code always make sure to create a build: `npm run-script build` and then run python server to check result.

### 3.7 Filtering with Django
1. Use BasicFilterBackend and SearchFilter from rest framework filters to create Price Filter and Search Filter for our app.

### 3.8 Filtering with React
1. Add code to Filters.js
2. Modify List.js to include Filter on top of the page
3. Modify retrieve API call to include the filter params as queryParams

### Module 3 Quiz
1. Output of code: `console.log('a'); this.setState({ a: 2 }, () => { console.log('b') }); console.log('c')` ---> acb
2. In Django, which is the correct code to filter a queryset where the "price" field is greater than or equal to "100"?\
Ans: `queryset.filter(price__gte=100)`
3. Write the code to use Axios to send the "item" query parameter\
Ans: `Axios.get('/', { params: { item: 1 } })`
4. What is the name of the Django REST framework paginator that paginates by limit and offset?\
Ans: `LimitOffsetPagination`
5. Which HTTP method is used to indicate that a request partially updates some data?\
Ans: `PATCH`
6. When using Axios for making HTTP calls, what is the name of the method that will send a DELETE request?\
Ans: delete
7. In React, when using the `map` fn to render a list of React components, which attribute uniquely identifies each component?\
Ans: key
8. Using Django REST Framework, which code will define a new route to the "ShoppingCartViewset"?
Ans: `router = DefaultRouter(); router.register(r'public/packages', ShoppingCartViewset)`

## 4. Forms with React and Django
### 4.1 Handling creating models with Django REST Framework
1. Create BookingViewSet in views.py
2. Create BookingSerializer using Booking model in serializers.py file
3. Register url path in urls.py file using Django default router `router.register(r'bookings', api.views.BookingViewSet)`
4. Check the result here: http://localhost:8000/api/v1/bookings/: where we will see our list of bookings and a form to create new bookings.

### 4.2 Creating a REST API service class with React and Axios
1. Call wishlist API in retrieveWishlist method in ServiceApi.js file.

Authentication:
1. Client credentials: Used for Back-end servers that communicate with other APIs or for front ends that communicate with a server.
2. Password: Used for Front ends where a user logs in with their username and password.

Code:
1. write createBooking method in ServiceApi.js file to do a POST call for booking.

### 4.3 Creating a basic form as a React Component
1. Add the Form elements and methods to Checkout.js page

### 4.4 Creating form fields for basic form
1. Each form field is controlled by FormField component in FormField.js. 
2. CSS for Checkout.js is in Checkout.css file.

### 4.5 Connecting a React component to a Service
1. Add validation to createBooking. In ServiceApi.js, add reject method.
2. In Checkout.js add validation for isOrderPlaced

### 4.6 Validating Data with Django REST Framework
1. Add validation to BookingSerializer for Street address format with `validate_street_address()` method

### 4.7 Displaying Validation errors with React
1. Add the code in Checkout.js

### 4.8 Module 4 Quiz
1. What is destructuring?\
Ans: Destructuring an object is to extract specific fields from objects and assigning them to variables. Ex: `const { a, b, c } = data;`
2. In Django REST Framework, how to define a custom validation fn for the field named "cost"?\
Ans: Add the following code to serializer: `def validate_cost(self, value): return True`
3. When using Promises in JS, how to handle errors? Write sample code.\
Ans: For Promise, the `catch()` method is used to handle errors. Code: `promise.then(() => {}).catch((error) => { console.log(error)) })`
4. In React, with form input fields, which 2 attributes should you bind?\
Ans: `value and onChange`
5. In React, what are contexts used for?\
Ans: Contexts are used to share data and methods without having to pass them through every component's props.
6. To use Axios to send an HTTP request, which code will set the OAuth token header correctly?\
Ans: ``{ headers: { 'Authorization': `Bearer ${oauthToken}` } }``
7. In Django REST Framework, how to set which serializer is used for a viewset?\
Ans: `serializer_class = MySerializer`

## 5. Refactoring React with Hooks and Higher-Order Components
### 5.1 Using timers with state to display data
1. When user is on checkout page, we will add some urgency that they should place order.
2. Create timer on OnHold.js component
3. Add OnHold component to Checkout.js page.

### 5.2 Creating a higher order component with React
1. Create FieldValidation.js, a higher order component
2. Use it to create a new component in Checkout.js page

### 5.3 Using React hooks and refactoring a component to use hooks
1. We will use useState, useEffect hooks in OnHold.js component.
2. **useState hook**: The new React hook that replaces setState and this.state = {}. And use `setVariablename` instead of `this.setState({ variablename })`.
3. **useEffect hook**: New React hook that replaces `componentWillMount` and `componentWillUnmount`.

### 5.4 Refactoring a higher order component to use hooks
1. we will useState hook in FieldValidation.js
2. Implement useValidation hook from FieldValidation.js in FormField.js component. Call validate method and render ErrorDisplay component.
3. In checkout page, use FormFieldUsingHooks instead of ValidatedFields.

### 5.5 Module 5 Quiz
1. In React, what does the `useState` hook do?\
Ans: It manages state in a React component. This React hook replaces setState and this.state = {}. And use `setVariablename` instead of `this.setState({ variablename })`.
2. In React, what does the `useEffect` hook do?\
Ans: It replaces the `componentWillMount` and `componentWillUnmount` methods of a React component.
3. What are higher order components in React?\
Ans: Higher order components in React are used to encapsulate reusable functinality that needs to be used in multiple components.

## 6. Testing React and Django
### 6.1 Unit testing a component
1. Add test cases to src/components/Filters_test.js file
2. Run `npm test`

### 6.2 Unit testing two React routes and navigation between components
1. Create mock data with jest.
2. Add async test cases to App.test.js file.
3. **@testing-library/react** utilities provide several useful fns:
    - **render**: mounts a component into the DOM and renders it
    - **fireEvent**: fires a click or input event on a DOM element
    - **cleanup**: unmounts a rendered component, deleting it from the DOM after tests are run
    - **wait**: asynchronous fn that waits until a component has been fully rendered
4. **@testing-library/react** query types:
    - **queryByTestId**: searches for DOM elements with the `data-testid` attribute
    - **getByText**: Finds elements containing the given text, similar to queryByPlaceholder
5. run `npm test`

### 6.3 End2End testing the form submission process for checkokut page
1. Use cypress for End2End testing.
2. Add checkout form test cases in: cypress/integration/submit_form_spec.js file.
3. For e2e test: make sure django server and react server are running and then run: `npm run e2e`

### 6.4 End2End testing the Filtered data table
1. Add e2e test cases in filter_item.spec.js file. (For testing filter)
2. `npm run e2e`

### 6.5 Unit testing caching with Django REST framework
1. django/api/tests.py file
2. Add test cases to `CachingTestCase` class.
3. Run test: python3 manage.py test

### 6.6 Unit testing sorting and filtering in Django
1. Add SortingFilteringTestCase to django/api/tests.py file.
2. Run test: `python3 manage.py test`

### 6.7 Unit testing validation for the REST API in Django
1. Create `class ValidationTestCase(APITestCase):` in django/api/tests.py file
2. Run test: `python3 manage.py test`

### 6.8 Module 6 Quiz
1. In Django unit testing, what is the function to assert two objects are the same?\
Ans: assertEqual. Ex: `self.assertEqual(response.status_code, 400)`
2. In Django unit testing, what is the fn to compare 2 lists?\
Ans: assertListEqual. Ex: `self.assertListEqual(response.data, [])`
3. When testing Django REST Framework, what should be the super class of the test suite class?\
Ans: APITestCase
4. Which code for Cypress end-to-end for React, testing will navigate the browser to a particular URL?\
Ans: `cy.visit('http://localhost:3000/path/to/page')`
5. In Cypress e2e testing for React, which code will enter test into a form field?\
Ans: `cy.get('input').type('hello')`
6. When writing a unit test in React using testing-library and jest, which code will select this HTML element? `<div test-id="content"></div>`\
Ans: `renderedComponent.queryByTestId('content')`
7. When writing a unit test in React using testing-library and Jest which code will select a button that contains the text "Click Here"?\
Ans: `renderedComponent.queryByText('Click Here')`