# COVID-19 Tracker
## 1. Intro and Setup
This is a web application using which we will be able to track covid-19 reports for any specific country. We will also be able to pin specific countries so that the pinned countries results will always show at the top.

### 1.1 Create app with create-react-app
1. Create react app is a tool that helps us create a react app quickly so that we don't have to setup the project from scrathc. Run the command: `npx create-react-app covid-tracker`.

### 1.2 Understanding Project structure
1. The project created by create-react-app has 2 main folders
    - **public**: to hold publicly accessible resources of our app
    - **src**: will hold actual react code
2. **public folder - public/index.html**:
    - index html file is present inside public folder. This file is going to be sent to the client when react app loads.
    - **div with id root**: index.html file has a div with id `root` which is the target where our react app is going to load.
    - There is a **noscript** tag which will execute if JS is disabled for client browser. So if client's browser has JS disabled, client will get the message written in noscript tag.
3. **src folder**:
    - **index.js**: Code in this will help us insert our React App into index.html with `ReactDOM.render()`. ReactDOM is an extension of React that helps us with rendering react components on to DOM.
    - **index.css**: Holds global css for our app. All styles written here will be applied to all the components in our App.
    - **App.js**: Holds JS code for our root React component
    - **App.css**: Holds CSS code for our root React component
4. **package.json**:
    - Holds details of all the packages that are used so far.
    - Also holds the scripts for starting dev server, creating a build and testing our app.
5. Run the command `npm run start` to run the project on localhost:3000
6. Change app title to COVID-19 Tracker in index.html file.

## 2. Building the App View by Creating Components
### 2.1 Create SearchCountryForm component
1. This component will hold the form which we will use to search covid report for a specific country.
2. Create src/countries/SearchCountryForm.js and src/countries/SearchCountryForm.css.
3. Add component code to .js file. Add the component to root component App.js file
4. Copy css to SearchCountryForm.css file. And add styles to App.css, index.css file.

### 2.2 Create CountriesList component
1. This functinoal component will hold the list of all countries we are tracking.
2. Create src/countries/CountriesList.js and CountriesList.css files.
3. Add CountriesList to App.js.

### 2.3 Create CountryDetail component
1. This functional component will hold the individual country details.
2. Create src/countries/CountryDetail.js and .css file.

### 2.4 Create sample countries and add to App.js
1. Create sample-countries.js and send that as props to CountriesList component in App.js file.

## 3. Managing State of the App with Redux
### 3.1 Why do we need Redux?
1. Let's have a look at ways to manage state:
    - **A single state**: Creating state for root component and using that for all child components following a prop chain. **Cons**: Not suitable for large applications. As lots of props get attached to root state. And we will have to deal with **props drilling**. For example: App ---> Page ---> Section ---> List ---> ListItem. Ugly and difficult to troubleshoot. Prone to errors if we break the prop chain by mistake.
    - **Components managing their own state**: Creating state for each component. Pros: No Props drilling. **Cons**: Difficult to share data between two components.
    - **Global State Management**: A single centralized state, With all child components having unlimited access to it. **Pros**: No Props drilling. Easy to share state data b/w components. **Cons**: No rules/organizations on how to create state and use it. Thus leads to inconsistency b/w developers. And hard to recreate bugs for troubleshooting. Thus, unrestricted global state is not an ideal choice.
    - **Redux** solves this problem by adding rules/orgnaizations to global state management.

### 3.2 Understanding Redux
1. Redux helps managing state or data in our application.
2. Redux consists of 3 things: A Redux Store, Redux Actions and Reducers.
    - **{ Redux Store }**: JSON object that contains current state of our app. Redux Works on global state management concept. It has one centralized state where all our data is available and the centralized state is called **Store**. **The redux store** is basically a JSON object that can hold any type of data we want. Ex: In our application, the store will hold all the countries data.
    - **Redux actions**: It defines different actions that can occur in our app. Ex: `COUNTRIES_DATA_LOADED`, `SUBMIT_BUTTON_CLICKED`. A Redux action is a JSON object consisting of two things: type of the action and payload. 
    - **Reducers**: This defines what changes to do with Redux Store when a Redux action occurs. Ex: When `SUBMIT_BUTTON_CLICKED` action occurs, we take all the data in payload and store it in countries property in our redux store.
