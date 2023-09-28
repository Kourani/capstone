

import React, { useEffect, useState } from "react"
import {useDispatch, useSelector} from 'react-redux'

import * as commentActions from '../../../store/comment'
import { useModal } from "../../../context/Modal"



export default function EditComment(commentId){

    const dispatch = useDispatch()
    const closeModal = useModal()


    useEffect(()=>{
        dispatch(commentActions.getComments())
    },[dispatch])

    const commentState = useSelector(state=>state.comment)

    console.log(commentState,'!!!!')

    const [comment, setComment] = useState(commentState[commentId.commentId]?.comment)
    const [errors, setErrors] = useState({})

    const payload ={
        comment:comment
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data = await dispatch(commentActions.getComments())

        if (data.errors){
            setErrors(data.errors)
        }

        closeModal()
    }

    return(

        <>
        <h1>Update Comment</h1>
        <form onSubmit={handleSubmit}>

          <label>
            Comment
            <input
              type="text"
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              required
            />
          </label>


          <button type="submit">Update</button>
        </form>
      </>

    )

}
