
import react, {useState} from 'react'


import { useDispatch } from 'react-redux'


import * as imageActions from "../../../store/image"


export default function CreateImages(){

    const dispatch = useDispatch()

    const [image1, setImage1] = useState("")
    const [image2, setImage2] = useState("")
    const [image3, setImage3] = useState("")
    const [image4, setImage4] = useState("")
    const [image5, setImage5] = useState("")
    const [errors, setErrors] = useState({})


    const handleSubmit= async(e) => {

        e.preventDefault()

        const data = await dispatch(imageActions.addImages(payload))

        if(data && data?.errors){
            setErrors(data.errors)
        }
    }


    return(
        <>
        <form onSubmit={handleSubmit}>
            <label>
                <input
                    type='text'
                    value={image1}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage1(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image1 ? errors.image1 : null}</div>

            <label>
                <input
                    type='text'
                    value={image2}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage2(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image2 ? errors.image2 : null}</div>

            <label>
                <input
                    type='text'
                    value={image3}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage3(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image3 ? errors.image3 : null}</div>

            <label>
                <input
                    type='text'
                    value={image4}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage4(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image4 ? errors.image4 : null}</div>

            <label>
                <input
                    type='text'
                    value={image5}
                    placeholder='Enter image link'
                    onChange={(e)=>setImage5(e.target.value)}
                />
            </label>

            <div className="errors"> {errors.image5 ? errors.image5 : null}</div>

            <button type='submit'>Submit</button>

        </form>
        </>
    )

}
