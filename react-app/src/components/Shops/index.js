

import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import * as shopActions from "../../store/shop"


export default function Shops(){

    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state?.shop)


    console.log(shopState,'WELCOME!')

    console.log(shopState?.businesses, 'todo!!!!!!!!!!!!!!!!!!!!')


    return (
        <>
        <h1>SHOPS</h1>
        </>
    )
}
