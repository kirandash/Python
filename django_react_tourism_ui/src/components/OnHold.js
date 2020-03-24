import React, { useState, useEffect } from 'react';
import './OnHold.css';

export default function(props) {
  const [remaining, setRemaining] = useState(props.duration); // useState instead of this.state = 

  useEffect(() => {
    const _timer = setTimeout(() => {
      setRemaining(remaining - 1); // setRemaining instead of this.setState
    }, 1000); // no need to mention setInterval since the useEffect is called every time there is a state change. So it automatically keeps calling it.
    return function cleanup() {
      clearTimeout(_timer);
    }; // called when component unmounts
  }) // Replacement of componentDidMount() and componentWillUnmount

  if (remaining <= 1) {
    return null;
  }

  return (
    <div className="OnHold">
      Your tickets are on hold for the
      next {remaining} seconds.
    </div>
  );
} // This function here is a replacement of the class shown below

export class OnHold extends React.Component {
  constructor(props) {
    super(props);
    this.state = { remaining: props.duration }; // Remaining time for checkokut timer
  }

  componentDidMount() {
    this._timer = setInterval(() => {
      const remaining = this.state.remaining - 1;
      this.setState({ remaining });
    }, 1000); // 1 sec timer
  }

  componentWillUnmount() {
    clearInterval(this._timer); // reset timer on navigating to a different component
  }

  render() {
    const { remaining } = this.state;
    if (remaining <= 1) {
      return null;
    }

    // Message to show whle the countdown is on 
    return (
      <div className="OnHold">
        Your tickets are on hold for the
        next {remaining} seconds.
      </div>
    );
  }
};