3. How redux helps react with state/data management?
    - We can also manage state or data without React but the main problem is there are no standard sets of rules to follow. So, if you are building a large application with a team, not having a set of standards will create more bugs in your project. Redux solves this problem by adding some extra set of standards or rules that each developer can follow.

### 3.3 Adding redux to our React App
1. We will need two packages for implementing Redux in our Application. 
    - redux to handle redux realated tasks and 
    - react-redux to integrate redux with react
    - Install using npm: `npm install redux react-redux`
2. Create src/store.js: This file will hold logic for our redux store. Since the store is global for the entire app, we will keep the store.js file at root level which is src folder instead of keeping it inside countries folder.
    - Create root store by combining all reducers
3. In index.js: wrap `App`with `Provider`. Provider provides our centralized Redux store to a react component. Ex: `<Provider store={configureStore()}><App/></Provider>`

### 3.4 Creating Redux Actions for Create Country and Remove Country
1. Create src/countries/actions.js file. This is inside countries folder. Because we don't want to make one centralized list of actions. Actions can also come from different modules.
2. Create Action type constant and Action creator function for CREATE_COUNTRY and REMOVE_COUNTRY actions.

### 3.5 Creating Reducers and Connecting it to root store
1. A reducer is basically a fn to perform some tasks when an action is dispatched.
2. Create src/countries/reducers.ts file.
3. Reducer takes 2 args: current state, action triggered
4. After countries reducers is created in reducers.ts file. Import it and add it to the list of reducers in store.js file

### 3.6 Connecting SearchCountryForm Component to the Store with connect from react-redux
1. connect is a higher order fn with 2 sets of args: `connect()()` Ex: `conneect(mapStateToProps, mapDispatchToProps)`
2. mapStateToProps is a Fn which takes the entire state of our app as input and return specific props from the state which the specific component requires. And all props defined inside mapStateToProps is automatically made available by connect as prop for the component to use.
3. mapDispatchToProps is a Fn which takes dispatch as input. A dispatch is a fn used to call an action creator.
4. useState react hook is used to create a variable inputCountryCode to hold country code data and setInputCountryCode is a fn to set the variable's value

### 3.7 Connecting CountriesList component to store and Running our React - Redux application
1. src/countries/CountriesList.js: Use connect witih mapStateToProps and mapDispatchToProps
2. Note: mapStateToProps and mapDispatchToProps are optional. Ex: `connect(mapStateToProps)(mycomponent)` and `connect(null, mapDispatchToProps)(mycomponent)`
3. Remove sampleCountries from CountriesList in App.js. Since now we are populating it from state. Later we will get it from API.
4. Run: `npm run start` and test create/delete functionality at http://localhost:3000/
5. Test Adding and Removing Country on browser

### 3.8 Persisting the Redux store with redux-persist
1. Our current store gets cleared on reloading browser. To persist data in store: use **redux-persist**. `npm install redux-persist`
2. store.js file: Wrap rootReducer with persistReducer configuration.
3. index.js file: Wrap App with PersistGate
4. Now on reloading browser, the state will be still saved. In order to clear it, delete the `persist:root` data from localStorage.

### 3.9 Redux DevTools
1. To monitor states from chrome dev tools.
2. Add Redux DevTools extension to chrome : https://chrome.google.com/webstore/detail/redux-devtools
3. Add __REDUX_DEVTOOLS_EXTENSION__ to store.js createStore fn. It should highlight the redux devtools extension once our app is loaded.
4. Run app with `npm run start`
5. Go to localhost and on performing some action: it will show the list of actions. The difference it makes to state and new state after the action, all in the Redux devtools extension

### 3.10 Redux flow for Pin Country
1. Create PIN_COUNTRY action in action.js and add it to the list of reducers in reducers.js
2. Dispatch the action Creator in CountriesList.js and pass it as a props to child component CountryDetail.js. Note: We are not connecting redux directly to CountryDetail.js because we want to keep it reusable. Always good practice to keep our redux connection at parent level and pass to child as props.
3. In CountryDetail.js hide the Pin Country button once it is pinned. Later we will modify the code to show all Pinned countries at top and not pinned one's at bottom.

