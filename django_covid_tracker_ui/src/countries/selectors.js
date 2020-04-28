import { createSelector } from 'reselect';

// Get Countries selector
export const getCountries = state => state.countries; // if structure of state changes, we don't have to change the mapping in mapStateToProps for every component. All we have to do is just change the code in selectors.js file here and the fns will handle everything else

// Get isLoading selector
export const getIsLoading = state => state.isLoading;

// Get Pinned Countries Selector - From getCountries with reselect
export const getPinnedCountries = createSelector(
    getCountries,
    (countries) => countries.filter(country => country.isPinned) // The last fn will take input from all the selectors mentioned before it, in our case only one getCountries. The output of last fn is the final o/p
);// createSelector accepts multiple selectors.

// Get Not Pinned Countries selector - From getCountries with reselect
export const getNotPinnedCountries = createSelector(
    getCountries,
    (countries) => countries.filter(country => !country.isPinned)
); // Diff b/w createSelector from reselect and normal fn. With a normal fn, the computation will happen all over again when component rerenders. But with createSelector, it does not compute everything when our component re-renders. It computes only the prop in state which has changed from the prev state. Thus, createSelector saves a lot of resource when building large scale applications by limiting the computation to only state which is changing on component rerendering.