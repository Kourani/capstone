

import React, {useEffect, useState} from "react"

import * as commentActions from '../../../store/comment'
import { useDispatch } from "react-redux"
import { useParams } from "react-router-dom"

import { useModal } from "../../../context/Modal"


export default function CreateCommment(productId){

    const dispatch = useDispatch()
    const {closeModal} = useModal()

    // const {productId} = useParams() WHY IS IT UNDEFINED !

    console.log(productId.productId,'!!!!!!!!!!!!!!!!!!!!!!')

    const [comment, setComment] = useState("")
    const [errors, setErrors] = useState({})
    const [clicked, setClicked] = useState('False')

    useEffect(()=>{
        dispatch(commentActions.getComments())
    },[dispatch,clicked])

    const payload = {
        comment
    }

    const handleSubmit = async (e) => {
        e.preventDefault()

        const data = await dispatch(commentActions.addComment(payload, productId.productId))

        console.log(data, 'HEREEEEEEEEEEE')
        if( data && data.error){
            setErrors(data.error)
        }

        setClicked('True')
        closeModal()
    }



    return (
        <>
            <h1>Create Comment</h1>
            <form onSubmit={handleSubmit}>
            <label>
            comment
            <input
                type='text'
                value={comment}
                placeholder="Enter Comment"
                onChange={(e)=>setComment(e.target.value)}
                />
            </label>
            <button> Submit </button>
            </form>
        </>
    )
}
