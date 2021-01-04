import { combineReducers } from 'redux';
import users from './users';
import { pages } from './users';

const reducers = combineReducers({
  users,
  pages
});

export default reducers;
