

import "./ProductDetails.css"

import React from "react"
import { useSelector } from "react-redux"
import { useParams } from "react-router-dom"

function ProductDetails(){

    const {productId} = useParams()

    const productState = useSelector(state=>state?.product)

    function productDetails(){
        const foundProduct = productState?.products?.find(element=>element.id=== parseInt(productId))
        return(
            <>
            <div>{foundProduct?.price}</div>
            <div>{foundProduct?.description}</div>
            </>
        )
    }

    return(
        <>
        {productDetails()}
        <button>Add to Cart </button>

        <p>More from this Shop</p>

        </>
    )
}

export default ProductDetails
