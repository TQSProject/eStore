<script>
   import CartProductCard from "./CartProductCard.svelte";
   import { orders, orderCount } from "../stores/store_order"
   import { onMount } from "svelte";
    import { get } from "svelte/store";

   let orders_ = {};
   let totalPrice = 0;

   const calculateTotalPrice = () => {
      totalPrice = Object.entries(orders_).reduce((total, [key, value]) => {
         const { price } = JSON.parse(key);
         return total + value * price;
      }, 0);
   }

   orders.subscribe(value => {
      orders_ = value;
      calculateTotalPrice();
   });

</script>
<div class="page-fullwidth cart">
   {#if $orderCount != 0}
      <div class="just">
         <div class="cart-outer">
            <table>
               <thead>
                  <tr class="top-row">
                     <th class="img">&nbsp;</th>
                     <th class="desc" colspan="2">Product</th>
                     <th>Price</th>
                     <th class="center">Quantity</th>
                  </tr>
               </thead>
               <tbody>
                  {#each Object.entries(orders_) as [order, orderCount]}
                     <CartProductCard product={JSON.parse(order)} count={orderCount}/>
                  {/each}
               </tbody>
            </table>
         </div>
         <div class="cart-info-container">
            <h1 class="info-subtotal">
               <span>Subtotal:</span>
               <span class="money">{totalPrice.toFixed(2)}€</span>
            </h1>
            <button class="btn-checkout">check out</button>
            <small>before taxes and shipping costs</small>
         </div>
      </div>
      <a class="cart-foot" href="/stores">
         Continue Shopping
      </a>
   {:else}
      <div class="empty-outer">
         <center>
            <div class="empty">
              <p class="gutter-bottom">Your cart is currently empty.</p>
              <a href="/stores" class="btn-shopping">Continue Shopping</a>
            </div> 
         </center>
      </div>
   {/if}
</div>
<style>
   .page-fullwidth {
      max-width: 100%;
      margin-top: -16px;
      padding: 40px 100px;
      color: #000;
      min-height: 60vh;
   }
   .cart {
      width: auto;
      position: relative;
      margin: 20px auto 0;
      overflow: visible;
      display: block;
   }
   .empty-outer {
      text-align: center!important;
      margin-top: 20px;
   }
   .cart .empty {
      text-align: center;
   }
   .gutter-bottom {
      padding-bottom: 50px;
   }
   .cart-outer {
      width: 68%;
   }
   .cart a {
      text-decoration: none;
      color: black !important;
   }
   .btn-shopping {
      padding: 20px;
      background-color: rgba(255, 255, 255, 0);
      border: 1px solid #e91a47;
      box-shadow: none;
      max-width: 300px;
      border-radius: 0px;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      vertical-align: middle;
      white-space: nowrap;
      appearance: none;
      line-height: 1.5;
      transition: all 0.15s ease;
      display: inline-block;
      width: 100%;
   }
   .btn-shopping:hover {
      background-color: #e91a47;
      border: 1px solid #e91a47;
   }
   .just {
      display: flex;
      justify-content: space-between;
   }
   .just > * {
      display: inline-block;
      text-align: left;
      vertical-align: top;
      font-size: 1rem;
   }
   .cart-info-container {
      text-align: left;
      width: 25%;
      margin: 20px 0;
   }
   .cart table {
      margin: 20px 0px;
      width: 100%;
      border: 0;
      table-layout: fixed;
      border-collapse: collapse;
      border-spacing: 0;
   }
   table tr > th {
      padding: 10px;
      vertical-align: middle;
   }
   .cart table th {
      font-size: 1em;
      border-right: 0;
      text-transform: uppercase;
      font-weight: 500;
      line-height: 1.5;
      margin: 0 0 0.5em;
   }
   .cart table thead th:last-child {
      text-align: right;
   }
   .btn-checkout {
      width: 100%;
      margin-top: 50px;
      font-weight: 700;
      padding: 15px;
      font-size: 22px;
      font-family: inherit;
      letter-spacing: 1px;
      text-transform: uppercase;
      cursor: pointer;
      background: #e91a47;
      color: #fff;
      text-decoration: none;
      text-align: center;
      vertical-align: middle;
      white-space: nowrap;
      border: 0;
      border-radius: 0px;
      appearance: none;
      line-height: 1.5;
      transition: all 0.15s ease;
      display: inline-block;
   }
   .btn-checkout:hover {
      background: #d5143e;
   }
   .cart-foot {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      border-left: none;
      border-right: none;
      border-top: none;
      border-radius: 0;
      background-color: rgba(255, 255, 255, 0);
      text-decoration: none !important;
      cursor: pointer;
      border-bottom: 1px solid #a4a4a4;
      padding: 0 0 3px;
      transition: all 0.25s ease-in;
      width: fit-content;
   }
   .cart-foot:hover {
      border-bottom: 1px solid #2b2b2b;
   }
   .cart-info-container {
      text-align: left;
      width: 25%;
      margin: 20px 0;
   }
   .info-subtotal {
      font-size: 1.8rem;
      line-height: 1.1;
      font-style: normal;
      font-weight: 500;
      margin: 0 0 0.5em 0;
      text-transform: uppercase;
   }
</style>