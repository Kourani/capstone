
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { useModal } from "../../../context/Modal";
import * as shopActions from "../../../store/shop"



function EditShop(shopId){

    const dispatch = useDispatch()
    const {closeModal} = useModal()
    const [clicked, setClicked] = useState('False')

    useEffect(()=>{
      dispatch(shopActions.getShops())
    },[dispatch,clicked])

    const shopState = useSelector(state=>state.shop)
    const [address, setAddress] = useState(shopState[shopId.shopId]?.address);
    const [city, setCity] = useState(shopState[shopId.shopId]?.city);
    const [state, setState] = useState(shopState[shopId.shopId]?.state);
    const [country, setCountry] = useState(shopState[shopId.shopId]?.country)
    const [currency, setCurrency] = useState(shopState[shopId.shopId]?.currency)
    const [name, setName] = useState(shopState[shopId.shopId]?.name)
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
        const data = await dispatch(shopActions.editShop(payload, shopId.shopId));
        if (data) {
          setErrors(data);
        }

        setClicked('True')
        closeModal()
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
