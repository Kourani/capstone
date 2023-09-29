
import "./AllProducts.css";
import * as productActions from "../../../store/product"
import * as shopActions from "../../../store/shop"

import React, { useEffect } from "react"
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
    const productElements = Object.values(productState)
    const shopElements = Object.values(shopState)



    function allProducts(){
        return productElements?.map(element=>{
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
        })
    }

    function shops(){
        let count = 0
        return shopElements?.map(element=>{
            if(element?.country === 'United States')
            {
                count++
                if(count<5){
                    return(
                        <button onClick={()=>{history.push(`/shops/${element.id}`)}}>
                            <img className="allLanding" src={element?.image} alt="Image"/>
                            <p>{element?.name}</p>
                        </button>
                    )

                }

            }
        })
    }

    return (
        <>
        <p className='headersProductDetails' > Fresh finds fit for cozy season </p>
        <div className="roundImagesDiv">
            <button className="roundImagesButton" onClick={()=>{history.push('/products/toys')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg" alt="Image"/>
                <p>Toys</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/books')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg" alt="Image"/>
                <p>Books</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/trinkets')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg" alt="Image"/>
                <p>Trinkets</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/ceramics')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg" alt="Image"/>
                <p>Ceramics</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/tools')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg" alt="Image"/>
                <p>Tools</p>
            </button>

            <button className="roundImagesButton" onClick={()=>{history.push('/products/jewelry')}}>
                <img className="roundImages" src="https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg" alt="Image"/>
                <p>Jewelry</p>
            </button>
        </div>
        <p className='headersProductDetails'> Popular gifts right now </p>

            <div className="allProducts"> {allProducts()} </div>

        <div className='landingShops'>
            <button className='headersProductDetails' > Discover shops in the US </button>
            {shops()}
        </div>

        </>
    )
}
