


//---------------------------------------CONSTANTS--------------------------------
const ADD_TO = "/cart/ADD_TO"
const REMOVE_FROM = "/cart/REMOVE_FROM"
//-----------------------------------ACTIONS----------------------------------------

const addTo = (product) =>({
    type:ADD_TO,
    product
})

const deleteFrom = (id) =>({
    type:REMOVE_FROM,
    id
})
//--------------------------------------THUNKS--------------------------------------

export const addCart = (payload) => async (dispatch) =>{
    dispatch(addTo(payload))
}

export const removeFrom = (itemId) => async (dispatch) =>{
    dispatch(deleteFrom(itemId))
}
//------------------------------------REDUCER----------------------------------------------

export default function cartReducer(state={}, action){
    switch(action.type){

        case ADD_TO:
            return{
                ...state
            }

        case REMOVE_FROM:
            return{
                ...state
            }

        default:
            return state
    }
}
