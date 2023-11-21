


import "./PaymentReview.css"

import { login } from "../../../store/session";

import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { useHistory } from "react-router-dom";


export default function PaymentReview(){

    const dispatch = useDispatch()
    const history = useHistory()

    const userState = useSelector(state=>state.session.user)

    const [name, setName] = useState()
    const [number, setNumber] = useState()
    const [expiration, setExpiration] = useState()
    const [security, setSecurity] = useState()

    const handleSubmit = async (e) => {
        e.preventDefault()
    }


    return(
        <>
        <h1>Enter your Payment Information</h1>
        <form onSubmit={handleSubmit}>


            <label>
                Name on card
                <input 
                    type="text"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                    required
                />
            </label>

            <label>
                Card number
                <input
                    type="text"
                    value={number}
                    onChange={(e)=>setNumber(e.target.value)} 
                />

            </label>

            <label>
                Expiration date 
                <input
                    type="text"
                    value={expiration}
                    onChange={(e)=>setExpiration(e.target.value)} 
                />
            </label>

            <label>
                Security code
                <input
                type="text"
                value={security}
                onChange={(e)=>setSecurity(e.target.value)}
                />
            </label>

            <button onClick={()=>{history.push('/cart/thankyou')}}>Review your order</button>
        </form>
        </>
    )
}