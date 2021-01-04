import * as actionTypes from '../actionTypes/users';

const DEFAULT_STATE = [];

const requestUsers = (state, action) => ([
  ...action.users
]);

const requestPages = (state, action) => (action.pages);

export default function users(state = DEFAULT_STATE, action) {
  return ({
    [actionTypes.REQUEST_USERS_SUCCESS]: requestUsers
  }[action.type] || (s => s))(state, action);
}

export function pages(state = DEFAULT_STATE, action) {
  return ({
    [actionTypes.REQUEST_USERS_SUCCESS]: requestPages
  }[action.type] || (s => s))(state, action);
}
