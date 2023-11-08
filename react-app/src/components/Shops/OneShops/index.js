

import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";

import * as shopActions from "../../../store/shop"
import * as productActions from "../../../store/product"
import "./OneShop.css"

import * as favoriteActions from "../../../store/favorite"
import * as additionalFunctions from "../../../context/additional"


export default function OneShop(){

    const dispatch = useDispatch()
    const history = useHistory()
    const {shopId} = useParams()

    useEffect(()=>{
        dispatch(shopActions.getShops())
        dispatch(productActions.getProducts())
    },[dispatch])

    const shopState = useSelector(state=>state?.shop)
    const productState = useSelector(state=>state?.product)
    const userState = useSelector(state=>state?.session)

    const productElements = Object.values(productState)

    const favoriteState = useSelector(state=>state?.favorite)
    const favoriteElements = Object.values(favoriteState)

    useEffect(()=>{
        dispatch(favoriteActions.getFavorites())
    },[dispatch, userState])


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

    function shop(){
        return productElements?.map(element=>{
                if (element.shopId === parseInt(shopId)){
                    let found = favoriteElements?.find(one => one.category === 'Product' && one.number === element.id && one.userId === userState?.user?.id)
                    return(
                        <div className="newestProd">
                        {userState?.user?.id ? <button className="heartStyleProduct" onClick={()=>{heartChangeProduct(element.id, found)}}> { found ? additionalFunctions.heart() : additionalFunctions.plainHeart() } </button> : null }
                            <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
                                <div>
                                    <img className="productImage" src={element?.image} alt="Image" />
                                    <div className="productName">{element?.name}</div>
                                    <div className="productPrice">${element?.price}</div>
                                </div>
                            </button>
                        </div>
                    )
                }
        })
    }


    return (
        <>
            <img className = "imageOneShop" src={shopState[shopId]?.image} alt='Image'/>
            <div className="shopInformation">
                <div>{shopState[shopId]?.name}</div>
                <div>{shopState[shopId]?.address}, {shopState[shopId]?.city}</div>
            </div>
            <div className="allProducts">{shop()}</div>
        </>
    )
}
