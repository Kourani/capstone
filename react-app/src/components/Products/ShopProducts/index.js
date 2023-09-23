

import React, {useEffect} from "react";
import { useDispatch, useSelector } from "react-redux";


import { useModal } from "../../../context/Modal"

import * as productActions from "../../../store/product"
import { useHistory, useParams } from "react-router-dom";

function ShopProducts(){


    const dispatch = useDispatch()
    const history = useHistory()
    const {shopId} = useParams()
    const {closeModal} = useModal()

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState = useSelector(state=>state.product)
    const productElements = Object.values(productState)

    function findProducts(){
        return productElements.map(element=>{
            if(element.shopId === parseInt(shopId)){
                return(
                    <div className="ownedProducts">
                    <div> {element.name} </div>
                    <div> {element.description} </div>
                    <div> {element.category} </div>
                    <div> {element.price} </div>

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
