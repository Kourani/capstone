import React, { useState, useEffect, useRef } from "react";
import {useHistory} from "react-router-dom"
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import DemoLogin from "../DemoLogin"

import {useModal} from "../../context/Modal"

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory()
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const {closeModal} = useModal()

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());

    history.push('/')
    closeMenu()
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button className='theBarSize' onClick={openMenu}>
        <i className="fa-regular fa-circle-user" />
      </button>
      <div className={ulClassName} ref={ulRef}>
        {user ? (
          <>

            <div className="userInformation">
              <div>Welcome back {user.firstName}</div>
              <div>{user.email}</div>
            </div>

            <div className="userButtons">
              <button className="userNavButton" onClick={()=>{history.push('/profile'); closeMenu()}}> My Profile </button>
              <button className="userNavButton" onClick={()=>{history.push('/favorites'); closeMenu()}}> Favorites </button>
              <button className="userNavButton" onClick={()=>{history.push('/shops/new'); closeMenu()}}>Launch a new shop </button>
              <button className="userNavButton" onClick={()=>{history.push('/shops/edit'); closeMenu()}}>Manage owned shops</button>
              <button className="userNavButton" onClick={handleLogout}>Log Out</button>
            </div>
          </>
        ) : (
          <>


            <OpenModalButton
              buttonText="Log In Demo"
              onItemClick={closeMenu}
              modalComponent={<DemoLogin/>}
            />

            <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />

            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            />

          </>
        )}
      </div>
    </>
  );
}

export default ProfileButton;
