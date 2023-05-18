import { writable, derived } from 'svelte/store';

export interface ProductType {
  id: number;
  slug: string;
  name: string;
  image: string;
  address: string;
  phone_number: string;
  type: string;
  // Add any additional properties here
}

/** Store for your data. 
This assumes the data you're pulling back will be an array.
If it's going to be an object, default this to an empty object.
**/
export const stores = writable<ProductType[]>([]);

/** Data transformation.
For our use case, we only care about the drink names, not the other information.
Here, we'll create a derived store to hold the drink names.
**/
export const storeNames = derived(stores, ($stores) => {
  if ($stores){
    return $stores.map(store => store.name);
  }
  return [];
});