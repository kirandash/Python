import React from 'react';
import './Checkout.css';
import { AppContext } from '../AppContext';
import OnHold from '../components/OnHold';
import { FormField, FormFieldUsingHooks } from '../components/form/FormField';
import { withFieldValidation } from '../components/form/FieldValidation';
import { FaMinusCircle } from 'react-icons/fa';

const ValidatedField = withFieldValidation(FormField);

export default class Checkout extends React.Component {
  static contextType = AppContext;

  constructor(props) {
    super(props);
    this.state = { validationErrors: [], orderPlaced: false }; // to check if order is placed or not and validation errors array to contain all validationErros messages
  }

  placeOrder() {
    // place order method
    this.context.placeOrder().then(() => {
      this.setState({ validationErrors: [], orderPlaced: true }); // If successful, set orderPlaced as true and remove validationErrors
    }).catch((validationErrors) => {
      this.setState({ validationErrors, orderPlaced: false }); // If error, set orderPlaced as false and add validationErrors
    });
  }

  render() {
    const { booking, item, updateField, clearOrderItem } = this.context; // data from context required for form
    const { validationErrors, orderPlaced } = this.state;
    const inputFields = [
      { label: 'Name', name: 'name' },
      { label: 'Email Address', name: 'email_address' },
      { label: 'Street Address', name: 'street_address' },
      { label: 'City', name: 'city' },
    ]; // input fields for Form

    // Extract errors and build list of errors to add in render
    const errors = [];
    inputFields.forEach((field) => {
      const error = validationErrors[field.name] 
      if (error) {
        errors.push(<li className="error" key={field.name}>{field.label}: {error}</li>);
      }
    });

    // const formFields = inputFields.map((fieldProps) => {
    //   return (
    //     <FormField
    //       key={fieldProps.name}
    //       value={booking[fieldProps.name]}
    //       onUpdate={updateField}
    //       {...fieldProps}
    //     />
    //   );
    // });

    // Fields to show on Form
    const formFields = inputFields.map((fieldProps) => {
      return (
        <ValidatedField
          key={fieldProps.name}
          value={booking[fieldProps.name]}
          onUpdate={updateField}
          {...fieldProps}
        />
      );
    });

    // const formFields = inputFields.map((fieldProps) => {
    //   return (
    //     <FormFieldUsingHooks
    //       key={fieldProps.name}
    //       value={booking[fieldProps.name]}
    //       onUpdate={updateField}
    //       {...fieldProps}
    //     />
    //   );
    // });
    
    // Check if order is placed
    if (orderPlaced) {
      return (
        <section className="Checkout">
          <header className="Checkout-header">
            <h2>Checkout</h2>
            <h3>Thanks for buying an excursion with Explore California!</h3>
          </header>
        </section>
      );
    }

    // If there is an item added to checkout. Show remove button
    let displayItem;
    if (item) {
      displayItem = (
        <div>
            <button className="Checkout-package-remove"
              onClick={() => clearOrderItem(item.id)}>
              <FaMinusCircle />
            </button>
            {item.name} - ${item.price} starts on {item.start} for {item.tour_length} days.
          </div>
      );
    }
    return (
      <section className="Checkout">
        <header className="Checkout-header">
          <h2>Checkout</h2>
        </header>
        <section className="Checkout-summary">
          {displayItem}
        </section>
        <section className="Checkout-form">
          <form>
            <ul>
              {errors} {/* List of Errors from API response */}
            </ul>
            {formFields}
          </form>
        </section>
        <section className="Checkout-actions">
          <div className="Checkout-actions__next">
            <button disabled={orderPlaced || item === null}
              onClick={this.placeOrder.bind(this)}>
                Place order
            </button>{/* on click place the order and disable the button if order is placed or if there is no item in cart */}
          </div>
        </section>
      </section>
    );
  }
};
