
import React, { useState } from "react";
import { useParams, useHistory } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";

import * as shopActions from "../../../store/shop"


function CreateShop(){

    const dispatch = useDispatch()
    const history = useHistory()

    const [address, setAddress] = useState("");
    const [city, setCity] = useState("");
    const [state, setState] = useState("");
    const [country, setCountry] = useState("")
    const [currency, setCurrency] = useState("")
    const [name, setName] = useState("")
    const [image, setImage] = useState("")

    const [errors, setErrors] = useState({});

      const payload = {
        address,
        city,
        state,
        country,
        name,
        currency,
        image
      }

      const handleSubmit = async (e) => {

        e.preventDefault();
        const data = await dispatch(shopActions.newShop(payload));

        if (data && data?.errors) {
          console.log('inside the ifffffff')
          setErrors(data?.errors);
        }
        else{
          history.push('/shops/edit')
        }

      };

      console.log(errors.image)
      console.log(errors, 'Errors!!!!!!!!!')

      return (
        <>
          <h1 className="createProductTitle"> Create Shop</h1>
          <form className="createProductForm" onSubmit={handleSubmit}>

          <label className="labelName">
              Shop Name
              <input
                type="text"
                placeholder="Enter shop name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
              />
            </label>

            <label className="labelName">
              Address
              <input
                type="text"
                placeholder="Enter shop address"
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                required
              />
            </label>

            <label className="labelName">
              City
              <input
                type="text"
                placeholder="Enter shop city"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                required
              />
            </label>

            <label className="labelName">
              State
              <input
                type="text"
                placeholder="Enter shop state"
                value={state}
                onChange={(e) => setState(e.target.value)}
                required
              />
            </label>

            <label className="labelName">
              Country
              <input
                type="text"
                placeholder="Enter shop country"
                value={country}
                onChange={(e) => setCountry(e.target.value)}
                required
              />
            </label>

            <label className="labelName">
              Accepted Currency
              <input
                type="text"
                placeholder="Enter accepted currency"
                value={currency}
                onChange={(e) => setCurrency(e.target.value)}
                required
              />
            </label>

            <label className="labelName">
              Shop Image
              <input
                type="text"
                placeholder="Enter shops backdrop image"
                value={image}
                onChange={(e) => setImage(e.target.value)}
                required
              />
            </label>

            <div className="errors">{errors?.image ? errors?.image : null}</div>

            <button type="submit">Create</button>
          </form>
        </>
      );
    }

export default CreateShop
