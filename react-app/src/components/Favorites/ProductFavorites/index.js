

import react, { useEffect, useState } from "react"
import {useDispatch, useSelector} from 'react-redux'


import * as favoriteActions from '../../../store/favorite'
import * as productActions from '../../../store/product'
import * as shopActions from '../../../store/shop'
import { useHistory } from "react-router-dom/cjs/react-router-dom.min"


export default function ProductFavorites(){

    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(()=>{
        dispatch(favoriteActions.getFavorites())
        dispatch(shopActions.getShops())
        dispatch(productActions.getProducts())
    },[dispatch])

    const favoriteState = useSelector(state=>state.favorite)
    const userState = useSelector(state=>state.session)
    const shopState = useSelector(state=>state.shop)
    const productState = useSelector(state=>state.product)
    const favoriteElements = Object.values(favoriteState)

    console.log(favoriteState,'favoriteState!!!!!!!1')

    function userFavorites(){
        return favoriteElements?.map(element =>{

            if(element.userId === userState?.user?.id){

                if(element.category === 'Product'){
                    <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
                        <div>
                            <img className="productImage"
                                src={productState[element.number]?.image ? productState[element.number]?.image : "https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg"}
                                alt="Image"
                            />
                            <div className="productName"> {productState[element.number]?.name} </div>
                            <div className="productPrice"> ${productState[element.number]?.price} </div>
                        </div>
                    </button>
                }

            }
        })
    }

    return(
        <>
           <button onClick={()=>{history.push('/favorites')}}> Shops </button>
            <button onClick={() => {history.push('/favorites/products')} }> Products </button>
            <div className="allProducts">{userFavorites()}</div>
        </>
    )
}
