
import react, {useEffect, useState} from 'react'


import { useDispatch, useSelector } from 'react-redux'

import * as imageActions from "../../../store/image"

import { useModal } from '../../../context/Modal'


export default function EditImages(product){

    console.log(product,'aaaaa!!!!!!')

    const dispatch = useDispatch()

    const {closeModal} = useModal()

    useEffect(()=>{
        dispatch(imageActions.getImages())
    },[dispatch])

    const imageState = useSelector(state=>state.image)

    const [image1, setImage1] = useState(imageState?.[product.productId]?.image1)
    const [image2, setImage2] = useState(imageState?.[product.productId]?.image2)
    const [image3, setImage3] = useState(imageState?.[product.productId]?.image3)
    const [image4, setImage4] = useState(imageState?.[product.productId]?.image4)
    const [image5, setImage5] = useState(imageState?.[product.productId]?.image5)
    const [errors, setErrors] = useState({})

    const payload = {
        productId:product.productId,
        image_1:image1,
        image_2:image2,
        image_3:image3,
        image_4:image4,
        image_5:image5
    }

    const handleSubmit= async(e) => {

        e.preventDefault()

        const data = await dispatch(imageActions.editImages(payload, product.productId))

        if(data && data?.errors){
            setErrors(data.errors)
        }
        else{
            closeModal()
        }
    }

    return(
        <>
        <form onSubmit={handleSubmit}>
            <div className='modalsInside'>

            <h1 className='modalHeader'>Edit Images for Product</h1>
            <div> Maximum of 5 side images accepted</div>

            <label className='labelName'> Top Image
                <input
                    type='text'
                    value={image1}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage1(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image1 ? errors.image1 : null}</div>

            <label className='labelName'> Second Image
                <input
                    type='text'
                    value={image2}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage2(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image2 ? errors.image2 : null}</div>

            <label className='labelName'> Third Image
                <input
                    type='text'
                    value={image3}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage3(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image3 ? errors.image3 : null}</div>

            <label className='labelName'> Fourth Image
                <input
                    type='text'
                    value={image4}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage4(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image4 ? errors.image4 : null}</div>

            <label className='labelName'> Bottom Image
                <input
                    type='text'
                    value={image5}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage5(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image5 ? errors.image5 : null}</div>

            <button type='submit'>Update</button>
            </div>

        </form>
        </>
    )

}
