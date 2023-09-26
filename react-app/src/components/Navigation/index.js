import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import * as additionalFunctions from '../../context/additional'
import './Navigation.css';



function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);


	console.log(additionalFunctions.shoppingCart(),'aaaaaaaaaaaaaaaaaaaaaaaaaa')

	return (
		<div className='NavBar'>
			<div className='NavCartHome'>
				<NavLink className='Home' exact to="/">Interact</NavLink>
				<NavLink className='Cart' exact to="/cart"> {additionalFunctions.shoppingCart()}</NavLink>
			</div>
			{isLoaded && (
				<>
					<ProfileButton user={sessionUser} />
				</>
			)}
		</div>
	);
}

export default Navigation;
