

import React, { useEffect } from "react";
import * as shopActions from "../../../store/shop"
import { useDispatch, useSelector } from "react-redux";
import {useHistory} from "react-router-dom"


function OwnedShops(){

    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(() =>{
        dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state.shop)
    const userState = useSelector(state=>state.session)

    console.log("user", userState?.user?.id);
    console.log(shopState, 'statettttttt')


    function ownedShops(){
        return shopState?.shops?.map(element =>{
            if(userState?.user?.id === element?.ownerId){
                return (
                    <>
                    <button onClick={()=>{history.push(`/shops/${element.id}/products/manage`)}}>
                    <div>{element.address}</div>
                    <div> {element.currency}</div>
                    </button>
                    <button onClick={()=>{history.push(`/shops/${element.id}/manage`)}}> Edit Shop </button>
                    <button> Delete Shop </button>
                    </>
                )
            }
        })


    }

    return(
        <>
        <div>{ownedShops()}</div>
        </>
    )
}

export default OwnedShops
