

import React, { useEffect } from "react";
import * as shopActions from "../../../store/shop"
import { useDispatch, useSelector } from "react-redux";


function ManageShops(){

    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(shopActions.getShops)
    })

    const shopState = useSelector(state=>state.shop)
    const userState = useSelector(state=>state.session)

    function ownedShops(){
        
    }

    return(
        <div>HELLO</div>
    )
}

export default ManageShops
