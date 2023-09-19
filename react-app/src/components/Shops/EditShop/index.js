

import React, { useState } from "react";
import { useParams } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";


import * as shopActions from "../../../store/shop"



function EditShop(){

    const dispatch = useDispatch();
    const {shopId} = useParams()
    const shopState = useSelector(state=>state.shops)

    const [address, setAddress] = useState("");
    const [city, setCity] = useState("");
    const [state, setState] = useState("");
    const [country, setCountry] = useState("")
    const [currency, setCurrency] = useState("")
    const [errors, setErrors] = useState([]);

      const payload = {
        address,
        city,
        state,
        country,
        currency,
      }

      const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await dispatch(shopActions.getShops(payload));
        if (data) {
          setErrors(data);
        }
      };

      return (
        <>
          <h1>Edit Shop</h1>
          <form onSubmit={handleSubmit}>

            <label>
              Address
              <input
                type="text"
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                required
              />
            </label>
            
            <label>
              City
              <input
                type="password"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                required
              />
            </label>

            <button type="submit">Submit </button>
          </form>
        </>
      );
    }

export default EditShop
