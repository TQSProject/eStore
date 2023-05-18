<script>
   export let product;
   export let count;
   import {removeFromOrders, updateOrderCount} from '../stores/store_cart'
   import { getStoreSlug } from '../utils';

   const store_slug = getStoreSlug(product.store)
</script>
<tr class="item">
  <td class="img">
     <div>
        <img src="{product.image}" alt="{product.name}">
     </div>
  </td>
  <td class="desc" colspan="2">
      <span class="name">{product.name}</span>
      <br>
      <a href="/stores/{store_slug}" class="store">{product.store}</a>
      <br>
      <button class="remove-from-cart" on:click={() => removeFromOrders(product)}>Remove</button>
  </td>
  <td class="price item-price">
     <p class="item-price-final"><span class="money">{product.price}€</span></p>
  </td>
  <td class="quantity center">
     <div class="quantity-selector">
        <button class="quantity-minus" on:click={() => updateOrderCount(product, -1)}>
           <svg viewBox="0 0 20 20" class="icon icon-minus">
              <path fill="#444" d="M17.543 11.029H2.1A1.032 1.032 0 011.071 10c0-.566.463-1.029 1.029-1.029h15.443c.566 0 1.029.463 1.029 1.029 0 .566-.463 1.029-1.029 1.029z"></path>
           </svg>
        </button>
        <input disabled class="quantity-input" type="number" min="1" size="4" pattern="[0-9]*" autocomplete="off" value="{count}">
        <button class="quantity-plus" on:click={() => updateOrderCount(product, 1)}>
           <svg viewBox="0 0 20 20" class="icon icon-plus">
              <path fill="#444" d="M17.409 8.929h-6.695V2.258c0-.566-.506-1.029-1.071-1.029s-1.071.463-1.071 1.029v6.671H1.967C1.401 8.929.938 9.435.938 10s.463 1.071 1.029 1.071h6.605V17.7c0 .566.506 1.029 1.071 1.029s1.071-.463 1.071-1.029v-6.629h6.695c.566 0 1.029-.506 1.029-1.071s-.463-1.071-1.029-1.071z"></path>
           </svg>
        </button>
     </div>
  </td>
</tr>

<style>
   .name {
      font-weight: 400;
   }
   .store {
      font-size: 14px;
      cursor: pointer;
      padding: 6px 0 1px;
      color: rgba(0, 0, 0, .75);
   }
   .store:hover {
      border-bottom: 1px solid #2b2b2b;
      color: rgba(0, 0, 0, .85);
   }
   .quantity-selector {
      float: right;
      display: block;
      position: relative;
      max-width: 7.5rem;
      padding-right: 0;
   }
   .quantity-plus, .quantity-minus {
      position: absolute;
      top: 0;
      height: 100%;
      width: 40%;
      display: flex;
      align-items: center;
      cursor: pointer;
      background: none;
      border: none;
      appearance: none;
      outline: none;
   }
   .quantity-minus {
      left: 0;
      justify-content: flex-start;
      padding-left: 10px;
   }
   .quantity-plus {
      right: 0;
      justify-content: flex-end;
      padding-right: 10px;
   }
   input.quantity-input {
      padding: 9px 28px;
      font-size: 1em;
      text-align: center;
      color: black !important;
      width: 100%;
   }
   .quantity-plus svg, .quantity-minus svg {
      width: 12px;
      height: 12px;
      color: black;
      display: inline-block;
      vertical-align: middle;
   }
   .desc {
      word-break: break-word;
   }
   .desc .remove-from-cart {
      display: block;
      font-size: 0.875em;
      opacity: .7;
   }
   .remove-from-cart {
      text-transform: uppercase;
      color: #e91a47 !important;
      border: 1px solid #E91A47;
      padding: 4px;
      margin-top: 20px;
      line-height: 1.5;
      width: fit-content;
      cursor: pointer;
      background: none;
      outline: none;
      appearance: none;
   }
   img {
      min-height: 50px;
      max-width: 100%;
   }
   td {
      font-size: 1em;
      border-top: none;
      border-left: none;
      border-right: none;
      padding: 10px 4px;
      line-height: 1.5;
      margin: 0 0 0.5em;
      vertical-align: middle;
      font-weight: 300;
      letter-spacing: 1px;
   }
</style>