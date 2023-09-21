

//------------------------------------CONSTANTS--------------------------
const GET_ALL = "products/GET_ALL";
const DELETE_PRODUCT = "products/DELETE_PRODUCT";
const ADD_PRODUCT = "products/ADD_PRODUCT";
const EDIT_PRODUCT = "products/EDIT_PRODUCT";
//-----------------------------------ACTIONS---------------------------------------
const getAll = (all) => ({
    type:GET_ALL,
    payload:all
})

const addOne =(product) =>({
    type: ADD_PRODUCT,
	payload:product
})

const editOne = (product) =>({
	type: EDIT_PRODUCT,
	payload:product
})

const deleteOne = () => ({
	type: DELETE_PRODUCT,
});


//-----------------------------------------THUNKS------------------------------------

export const getProducts = () => async (dispatch) => {

	const response = await fetch("/api/products")

	if (response.ok) {
		const allProducts = await response.json()
		dispatch(getAll(allProducts));
	}
	else {
		return await response.json()
	}
};

export const newProduct = (payload, shopId) => async(dispatch) => {

	console.log('inside new product thunk')
	const response = await fetch(`/api/shops/${shopId}/products`, {
		method:'POST',
		headers:{
			"Content-Type" : "application/json",
			// "Content-Type" : "multipart/form-data"
		},
		body:JSON.stringify(payload)
	})


	if(response.ok){
		const releasedProduct = await response.json()
		console.log(releasedProduct, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		dispatch(addOne(releasedProduct))
	}
	else{
		return await response.json()
	}
}

export const editProduct = (payload, productId) => async(dispatch) => {
	const response = await fetch(`/api/shops/${productId}/products`, {
		method:'PUT',
		headers:{
			"Content-Type" : "application/json",
		},
		body:JSON.stringify(payload)
	})

	if(response.ok){
		const updatedProduct = await response.json()
		dispatch(editOne(updatedProduct))
	}
	else{
		return await response.json()
	}
}

//-------------------------------------------REDUCER------------------------------------------
function productsReducer(state = {}, action) {
	switch (action.type) {
		case GET_ALL:
			return {
                ...state,
                ...action.payload
            }

        case ADD_PRODUCT:
            return{
				...state,
				// action.payload.id : action.payload
			}

		case EDIT_PRODUCT:
			return{
				...state,
				...action.payload
			}

		case DELETE_PRODUCT:
			return {
				...state
			}

		default:
			return state;
	}
}

export default productsReducer
