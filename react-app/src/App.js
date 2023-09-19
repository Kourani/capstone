import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

import AllProducts from "./components/Products/AllProducts";
import ProductDetails from "./components/Products/ProductDetails";
import AllShops from "./components/Shops/AllShops"

import OwnedShops from "./components/Shops/OwnedShops"
import EditShop from "./components/Shops/EditShop";

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



          <Route path="/products/:productId">
            <ProductDetails/>
          </Route>

          <Route path="/shops/:shopId/manage">
            <EditShop/>
          </Route>

          <Route path="/shops/manage">
            <OwnedShops/>
          </Route>

          <Route path="/shops">
            <AllShops/>
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
