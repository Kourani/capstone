
import "./ShopProducts.css"

import React, {useEffect, useState, useRef} from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";

import OpenModalButton from "../../OpenModalButton";
import { useModal } from "../../../context/Modal";
import DeleteProduct from "../DeleteProduct";
import EditProduct from "../EditProduct"

import * as shopActions from "../../../store/shop"
import * as productActions from "../../../store/product";
import * as imageActions from "../../../store/image"
import EditImages from "../../Images/EditImages";
import CreateImages from "../../Images/CreateImages";


function ShopProducts(){

    const dispatch = useDispatch()
    const history = useHistory()
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
        dispatch(imageActions.getImages())
        dispatch(shopActions.getShops())
    },[dispatch])

    const productState = useSelector(state=>state.product)
    const productElements = Object.values(productState)

    const userState = useSelector(state=>state.session)
    const shopState = useSelector(state=>state.shop)

    const shopElements = Object.values(shopState)

    const imageState = useSelector(state=>state.image)

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

    function editImages(productId, productName){
        return (
            <OpenModalButton
            buttonText="Edit Images"
            onItemClick={closeMenu}
            modalComponent={<EditImages productId={productId}/>}
            />
        )
    }

    function addImages(productId, productName){
        return (
            <OpenModalButton
            buttonText="Add Images"
            onItemClick={closeMenu}
            modalComponent={<CreateImages productId={productId}/>}
            />
        )
    }

    const foundShop = shopElements.find(element=>element.id === parseInt(shopId) && element.ownerId === userState?.user?.id)

    function findProducts(){
        if(foundShop){
            return productElements?.map(element=>{
                if(element?.shopId === parseInt(shopId)){
                    return(
                        <div className="ownedProducts">
                            <img className='imageShopProducts' onClick={()=>{history.push(`/products/${element.id}`)}} src={element?.image} alt="Image"/>
                            <div className="imageButtons">
                                <div>{imageState?.[element.id] ? (Object.values(imageState?.[element.id]).length - 2 ) : '0' }</div>
                                {!imageState?.[element.id] || (imageState?.[element.id] && (Object.values(imageState?.[element.id]).length - 2)<5) ? addImages(element.id, element.name) : null }
                                {imageState?.[element.id] ? <button onClick={()=>{history.push(`/products/${element.id}`)}}> View Layout </button> : null}
                                {imageState?.[element.id] ? editImages(element.id, element.name): null}
                            </div>
                            <div> {element?.name} </div>
                            <div> {element?.description} </div>
                            <div> {element?.category} </div>
                            <div> ${element?.price} </div>
                            {editProduct(element?.id)}
                            {deleteProduct(element?.id)}
                        </div>
                    )
                }
            })
        }


    }

    return (
        <>
        {foundShop ? <button onClick={()=>{history.push(`/shops/${shopId}/products/new`)}}> Add a New Product </button> : null}
        {findProducts()}
        </>
    )

}

export default ShopProducts
