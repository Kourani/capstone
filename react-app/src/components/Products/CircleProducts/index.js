

import "./CircleProducts.css"

import React, {useEffect, useState, useRef} from "react";
import { useDispatch, useSelector } from "react-redux";
import {useParams, useHistory } from "react-router-dom";

import * as productActions from "../../../store/product";
import * as favoriteActions from "../../../store/favorite"
import additional from "../../../context/additional"
import * as additionalFunctions from "../../../context/additional"




export default function CircleProducts(){
    const dispatch = useDispatch()
    const history = useHistory()
    const {category} = useParams()


    useEffect(()=>{
        dispatch(productActions.getProducts())
        dispatch(favoriteActions.getFavorites())
    },[dispatch])

    const productState = useSelector(state=>state.product)
    const favoriteState = useSelector(state=>state?.favorite)
    const userState = useSelector(state=>state?.session)

    const productElements = Object.values(productState)
    const favoriteElements = Object.values(favoriteState)

    function heartChangeProduct(theProductId, favoriteElement){
        if(!favoriteElement){
            const payload={
                category:'Product',
                number:theProductId,
                userId:userState?.user?.id
            }
            dispatch(favoriteActions.addFavorite(payload))
        }

        if(favoriteElement){
            if(favoriteElement)
            dispatch(favoriteActions.deleteFavorite(favoriteElement.id))
        }

    }

    function foundProducts(){
        return productElements?.map(element=>{
            if(element?.category === category){
                let found = favoriteElements?.find(one => one.category === 'Product' && one.number === element.id && one.userId === userState?.user?.id)
                return(
                    <div className="newestProd">
                    {userState?.user?.id ? <button className="heartStyleProduct" onClick={()=>{heartChangeProduct(element.id, found)}}> { found ? additionalFunctions.heart() : additionalFunctions.plainHeart() } </button> : null }
                    <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
                        <div>
                            <img className='productImage' src={element?.image} alt="Image"/>
                            <div className="productName"> {element?.name} </div>
                            <div className="productPrice"> ${element?.price} </div>
                        </div>
                    </button>
                    </div>
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
