

import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import * as shopActions from "../../../store/shop"


export default function Shops(){

    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state?.shop)

    function shops(){
        const elementsArray = Object.values(shopState)
        console.log(elementsArray)

        return elementsArray.map(element=>{
            return (
                <button>
                <div>{element?.address} </div>
                </button>
            )
        })
    }


    return (
        <>
        <h1>SHOPS</h1>
        <div>{shops()}</div>
        </>
    )
}
