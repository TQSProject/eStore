import { writable, type Writable } from 'svelte/store';
import Cookies from 'js-cookie';

interface CookiesData {
  [key: string]: string;
}

// Define a writable store for cookies
const cookieStore: Writable<CookiesData> = writable({});

// Function to set a cookie
const setCookie = (name: string, value: string, options?: Cookies.CookieAttributes): void => {
  Cookies.set(name, value, options);
};

// Function to remove a cookie
const removeCookie = (name: string, options?: Cookies.CookieAttributes): void => {
  Cookies.remove(name, options);
};

// Function to get the value of a specific cookie
const getCookie = (name: string): any => {
  return Cookies.get(name)
};

// Export the store and utility functions
export {
  cookieStore,
  setCookie,
  removeCookie,
  getCookie
};
