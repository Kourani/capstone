
import "./AllProducts.css";
import * as productActions from "../../../store/product"

import React, { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from 'react-router-dom'


export default function Products(){

    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState = useSelector(state=>state.product)


    // function productDetails(id){
    //     history.push(`/products/${id}`)
    //     return
    // }

    // onClick={productDetails(element.id)}

    //explain it to me please
    function allProducts(){
        return productState?.products?.map(element=>{
            return (
                <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
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
