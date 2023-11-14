
import React, {useEffect, useState} from "react"
import {useDispatch} from "react-redux"

import * as commentActions from "../../../store/comment"
import { useModal } from "../../../context/Modal"

export default function DeleteComment(commentId){

    const dispatch = useDispatch()
    const {closeModal} = useModal()

    const [clicked, setClicked] = useState('False')


    function toDelete(){
        dispatch(commentActions.deleteComment(commentId.commentId))
        setClicked('True')
        closeModal()
        return
    }

    return (
        <div className="modalsInside">
            <div>Are you sure you want to delete comment?</div>
            <div className="sleepButton">
                <button className='uniButton' onClick={toDelete}> YES, DELETE </button>
                <button className='uniButton' onClick={()=>{closeModal()}}>No, Keep </button>
            </div>
        </div>
    )

}
