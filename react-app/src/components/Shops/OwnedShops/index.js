

import React, { useEffect } from "react";
import * as shopActions from "../../../store/shop"
import { useDispatch, useSelector } from "react-redux";


function OwnedShops(){

    const dispatch = useDispatch()

    useEffect(() =>{
        dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state.shop)
    const userState = useSelector(state=>state.session)

    console.log("user", userState?.user?.id);
    console.log(shopState, 'statettttttt')


    function ownedShops(){
        shopState?.shops?.forEach(element =>{
            if(userState?.user?.id === element?.ownerId){
                console.log('inside the ifffffffffffffffffffffff')
                return (
                    <div>{element.name}</div>
                )
            }
        })

        return

    }

    return(
        <>
        <div>{ownedShops()}</div>
        </>
    )
}

export default OwnedShops
