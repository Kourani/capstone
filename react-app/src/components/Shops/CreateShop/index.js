

import React, { useState } from "react";
import { useParams } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";


import * as shopActions from "../../../store/shop"



function CreateShop(){

    const dispatch = useDispatch()

    const [address, setAddress] = useState("");
    const [city, setCity] = useState("");
    const [state, setState] = useState("");
    const [country, setCountry] = useState("")
    const [currency, setCurrency] = useState("")
    const [name, setName] = useState("")

    const [errors, setErrors] = useState([]);

      const payload = {
        address:address,
        city:city,
        state:state,
        country:country,
        currency:currency,
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
          <h1>Create Shop</h1>
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

            <label>
              Accepted Currency
              <input
                type="text"
                value={currency}
                onChange={(e) => setCurrency(e.target.value)}
                required
              />
            </label>

            <label>
              Shop Name
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
              />
            </label>

            <button type="submit">Create</button>
          </form>
        </>
      );
    }

export default CreateShop