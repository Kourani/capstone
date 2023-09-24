

import React, {useEffect, useState, useRef} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import OpenModalButton from "../../OpenModalButton";
import { useModal } from "../../../context/Modal";
import * as productActions from "../../../store/product";
import DeleteProduct from "../DeleteProduct";
import EditProduct from "../EditProduct"

function ShopProducts(){

    const dispatch = useDispatch()
    const {shopId} = useParams()
    const {closeModal} = useModal()

    const [showMenu, setShowMenu] = useState(false);
    const ulRef = useRef();

    const closeMenu = (e) => {
        if (!ulRef.current.contains(e.target)) {
          setShowMenu(false);
        }
      };

    useEffect(()=>{
        dispatch(productActions.getProducts())
    },[dispatch])

    const productState = useSelector(state=>state.product)
    const productElements = Object.values(productState)

    function deleteProduct(productId){
        return(
        <OpenModalButton
        buttonText="Delete Product"
        onItemClick={closeMenu}
        modalComponent={<DeleteProduct productId={productId}/>}
        />)
    }

    function editProduct(productId){
        return(
        <OpenModalButton
        buttonText="Edit Product"
        onItemClick={closeMenu}
        modalComponent={<EditProduct productId={productId}/>}
        />)
    }

    function findProducts(){
        return productElements.map(element=>{
            if(element.shopId === parseInt(shopId)){
                return(
                    <div className="ownedProducts">
                    <div> {element.name} </div>
                    <div> {element.description} </div>
                    <div> {element.category} </div>
                    <div> {element.price} </div>
                    {editProduct(element.id)}
                    {deleteProduct(element.id)}
                    </div>
                )
            }
        })

    }

    return (
        <>
        {findProducts()}
        </>
    )

}

export default ShopProducts
