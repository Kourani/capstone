

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
        dispatch(shopActions.getShops())
        dispatch(productActions.getProducts())
    },[dispatch])

    const shopState = useSelector(state=>state?.shop)
    const productState = useSelector(state=>state?.product)
    const productElements = Object.values(productState)

    function shop(){
        return productElements?.map(element=>{
                if (element.shopId === parseInt(shopId)){

                    return(
                        <>
                            <button className="product">
                                <img className="productImage" src={element?.image} alt="Image" />
                                <div className="productName">{element?.name}</div>
                                <div className="productPrice">{element?.price}</div>
                            </button>
                        </>
                    )
                }
        })
    }


    return (
        <>
            <img className = "imageOneShop" src={shopState[shopId]?.image} alt='Image'/>
            <div className="shopInformation">
                <div>{shopState[shopId]?.name}</div>
                <div>{shopState[shopId]?.address}, {shopState[shopId]?.city}</div>
            </div>
            <div className="allProducts">{shop()}</div>
        </>
    )
}
