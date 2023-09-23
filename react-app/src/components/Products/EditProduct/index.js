
import React, { useEffect, useState } from "react"
import {useDispatch, useSelector} from "react-redux"
import { useParams } from "react-router-dom"

import * as productActions from "../../../store/product"
import { useModal } from "../../../context/Modal"




function EditProduct(){

    const dispatch = useDispatch()
    const {closeModal} = useModal()
    const {shopId, productId} = useParams()

    console.log(shopId,'AAAAAAAAAAAAAAAAAAAAAAAAAAA')
    console.log(productId,'!!!!!!!!!!!!!')

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState= useSelector(state=>state.product)

    console.log(productState)

    const [name, setName] = useState(productState[productId]?.name)
    const [price, setPrice] = useState(productState[productId]?.price)
    const [description, setDescription] = useState(productState[productId]?.description)
    const [category, setCategory] = useState(productState[productId]?.category)
    const [image, setImage] = useState(productState[productId]?.image)
    const [errors, setErrors] = useState("")


    const payload = {
        name:name,
        price:price,
        description:description,
        category:category,
        image:image
    }

    const handleSubmit = async (e) => {
        e.preventDefault()

        const data = await dispatch(productActions.editProduct(payload,productId))

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

            <label>
                Category
                <input
                    type='text'
                    value={category}
                    onChange={(e)=>setCategory(e.target.value)}
                    required
                    />
            </label>

            <label>
                image
                <input
                    type='text'
                    value={image}
                    onChange={(e)=>setImage(e.target.value)}
                    required
                    />
            </label>


        </form>
        </>



    )
}

export default EditProduct
