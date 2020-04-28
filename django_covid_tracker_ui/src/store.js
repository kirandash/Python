import { 
    createStore, // Helps creating a store using reducer
    combineReducers, // Helps combining multiple reducers in a form that the result can be passed to createStore fn
    applyMiddleware,
} from 'redux';
import { persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';
import autoMergeLevel2 from 'redux-persist/lib/stateReconciler/autoMergeLevel2';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension'; // for adding redux-thunk to our devtools middleware.

import { countries, isLoading } from './countries/reducers';

const reducers = {
    countries,
    isLoading,
}; // will contain list of all reducers to use in our App

const persistConfig = {
    key: 'root',
    storage, // defaults to localstorage on web
    stateReconciler: autoMergeLevel2, // autoMergeLevel2 tells app how to consider current and stored state of our app
}

const rootReducer = combineReducers(reducers); // Combines all our reducers in a form that can be passed to createStore fn

const persistedReducer = persistReducer(persistConfig, rootReducer); // Wraps root reducer witih persistReducer configuration

export const configureStore = () => 
    createStore(
        persistedReducer,
        composeWithDevTools( // for dev tools support
            applyMiddleware(thunk) // thunk is used with applyMiddleware from redux
        )
        // window.__REDUX_DEVTOOLS_EXTENSION__ && 
        // window.__REDUX_DEVTOOLS_EXTENSION__(), // connects our app to redux devtools extension
    ); // Create configureStore: The root centralized store of our App