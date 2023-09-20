
import React, { useEffect, useState } from "react"

import {useDispatch} from "react-redux"

import { useParams, useHistory} from "react-router-dom"

import * as productActions from "../../../store/product"



function CreateProduct(){

    const dispatch = useDispatch()
    const history = useHistory()
    const {shopId} = useParams()

    console.log(shopId,'createProduct shopId')

    const [name, setName] = useState("")
    const [price, setPrice] = useState("")
    const [description, setDescription] = useState("")
    const [category, setCategory] = useState("")
    const [errors, setErrors] = useState("")



    const payload = {
        name:name,
        price:price,
        description:description
    }

    console.log(payload, 'create product payload')

    const handleSubmit = async (e) => {
        e.preventDefault()

        const data = await dispatch(productActions.newProduct(payload, shopId))

        if(data){
            setErrors(data)
        }
    }


    return(
        <>
        <h1> Create Product </h1>

        <form onSubmit={handleSubmit}>

            <label>
                Name
                <input
                    type='text'
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                    required
                    />
            </label>

            <label>
                Price
                <input
                    type='text'
                    value={price}
                    onChange={(e)=>setPrice(e.target.value)}
                    required
                    />
            </label>

            <label>
                Description
                <input
                    type='text'
                    value={description}
                    onChange={(e)=>setDescription(e.target.value)}
                    required
                    />
            </label>

            <button type='submit'>Submit</button>

        </form>
        </>



    )
}

export default CreateProduct
