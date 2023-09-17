

//------------------------------------CONSTANTS--------------------------
const GET_ALL = "shops/GET_ALL";
const DELETE_SHOP = "shops/DELETE_PRODUCT";
const ADD_SHOP = "shops/ADD_PRODUCT"


//-----------------------------------ACTIONS---------------------------------------
const getAll = (all) => ({
    type:GET_ALL,
    payload:all
})

const deleteOne = () => ({
	type: DELETE_SHOP,
});

const addOne =() =>({
    type: ADD_SHOP,
})


//-----------------------------------------THUNKS------------------------------------

export const getShops = () => async (dispatch) => {

	const response = await fetch("/api/shops")

	if (response.ok) {
		const allShops = await response.json()
		dispatch(getAll(allShops));
	}
	else {
		return await response.json()
	}
};

//-------------------------------------------REDUCER------------------------------------------
function shopsReducer(state = {}, action) {
	switch (action.type) {
		case GET_ALL:
			return {
                ...state,
                ...action.payload
            }

        case ADD_SHOP:
            return{
				...state
			}

		case DELETE_SHOP:
			return {
				...state
			}

		default:
			return state;
	}
}

export default shopsReducer
