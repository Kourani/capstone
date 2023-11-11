


//---------------------------------------CONSTANTS--------------------------------
const ADD_TO = "/cart/ADD_TO"
const REMOVE_FROM = "/cart/REMOVE_FROM"
const DELETE_ALL="/cart/DELETE_ALL"
//-----------------------------------ACTIONS----------------------------------------

const addTo = (product) =>({
    type:ADD_TO,
    product
})

const deleteFrom = (id) =>({
    type:REMOVE_FROM,
    id
})

const deleteAllItems = all => ({
    type:DELETE_ALL,
    all
})
//--------------------------------------THUNKS--------------------------------------

export const addCart = (payload) => async (dispatch) =>{
    dispatch(addTo(payload))
}

export const removeFrom = (itemId) => async (dispatch) =>{
    dispatch(deleteFrom(itemId))
}

export const deleteAll = () => async dispatch =>{
    dispatch(deleteAllItems())
}
//------------------------------------REDUCER----------------------------------------------

export default function cartReducer(state={}, action){
    switch(action.type){

        case ADD_TO:
            let addedState = {...state}
            addedState[action.product.id] = action.product
            return addedState

        case REMOVE_FROM:
            let gone = {...state}
            delete gone[action.remove]
            return gone
        
        case DELETE_ALL:
            return {}

        default:
            return state
    }
}
