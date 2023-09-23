
//---------------------------------CONSTANTS--------------------------------------

const GET_ALL = "./comments/GET_ALL"
const ADD_COMMENT = "./comments/ADD_COMMENT"
const EDIT_COMMENT = "./comments/EDIT_COMMENT"
const DELETE_COMMENT = "./comments/DELETE_COMMENT"
//-----------------------------------ACTIONS---------------------------------------

const getAll = (all) => ({
    type:GET_ALL,
    payload:all
})

const addOne = (one) => ({
    type:ADD_COMMENT,
    payload:one
})

//----------------------------------------THUNKS-----------------------------------

export const getComments = () => async (dispatch) => {

    const response = await fetch("/api/comments/")

    if (response.ok){
        const allComments = await response.json()
        dispatch(getAll(allComments))
    }
    else {
        return await response.json()
    }
}


//-------------------------------REDUCER-------------------------------

function commentsReducer(state={}, action){
    switch(action.type){

        case GET_ALL :
            let newState={...state}
            action.payload.comments.forEach(element => {
                newState[element.id]=element
            });
            return newState

        case ADD_COMMENT:
            return{
                ...state
            }

        case EDIT_COMMENT:
            return {
                ...state
            }

        case DELETE_COMMENT:
            return {
                ...state
            }

        default:
            return state
    }
}

export default commentsReducer
