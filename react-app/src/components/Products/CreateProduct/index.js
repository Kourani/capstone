
import "./CreateProduct.css"

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
    const [image, setImage] = useState("")
    const [errors, setErrors] = useState({})



    const payload = {
        name:name,
        price:price,
        description:description,
        category,
        image,

    }

    console.log(payload, 'create product payload')

    const handleSubmit = async (e) => {
        e.preventDefault()

        const data = await dispatch(productActions.newProduct(payload, shopId))

        console.log(data)
        if(data.errors){
            setErrors(data.errors)
        }



        history.push(`/shops/${shopId}/products`)
    }

    console.log(errors, 'ERRORS')

    return(
        <>
        <h1 className="createProductTitle"> Create Product </h1>

        <form className="createProductForm" onSubmit={handleSubmit}>

            <label className="createProductName">
                Name
                <input
                    type='text'
                    value={name}
                    placeholder="Enter Product Name/Title"
                    onChange={(e)=>setName(e.target.value)}
                    required
                    />
            </label>

            <label className="createProductName">
                Price
                <input
                    type='text'
                    value={price}
                    placeholder="Enter Product Price"
                    onChange={(e)=>setPrice(e.target.value)}
                    required
                    />
            </label>

            <label className="createProductName">
                Description
                <input
                    type='text'
                    placeholder="Enter Product Description"
                    value={description}
                    onChange={(e)=>setDescription(e.target.value)}
                    required
                    />
            </label>

            <label className="createProductName" >
                Category
                <select
                onChange={(e)=>setCategory(e.target.value)}
                value={category}
                placeholder="Choose a Category">
                    <option value='toys'>toys</option>
                    <option value='books'>books</option>
                    <option value='trinkets'>toys</option>
                </select>
            </label>

            <label className="createProductName" >
                Image
                <input
                    type='text'
                    value={image}
                    placeholder="Enter Product Image"
                    onChange={(e)=>setImage(e.target.value)}
                    required
                    />
            </label>

            <button type='submit'>Submit</button>
        </form>
        </>



    )
}

export default CreateProduct
