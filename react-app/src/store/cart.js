


//---------------------------------------CONSTANTS--------------------------------
const ADD_TO = "/cart/ADD_TO"
const REMOVE_FROM = "/cart/REMOVE_FROM"
//-----------------------------------ACTIONS----------------------------------------

const addTo = (product) =>({
    type:ADD_TO,
    product
})
//--------------------------------------THUNKS--------------------------------------

export const addCart = (payload) => async (dispatch) =>{
    dispatch(addTo(payload))
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
