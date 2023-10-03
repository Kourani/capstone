

//-------------------CONSTANTS-----------

const GET_ALL = "images/GET_ALL"

//-----------------ACTIONS---------------

const getAll = (images) => ({
    type:GET_ALL,
    payload:images
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


//---------------------REDUCER-----------------
function imagesReducer(state={}, action){
    switch (action.type){
        case GET_ALL:
            let newState = {...state}
            action?.images?.forEach(element => {
                newState[element.id]=element
            })
        return newState

        default:
            return state;
    }
}

export default imagesReducer
