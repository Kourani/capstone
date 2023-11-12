import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import {useHistory} from "react-router-dom";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const history = useHistory();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
        closeModal()
    }
  };

  const errorMap = Object.values(errors)

  function demoUser(){
    const email = 'demo@aa.io'
    const password = 'password'

    dispatch(login(email, password))
    closeModal(false)
    history.push('/')
    return
  }

  return (
    <>

      <form onSubmit={handleSubmit}>
        <div className="modalsInside">
        <h1 className="modalHeader">Log In</h1>
        <label className="labelName">
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>

        <div className="errors"> {errors.email ? errors.email : null}</div>

        <label className="labelName">
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>

        <div className="errors">{errors.password ? errors.password : null}</div>

        <button className='uniButton' type="submit">Log In</button>
        </div>
      </form>

      <button className='uniButton' onClick={()=>demoUser()}>Login as Demo User</button>
    </>
  );
}

export default LoginFormModal;
