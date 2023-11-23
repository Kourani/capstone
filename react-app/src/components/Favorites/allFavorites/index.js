

import react, { useEffect, useState } from "react"
import {useDispatch, useSelector} from 'react-redux'


import * as favoriteActions from '../../../store/favorite'
import * as productActions from '../../../store/product'
import * as shopActions from '../../../store/shop'
import { useHistory } from "react-router-dom/cjs/react-router-dom.min"


export default function AllFavorites(){

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

    function userFavorites(){
        return favoriteElements?.map(element =>{

            if(element.userId === userState?.user?.id){

                if(element.category === 'Shop'){
                    return (
                        <button className="product" onClick={()=>{history.push(`/shops/${element.number}`)}}>
                            <div>
                                <img className="productImage" src={shopState[element.number]?.image} alt="Image" />
                                <div className="productName">{shopState[element.number]?.name}</div>
                            </div>
                        </button>
                    )

                }
            }
        })
    }

    return(
        <>

            <div className="favoritesPageButtons">
                <button className='universalModalButtons' onClick={()=>{history.push('/favorites')}}> Shops </button>
                <button className = 'universalModalButtons' onClick={() => {history.push('/favorites/products')} }> Products </button>
            </div>
            
            <div className="allProducts">{userFavorites()}</div>

        </>
    )
}
