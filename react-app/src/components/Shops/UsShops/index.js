

import * as shopActions from "../../../store/shop"
import * as favoriteActions from "../../../store/favorite"
import * as additionalFunctions from "../../../context/additional"

import React, { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from 'react-router-dom'

export default function UsShops(){

    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(()=>{
        dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state.shop)
    const userState = useSelector(state=>state.session)
    const favoriteState = useSelector(state=>state.favorite)

    const shopElements = Object.values(shopState)
    const favoriteElements = Object.values(favoriteState)

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
        return shopElements?.map(element=>{

            if(element?.country === 'United States')
            {
                let found = favoriteElements?.find(one => one.category === 'Shop' && one.number === element.id)

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
        })
    }


    return (
        <div>
            {shops()}
        </div>
    )
}
