import { writable, derived } from 'svelte/store';

interface Product {
  id: number;
  tags: string[];
  store: string;
  image: string;
  name: string;
  description: string;
  price: string;
}


/** Store for your data. 
This assumes the data you're pulling back will be an array.
If it's going to be an object, default this to an empty object.
**/
export const products = writable<Product[]>([]);

/** Data transformation.
For our use case, we only care about the drink names, not the other information.
Here, we'll create a derived store to hold the drink names.
**/
export const productsNames = derived(products, ($stores) => {
  if ($stores){
    return $stores.map(product => product.name);
  }
  return [];
});