

import "./CircleProducts.css"

import React, {useEffect, useState, useRef} from "react";
import { useDispatch, useSelector } from "react-redux";
import {useParams, useHistory } from "react-router-dom";

import * as productActions from "../../../store/product";
import additional from "../../../context/additional"




export default function CircleProducts(){
    const dispatch = useDispatch()
    const history = useHistory()
    const {category} = useParams()


    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState = useSelector(state=>state.product)
    const productElements = Object.values(productState)

    function foundProducts(){
        return productElements?.map(element=>{
            if(element?.category === category){
                return(
                    <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
                        <div>
                            <img className='productImage' src={element?.image} alt="Image"/>
                            <div className="productName"> {element?.name} </div>
                            <div className="productPrice"> ${element?.price} </div>
                        </div>
                    </button>
                )
            }
        })

    }



    return (
        <>
        <div className="allProducts"> {foundProducts() ? foundProducts() : additional.futureWork()}</div>
        </>
    )

}
