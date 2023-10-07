

//-------------------CONSTANTS-----------

const GET_ONE = "images/GET_ONE"
const ADD_IMAGES = "images/ADD_IMAGES"
const EDIT_IMAGES = 'images/EDIT_IMAGES'

//-----------------ACTIONS---------------

const getAll = (images) => ({
    type:GET_ONE,
    payload:images
})

const addOne = (images) => ({
    type:ADD_IMAGES,
    images
})

const editOne = (image) =>({
    type:EDIT_IMAGES,
    image
})


//------------------THUNKS------------------

export const getImages = () => async (dispatch) => {

    const response = await fetch("/api/images/")

    if(response.ok){
        const allImages = await response.json()
        dispatch(getAll(allImages))
        console.log(allImages,'THUNK IF')
    }
    else {
        return await response.json()
    }
}

export const addImages = (payload, productId) => async (dispatch) => {
    const response = await fetch(`/api/products/${productId}/images`,{
        method:'POST',
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify(payload)
    })

    if(response.ok){
        const newImages = await response.json()
        dispatch(addOne(newImages))
    }
    else{
        return await response.json()
    }
}

export const editImages = (payload, productId) => async (dispatch) => {
    const response = await fetch(`/api/products/${productId}/images`, {
        method:'PUT',
        headers:{
            "Content-Type" : "application/json"
        },
        body: JSON.stringify(payload)
    })

    if(response.ok){
        const updatedImages = await response.json()
        dispatch(editOne(updatedImages))
    }
    else{
        return await response.json()
    }
}


//---------------------REDUCER-----------------
function imagesReducer(state={}, action){
    switch (action.type){
        case GET_ONE:
            let newState = {...state}
            console.log(action.payload.images,'IMAGES REDUCER')
            action.payload.images.forEach(element => {
                newState[element.productId]=element
            })
            return newState

        case ADD_IMAGES:
            let addition = {...state}
            addition[action.images.id]=action.images
            return addition

        case EDIT_IMAGES:
            let edited = {...state}
            edited[action.payload.id]=action.payload
            return edited

        default:
            return state;
    }
}

export default imagesReducer
