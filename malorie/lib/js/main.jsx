var $ = require('jquery');
import React, {Component} from 'react';
import {render} from 'react-dom';


class Portfolio extends React.Component {
    render(){
        return <div>Hi</div>;
    }
}

render(<Portfolio />, $('#app').get(0))
