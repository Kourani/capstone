

//------------------------------------CONSTANTS--------------------------
const GET_ALL = "shops/GET_ALL";
const ADD_SHOP = "shops/ADD_SHOP"
const DELETE_SHOP = "shops/DELETE_SHOP";



//-----------------------------------ACTIONS---------------------------------------
const getAll = (all) => ({
    type:GET_ALL,
    payload:all
})

const addOne =(shop) =>({
    type: ADD_SHOP,
	shop
})

const deleteOne = () => ({
	type: DELETE_SHOP,
});



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

export const newShop = (payload) => async (dispatch) => {

	const response = await fetch(`/api/shops`, {
		method:"POST",
		headers:{
			"Content-Type":"application/json"
		},
		body:JSON.stringify(payload)
	})
	if(response.ok){
		const releasedShop= await response.json()
		console.log(releasedShop, 'releasedShop')
		dispatch(addOne(releasedShop))
	}
	else{
		return await response.json()
	}
}

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