## 4. Handling API/Asynchronous Calls with Thunks or Redux Thunks
### 4.1 Why Do We need Redux-Thunk?
1. With Redux now our components size are really small as most of the state management code is moved out of component to store.js, actions.js and reducers.js file.
2. Still in our current code: component has to contain code for asnyc/API calls.
3. We can handle API calls in React component. But since our goal is to create a scalable application, we will handover the responsibility of making API calls to Thunks which has better sets of standards for managing API calls.
4. Thus we have used Redux for State Management, Components for creating Views and now we will use Redux Thunks for handling API calls.
5. Alternate Libraries to Redux Thunk for managing API calls: Redux Saga, Redux Logic etc.
6. Redux saga is more popular.
7. But Redux Thunk is simpler and easy to learn. And It does a pretty good job. I use it in most of my projects.

### 4.2 Understanding Redux Thunk Flow
1. UI Triggers Action ---> Redux Thunk is executed to make Async/API calls ---> State is Updated ---> Component See updated State.

### 4.3 Adding Redux Thunk to React
1. `npm install redux-thunk redux-devtools-extension @babel/runtime`
    - redux-thunk is the main thunk library to be used in our app
    - redux-devtools-extension is used for adding redux-thunk to our devtools middleware.
    - @babel/runtime: is used so that async thunks can work in our app
2. `npm install --save-dev @babel/plugin-transform-runtime`
    - Dev version of @babel/runtime: used for async thunks to work in our app
3. Add thunk to store.js file
4. thunk is used with applyMiddleware from redux.
5. The result is passed through composeWithDevTools for dev tools support
5. After adding Thunks throw applyMiddleware, test on chrome if every thing working as before - action dispatch in dev tool.

### 4.4 Creating a showAlert thunk
1. Create src/countries/thunks.js file
2. A thunk is a fn which calls another fn which performs a particular task
3. Create a sample showAlert Thunk to test
4. Add the thunk to CountriesList.js for temporary testing.

### 4.5 Async thunks - for loadCountry API from thevirustracker
1. Create actions for in progress, success and failure state in actions.js file.
2. Create thunk `loadCountry` in thunks.js file.
3. API URL to be called in loadCountry thunk: `https://api.thevirustracker.com/free-api?countryTotal=US`. (Not reliable. If this API is not working, please use any other working API from postman URL) Note that countries JSON structure will change based on API URL.
4. More APIs: `https://covid-19-apis.postman.com/`

### 4.6 Adding isLoading reducer and calling loadCountry in SearchCountryForm.js
1. Create reducer in reducers.js file - to check if API is loading, success or failure.
2. Add it to list of reducers in store.js file.
3. Call loadCountry thunk in SearchCountryForm.js file. When submit button is pressed. Remove create Country action since load country will handle country creation for us
4. send country code to loadCountry thunk, thunk.js file and add a delay to demonstrate isLoading feature
5. Add loader to CountriesList.js file. Which will show loading message whenever a new country is added to Tracking List.

### 4.7 Modify the countries reducer to show countries from API
1. reducers.js file - Add actions for LOAD_COUNTRY_SUCCESS, LOAD_COUNTRY_IN_PROGRESS and LOAD_COUNTRY_FAILURE
2. Sample Country Codes for testing: GB (United Kingdom), US (USA), SG (Singapore), GE (Georgia), IN (India), IT (Italy), ES (Spain)
3. We have also handled error for use case when user enters invalid countrycode. Pls test.
4. Also remove manual delay of 3s from loadCountry thunk.

### 5. Selectors
### 5.1 Why do we need selectors?
1. Till now we have separated the application responsibilities as follows:
    - Component ---> Display View
    - Reducers ---> Manage State
    - Thunks ---> API/Async calls
2. Currently, we are mapping data from state directly to mapStateToProps. Ex in CountriesList.js file. But what if we need to modify the data from state before assigning to mapStateToProps.
3. **Selectors** 
    - gives us a place to put logic for combining, filtering, transforming and storing data before passing it to the React View Component. It is one more layer between Redux reducers and React view components.
    - If JSON data structure of state changes, we don't have to change the mapping in mapStateToProps for every component. All we have to do is just change the code in selectors.js file.

### 5.2 Creating selector - getCountries and getIsLoading
1. Create src/countries/selectors.js file
2. Add getCountries and getIsLoading selectors in selectors.js
3. **IMPORTANT:** The beauty of selectors is: now if structure of state changes, we don't have to change the mapping in mapStateToProps for every component. All we have to do is just change the code in selectors.js file.

