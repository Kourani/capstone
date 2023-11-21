


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
        <h1 className="shipping">Enter your Payment Information</h1>
        <form className='hiThere' onSubmit={handleSubmit}>


            <label>
                <div className="might"> Name on card <div className="red"> * </div></div>
                <input className="toInput"
                    type="text"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                    required
                />
            </label>

            <label>
                <div className="might"> Card number <div className="red"> * </div></div>
                <input className="toInput"
                    type="text"
                    value={number}
                    onChange={(e)=>setNumber(e.target.value)} 
                />

            </label>

            <label>
                <div className="might"> Expiration date <div className="red"> * </div></div>
                <input className="toInput"
                    type="text"
                    value={expiration}
                    onChange={(e)=>setExpiration(e.target.value)} 
                />
            </label>

            <label>
                <div className="might"> Security code <div className="red"> * </div></div>
                <input className="toInput"
                type="text"
                value={security}
                onChange={(e)=>setSecurity(e.target.value)}
                />
            </label>

            <button className='paymentButton' onClick={()=>{history.push('/cart/thankyou')}}>Review your order</button>
        </form>
        </>
    )
}