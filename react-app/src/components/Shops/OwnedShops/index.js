

import React, { useState, useEffect, useRef} from "react";
import * as shopActions from "../../../store/shop"
import { useDispatch, useSelector } from "react-redux";
import {useHistory} from "react-router-dom"

import OpenModalButton from "../../OpenModalButton";
import { useModal } from "../../../context/Modal";
import EditShop from "../EditShop"
import DeleteShop from "../DeleteShop"
import "./OwnedShops.css"


function OwnedShops(){

    const { closeModal } = useModal();
    const [showMenu, setShowMenu] = useState(false);
    const ulRef = useRef();

    const closeMenu = (e) => {
        if (!ulRef.current.contains(e.target)) {
          setShowMenu(false);
        }
      };

    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(() =>{
        dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state.shop)
    const userState = useSelector(state=>state.session)

    console.log("user", userState?.user?.id);
    console.log(shopState, 'statettttttt')


    function editShop(shopId){
        return(
        <OpenModalButton
        buttonText="Edit Shop"
        onItemClick={closeMenu}
        modalComponent={<EditShop shopId={shopId}/>}
        />)
    }

    function deleteShop(shopId){
        return(
        <OpenModalButton
        buttonText="Delete Shop"
        onItemClick={closeMenu}
        modalComponent={<DeleteShop shopId={shopId}/>}
        />)
    }

    function ownedShops(){
        const elementsArray = Object.values(shopState)
        return elementsArray.map(element =>{
            if(userState?.user?.id === element?.ownerId){
                return (
                    <>
                        <div className="allContentShops">
                            <div className="buttonContentOwned">
                                <img className='productImage' src={element.image} alt='Image'/>
                                <div>Name: {element.name}</div>
                                <div>Address: {element.address}</div>
                                <div>City: {element.city}</div>
                                <div>State: {element.state}</div>
                                <div>Country: {element.country}</div>
                                <div>Accepted Currency: {element.currency}</div>
                            </div>
                            <div className="buttonsOwned">
                                {editShop(element.id)}
                                {deleteShop(element.id)}
                                <button onClick={()=>{history.push(`/shops/${element.id}/products/manage`)}}> View/Manage Products </button>
                            </div>
                        </div>
                    </>
                )
            }
        })
    }

    return(
        <>

        <div className="shopsOwned">{ownedShops()}</div>
        </>
    )
}

export default OwnedShops
