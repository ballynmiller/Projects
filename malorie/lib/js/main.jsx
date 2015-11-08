import React from 'react';
var rDom = require('react-dom');

class Test extends React.Component {
    render(){
        return <div>Yes I am Ballyn Sheesh you messing up dawg!</div>;
    }
}

rDom.render(
    <Test />,
    document.getElementById('app')
);
