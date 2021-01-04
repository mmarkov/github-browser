import * as actionTypes from '../actionTypes/users';
import { get } from '../utils/api';

export function requestUsers(page) {
  return async dispatch => {
    dispatch({
      type: actionTypes.REQUEST_USERS
    });

    try {
      let request_url = '/api/users';
      if (page) {
        request_url = '/api/users?page=' + page;
      }
      const result = await get(request_url);

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
