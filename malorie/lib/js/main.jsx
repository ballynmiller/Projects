var $ = require('jquery');
var rDom = require('react-dom');
var React = require('react');

class Portfolio extends React.Component {
    render(){
        return <div>Filler Text</div>;
    }
}

rDom.render(
    <Portfolio />,
    $('#app').get(0)
);
