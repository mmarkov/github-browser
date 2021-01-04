import React from 'react';
import useSheet from 'react-jss';
import { connect } from 'react-redux';
import { navigatePage } from '../actions/users';
import Row from 'react-bootstrap/lib/Row';
import Panel from 'react-bootstrap/lib/Panel';
import Pagination from 'react-bootstrap/lib/Pagination';
import User from './User';

const Users = ({ sheet, users, pages, navigatePage }) =>
  <Row>
    <Panel>
      {pages && <Pagination 
        maxButtons={5}
        bsSize="large" 
        activePage={pages.current} 
        items={pages.total}
        prev={true}
        next={true} />
      }
      <div className="list-group">
      	{users.map(user => (
          <User key={user.id} user={user} />
        ))}
      </div>
    </Panel>
  </Row>

const STYLES = {
};

export default connect(
  state => ({ users: state.users, pages: state.pages }),
  { navigatePage }
)(
  useSheet(Users, STYLES)
);