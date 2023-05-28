import { writable, derived } from 'svelte/store';

interface Order {
    id: number;
    store: string;
    buyer: string;
    product: string;
    acp: {
        id: number,
        name: string,
        city: string,
        status: string,
    }
    status: string;
    createdDateTime: Date;
    approvedDateTime: Date;
    estimatedDeliveryDateTime: Date;
    deliveredDeliveryDateTime: Date;
    pickedUpDateTime: Date;
  }
  
  
  /** Store for your data. 
  This assumes the data you're pulling back will be an array.
  If it's going to be an object, default this to an empty object.
  **/
  export const orders = writable<Order[]>([]);