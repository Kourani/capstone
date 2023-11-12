
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
        dispatch(shopActions.getShops())
    },[dispatch])

    const productState = useSelector(state=>state.product)
    const productElements = Object.values(productState)

    const userState = useSelector(state=>state.session)
    const shopState = useSelector(state=>state.shop)

    const shopElements = Object.values(shopState)

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


    const foundShop = shopElements.find(element=>element.id === parseInt(shopId) && element.ownerId === userState?.user?.id)



    function findProducts(){
        if(foundShop){
            return productElements?.map(element=>{
                if(element?.shopId === parseInt(shopId)){

                    return(



                        <div className="ownedProducts">
                            
                            <div className="approxWidth">
                                <img className='imageShopProducts' onClick={()=>{history.push(`/products/${element.id}`)}} src={element?.image} alt="Image"/>
                            </div>

                            {/* <div className="imageButtons">
                                <div className="approxWidth">{[element.image1]}</div>
                            </div> */}

                            <div className="approxWidth"> {element?.image5 ? '5 Images' : element?.image4 ? '4 Images' : element?.image3 ? '3 Images' : element?.image2 ? '2 Images' : element?.image1 ? '1 Image' : 'No sides images have been added. Edit product to upload more images.'} </div>
                            <div className="approxWidth"> {element?.name} </div>
                            <div className="approxWidth"> {element?.description} </div>
                            <div className="approxWidth" > {element?.category} </div>
                            <div className="approxWidth"> ${element?.price} </div>

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

            {foundShop ? <button className='uniOneButton' onClick={()=>{history.push(`/shops/${shopId}/products/new`)}}> Add a New Product </button> : null}

           <div className="HeadingsForEdit">
                <div className="approxWidth">Main Image</div>
                <div className="approxWidth"># of Side Images</div>
                <div className="approxWidth">Name</div>
                <div className="approxWidth">Description</div>
                <div className="approxWidth">Category</div>
                <div className="approxWidth">Price</div>
            </div>

            {findProducts()}
        </>
    )

}

export default ShopProducts
