
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

const editOne =(comment) => ({
    type:EDIT_COMMENT,
    comment
})

const deleteOne = (comment) => ({
    type:DELETE_COMMENT,
    comment
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

export const addComment = (payload, productId) => async (dispatch) => {
    const response = await fetch(`/api/products/${productId}/comments`, {
        method:'POST',
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(payload)
    })

    if(response.ok){
        const newComment = await response.json()
        dispatch (addOne(newComment))
    }
    else {
        const fava = await response.json()
        return await response.json()
    }
}

export const editComment = (payload, commentId) => async (dispatch) => {

    const response = await fetch(`/api/comments/${commentId}/edit`, {
        method:'PUT',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(payload)
    })

    if(response.ok){
        const updatedComment = await response.json()
        dispatch(editOne(updatedComment))
    }
    else{
        let fave = await response.json()
        return await response.json()
    }
}

export const deleteComment = (commentId) => async(dispatch) =>{
    const response = await fetch(`/api/comments/${commentId}`,{
        method:'DELETE',
        headers:{
            "Content-Type":"application/json"
        }
    })

    if(response.ok){
        dispatch(deleteOne(commentId))
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
                let old = {...state}
                old[action.payload.id]=action.payload
                return old


        case EDIT_COMMENT:
                let edited = {...state}
                edited[action.comment.id]=action.comment
                return edited

        case DELETE_COMMENT:
                let gone = {...state}
                delete gone[action.comment]
                return gone

        default:
            return state
    }
}

export default commentsReducer
