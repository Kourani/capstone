

import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import * as shopActions from "../../../store/shop"
import "./OneShop.css"


export default function OneShop(){

    const dispatch = useDispatch()
    const {shopId} = useParams()

    useEffect(()=>{
        dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state?.shop)


    function shop(){

        return(
            <>
            <img className="imageAll"
                src={shopState[shopId]?.image}
                alt='Image'
            />
            <div>{shopState[shopId]?.address}</div>
            </>
        )
    }


    return (
        <>
            <div>{shop()}</div>
        </>
    )
}
