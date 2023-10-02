

//-------------------CONSTANTS-----------

const GET_ALL = "images/GET_ALL"

//-----------------ACTIONS---------------

const getAll = () => ({
    type:GET_ALL,
    payload
})

//------------------THUNKS------------------

export const getImages = () => async (dispatch) => {

    const response = await fetch("/api/images")

    if(response.ok){
        const allImages = await response.json()
        dispatch(getAll(allImages))
    }
    else {
        return await response.json()
    }
}


//---------------------REDUCER-----------------
function imagesReducer(state={}, action){
    switch (action.type){
        case GET_ALL:
            let newState = {...state}
            action.payload.images.forEach(element => {
                newState[element.id]=element
            })
        return newState

        default:
            return state;
    }
}

export default imagesReducer
