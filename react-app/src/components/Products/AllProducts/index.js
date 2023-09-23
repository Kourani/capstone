
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
    const productElements = Object.values(productState)



    function allProducts(){
        return productElements.map(element=>{
            return (
                <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
                    <div>
                        <img className="productImage"
                            src={element?.image ? element?.image : "https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg"}
                            alt="Image"
                        />
                        <div className="productName"> {element?.name} </div>
                        <div className="productPrice"> ${element?.price} </div>
                        <div className="productCategory"> {element?.category} </div>
                    </div>
                </button>
            )
        })
    }

    return (
        <>
        <button onClick={()=>history.push('shops/new')}>Create Shop</button>

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
