

import "./ProductDetails.css"

import React from "react"
import { useSelector } from "react-redux"
import { useParams } from "react-router-dom"

function ProductDetails(){

    const {productId} = useParams()
    const productState = useSelector(state=>state?.product)

    //explain this function to me
    // function sameShopProducts1(shopId){

    //     return productState?.products?.map(element => {
    //         if(element.shopId === shopId){
    //             console.log('inside the iffff')
    //             console.log(shopId)
    //             return(
    //                 <>
    //                 <div>what is going on ?</div>
    //                     <div>{element?.name}</div>
    //                     <div>{element?.price}</div>
    //                     <div>{element?.category}</div>
    //                 </>
    //             )
    //         }

    //     })

    // }

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
