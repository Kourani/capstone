
import React, { useEffect, useState } from "react"
import {useDispatch, useSelector} from "react-redux"
import { useParams } from "react-router-dom"

import * as productActions from "../../../store/product"
import { useModal } from "../../../context/Modal"




function EditProduct(productId){

    console.log(productId.productId)

    const dispatch = useDispatch()
    const {closeModal} = useModal()
    const [clicked, setClicked] = useState('False')

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch, clicked])

    const productState= useSelector(state=>state.product)

    const [name, setName] = useState(productState[productId.productId]?.name)
    const [price, setPrice] = useState(productState[productId.productId]?.price)
    const [description, setDescription] = useState(productState[productId.productId]?.description)
    const [category, setCategory] = useState(productState[productId.productId]?.category)
    const [image, setImage] = useState(productState[productId.productId]?.image)
    const [errors, setErrors] = useState([]);


    const payload = {
        name:name,
        price:price,
        description:description,
        category:category,
        image:image
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        const data = await dispatch(productActions.editProduct(payload, productId.productId))
        console.log(data,'data!')
        if(data){
            setErrors(data.errors)
        }
        else{
            closeModal()
        }

        setClicked('True')
    }
    console.log(errors,'errors')
    console.log(errors.price,'dot price')
    console.log(errors[price],'bracket price')
    
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

            <div className="errors"> {errors.price ? errors.price : null}</div>

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

            <div className="errors"> {errors.image ? errors.image : null}</div>

            <button>Update</button>
        </form>
        </>



    )
}

export default EditProduct
