
import "./CreateProduct.css"

import React, {useState } from "react"

import {useDispatch} from "react-redux"

import { useParams, useHistory} from "react-router-dom"

import * as productActions from "../../../store/product"

function CreateProduct(){

    const dispatch = useDispatch()
    const history = useHistory()
    const {shopId} = useParams()

    const [name, setName] = useState("")
    const [price, setPrice] = useState("")
    const [description, setDescription] = useState("")
    const [category, setCategory] = useState('sweets')
    const [image, setImage] = useState("")
    const [image1, setImage1] = useState("")
    const [image2, setImage2] = useState("")
    const [image3, setImage3] = useState("")
    const [image4, setImage4] = useState("")
    const [image5, setImage5] = useState("")
    const [errors, setErrors] = useState({})

    const payload = {
        name:name,
        price:price,
        description:description,
        category,
        image,
        image1,
        image2,
        image3,
        image4,
        image5,

    }

    const handleSubmit = async (e) => {
        e.preventDefault()

        const data = await dispatch(productActions.newProduct(payload, shopId))

        if(data && data?.errors){
            setErrors(data?.errors)
        }
        else{
            history.push(`/shops/${shopId}/products`)
        }
    }


    return(
        <>
        <form className="createProductForm" onSubmit={handleSubmit}>

            <h1 className="createProductTitle"> Create Product </h1>
            <label className="labelName">
                Name
                <input
                    type='text'
                    value={name}
                    placeholder="Enter Product Name/Title"
                    onChange={(e)=>setName(e.target.value)}
                    required
                    />
            </label>

            <label className="labelName">
                Price
                <input
                    type='text'
                    value={price}
                    placeholder="Enter Product Price"
                    onChange={(e)=>setPrice(e.target.value)}
                    required
                    />
            </label>

            <div className="errors"> {errors.price ? errors.price : null}</div>

            <label className="labelName">
                Description
                <input
                    type='text'
                    placeholder="Enter Product Description"
                    value={description}
                    onChange={(e)=>setDescription(e.target.value)}
                    required
                    />
            </label>

            <label className="labelName" >
                Category
                <select
                onChange={(e)=>setCategory(e.target.value)}
                value={category}
                placeholder="Choose a Category">
                    <option value='sweets'>Sweets</option>
                    <option value='books'>Books</option>
                    <option value='watches'>Watches</option>
                    <option value = 'ceramics'>Ceramics</option>
                    <option value = 'tools'>Tools</option>
                    <option value = 'jewelry'> Jewelry</option>
                </select>
            </label>

            <label className="labelName" >
                Image
                <input
                    type='text'
                    value={image}
                    placeholder="Enter Product Image"
                    onChange={(e)=>setImage(e.target.value)}
                    required
                    />
            </label>

            <div className="errors"> {errors.image ? errors.image : null}</div>

            <label className="labelName" >
                Side Image #1
                <input
                    type='text'
                    value={image1}
                    placeholder="Enter Product Image"
                    onChange={(e)=>setImage1(e.target.value)}
                    />
            </label>

            <div className="errors"> {errors.image1 ? errors.image1 : null}</div>

            <label className="labelName" >
                Side Image #2
                <input
                    type='text'
                    value={image2}
                    placeholder="Enter Product Image"
                    onChange={(e)=>setImage2(e.target.value)}
                    />
            </label>

            <div className="errors"> {errors.image2 ? errors.image2 : null}</div>

            <label className="labelName" >
                Side Image #3
                <input
                    type='text'
                    value={image3}
                    placeholder="Enter Product Image"
                    onChange={(e)=>setImage3(e.target.value)}
                    />
            </label>

            <div className="errors"> {errors.image3 ? errors.image3 : null}</div>

            <label className="labelName" >
                Side Image #4
                <input
                    type='text'
                    value={image4}
                    placeholder="Enter Product Image"
                    onChange={(e)=>setImage4(e.target.value)}
                    />
            </label>

            <div className="errors"> {errors.image4 ? errors.image4 : null}</div>

            <label className="labelName" >
                Side Image #5
                <input
                    type='text'
                    value={image5}
                    placeholder="Enter Product Image"
                    onChange={(e)=>setImage5(e.target.value)}
                    />
            </label>

            <div className="errors"> {errors.image5 ? errors.image5 : null}</div>

            <button className='uniButton' type='submit'>Submit</button>
        </form>
        </>



    )
}

export default CreateProduct
