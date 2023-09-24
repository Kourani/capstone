
import React from "react"
import {useDispatch} from "react-redux"

import * as productActions from "../../../store/product"
import { useModal } from "../../../context/Modal"




export default function DeleteProduct(productId){

    const dispatch = useDispatch()
    const {closeModal} = useModal()


    function toDelete(){
        dispatch(productActions.deleteProduct(productId.productId))
        closeModal()
        return
    }

    return (
        <>
            <div>Are you sure you want to delete product?</div>
            <button onClick={toDelete}> YES, DELETE </button>
            <button>No, Keep </button>
        </>
    )

}
