import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

import AllProducts from "./components/Products/AllProducts";
import ProductDetails from "./components/Products/ProductDetails";
import CreateProduct from "./components/Products/CreateProduct";
import EditProduct from "./components/Products/EditProduct"

import ShopProducts from "./components/Products/ShopProducts";
import OneShops from "./components/Shops/OneShops"
import OwnedShops from "./components/Shops/OwnedShops"
import EditShop from "./components/Shops/EditShop"
import CreateShop from "./components/Shops/CreateShop"


function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>

          <Route path="/login" >
            <LoginFormPage />
          </Route>

          <Route path="/signup">
            <SignupFormPage />
          </Route>

          <Route path="/shops/:shopId/products/new">
            <CreateProduct/>
          </Route>

          <Route path="/shops/:shopId/products">
            <ShopProducts/>
          </Route>

          <Route path="/shops/:shopId/products/manage">
            <ShopProducts/>
          </Route>

          <Route path="/shops/manage">
            <OwnedShops/>
          </Route>

          <Route path="/shops/new">
            <CreateShop/>
          </Route>

          <Route path="/shops/:shopId">
            <OneShops/>
          </Route>

          <Route path="/products/:productId">
            <ProductDetails/>
          </Route>

          <Route exact path="/">
            <AllProducts/>
          </Route>

        </Switch>
      )}
    </>
  );
}

export default App;
