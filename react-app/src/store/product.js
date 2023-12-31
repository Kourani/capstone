

//------------------------------------CONSTANTS--------------------------
const GET_ALL = "products/GET_ALL";
const ADD_PRODUCT = "products/ADD_PRODUCT";
const EDIT_PRODUCT = "products/EDIT_PRODUCT";
const DELETE_PRODUCT = "products/DELETE_PRODUCT";
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

const deleteOne = (product) => ({
	type: DELETE_PRODUCT,
	product
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
		dispatch(addOne(releasedProduct))
	}
	else{
		// const key = await response.json()
		// console.log(key)
		return await response.json()
	}
}

export const editProduct = (payload, productId) => async(dispatch) => {
	const response = await fetch(`/api/products/${productId}/edit`, {
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

export const deleteProduct = (productId) => async (dispatch) => {
	const response = await fetch(`/api/products/${productId}`, {
		method:'DELETE',
		headers:{
			'Content-Type': "application/json"
		}
	})

	if(response.ok){
		dispatch(deleteOne(productId))
	}

	else{
		return await response.json
	}
}

//-------------------------------------------REDUCER------------------------------------------
function productsReducer(state = {}, action) {
	switch (action.type) {
		case GET_ALL:
			let newState = {...state}
			action.payload.products.forEach(element=>{
				newState[element.id]=element
			})
			return newState

        case ADD_PRODUCT:
            let addition = {...state}
			addition[action.payload.id]=action.payload
			return addition

		case EDIT_PRODUCT:
			let edited = {...state}
			edited[action.payload.id]=action.payload
			return edited

		case DELETE_PRODUCT:
			let newSt={...state}
			delete newSt[action.product]
			return {
				...newSt
			}

		default:
			return state;
	}
}

export default productsReducer
