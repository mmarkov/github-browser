import React, { PropTypes } from 'react';
import useSheet from 'react-jss';
import UserIcon from '../svg/user.svg';


const User = ({ sheet, user }) => (
  <a href={user.html_url} className="list-group-item">
    <div className="media">
      <div className="media-left">
        {!user.avatar_url &&
        <UserIcon className="media-object" width="64px" height="64px"/>}
        {user.avatar_url && 
        <img className="media-object" width="64px" height="64px" src={user.avatar_url} />
        }
      </div>
      <div className="media-body">
        <h4 className="list-group-item-heading">{user.login}</h4>
        <p className="list-group-item-text">{user.name}</p>
        <p>{user.html_url}</p>
      </div>
    </div>
  </a>
);

const STYLES = {
};

export default useSheet(User, STYLES);