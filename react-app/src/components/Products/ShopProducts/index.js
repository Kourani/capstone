

import React, {useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom"

import { useModal } from "../../../context/Modal"

import * as productActions from "../../../store/product"
import { useHistory } from "react-router-dom";

function ShopProducts(){


    const dispatch = useDispatch()
    const history = useHistory()
    const {shopId} = useParams()

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState = useSelector(state=>state.product)

    function findProducts(){
        return productState?.products?.map(element=>{
            if(element.shopId === parseInt(shopId)){
                return(
                    <div>
                    <div> {element.name} </div>
                    <div> {element.price} </div>
                    <div> {element.description} </div>
                    <button onClick={()=>history.push(`/shops/${shopId}/products/${element.id}/edit`)}> Edit Product </button>
                    <button> Delete Product </button>
                    </div>
                )
            }
        })

    }

    return (
        <>
        {findProducts()}
        </>
    )

}

export default ShopProducts
