

import React, { useState } from "react";
import { useParams } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";


import * as shopActions from "../../../store/shop"



function EditShop(){

    const dispatch = useDispatch();
    const {shopId} = useParams()
    const shopState = useSelector(state=>state?.shop)

    console.log(shopState,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    const [address, setAddress] = useState(`${shopState?.shops[shopId]?.address}`);
    const [city, setCity] = useState(`${shopState?.shops[shopId]?.city}`);
    const [state, setState] = useState(`${shopState?.shops[shopId]?.state}`);
    const [country, setCountry] = useState(`${shopState?.shops[shopId]?.country}`)
    const [currency, setCurrency] = useState(`${shopState?.shops[shopId]?.currency}`)
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
                type="text"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                required
              />
            </label>

            <label>
              State
              <input
                type="text"
                value={city}
                onChange={(e) => setState(e.target.value)}
                required
              />
            </label>

            <label>
              Country
              <input
                type="text"
                value={city}
                onChange={(e) => setCountry(e.target.value)}
                required
              />
            </label>


            <button type="submit">Submit </button>
          </form>
        </>
      );
    }

export default EditShop
