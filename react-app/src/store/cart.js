


//---------------------------------------CONSTANTS--------------------------------
const ADD_TO = "/cart/ADD_TO"
const REMOVE_FROM = "/cart/REMOVE_FROM"
//-----------------------------------ACTIONS----------------------------------------

//--------------------------------------THUNKS--------------------------------------

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
    }
}
