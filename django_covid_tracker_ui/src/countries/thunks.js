import { loadCountryInProgress, loadCountrySuccess, loadCountryFailure } from './actions';

export const loadCountry = (countryCode) => async (dispatch, getState) => { // loadCountry is a thunk: A fn which calls another fn which performs a particular task. The 2nd fn is an async fn which takes 2 args: dispatch to dispatch actions and getState to get current state of app
    try {
        dispatch(loadCountryInProgress()); // dispatch in progress action
        const response = await fetch(`https://api.thevirustracker.com/free-api?countryTotal=${countryCode}`); // calling country api
        const country = await response.json(); // Get the response in JSON format (Mandatory with fetch calls. Not required when we use addons like Axios to do API calls)

        // await new Promise(resolve => setTimeout(resolve, 3000)); // creating delay to check isLoading functionality

        dispatch(loadCountrySuccess(country)); // dispatch success action
    } catch (e) {
        dispatch(loadCountryFailure()); // on error, dispatch failure action
        dispatch(showAlert(e)); // on error, dispatch alert thunk with error message
    } // try catch block to catch any error
}

export const showAlert = text => () => {
    alert(text);
} // showAlert is a thunk: A fn which calls another fn which performs a particular task