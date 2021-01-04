import React, { Component } from 'react';
import useSheet from 'react-jss';
import Users from '../components/Users';
import { connect } from 'react-redux';
import { requestUsers } from '../actions/users';
import Navbar from 'react-bootstrap/lib/Navbar';
import Nav from 'react-bootstrap/lib/Nav';
import NavItem from 'react-bootstrap/lib/NavItem';

export class Index extends Component {
  componentDidMount() {
    this.props.requestUsers();
  }

  render() {
    const { sheet } = this.props;

    return (
      <div className={sheet.classes.index}>
          <Navbar bsStyle="inverse">
            <Navbar.Header>
              <Navbar.Brand>
                <a href="#">Github Users</a>
              </Navbar.Brand>
            </Navbar.Header>
            <Nav pullRight>
              <NavItem href="https://github.com/mmarkov/github-browser">
                Open on Github
              </NavItem>
            </Nav>  
          </Navbar>
          <div className="container">
            <Users />
          </div>
      </div>
      
    );
  }
}

const STYLES = {
};

export default connect(
  () => ({}),
  { requestUsers }
)(
  useSheet(Index, STYLES)
);
