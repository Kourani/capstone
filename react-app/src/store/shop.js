

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

const deleteOne = (shopId) => ({
	type: DELETE_SHOP,
	shopId //can call it any variable
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

	const response = await fetch(`/api/shops/`, {
		method:"POST",
		headers:{
			"Content-Type":"application/json"
		},
		body:JSON.stringify(payload)
	})
	if(response.ok){
		const releasedShop= await response.json()
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
		dispatch(editOne(updatedShop))
	}
	else{
		return await response.json()
	}
}

export const deleteShop = (shopId) => async (dispatch) =>{
	const response = await fetch(`/api/shops/${shopId}/delete`, {
		method:"DELETE",
		headers:{
			"Content-Type":"application/json"
		}
	})
	if(response.ok){
		const removedShop = await response.json()
		dispatch(deleteOne(shopId))
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
			let addition = {...state}
			addition[action.shop.id]=action.shop
			return addition

		case EDIT_SHOP:
			const edited = {...state}
			edited[action.shop.id]=action.shop
			return edited

		case DELETE_SHOP: //shop deleted from the backend but still exists on the frontEnd without a refresh 
			let newSt = {...state}
			delete newSt[action.shopId]
			return newSt

		default:
			return state;
	}
}

export default shopsReducer
