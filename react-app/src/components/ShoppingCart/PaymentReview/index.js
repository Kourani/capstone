


import "./PaymentReview.css"
import * as additionalFunctions from '../../../context/additional'

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
    const [errors, setErrors] = useState()

    const handleSubmit = async (e) => {
        e.preventDefault()

        let error = {}

        if(!name){
            error['name'] = 'Name is required'
        }

        if(!number){
            error['number'] ='Credit card number is required'
        }

        if(number){
            let num = parseInt(number)

            if(isNaN(num) || number.length < 16 ){
                error['number'] = 'please enter a valid credit card number'
            }
        }

        if(!security){
            error['security'] = 'Security code is required'

        }
        if(security){
            let sec = parseInt(security)

            if(isNaN(sec) || security.length !== 3){
                error['security'] = 'Invalid security code'
            }
        }

        if(!expiration){
            error['expiration'] = 'Expiration date is required'
        }

        setErrors(error)

        let ari = Object.values(error) 

        if(ari.length === 0){
            history.push('/cart/thankyou')
        }
    }


    return(
        <>
        <h1 className="shipping">Enter your Payment Information</h1>
        <p className="sub">we accept all major credit cards
            <div className="cards">
                {additionalFunctions.amex()} 
                {additionalFunctions.mastercard()}
                {additionalFunctions.visa()}
                {additionalFunctions.discover()}
            </div>
        </p>
        <form className='hiThere' onSubmit={handleSubmit}>


            <label>
                <div className="might"> Name on card <div className="red"> * </div></div>
                <input className="toInput"
                    type="text"
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                />
            </label>

            <div className="errorss"> {errors?.name ? errors.name : null}</div>


            <label>
                <div className="might"> Card number <div className="red"> * </div></div>
                <input className="toInput"
                    type="text"
                    value={number}
                    onChange={(e)=>setNumber(e.target.value)} 
                />

            </label>

            <div className="errorss"> {errors?.number ? errors.number : null}</div>


            <label>
                <div className="might"> Expiration date <div className="red"> * </div></div>
                <input className="toInput"
                    type="text"
                    value={expiration}
                    onChange={(e)=>setExpiration(e.target.value)} 
                />
            </label>

            <div className="errorss"> {errors?.expiration ? errors.expiration : null}</div>


            <label>
                <div className="might"> Security code <div className="red"> * </div></div>
                <input className="toInput"
                type="text"
                value={security}
                onChange={(e)=>setSecurity(e.target.value)}
                />
            </label>

            <div className="errorss"> {errors?.security ? errors.security : null}</div>


            <button className='paymentButton'>Review your order</button>
        </form>
        </>
    )
}