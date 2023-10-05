

//-------------------CONSTANTS-----------

const GET_ALL = "images/GET_ALL"
const ADD_IMAGES = "images/ADD_ONE"

//-----------------ACTIONS---------------

const getAll = (images) => ({
    type:GET_ALL,
    payload:images
})

const addOne = (images) => ({
    type:ADD_IMAGES,
    images
})


//------------------THUNKS------------------

export const getImages = () => async (dispatch) => {

    const response = await fetch("/api/images")

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
    const response = await fetch("/api/images",{
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


//---------------------REDUCER-----------------
function imagesReducer(state={}, action){
    switch (action.type){
        case GET_ALL:
            let newState = {...state}
            console.log(action.payload.images,'IMAGES REDUCER')
            action.payload.images.forEach(element => {
                newState[element.id]=element
            })
            return newState
            
        case ADD_IMAGES:
            let addition = {...state}
            addition[action.images.id]=action.images
            return addition



        default:
            return state;
    }
}

export default imagesReducer
