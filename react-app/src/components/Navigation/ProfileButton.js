import React, { useState, useEffect, useRef } from "react";
import {useHistory} from "react-router-dom"
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import DemoLogin from "../DemoLogin"

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory()
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

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
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button onClick={openMenu}>
        <i className="fas fa-user-circle" />
      </button>
      <div className={ulClassName} ref={ulRef}>
        {user ? (
          <>

            <div>{user.username}</div>
            <div>{user.email}</div>
            <button onClick={()=>{history.push('/shops/new')}}>Create Shop</button>
            <button onClick={()=>{history.push('/shops/edit')}}>Manage Shops</button>
            <button onClick={handleLogout}>Log Out</button>

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
