
import {React} from "react"

import * as additionalFunctions from "../../context/additional"

import "./Cart.css"

export default function Cart(){
    return(
        <>
        <div className="cartPage">
        Add items to your cart
        <button onClick={()=>additionalFunctions.comingSoon()}>Continue Shopping</button>
        <button onClick={()=>additionalFunctions.comingSoon()}>Checkout</button>
        </div>
        </>
    )
}
