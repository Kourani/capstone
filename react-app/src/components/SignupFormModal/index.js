import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			const data = await dispatch(signUp(username, email, password));

			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors({"password":"Confirm Password field must be the same as the Password field"});
		}
	};

	return (
		<>


			<form onSubmit={handleSubmit}>
			<div className="modalsInside">
			<h1 className="modalHeader">Sign Up</h1>
				<label className="labelName">
					Email
					<input
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</label>

				<div className="errors">{errors?.email ? errors?.email : null}</div>

				<label className="labelName">
					Username
					<input
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>

				<div className="errors">{errors?.username ? errors?.username : null}</div>

				<label className="labelName">
					Password
					<input
						type="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>

				<label className="labelName">
					Confirm Password
					<input
						type="password"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>

				<div className="errors">{errors?.password ? errors?.password : null}</div>

				<button className='uniButton' type="submit">Sign Up</button>
				</div>
			</form>
		</>
	);
}

export default SignupFormModal;
