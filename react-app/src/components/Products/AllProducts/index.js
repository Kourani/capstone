
import "./AllProducts.css";
import * as productActions from "../../../store/product"
import * as shopActions from "../../../store/shop"
import * as favoriteActions from "../../../store/favorite"

import * as additionalFunctions from "../../../context/additional"

import React, { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from 'react-router-dom'


export default function Products(){

    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(()=>{
        dispatch(productActions.getProducts())
        dispatch(shopActions.getShops())
    },[dispatch])



    const productState = useSelector(state=>state.product)
    const shopState = useSelector(state=>state.shop)
    const favoriteState = useSelector(state=>state.favorite)
    const userState = useSelector(state=>state.session)

    const productElements = Object.values(productState)
    const shopElements = Object.values(shopState)
    const favoriteElements = Object.values(favoriteState)


    useEffect(()=>{
        dispatch(favoriteActions.getFavorites())
    },[dispatch, userState])

    
    function allProducts(){
        let count = 0
        return productElements?.map(element=>{
            count ++

                if(count<6){

                return (
                <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
                    <div>
                        <img className="productImage"
                            src={element?.image ? element?.image : "https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg"}
                            alt="Image"
                        />
                        <div className="productName"> {element?.name} </div>
                        <div className="productPrice"> ${element?.price} </div>
                    </div>
                </button>
            )
            }
        })
    }


    function heartChange(theShopId, favoriteElement){


        if(!favoriteElement){
            const payload={
                category:'Shop',
                number:theShopId,
                userId:userState?.user?.id
            }
            dispatch(favoriteActions.addFavorite(payload))
        }

        if(favoriteElement){
            if(favoriteElement)
            dispatch(favoriteActions.deleteFavorite(favoriteElement.id))
        }

    }

    function shops(){
        let count = 0
        return shopElements?.map(element=>{

            if(element?.country === 'United States')
            {
                count++
                if(count<5){

                    let found = favoriteElements?.find(one => one.category === 'Shop' && one.number === element.id && one.userId === userState?.user?.id)

                    return(
                        <div>
                            {userState?.user?.id ? <button className="heartStyle" onClick={()=>{heartChange(element.id, found)}}> { found ? additionalFunctions.heart() : additionalFunctions.plainHeart() } </button> : null }
                            <button className= "landingShopsButton" onClick={()=>{history.push(`/shops/${element.id}`)}}>
                                <img className="landingShopsInside" src={element?.image} alt="Image"/>
                                <p className="landingShopName">{element?.name}</p>
                            </button>
                        </div>
                    )

                }

            }
        })
    }

    return (
        <>
        <p className='headersProductDetails' > Fresh finds fit for cozy season </p>
        <div className="roundImagesDiv">
            <button className="roundImagesButton" onClick={()=>{history.push('/products/categories/sweets')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg" alt="Image"/>
                <p>Sweets</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/categories/books')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/1290141/pexels-photo-1290141.jpeg" alt="Image"/>
                <p>Books</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/categories/watches')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/190819/pexels-photo-190819.jpeg" alt="Image"/>
                <p>Watches</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/categories/ceramics')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/4207892/pexels-photo-4207892.jpeg" alt="Image"/>
                <p>Ceramics</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/categories/tools')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/5691629/pexels-photo-5691629.jpeg" alt="Image"/>
                <p>Tools</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/categories/jewelry')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/4595723/pexels-photo-4595723.jpeg" alt="Image"/>
                <p>Jewelry</p>
            </button>
        </div>
        <p className='headersProductDetails'> Popular gifts right now </p>

            <div className="allProducts"> {allProducts()} </div>

        <div className='landingShops'>
        <button className='headersProductDetailsLanding' onClick={()=>{history.push('/usshops')}}>Discover shops in the US </button>
            {shops()}
        </div>
        </>
    )
}
