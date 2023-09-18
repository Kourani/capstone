import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

import { shoppingCart } from '../../context/help';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);



	return (
		<ul>
			<li>
				<NavLink exact to="/">Interact</NavLink>
				<NavLink exact to="/cart"> cart </NavLink>
			</li>
			
			{isLoaded && (
				<li>
					<ProfileButton user={sessionUser} />
				</li>
			)}
		</ul>
	);
}

export default Navigation;
