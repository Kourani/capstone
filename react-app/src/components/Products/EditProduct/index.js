
import React, { useEffect, useState } from "react"
import {useDispatch, useSelector} from "react-redux"
import { useParams } from "react-router-dom"

import * as productActions from "../../../store/product"
import { useModal } from "../../../context/Modal"




function EditProduct(productId){

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
     
        if(data){
            setErrors(data.errors)
        }
        else{
            setClicked('True')
            closeModal()
        }


    }


    return(
        <>
        <form onSubmit={handleSubmit}>

        <div className="modalsInside">
            <h1 className="modalHeader"> Edit Product </h1>
            <label className="labelName" >
                Product Name
                <input
                    type='text'
                    value={name}
                    onChange={(e)=>setName(e.target.value)}
                    required
                    />
            </label>

            <label className="labelName">
                Price
                <input
                    type='text'
                    value={price}
                    onChange={(e)=>setPrice(e.target.value)}
                    required
                    />
            </label>

            <div className="errors"> {errors.price ? errors.price : null}</div>

            <label className="labelName" >
                Description
                <input
                    type='text'
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
                Main Image
                <input
                    type='text'
                    value={image}
                    onChange={(e)=>setImage(e.target.value)}
                    required
                    />
            </label>

            <div className="errors"> {errors.image ? errors.image : null}</div>

            <button className="uniButton">Update</button>
            </div>
        </form>
        </>



    )
}

export default EditProduct
