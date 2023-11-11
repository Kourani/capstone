

import React, { useEffect, useState } from "react"
import {useDispatch, useSelector} from 'react-redux'

import * as commentActions from '../../../store/comment'
import { useModal } from "../../../context/Modal"

import "./EditComment.css"


export default function EditComment(commentId){

    const dispatch = useDispatch()
    const {closeModal} = useModal()


    useEffect(()=>{
        dispatch(commentActions.getComments())
    },[dispatch])

    const commentState = useSelector(state=>state.comment)

    const [comment, setComment] = useState(commentState[commentId.commentId]?.comment)
    const [errors, setErrors] = useState({})

    const payload ={
        comment:comment
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data = await dispatch(commentActions.editComment(payload, commentId.commentId))

        if (data && data.errors){
          setErrors(data.errors)
        }

        closeModal()
    }

    return(

        <>

        <form onSubmit={handleSubmit}>
        <div className="modalsInside">
        <h1 className="modalHeader">Update Comment</h1>
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
          </div>
        </form>
      </>

    )

}
