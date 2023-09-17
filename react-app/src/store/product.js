

//------------------------------------CONSTANTS--------------------------
const GET_ALL = "products/GET_ALL";
const DELETE_PRODUCT = "products/DELETE_PRODUCT";
const ADD_PRODUCT = "products/ADD_PRODUCT"


//-----------------------------------ACTIONS---------------------------------------
const getAll = (all) => ({
    type:GET_ALL,
    payload:all
})

const deleteOne = () => ({
	type: DELETE_PRODUCT,
});

const addOne =() =>({
    type: ADD_PRODUCT,
})


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
				...state
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
