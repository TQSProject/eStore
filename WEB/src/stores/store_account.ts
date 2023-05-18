import axios from 'axios';
import { derived, writable } from 'svelte/store';
import { getCookie, removeCookie } from './store_cookies';
import { PUBLIC_BASE_URL, PUBLIC_USER_PATH } from '$env/static/public';

interface UserData {
    id: number,
    email: string,
    first_name: string,
    last_name: string,
}

// Create a writable store for the account
const account = writable<UserData | null>(null);

// Define functions to update the account store
function setAccount(accountData: UserData) {
  account.set(accountData);
}

function clearAccount() {
  account.set(null);
}

const updateAccount = async () => {
    const access_token = getCookie('access_token');
    if (access_token) {
        try {
            const response = await axios.get(`${PUBLIC_BASE_URL}${PUBLIC_USER_PATH}`, {
                headers: {
                    Authorization: `Bearer ${access_token}`,
                },
            });
            setAccount(response.data)
        } catch (error) {
            console.error('Error fetching user data:', error);
        }
    }
};

updateAccount();

const logoutAccount = () => {
    clearAccount();
    removeCookie('access_token')
}

// Derive the account first name
const accountFirstName = derived(account, ($account) => {
    const { first_name } = $account || {};
    return first_name || '';
});

// Derive the account last name
const accountLastName = derived(account, ($account) => {
    const { last_name } = $account || {};
    return last_name || '';
});

// Derive the account email
const accountEmail = derived(account, ($account) => {
    const { email } = $account || {};
    return email || '';
});

// Export the store and utility functions
export {
    account,
    setAccount,
    clearAccount,
    updateAccount,
    logoutAccount,
    accountFirstName,
    accountLastName,
    accountEmail,
};
