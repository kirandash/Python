import React, { useState } from 'react';
import { connect } from 'react-redux';
import styled from 'styled-components';

// import { createCountry } from './actions';
import { loadCountry } from './thunks';
import { getCountries } from './selectors';

// import './SearchCountryForm.css';

const SearchCountryFormWrapper = styled.div`
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 0px 2px white;
    background: #212121;
`;

const SearchCountryInput = styled.input`
    font-size: 1rem;
    padding: 8px;
    border: none;
    width: 70%;
    outline: none;
`;

const SearchCountryButton = styled.button`
    font-size: 1rem;
    font-weight: bold;
    padding: 0.5rem;
    border: none;
    outline: none;
    cursor: pointer;
    margin-left: 0.5rem;
    width: 20%;
    background-color: #73b2ff;
    text-transform: uppercase;
`;

const SearchCountryForm = ({ countries = [],  onSubmitPressed }) => { // countries is now automatically made available by connect as prop for the component to use. as it is added to mapStateToProps below
    const [inputCountryCode, setInputCountryCode] = useState(''); // using useState react hook to create a variable inputCountryCode to hold country code data and setInputCountryCode is a fn to set the variable's value

    return (
        <SearchCountryFormWrapper>
            <SearchCountryInput 
                placeholder="Type country code and submit to start tracking"
                value={inputCountryCode}
                onChange={e => setInputCountryCode(e.target.value)} />
            <SearchCountryButton 
                onClick={()=>{
                    const isDuplicateCountry = countries.some(country => country.info.code === inputCountryCode)
                    if(!isDuplicateCountry && inputCountryCode) { // Not Duplicate and Null Check
                        onSubmitPressed(inputCountryCode); // Passing input value to createCountry action creator
                        setInputCountryCode(''); // Clear input value for next use
                    }
                }}
                className="search-country-button">Submit</SearchCountryButton>
        </SearchCountryFormWrapper>
    )
}

const mapStateToProps = (state) => ({
    // countries: state.countries,
    countries: getCountries(state),
});

const mapDispatchToProps = dispatch => ({
    // onSubmitPressed: countryCode => dispatch(createCountry(countryCode)), // onSubmitPressed is the fn our component will use to call createCountry action creator
    onSubmitPressed: countryCode => dispatch(loadCountry(countryCode)),
}); // Fn to map Dispatch to props

export default connect(mapStateToProps, mapDispatchToProps)(SearchCountryForm);
// export default SearchCountryForm;