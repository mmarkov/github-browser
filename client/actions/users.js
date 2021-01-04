import * as actionTypes from '../actionTypes/users';
import { get } from '../utils/api';

export function requestUsers() {
  return async dispatch => {
    dispatch({
      type: actionTypes.REQUEST_USERS
    });

    try {
      const result = await get('/api/users');

      dispatch({
        type: actionTypes.REQUEST_USERS_SUCCESS,
        users: result.users,
        pages: result.pages
      });
    } catch(e) {
      dispatch({
        type: actionTypes.REQUEST_USERS_ERROR
      });
    }
  }
}

export function navigatePage() {
  return async dispatch => {
    dispatch({
      type: actionTypes.REQUEST_USERS
    });

    try {
      const result = await get('/api/users');

      dispatch({
        type: actionTypes.REQUEST_USERS_SUCCESS,
        users: result.users,
        pages: result.pages
      });
    } catch(e) {
      dispatch({
        type: actionTypes.REQUEST_USERS_ERROR
      });
    }
  }
}
