
import react, {useState} from 'react'


import { useDispatch } from 'react-redux'
import {useParams} from 'react-router-dom'


import * as imageActions from "../../../store/image"
import { useHistory } from 'react-router-dom'


export default function CreateImages(){

    const dispatch = useDispatch()
    const history = useHistory()
    const {productId} = useParams()


    console.log(productId,'aaaaaaaaaaaaaaaaaahhhhhhhh')

    const [image1, setImage1] = useState("")
    const [image2, setImage2] = useState("")
    const [image3, setImage3] = useState("")
    const [image4, setImage4] = useState("")
    const [image5, setImage5] = useState("")
    const [errors, setErrors] = useState({})

    const payload = {
        productId:parseInt(productId),
        image1,
        image2,
        image3,
        image4,
        image5
    }

    const handleSubmit= async(e) => {

        e.preventDefault()

        const data = await dispatch(imageActions.addImages(payload, productId))

        if(data && data?.errors){
            setErrors(data.errors)
        }
        else{
            history.push(`/products/${productId}`)

        }
    }

    return(
        <>
        <form onSubmit={handleSubmit}>
            <div className='modalsInside'>
            <div className='modalHeader'> Add Images for Product </div>
            <label > Top Image
                <input className='labelName'
                    type='text'
                    value={image1}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage1(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image1 ? errors.image1 : null}</div>

            <label className='labelName'>
                Second Image
                <input
                    type='text'
                    value={image2}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage2(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image2 ? errors.image2 : null}</div>

            <label className='labelName'>
                Third Image
                <input
                    type='text'
                    value={image3}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage3(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image3 ? errors.image3 : null}</div>

            <label className='labelName'>
                Fourth Image
                <input
                    type='text'
                    value={image4}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage4(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image4 ? errors.image4 : null}</div>

            <label className='labelName'>
                Bottom Image
                <input
                    type='text'
                    value={image5}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage5(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image5 ? errors.image5 : null}</div>

            <button type='submit'>Submit</button>
            </div>

        </form>
        </>
    )

}
