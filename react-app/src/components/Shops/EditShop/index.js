
import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";

import * as shopActions from "../../../store/shop"


function EditShop(){

    const dispatch = useDispatch()
    const history = useHistory()
    const {shopId} = useParams()

    console.log(shopId,'!!!!!!!!!!!!!!!!!!!!!')

    useEffect(()=>{
      dispatch(shopActions.getShops())
    },[dispatch])

    const shopState = useSelector(state=>state.shop)
    console.log(shopState)
    console.log(shopState[shopId],'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    const [address, setAddress] = useState(shopState[shopId]?.address);
    const [city, setCity] = useState(shopState[shopId]?.city);
    const [state, setState] = useState(shopState[shopId]?.state);
    const [country, setCountry] = useState(shopState[shopId]?.country)
    const [currency, setCurrency] = useState(shopState[shopId]?.currency)
    const [name, setName] = useState(shopState[shopId]?.name)

    const [errors, setErrors] = useState([]);

      const payload = {
        address:address,
        city:city,
        state:state,
        country:country,
        name:name,
        currency:currency,
      }

      const handleSubmit = async (e) => {

        e.preventDefault();
        const data = await dispatch(shopActions.editShop(payload, shopId));
        if (data) {
          setErrors(data);
        }

        history.push('/shops/manage')
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
                value={state}
                onChange={(e) => setState(e.target.value)}
                required
              />
            </label>

            <label>
              Country
              <input
                type="text"
                value={country}
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

            <button type="submit">Update</button>
          </form>
        </>
      );
    }

export default EditShop
