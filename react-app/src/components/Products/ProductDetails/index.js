

import "./ProductDetails.css"
import * as productActions from "../../../store/product"
import * as shopActions from "../../../store/shop"
import * as commentActions from "../../../store/comment"
import * as userActions from '../../../store/session'
import OpenModalButton from '../../OpenModalButton'
import EditComment from "../../Comments/EditComment"
import DeleteComment from "../../Comments/DeleteComment"
import CreateComment from "../../Comments/CreateComment"
import * as imageActions from "../../../store/image"

import { useModal } from "../../../context/Modal"

import React,  { useEffect, useState, useRef } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams, useHistory } from "react-router-dom"

function ProductDetails(){

    const dispatch = useDispatch()
    const history = useHistory()
    const ulRef = useRef();
    const {productId} = useParams()

    const { closeModal } = useModal();
    const [showMenu, setShowMenu] = useState(false);

    const closeMenu = (e) => {
        if (!ulRef.current.contains(e.target)) {
          setShowMenu(false);
        }
      };

    useEffect(()=>{
        dispatch(productActions.getProducts())
        dispatch(shopActions.getShops())
        dispatch(commentActions.getComments())
        dispatch(userActions.getUsers())
        dispatch(imageActions.getImages())
    }, [dispatch])

    const userState = useSelector(state=>state?.session)
    const productState = useSelector(state=>state?.product)
    const shopState = useSelector(state=>state?.shop)
    const commentState = useSelector(state=>state?.comment)
    const imageState = useSelector(state=>state?.image)

    const productElements = Object.values(productState)
    const commentElements = Object.values(commentState)
    const imageElements = Object.values(imageState)

    console.log(productState[productId])
    const [bee, setBee] = useState(productState?.[productId]?.image)

    const shopOwner = shopState[productState[productId]?.shopId]?.ownerId

    const monthNames = {
        1:'Janurary',
        2:'Febuary',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
    }

    console.log(imageElements, 'imageElements!!')



    //returns details of a product
    function productDetails(){
        // const foundProduct = productState?.products?.find(element=>element.id === parseInt(productId))
        const foundImage = imageElements?.find(element=>element.productId ===parseInt(productId))
        console.log(foundImage,'foundIMage!')

        function iteration(){
            let array = []
            for(let i=1; i<11; i++){
                console.log('inside the for ')
                if(foundImage && foundImage[`image${i}`]) {
                        array.push(<div onClick={()=>{setBee(foundImage[`image${i}`]) }}> {<img className='tinyImage' src={foundImage[`image${i}`]} alt="Image"/>}</div>)
                }
            }
            return array
        }

        return(
            <div className="productDetails">

                {iteration()}

                <img className="productImageOnDetails"
                                src={bee}
                                alt="Image"
                />

                <div>
                    <div> ${productState[productId]?.price}</div>
                    <div>{productState[productId]?.description}</div>
                    <div>{shopState[productState[productId]?.shopId]?.name}</div>
                    <p>Quantity</p>
                    <p>Color</p>
                    <div className="productDetailsButtons">
                        <button className="buyItNowProductDetails">Buy it Now </button>
                        <button className="addToCartProductDetails"> Add to Cart </button>
                    </div>
                    <p>Meet your Seller</p>
                    <div>{userState[shopOwner]?.firstName} {userState[shopOwner]?.lastName}</div>
                    <div>Owner of {shopState[productState[productId]?.shopId]?.name} </div>
                    <button>Message {userState[shopOwner]?.firstName}</button>
                </div>
            </div>
        )
    }

    //returns other products for a shop
    function otherProducts(){
        return productElements?.map(element=>{
            if(element?.shopId===productState[productId]?.shopId && productState[productId]?.id !== element?.id){
                return(
                    <button className="product" onClick={()=>{history.push(`/shops/${element.shopId}`)}}>
                        <div>
                            <img className="productImage"
                                    src={element?.image ? element?.image : "https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg"}
                                    alt="Image"
                            />
                            <div className="productName">{element?.name}</div>
                            <div className="productPrice">${element?.price}</div>
                        </div>
                    </button>
                )
            }
        })
    }

    //checks if the comment belongs to the user returns edit and delete button
    function commentButtons(userId, commentId){

        if(userState?.user?.id === userId){
            return(
                <>
                    <OpenModalButton
                    buttonText="Edit"
                    onItemClick={closeMenu}
                    modalComponent={<EditComment commentId={commentId}/>}
                    />

                    <OpenModalButton
                    buttonText="Delete"
                    onItemClick={closeMenu}
                    modalComponent={<DeleteComment commentId={commentId}/>}
                    />
                </>
            )
        }
    }

    //checks if the user has no comment for the product and returns post button
    function newComment(){

        const foundUser = commentElements.find((element)=>element?.userId === userState?.user?.id)

        console.log(foundUser,'found')

        console.log(userState?.user, 'POST')
        console.log(foundUser, 'foundUsersssssssssss')
        if (userState?.user?.id && foundUser)
        {
            console.log('inside the ifffffffffff')
            return(
                <OpenModalButton
                buttonText="Post"
                onItemClick={closeMenu}
                modalComponent={<CreateComment productId={productId}/>}
                />)

        }
    }

    //returns the comments, date posted, user icon, edit/delete buttons for each product
    function productComments(){
        return commentElements?.map(element=>{

            if(element.productId === parseInt(productId)){
                let date = new Date(element.createdAt)
                let year = date.getFullYear()
                let month = date.getMonth()+1
                let day = date.getDate()

                return(

                    <div className="productComments">
                        <div>{element.comment}</div>
                        <div className="commentUserImage">
                            <img className="userImageDetails"
                                src={userState[element.userId]?.profileIcon}
                                alt='Image'
                            />
                            <div>{userState[element.userId]?.firstName} {userState[element.userId]?.lastName} {monthNames[month]} {day}, {year}</div>
                            {commentButtons(element.userId, element.id)}
                        </div>
                    </div>
                )
            }
        })

    }

    //returns the number of comments for each product
    function commentCount(){
        let count = 0
        commentElements?.forEach(element=>{
            if(element.productId === parseInt(productId)){
                count++
            }
        })
        return count
    }

    return(
        <>
            <div className="productDetailsFunction">{productDetails()}</div>

            <p className="headersProductDetails">{commentCount()} Comments</p>

            <div> {newComment()}</div>

            <div>{commentCount() >0 ? productComments() : 'We would love to hear your feedback! Be the first to share your thoughts '}</div>

            <p className="headersProductDetails">More from this Shop</p>
            <div className="shopDetailsOtherProducts">{otherProducts()} </div>
        </>
    )
}

export default ProductDetails
