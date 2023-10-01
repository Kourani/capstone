

//---------------------CONSTANTS----------------------------------
const GET_ALL = '/favorites/GET_ALL'

//-------------------------ACTIONS----------------------------------

const getAll = (payload)=> ({
    type:GET_ALL,
    payload
})

//--------------------THUNKS---------------------------------

export const getFavorites = () => async (dispatch) => {
    const response = await fetch('/api/favorites/')

    if(response.ok){
        const allFavorites = await response.json()
        dispatch(getAll(allFavorites))
    }

    else {
        return await response.json()
    }
}

//--------------------------REDUCER----------------------------------------

export default function favoriteReducer(state={}, action){
    switch(action.type){

        case GET_ALL:
            let newState = {...state}
            action.payload.favorites.forEach(element=>{
                newState[element.id] = element
            })
            return newState

        default:
            return state
    }

}
