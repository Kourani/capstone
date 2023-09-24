

//------------------------------------CONSTANTS--------------------------
const GET_ALL = "shops/GET_ALL";
const ADD_SHOP = "shops/ADD_SHOP";
const EDIT_SHOP = "shops/EDIT_SHOP";
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

const editOne = (shop) =>({
	type : EDIT_SHOP,
	shop
})

const deleteOne = (shop) => ({
	type: DELETE_SHOP,
	shop
});




//-----------------------------------------THUNKS------------------------------------

export const getShops = () => async (dispatch) => {

	const response = await fetch("/api/shops")

	if (response.ok) {
		const allShops = await response.json()
		console.log(allShops);
		dispatch(getAll(allShops));
	}
	else {
		return await response.json()
	}
};

export const newShop = (payload) => async (dispatch) => {

	const response = await fetch(`/api/shops/`, {
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

export const editShop = (payload, shopId) => async (dispatch) => {

	const response = await fetch(`/api/shops/${shopId}/edit`, {
		method:"PUT",
		headers:{
			"Content-Type":"application/json"
		},
		body:JSON.stringify(payload)
	})
	if(response.ok){
		const updatedShop= await response.json()
		console.log(updatedShop, 'updatedShop')
		dispatch(editOne(updatedShop))
	}
	else{
		return await response.json()
	}
}

export const deleteShop = (shopId) => async (dispatch) =>{
	const response = await fetch(`/api/shops/${shopId}`, {
		method:"DELETE",
		headers:{
			"Content-Type":"application/json"
		}
	})
	if(response.ok){
		const removedShop = await response.json()
		console.log(removedShop,'removedShop')
		dispatch(deleteOne(removedShop))
	}
	else {
		return await response.json()
	}
}

//-------------------------------------------REDUCER------------------------------------------
function shopsReducer(state = {}, action) {
	switch (action.type) {
		case GET_ALL:
			let newState = {...state}
			action.payload.shops.forEach(element => {
				newState[element.id]=element
			});
			return newState

        case ADD_SHOP:
            return{
				...state
			}

		case EDIT_SHOP:
			return {
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
