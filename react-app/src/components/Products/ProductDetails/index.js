

import "./ProductDetails.css"

import React from "react"
import { useSelector } from "react-redux"
import { useParams } from "react-router-dom"

function ProductDetails(){

    const {productId} = useParams()
    const productState = useSelector(state=>state?.product)



    let shopId
    console.log(shopId,'before the function')
    function productDetails(){
        const foundProduct = productState?.products?.find(element=>element.id === parseInt(productId))
        shopId = foundProduct.shopId
        console.log(shopId, 'inside the function')
        return(
            <>
            <div>{foundProduct?.price}</div>
            <div>{foundProduct?.description}</div>
            </>
        )
    }

    productDetails()
    console.log(shopId,'after the function')



    return(
        <>
        {productDetails()}
        <button>Add to Cart </button>

        <p>More from this Shop</p>
        </>
    )
}

export default ProductDetails
