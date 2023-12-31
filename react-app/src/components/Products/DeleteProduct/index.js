
import React, {useEffect, useState} from "react"
import {useDispatch} from "react-redux"

import * as productActions from "../../../store/product"
import { useModal } from "../../../context/Modal"




export default function DeleteProduct(productId){

    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const [clicked, setClicked] = useState('False')


    function toDelete(){
        dispatch(productActions.deleteProduct(productId.productId))
        setClicked('True')
        closeModal()
        return
    }

    return (
        <div className="modalsInside">
            <div>Are you sure you want to delete product?</div>
            <button className='uniButton' onClick={toDelete}> YES, DELETE </button>
            <button className='uniButton' onClick={()=>{closeModal()}}>No, Keep </button>
        </div>
    )

}
