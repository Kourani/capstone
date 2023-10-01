

import React, { useEffect, useState } from "react";

import { useModal } from "../../../context/Modal";
import * as shopActions from "../../../store/shop"
import { useDispatch } from "react-redux";

export default function DeleteShop(shopId){

    console.log(shopId,'!!!!!!!!!!!!!!!!!!!')

    const {closeModal} = useModal()
    const dispatch = useDispatch()
    const [clicked, setClicked] = useState('False')


    // useEffect(()=>{
    //     dispatch(shopActions.getShops())
    // },[dispatch, clicked])

    function toDelete(){
        dispatch(shopActions.deleteShop(shopId.shopId))
        setClicked('True')
        closeModal()
        return
    }




    return(
        <>
            <p>Are you sure you want to delete this shop?</p>
            <button onClick={toDelete}> YES, DELETE </button>
            <button onClick={()=>{closeModal()}}> No, keep </button>
        </>
    )


}