### 5.3 Combining selectors with createSelector from Reselect to create getPinnedCountries and getNotPinnedCountries selectors
1. Create selectors getPinnedCountries and getNotPinnedCountries to get separate list of countries: pinned and not pinned countries in selectors.js
2. We will use getCountries selector to create these selectorr. For this we will use a tool called **reselect** used for combining selectors / modifying them.
3. `npm install reselect`
4. **createSelector**: It accepts multiple args. The last fn will take input from all the selectors mentioned before it. The output of last fn is the final o/p
5. Diff b/w createSelector from reselect and normal fn. With a normal fn, the computation will happen all over again when component rerenders. But with createSelector, it does not compute everything when our component re-renders. It computes only the prop in state which has changed from the prev state. Thus, createSelector saves a lot of resource when building large scale applications by limiting the computation to only state which is changing on component rerendering.

### 5.4 Adding getPinnedCountries and getNotPinnedCountries to components
1. Add both the selectors to mapStateToProps of CountriesList.js
2. Note: If any issue comes in loading the app, it might be bcoz of the localStorage, so clear the localStorage data. Make sure the defaults are set to empty array and reload the app.

## 6. Styled Components
### 6.1 Why do we need styled components?
1. So far we have separated the concerns as follows
    - Components ---> Display data
    - Reducers ---> Manage state
    - Thunks ---> Side Effect Logic
    - Selectors ---> Abstracting the state's format, transforming state data
2. For handling CSS: we are currently using separate .css file aka **css modules**. Ex: component.js and component.css file. This is not ideal to have extra css file or modules for every component.
    - It will clutter our folder structure.
3. **Styled Component:** Allows us to define styles inside our JS files.
    - Benefit: Lesser files. Clean folder structure.
    - Important Benefit: can pass props to Styled Component and thus can dynamically change styles. And hence the styled components are reusable.

### 6.2 Creating a Styled Component
1. Install: `npm install styled-components`
2. Create styled components in CountriesList.js using tagged fns. styled.div or styled.h1 or styled.button etc
3. Organizing styled components (Thumb Rules): 
    - If the component is unique and there is less amount of code then keep it in js file. 
    - If amount of code is more, create separate styled component js file. 
    - If component is common and can be reused, create seaparate file and store all styled components in src/todos/user-interface folder.

### 6.3 Converting CSS modules to Styled components
1. Move code from .css modules to .js files, comment import of css files and delete the css files. For: CountriesList.css, CountryDetail.css, SearchCountryForm.css and App.css
2. Ex: copy styles of list-wrapper from CountriesList.css file to CountriesList.js file with styled.div and replace `<div className="countries-list-wrapper">` with `<CountriesListWrapper>`

### 6.4 Passing props to Styled Components - Diff bg for pinned countries
1. The main benefit of styled components is we can pass props to them and thus can dynamically change styles. Thus condition for styling is moved to styled tagged fns and JSX is much more cleaner.
2. Ex: `background: ${props => props.isPinned ? '#350000' : '#212121'};`

### 6.5 Extending Styled Components
1. Extend style of one component to another. Like class inheritance.
2. Test after changing code.

### 6.6 Media Queries
1. CountryDetail.JS: Let's change btn color for mobile devices. @media screen and (max-width: 767px) {}

## 7. Building Files for Production
1. Run command `npm run build` and move the files to your server where you want your files.
2. If you want to move your files to a subfolder, then you will have to add another property called: `homepage` to package.json file. Note that this will only work if you app is built using create-react-app tool.

### 7.1 Next Tasks
1. Create Unpin Country Button, clicking which The pinned Countries can come back to the Not Pinned Countries Section.
2. Create another React Component to show the Global Stats of total cases,  from API: https://api.thevirustracker.com/free-api?global=stats. Use the same flow of first creating a GlobalStats.js component, add redux globalstats reducer, add selectors and finally adding styles with styled components.
3. Modify the reducer code to remove isLoading reducer and add isLoading as a property of state.countries instead of direct child of the state. Because now we are adding a new API. and we will need isLoading property for individual API. So also we need to add another isLoading prop for state.globalstats.