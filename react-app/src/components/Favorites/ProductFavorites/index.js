

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
        dispatch(productActions.getProducts())
    },[dispatch])

    const favoriteState = useSelector(state=>state.favorite)
    const userState = useSelector(state=>state.session)
    const productState = useSelector(state=>state.product)
    const favoriteElements = Object.values(favoriteState)

    function userProductFavorites(){
        return favoriteElements?.map(element =>{

            console.log(productState[element.number]?.image, 'hello')
            console.log(productState[element.number], 'hello there')

            if(element.userId === userState?.user?.id){
                console.log('inside if one')

                if(element?.category === 'Product'){
                    return(
                    <button className="product" onClick={()=>{history.push(`/products/${element.id}`)}}>
                        <div>
                            <img className="productImage"
                                src={productState[element?.number]?.image}
                                alt="Image"
                            />
                            <div className="productName"> {productState[element?.number]?.name} </div>
                            <div className="productPrice"> ${productState[element?.number]?.price} </div>
                        </div>
                    </button>
                    )
                }

            }
        })
    }

    console.log(userProductFavorites(), 'userrrrrrr')

    return(
        <>
            <button onClick={()=>{history.push('/favorites')}}> Shops </button>
            <button onClick={() => {history.push('/favorites/products')} }> Products </button>

            <div className="allProducts">{ userProductFavorites() }</div>
        </>
    )
}
