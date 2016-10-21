var $ = require('jquery');
import React, {Component} from 'react';
import {render} from 'react-dom';
import {browserHistory, Route, Router, Link} from 'react-router';

import Navigation from './components/navigation';
import Slideshow from './components/slideshow';

class App extends React.Component {
    render(){
        return (
            <div>
                <h3>Home</h3>
                <ul>
                    <li><Link to="/test">Test</Link></li>
                </ul>
            </div>
        );
    }
}

class Test extends React.Component {
    render() {
        return <h3>Test</h3>;
    }
}

render((
    <Router history={browserHistory}>
        <Route path="/" component={App}>
            <Route path="test" component={Test} />
        </Route>
    </Router>
), $('#app').get(0));
