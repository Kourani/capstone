
import "./Products.css";

import React, { useEffect } from "react"

import * as productActions from "../../store/product"

import { useDispatch } from "react-redux"

import { useSelector } from "react-redux"


export default function Products(){

    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState = useSelector(state=>state.product)

    console.log(productState,'hello')
    console.log(productState?.products,'hello!!!!!!!!!!!!!!!!!!!!!!!!')

    function allProducts(){
        return productState?.products?.map(element=>{
            return (
                <button className="product">
                    <div className="productName"> {element?.name} </div>
                    <div className="productPrice"> {element?.price} </div>
                    <div className="productCategory"> {element?.category} </div>
                </button>
            )
        })
    }

    return (
        <>
        <p> Fresh finds fit for cozy season </p>
        <p> Popular gifts right now </p>

            <div className="allProducts"> {allProducts()} </div>

        <p> Design Ideas and Inspiration </p>
        <p> Shop the look </p>
        <p> Select a shop to feature </p>
        <p> Shop our selections </p>
        <p> Discover shops in the US </p>
        <p> Fresh from the blog </p>
        </>
    )
}
