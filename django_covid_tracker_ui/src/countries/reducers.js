import { CREATE_COUNTRY, REMOVE_COUNTRY, PIN_COUNTRY,
    LOAD_COUNTRY_IN_PROGRESS,
    LOAD_COUNTRY_SUCCESS,
    LOAD_COUNTRY_FAILURE, } from './actions';

export const isLoading = (state = false, action) => {
    const { type } = action;

    switch (type) {
        case LOAD_COUNTRY_IN_PROGRESS:
            return true;
        case LOAD_COUNTRY_SUCCESS:
        case LOAD_COUNTRY_FAILURE:
            return false; // false for both success and failure actions
        default:
            return state;
    }
} // Reducer to return true or false based on actions occuring in our app

export const countries = (state = [], action) => { // Default state is mentioned as an empty array to avoid any error in case, the state passed is not having any data
    const { type, payload } = action; // Get Action Type and payload from the action (By destructuring)
    switch (type) {
        case CREATE_COUNTRY: { // Note: We could use 'CREATE_COUNTRY' string but it is better to import the constants we created in actions.js file. Since there will be less chance of making a typo
            const { countryCode } = payload;
            const newCountry = {
                "info":{
                    "ourid":177,
                    "title":countryCode,
                    "code":countryCode,
                    "source":"https://thevirustracker.com/singapore-coronavirus-information-sg"
                },
                "total_cases":2299,
                "total_recovered":528,
                "total_unresolved":0,
                "total_deaths":8,
                "total_new_cases_today":0,
                "total_new_deaths_today":0,
                "total_active_cases":1763,
                "total_serious_cases":31,
                "total_danger_rank":50,
                "isPinned": false // isPinned will not be present in API response - we will add it to the state manually. Would have added the prop to API if we had backend control
            }; // Hard Coded Country details, later to be replaced by API response
            return state.concat(newCountry);
        }
        case REMOVE_COUNTRY: {
            const { countryCode } = payload;
            return state.filter(country => country.info.code !== countryCode); // Remove country with countrycode received in payload
        }
        case PIN_COUNTRY: {
            const { countryCode } = payload;
            return state.map(country => {
                if(country.info.code === countryCode) {
                    return { ...country, isPinned: true }; // isPinned will not be present in API response - we will add it to the state. Would have added the prop to API if we had backend control
                }
                return country;
            });
        }
        case LOAD_COUNTRY_SUCCESS: {
            if(payload.countries.results && payload.countries.results[0].data === "none"){  
                alert("Invalid country code!"); // error handling
                return state;
            }
            const apiCountry = payload.countries.countrydata[0];
            const newCountry = {...apiCountry, isPinned: false}; // Country Data from API + isPinned not present in API response - we are adding it manually to the state
            return state.concat(newCountry); // Add the new country to the list of existing countries in state
        }
        case LOAD_COUNTRY_IN_PROGRESS:
        case LOAD_COUNTRY_FAILURE: // retrun the default state for IN PROGRESS and FAILURE Action for now
        default: {
            return state;
        } // Since this reducer is going to be common to our app. The Countries reducer will be called for other actions as well. So if the action is not defined in our switch case block, default block will return the state as is
    }
}