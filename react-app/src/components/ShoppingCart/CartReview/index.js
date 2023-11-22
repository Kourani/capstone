

import "./CartReview.css"


import { login } from "../../../store/session";
import { countries } from "../../../context/additional";

import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { useHistory } from "react-router-dom";


export default function CartReview(){

    const dispatch = useDispatch()
    const history = useHistory()

    const userState = useSelector(state=>state.session.user)
    
    const [country, setCountry] = useState('Select a country')
    const [state, setState] = useState('')
    const [city, setCity] = useState('')
    const [streetAddress, setStreetAddress] = useState('')

    const [name, setName] = useState('')
    const [other, setOther] = useState('')
    const [zipCode, setZipCode] = useState()
    const [phoneNumber, setPhoneNumber] = useState()

    const [errors, setErrors] = useState()

    const payload = {
        country,
        state,
        city,
        address:streetAddress,
    }

    const handleSubmit = async (e) => {
        
        e.preventDefault()
        let error = {}

        if( zipCode && (zipCode.length !== 5 ) ){
            error['zipCode'] = 'Please enter a valid Zip Code'
        }

        if(phoneNumber){
            let num = parseInt(phoneNumber)

            if(isNaN(num)){
                error['phoneNumber'] = 'Phone number must consist entirely of numbers'
            }
            else if(typeof(num) === 'number' && !isNaN(num)){
                error['phoneNumber'] = 'Please enter a valid phone number'
            }
            
        }
        
        if (name.length <=2 ){
            error['name'] = 'Must be greater than 2 characters long'
        }

        if(!city){
            error['city'] = 'City is required'
        }

        if(city.length < 3){
            error['city'] = 'Please enter the full city name no abbreviations'
        }

        if(!state){
            error['state'] = 'State is required'
        }

        if(state.length < 3){
            error['state'] = 'Please enter the full state name no abbreviations'
        }

        if(country === 'Select a country'){
            error['country'] = 'Country is required'
        }

        if(!streetAddress){
            error['streetAddress'] = 'Street Address is required'
        }

        setErrors(error)

        let ari = Object.keys(error)

        if(ari.length === 0){
            history.push('/cart/review/payment')
        }
     
    }


    return(
        <>
            <h1 className="shipping">Enter your Shipping Address</h1>
            
            <form className='hiThere' onSubmit={handleSubmit}>

                <label>
                    <div className="might"> Name <div className="red"> * </div></div>
                    <input className="toInput"
                        type='text'
                        value={name}
                        onChange={(e)=>setName(e.target.value)}
                    />
                </label>

                <div className="errorss"> {errors?.name ? errors.name : null}</div>

            

                <label>
                    <div className="might"> Phone Number <div className="grey"> (optional) </div></div>
                    <input className="toInput"
                        type='text'
                        value={phoneNumber}
                        onChange={(e)=>setPhoneNumber(e.target.value)}
                    />
                </label>

                <div className="errorss"> {errors?.phoneNumber ? errors.phoneNumber : null}</div>

                <label className="toShip">
                    <div className="might">Country <div className="red">*</div></div>
                    <select
                        className="toInput"
                        value={country}
                        onChange={(e) => setCountry(e.target.value)}
                    >
                        <option value="">Select a country</option>
                        {countries.map((countryName, index) => (
                        <option key={index} value={countryName}>{countryName}</option>
                        ))}
                    </select>
                </label>

                <div className="errorss"> {errors?.country ? errors.country : null}</div>
                

            <div className="allThree">
                <label className="toShip">
                    <div className="might">  State <div className="red"> *</div></div>
                    <input className="toInput"
                        type="text"
                        value={state}
                        onChange={(e)=>setState(e.target.value)} 
                    />

                </label>

                <div className="specErrors"> {errors?.state ? errors.state : null}</div>

                <label className="toShip">
                    <div className="might"> City <div className="red"> *</div></div>
                    <input className="toInput"
                        type="text"
                        value={city}
                        onChange={(e)=>setCity(e.target.value)} 
                    />
                </label>

                
                <div className="specErrors"> {errors?.city ? errors.city : null}</div>


                
                <label>
                    <div className="might"> Zip Code <div className="grey"></div></div>
                    <input className="toInput"
                        type='text'
                        value={zipCode}
                        onChange={(e)=>setZipCode(e.target.value)}
                    />
                </label>

                
                <div className="specErrors"> {errors?.zipCode ? errors.zipCode : null}</div>

            </div>

                <label className="toShip">
                    <div className="might"> Street Address <div className="red"> *</div></div>
                    <input className="toInput"
                    type="text"
                    value={streetAddress}
                    onChange={(e)=>setStreetAddress(e.target.value)}
                    />
                </label>

                <div className="errorss"> {errors?.streetAddress ? errors.streetAddress : null}</div>

                <label>
                    <div className="might"> Apt/Suite/Other <div className="grey"> (optional) </div></div>
                    <input className="toInput"
                        type='text'
                        value={other}
                        onChange={(e)=>setOther(e.target.value)}
                    />
                </label>

                <div className="errorss"> {errors?.other ? errors.other : null}</div>

                <button className = 'paymentButton'>Continue to Payment</button>
            </form>   
        </>
    )
}