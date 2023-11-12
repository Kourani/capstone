import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
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

        <button type="submit">Log In</button>

        </div>
      </form>
    </>
  );
}

export default LoginFormModal;
