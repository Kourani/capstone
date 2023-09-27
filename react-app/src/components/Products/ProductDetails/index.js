

import "./ProductDetails.css"
import * as productActions from "../../../store/product"
import * as shopActions from "../../../store/shop"
import * as commentActions from "../../../store/comment"
import * as userActions from '../../../store/session'

import React,  { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams, useHistory } from "react-router-dom"

function ProductDetails(){

    const {productId} = useParams()
    const dispatch = useDispatch()
    const history = useHistory()

    useEffect(()=>{
        dispatch(productActions.getProducts())
        dispatch(shopActions.getShops())
        dispatch(commentActions.getComments())
        dispatch(userActions.getUsers())
    }, [dispatch])

    const userState = useSelector(state=>state?.session)
    const productState = useSelector(state=>state?.product)
    const shopState = useSelector(state=>state?.shop)
    const commentState = useSelector(state=>state?.comment)

    const productElements = Object.values(productState)
    const commentElements = Object.values(commentState)

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

    function productDetails(){
        // const foundProduct = productState?.products?.find(element=>element.id === parseInt(productId))
        return(
            <div className="productDetails">
                <img className="productImageOnDetails"
                                src={productState[productId]?.image ? productState[productId]?.image : "https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg"}
                                alt="Image"
                />

                <div>
                    <div> ${productState[productId]?.price}</div>
                    <div>{productState[productId]?.description}</div>
                    <div>{shopState[productState[productId]?.shopId]?.name}</div>
                    <p>Quantity</p>
                    <p>Color</p>
                    <button> Add to Cart </button>
                    <p>Meet your Seller</p>
                    <div>{userState[shopOwner]?.firstName} {userState[shopOwner]?.lastName}</div>
                    <div>Owner of {shopState[productState[productId]?.shopId]?.name} </div>
                    <button>Message {userState[shopOwner]?.firstName}</button>
                </div>
            </div>
        )
    }

    function otherProducts(){
        return productElements?.map(element=>{
            if(element?.shopId===productState[productId]?.shopId && productState[productId]?.id !== element?.id){
                return(
                    <button onClick={()=>{history.push(`/shops/${element.shopId}`)}}>
                         <img className="moreFromThisShopImages"
                                src={element?.image ? element?.image : "https://images.pexels.com/photos/715134/pexels-photo-715134.jpeg"}
                                alt="Image"
                        />
                        <div>{element?.name}</div>
                        <div>{element?.description}</div>
                        <div>${element?.price}</div>
                    </button>
                )
            }
        })
    }

    //checks if user is logged in and returns edit/delete buttons
    function commentButtons(){

        if(userState?.user?.id !== null){
            return (
                <>
                    <button>Edit</button>
                    <button>Delete</button>
                </>
            )
        }
    }

    //returns the comments, date posted, user icon, edit/delete buttons for each product
    function productComments(){
        return commentElements?.map(element=>{

            function owned(){
                if (userState?.user?.id === element?.userId){
                    return commentButtons()
                }
            }


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
                            {owned()}
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
            {productDetails()}

            <p>{commentCount()} Comments</p>
            {productComments()}

            <p>More from this Shop</p>
            {otherProducts()}
        </>
    )
}

export default ProductDetails
