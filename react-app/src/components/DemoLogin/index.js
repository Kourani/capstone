import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";

function DemoLogin() {
  const dispatch = useDispatch();
  const email = 'demo@aa.io'
  const password = 'password'
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
        closeModal()
  };

  return (
    <>
      <h1>Demo</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Email
          <input
            type="text"
            value={email}
            required
          />
        </label>
        <label>
          Password
          <input
            type="password"
            value={password}
            required
          />
        </label>
        <button type="submit">Log In Demo</button>
      </form>
    </>
  );
}

export default DemoLogin;
