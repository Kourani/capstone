

import react, { useEffect } from 'react'
import { useDispatch } from 'react-redux'

import * as imageActions from "../../../store/images"

export default function AllImages() {

    const dispatch = useDispatch()
    useEffect(()=>{
        dispatch(imageActions.getImages())
    },[dispatch])

    return(
        <>
        <h1>HELLO</h1>
        </>
    )

}
