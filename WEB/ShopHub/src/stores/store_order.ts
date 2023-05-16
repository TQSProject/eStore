import { persisted } from 'svelte-local-storage-store';
import { writable } from 'svelte/store';

export const orders = persisted('orders', {});
export const orderCount = writable(0);

orders.subscribe((value: Record<string, number>) => {
    orderCount.set(value ? Object.values(value).reduce((a, b) => a + b, 0) : 0);
});

export const addToOrders = (object) => {
    orders.update(ordersValue => {
        const key = JSON.stringify(object); // convert object to string
        if (ordersValue && ordersValue[key]) {
            ordersValue[key]++;
        } else {
            ordersValue = {
            ...ordersValue,
            [key]: 1,
            };
        }
        return ordersValue;
    });
}

export const removeFromOrders = (object) => {
    orders.update(ordersValue => {
        const key = JSON.stringify(object);
        if (ordersValue && ordersValue[key]) {
            delete ordersValue[key];
        }
        return ordersValue;
    });
}
  
export const updateOrderCount = (object, count) => {
    orders.update(ordersValue => {
        const key = JSON.stringify(object);
        if (ordersValue && ordersValue[key]) {
            let orderCount = ordersValue[key];
            orderCount += count;
            if (orderCount < 1) {
                delete ordersValue[key];
            }
            else {
                ordersValue[key] = orderCount;
            }
        } else {
            ordersValue = {
                ...ordersValue,
                [key]: count,
            };
        }
        return ordersValue;
    });
  }