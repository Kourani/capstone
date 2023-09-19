
import React, { useState } from "react"

import {useDispatch} from "react-redux"

import * as productActions from "../../../store/product"


function EditProduct(){

    const dispatch = useDispatch()

    const [name, setName] = useState("")
    const [price, setPrice] = useState("")
    const [description, setDescription] = useState("")
    const [category, setCategory] = useState("")
    const [errors, setErrors] = useState("")



    const handleSubmit = async (e) => {
        e.preventDefault()

        const data = await dispatch(productActions)

        if(data){
            setErrors(data)
        }
    }


    return(
        <>
        <h1> Edit Product </h1>

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


        </form>
        </>



    )
}

export default EditProduct
