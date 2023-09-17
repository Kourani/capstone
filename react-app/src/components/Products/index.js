
import React, { useEffect } from "react"

import * as productActions from "../../store/product"

import { useDispatch } from "react-redux"

import { useSelector } from "react-redux"


export default function Products(){

    const dispatch = useDispatch()

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    return (
        <h1>HELLO</h1>
    )
}
