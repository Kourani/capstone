

//---------------------CONSTANTS----------------------------------
const GET_ALL = '/favorites/GET_ALL'
const ADD_FAVORITE = '/favorites/ADD_FAVORITE'
const DELETE_FAVORITE = '/favorites/DELETE_FAVORITE'
export const DELETE_ALL = '/favorites/DELETE_ALL'

//-------------------------ACTIONS----------------------------------

const getAll = (payload)=> ({
    type:GET_ALL,
    payload
})

const addOne = (one) => ({
    type:ADD_FAVORITE,
    one
})

const deleteOne = (one) => ({
    type: DELETE_FAVORITE,
    one
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

export const addFavorite = (payload) => async (dispatch) => {
    const response = await fetch('/api/favorites/', {
        method:'POST',
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(payload)
    })

    if(response.ok){
        const newFavorite = await response.json()
        dispatch (addOne(newFavorite))
    }

    else {
        let res = await response.json()
        return await response.json()
    }

}

export const deleteFavorite = (favoriteId) => async (dispatch) => {
    const response = await fetch(`/api/favorites/${favoriteId}`,{
        method:'DELETE',
        headers:{
            'Content-Type':"application/json"
        }
    })

    if(response.ok){
        const removedFavorite = await response.json()
        dispatch(deleteOne(favoriteId))
    }
    else {
        return await response.json()
    }
}

//--------------------------REDUCER----------------------------------------

export default function favoriteReducer(state={}, action){
    switch(action.type){

        case GET_ALL:
            let newState = {}
            action.payload.favorites.forEach(element=>{
                newState[element.id] = element
            })
            return newState

        case ADD_FAVORITE:
            let addition = {...state}
            addition[action.one.id]=action.one
            return addition

        case DELETE_FAVORITE:
            let gone = {...state}
            delete gone[action.one]
            return gone

        case DELETE_ALL:
            return {}

        default:
            return state
    }

}
