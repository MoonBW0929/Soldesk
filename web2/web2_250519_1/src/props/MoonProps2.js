import React from 'react'
import PropTypes from 'prop-types'

const MoonProps2 = (props) => {

  return (
    <div>
        <h3>{props.name}</h3>
        <h3>{props.age}</h3>
    </div>
  );
};

MoonProps2.prototype = {
  name : PropTypes.string,
  price : PropTypes.number
}

export default MoonProps2;