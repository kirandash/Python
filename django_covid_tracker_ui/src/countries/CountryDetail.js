import React from 'react';
import styled from 'styled-components';

// import './CountryDetail.css';

const CountryWrapper = styled.div`
    background: ${props => props.isPinned ? '#350000' : '#212121'};
    color: white;
    margin-top: 1rem;
    padding: 1rem;
    position: relative;
    box-shadow: 0 0px 2px white;
`;

const ButtonsWrapper = styled.div`
    margin-top: 1rem;
`;

const ButtonComponent = styled.button`
    font-size: 1rem;
    font-weight: bold;
    padding: 8px;
    border: none;
    outline: none;
    cursor: pointer;
`;

const PinButton = styled(ButtonComponent)`
    display: inline-block;
    background-color: #73b2ff;
`;

const RemoveButton = styled(ButtonComponent)`
    display: inline-block;
    background-color: #e60000;
    margin-left: 8px;
    @media screen and (max-width:767px) {
        background-color: white;
    }
`;

const CountryDetail = ({ country, onRemovePressed, onPin }) => {
    return (
        <CountryWrapper isPinned={country.isPinned}>
            <h3>{country.info.title}</h3>
            <table>
                <thead>
                    <tr>
                        <th>Total Cases</th>
                        <th>Total Recovered</th>
                        <th>Total Deaths</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>{country.total_cases}</td>
                        <td>{country.total_recovered}</td>
                        <td>{country.total_deaths}</td>
                    </tr>
                </tbody>
            </table>
            <ButtonsWrapper>
                {!country.isPinned && <PinButton 
                    onClick={() => onPin(country.info.code)}
                    >
                        Pin Country
                </PinButton>}
                <RemoveButton 
                    onClick={() => onRemovePressed(country.info.code)}
                    >
                        Remove
                </RemoveButton>
            </ButtonsWrapper>
        </CountryWrapper>
    );
};

export default CountryDetail;