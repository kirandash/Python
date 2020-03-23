import React from 'react';
import './Pagination.css';

export default function Pagination(props) {
  const { pageIndex, total, perPage, onNext, onPrevious } = props; // Current pageIndex, total packages, packages per page, next and prev page callbacks
  const lastPage = Math.ceil(total / perPage); // calculate last page
  const previous = pageIndex > 1 ? (<button onClick={onPrevious}>Previous</button>) : null; // whether to display prev btn
  const next = pageIndex < lastPage ? (<button onClick={onNext}>Next</button>) : null;
  return (
    <div className="Pagination">
      <div className="Pagination-actions">
        {previous}
        {next}
      </div>
      <div className="Pagination-stats">
        Page {pageIndex} of {lastPage}
        &nbsp;(displaying {perPage} items per page)
      </div>
    </div>
  )
}
