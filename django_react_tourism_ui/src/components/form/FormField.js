import React from 'react';
import './FormField.css';
import { useValidation } from './FieldValidation';

export function FormField(props) {
  // Form Field class to create form field in Checkout.js
  const { name, label, value, onUpdate } = props;
  const onChange = (event) => {
    onUpdate(name, event.target.value);
  };
  return (
    <div key={name} className="FormField">
      <label>{label}</label>
      <br/>
      <input type="text" name={name} value={value} onChange={onChange} />
    </div>
  );
}

export function FormFieldUsingHooks(props) {
  const [ErrorDisplay, validate] = useValidation();
  const { name, label, value } = props;
  const onChange = (event) => {
    validate(event);
    props.onUpdate(name, event.target.value);
  };
  return (
    <div key={name} className="FormField">
      <label>{label}</label>
      <br/>
      <input type="text" name={name} value={value} onChange={onChange} />
      <ErrorDisplay />
    </div>
  );
}
