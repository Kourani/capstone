

import "./CartReview.css"


import { login } from "../../../store/session";

import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { useHistory } from "react-router-dom";


export default function CartReview(){

    const dispatch = useDispatch()
    const history = useHistory()

    const userState = useSelector(state=>state.session.user)
    
    const [country, setCountry] = useState()
    const [state, setState] = useState()
    const [city, setCity] = useState()
    const [streetAddress, setStreetAddress] = useState()

    const [name, setName] = useState()
    const [other, setOther] = useState()
    const [zipCode, setZipCode] = useState()
    const [phoneNumber, setPhoneNumber] = useState()

    const payload = {
        country,
        state,
        city,
        address:streetAddress,
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data = await dispatch(login(payload))
    }


    return(
        <>
        <h1>Enter your Shipping Address</h1>
        <form onSubmit={handleSubmit}>


            <label>
                Country 
                <input 
                    type="text"
                    value={country}
                    onChange={(e)=>setCountry(e.target.value)}
                    required
                />
            </label>

            <label>
                State 
                <input
                    type="text"
                    value={state}
                    onChange={(e)=>setState(e.target.value)} 
                />

            </label>

            <label>
                City 
                <input
                    type="text"
                    value={city}
                    onChange={(e)=>setCity(e.target.value)} 
                />
            </label>

            <label>
                Street Address
                <input
                type="text"
                value={streetAddress}
                onChange={(e)=>setStreetAddress(e.target.value)}
                />
            </label>

            <button onClick={()=>{history.push('/cart/review/payment')}}>Continue to Payment</button>
        </form>
        </>
    )
}