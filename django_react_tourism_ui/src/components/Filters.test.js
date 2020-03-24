import React from 'react';
import { render, cleanup, fireEvent } from '@testing-library/react';

import Filters from './Filters';

afterEach(cleanup); // after each test cleanup the DOM and unmount the React component

it('updates filter', async (done) => {
  let callback = (filters) => {
    expect(filters).toEqual({
      price_min: '123.45',
      price_max: '',
      search: ''
    });
    done(); // call done() to tell React that test has finished running
  };
  const filters = render(
    <Filters onFilterUpdate={callback} />
  );

  expect(filters.queryByText('Price')).toBeDefined(); // Check Label Price to be present
  const priceMin = filters.queryByPlaceholderText('Minimum'); // get input with Minimum placeholder
  expect(priceMin.getAttribute('value')).toEqual(''); // price min value should be empty in the beginning

  fireEvent.change(priceMin, { target: { value: '123.45' }}); // fire a change event to change minimum price
  expect(priceMin.getAttribute('value')).toEqual('123.45'); // confirm if the fire event worked and field value has changed or not

  fireEvent.click(filters.queryByText('Apply')); // check if Apply btn is working
});

