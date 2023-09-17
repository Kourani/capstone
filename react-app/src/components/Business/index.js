

import React, { useEffect } from "react";
import { useDispatch } from "react-redux";

import * as businessActions from "../../store/business"


export default function Business(){
    
    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(businessActions.getBusinesses())
    },[dispatch])

    return (
        <h1>SHOPS</h1>
    )
}
