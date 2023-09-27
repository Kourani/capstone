

import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import * as shopActions from "../../../store/shop"
import * as productActions from "../../../store/product"
import "./OneShop.css"


export default function OneShop(){

    const dispatch = useDispatch()
    const {shopId} = useParams()

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState = useSelector(state=>state?.product)
    const productElements = Object.values(productState)

    function shop(){
        return productElements?.map(element=>{
                if (element.shopId === parseInt(shopId)){

                    return(
                        <>
                            <img className="productImageOneShop" src={element?.image} alt="Image" />
                            <div>{element?.name}</div>
                            <div>{element?.price}</div>
                        </>
                    )
                }
        })
    }


    return (
        <>
            <div>{shop()}</div>
        </>
    )
}
