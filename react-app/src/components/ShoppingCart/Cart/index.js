
import {React} from "react"
import { useSelector } from "react-redux"
import { useHistory } from "react-router-dom"

import * as additionalFunctions from "../../../context/additional"

import "./Cart.css"

export default function Cart(){

    const history = useHistory()

    const cartState = useSelector(state=>state.cart)

    const cartElements = Object.values(cartState)

    function cartDisplay(){
        if(cartElements.length > 0){
            return cartElements.map(element=>{
                return (
                    <div className="newestProd">
                        <img className="productImage" src={element.image} alt=""/>
                        <div className="cartName">{element.name}</div>
                        <div className="cartPrice">${element.price}</div>
                    </div>
                )

            }) 
        }
    }

    return(
    

        cartElements.length>0 ? 

        <>
        <div className="cartNews">
            <button className="universalModalButtons" onClick={()=>{history.push('/')}}>Continue Shopping</button>
            <button className="universalModalButtons" onClick={()=> {history.push('/cart/review/shipping')}}>Checkout</button>
        </div>
        <div className="allProducts"> {cartDisplay()}</div>
        </>
            :

        <div className="cartPage">
            Your shopping bag is currently empty
            <div className="cartNews">
            <button className="universalModalButtons" onClick={()=>{history.push('/')}}>Continue Shopping</button>
            {/* <button className="universalModalButtons" onClick={()=>{history.push('/cart/review/shipping')}}>Checkout</button> */}
            </div>
        </div>

        
    )
}
