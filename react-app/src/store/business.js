
//--------------------------------CONSTANTS---------------------------------
const GET_ALL = "business/GET_ALL"
const DELETE_BUSINESS = "business/DELETE_BUSINESS"
const ADD_BUSINESS = "business/ADD_BUSINESS"

//---------------------------------ACTIONS-----------------------------------
const getAll = (all) => ({
    type: GET_ALL,
    payload:all
})

const createOne = (one) => ({
    type:ADD_BUSINESS,
    payload:one
})

const deleteOne = (one) => ({
    type:DELETE_BUSINESS,
    payload:one
})


//-----------------------------------THUNKS------------------------------------

export const getBusinesses = () => async(dispatch) => {

    const response = await fetch("/api/shops")

    if(response.ok){
        const allBusinesses = await response.json()
        dispatch(getAll(allBusinesses))
    }
    else {
        return await response.json()
    }


}
//-----------------------------------REDUCERS----------------------------------------

function businessReducer(state={}, action){
    switch(action.type){
        case GET_ALL :
            return{
                ...state,
                ...action.payload
            }
        default:
            return state
    }
}

export default businessReducer
