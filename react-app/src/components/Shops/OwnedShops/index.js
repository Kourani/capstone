

import React, { useState, useEffect, useRef} from "react";
import * as shopActions from "../../../store/shop"
import { useDispatch, useSelector } from "react-redux";
import {useHistory} from "react-router-dom"

import OpenModalButton from "../../OpenModalButton";
import { useModal } from "../../../context/Modal";
import EditShop from "../EditShop"


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


    function toOpen(){
        return(
        <OpenModalButton
        buttonText="Edit Shop"
        onItemClick={closeMenu}
        modalComponent={<EditShop/>}
        />)
    }

    function ownedShops(){
        const elementsArray = Object.values(shopState)
        return elementsArray.map(element =>{
            if(userState?.user?.id === element?.ownerId){
                return (
                    <>
                    <button onClick={()=>{history.push(`/shops/${element.id}/products/manage`)}}>
                    <div>{element.address}</div>
                    <div> {element.currency}</div>
                    </button>
                    {toOpen()}
                    <button> Delete Shop </button>
                    </>
                )
            }
        })
    }

    return(
        <>

        <div>{ownedShops()}</div>
        </>
    )
}

export default OwnedShops
