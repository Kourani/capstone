import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";

import { authenticate } from "./store/session";

import ProtectedRoute from "./components/auth/ProtectedRoute"
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import Navigation from "./components/Navigation";
import Footer from "./components/Footer"

import AllProducts from "./components/Products/AllProducts";
import ProductDetails from "./components/Products/ProductDetails";
import CreateProduct from "./components/Products/CreateProduct";
import ShopProducts from "./components/Products/ShopProducts";
import CircleProducts from "./components/Products/CircleProducts";

import OneShops from "./components/Shops/OneShops"
import OwnedShops from "./components/Shops/OwnedShops"
import CreateShop from "./components/Shops/CreateShop"

import AllFavorites from "./components/Favorites/allFavorites";

import Cart from "./components/Cart"



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

          <Route path="/favorites">
              <AllFavorites/>
          </Route>

          <Route path="/login" >
            <LoginFormPage />
          </Route>

          <Route path="/signup">
            <SignupFormPage />
          </Route>

          <ProtectedRoute path="/shops/edit">
            <OwnedShops/>
          </ProtectedRoute>

          <ProtectedRoute path="/shops/new">
            <CreateShop/>
          </ProtectedRoute>

          <Route path="/cart">
            <Cart/>
          </Route>

          <ProtectedRoute path="/shops/:shopId/products/new">
            <CreateProduct/>
          </ProtectedRoute>

          <ProtectedRoute path="/shops/:shopId/products/edit">
            <ShopProducts/>
          </ProtectedRoute>

          <ProtectedRoute path="/shops/:shopId/products">
            <ShopProducts/>
          </ProtectedRoute>

          <Route path="/shops/:shopId">
            <OneShops/>
          </Route>


          <Route path="/products/categories/:category">
            <CircleProducts/>
          </Route>

          <Route path="/products/:productId">
            <ProductDetails/>
          </Route>

          <Route exact path="/">
            <AllProducts/>
          </Route>

        </Switch>

      )}
      <Footer isLoaded={isLoaded} />
    </>
  );
}

export default App;
