
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { useModal } from "../../../context/Modal";
import * as shopActions from "../../../store/shop"
import "./EditShop.css"



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
    const [image, setImage] = useState(shopState[shopId.shopId]?.image)
    const [errors, setErrors] = useState({});

      const payload = {
        address:address,
        city:city,
        state:state,
        country:country,
        name:name,
        currency:currency,
        image
      }


      const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await dispatch(shopActions.editShop(payload, shopId.shopId));

        if (data && data.errors) { //because there is no return in the response.ok
          setErrors(data.errors);
        }
        else{
          closeModal()
        }
        setClicked('True')

      };

      return (
        <>

          <form onSubmit={handleSubmit}>

            <div className="modalsInside">
              <h1 className="modalHeader"> Edit {name}</h1>

              <label className="labelName">
                Shop Name <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                />
              </label>

              <label className="labelName">
                Address <input
                  type="text"
                  value={address}
                  onChange={(e) => setAddress(e.target.value)}
                  required
                />
              </label>

              <label className="labelName" >
                City <input
                  type="text"
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  required
                />
              </label>

              <label className="labelName" >
                State <input
                  type="text"
                  value={state}
                  onChange={(e) => setState(e.target.value)}
                  required
                />
              </label>

              <label className="labelName" >
                Country <input
                  type="text"
                  value={country}
                  onChange={(e) => setCountry(e.target.value)}
                  required
                />
              </label>

              <label className="labelName" >
                Accepted Currency <input
                  type="text"
                  value={currency}
                  onChange={(e) => setCurrency(e.target.value)}
                  required
                />
              </label>

              <label className="labelName">
                Shop Image <input
                  type="text"
                  value={image}
                  onChange={(e) => setImage(e.target.value)}
                  required
                />
              </label>

              <div className="errors">{errors?.image ? errors?.image : null}</div>

              <button type="submit">Update</button>
            </div>
          </form>
        </>
      );
    }

export default EditShop
