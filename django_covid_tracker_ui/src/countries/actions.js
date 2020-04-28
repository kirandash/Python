// CREATE_COUNTRY Action
export const CREATE_COUNTRY = 'CREATE_COUNTRY'; // Action Type
export const createCountry = countryCode => ({
    type: CREATE_COUNTRY,
    payload: { countryCode }
}); // Action Creator

// REMOVE_COUNTRY Action
export const REMOVE_COUNTRY = 'REMOVE_COUNTRY'; // Action Type
export const removeCountry = countryCode => ({
    type: REMOVE_COUNTRY,
    payload: { countryCode }
}); // Action Creator

// PIN_COUNTRY Action
export const PIN_COUNTRY = 'PIN_COUNTRY'; // Action Type
export const pinCountry = countryCode => ({
    type: PIN_COUNTRY,
    payload: { countryCode }
}); // Action Creator

/* Country API Actions Start */

// LOAD_COUNTRY_IN_PROGRESS Action
export const LOAD_COUNTRY_IN_PROGRESS = 'LOAD_COUNTRY_IN_PROGRESS'; // Action Type
export const loadCountryInProgress = () => ({
    type: LOAD_COUNTRY_IN_PROGRESS,
}); // Action Creator

// LOAD_COUNTRY_SUCCESS Action
export const LOAD_COUNTRY_SUCCESS = 'LOAD_COUNTRY_SUCCESS'; // Action Type
export const loadCountrySuccess = countries => ({
    type: LOAD_COUNTRY_SUCCESS,
    payload: { countries }
}); // Action Creator

// LOAD_COUNTRY_FAILURE Action
export const LOAD_COUNTRY_FAILURE = 'LOAD_COUNTRY_FAILURE'; // Action Type
export const loadCountryFailure = () => ({
    type: LOAD_COUNTRY_FAILURE,
}); // Action Creator
/* Countries API Actions End */