

import React, { useEffect, useState } from "react";

import { useModal } from "../../../context/Modal";
import * as shopActions from "../../../store/shop"
import { useDispatch } from "react-redux";

export default function DeleteShop(shopId){

    const {closeModal} = useModal()
    const dispatch = useDispatch()
    const {clicked, setClicked} = useState('False')

    useEffect(()=>{
        dispatch(shopActions.getShops())
    },[dispatch, clicked])




    return(
        <>
            <p>Are you sure you want to delete this shop?</p>
            <button>YES, DELETE</button>
            <button>No, keep</button>
        </>
    )


}
