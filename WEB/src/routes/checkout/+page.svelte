<script>
    import { onMount } from "svelte";
    import { clickOutside, navigate } from "../../utils";
    import { getCookie } from "../../stores/store_cookies";
    import { afterNavigate } from "$app/navigation";
    import { account } from "../../stores/store_account";
    import { orders, orderPrice } from "../../stores/store_cart"
    import axios from "axios";

    let invalidEmail = false;
    let invalidFname = false;
    let invalidLname = false;
    let invalidAddress = false;
    let invalidPhone = false;

    let subTotal = 0;
    let shipping = 0

    orders.subscribe(value => {
        subTotal = $orderPrice
    });

    let address = '';
    let phone_number = '';
    let first_name = '';
    let last_name = '';
    let email = '';

    account.subscribe(account => {
        first_name = account?.first_name;
        last_name = account?.last_name;
        email = account?.email;
    })

    let previousPage = '/' ;

    const options = [
        "Address 1",
        "Address 2",
        "Address 3",
        "Address 4",
    ]

    let filteredOptions = options;
    let showDropdown = false;
    let selectedOption = ''

    // Filter options based on the input value
    function filterOptions() {
		filteredOptions = options.filter(item => item.toLowerCase().match(address.toLowerCase()));
        if (filteredOptions.length === 0) {
            filteredOptions = options
        }	
    }

    function selectOption(option) {
        selectedOption = option;
        address = selectedOption;
        showDropdown = false;
    }

    function onEmailFocus() {
        invalidEmail = false;
    }

    function onFnameFocus() {
        invalidFname = false;
    }

    function onLnameFocus() {
        invalidLname = false;
    }

    function onPhoneFocus() {
        invalidPhone = false;
    }

    function onAddressBlur() {
        if (selectedOption && selectedOption !== address)
            address = selectedOption
        showDropdown = false;
    }

    function onAddressFocus() {
        invalidAddress = false;
        showDropdown = true;
    }

    afterNavigate(({from}) => {
        previousPage = from?.url.pathname || previousPage
    })

    onMount(() => {

        // Check if the user is already logged in
        const newPage = '/login'
        const access_token = getCookie('access_token')
        if (!access_token) {
            navigate(newPage)
        }
    })

    function checkAddress() {
        let ret = options.includes(address);

        if (!ret) {
            invalidAddress = true;
        }

        return ret;
    }

    function checkName() {
        let ret1 = first_name;
        let ret2 = last_name;

        if(!ret1) {
            invalidFname = true;
        }

        if (!ret2) {
            invalidLname = true;
        }

        return ret1 && ret2;
    }

    const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

    function checkEmail() {
        let ret = email.match(emailRegex);

        if (!ret) {
            invalidEmail = true;
        }

        return ret;
    }

    const phoneRegex = /^[0-9]{9}$/;

    function checkPhone() {
        let ret = phone_number.match(phoneRegex);

        if (!ret) {
            invalidPhone = true;
        }

        return ret;
    }

    function validate() {
        let ret1 = checkEmail();
        let ret2 = checkName();
        let ret3 = checkAddress();
        let ret4 = checkPhone();
        return ret1 && ret2 && ret3 && ret4;
    }

    function submitOrder() {
        let ret = validate();
        if (ret) {
            postOrder();
        }
    }

    const url = 

    async function postOrder() {
        try {
        const response = await axios.post(url, {
            first_name,
            last_name,
            email,
            phone_number
        });

        const { access: access_token } = response.data;
        }
        catch (error) {

        }
    }
</script>


<div class="checkout-main container">
    <div class="card-shipping-section row">
        <div class="shipping-content col-xs-12 col-sm-7 col-lg-8">
            <form class="shipping-form" novalidate>
                <div class="summary-wrapper">
                    <h2> CONTACT INFO </h2>
                    <div class="shipping-information">
                        <div class="form-wrapper">
                            <label class="form-label" for="email">Email address</label>
                            <input class:error-input={invalidEmail} on:focus={onEmailFocus} disabled type="text" class="form-input" id="email" required bind:value={email} name="email" maxlength="50">
                            {#if invalidEmail}<small class="error email-error">Invalid Email!</small>{/if}
                        </div>
                    </div>
                </div>
                <div class="shipping-address-wrapper">
                    <h2> SHIPPING ADDRESS </h2>
                    <div class="shipping-address">
                        <div class="name-wrapper row">
                            <div class="form-wrapper col-6">
                                <label class="form-label" for="lname"> First Name </label>
                                <input class:error-input={invalidFname} on:focus={onFnameFocus} disabled type="text" class="form-input" id="fname" required bind:value={first_name} name="fname" maxlength="50">
                                {#if invalidFname}<small class="error fname-error">Invalid First Name!</small>{/if}
                            </div>
                            <div class="form-wrapper col-6">
                                <label class="form-label" for="lname"> Last Name </label>
                                <input class:error-input={invalidLname} on:focus={onLnameFocus} disabled type="text" class="form-input" id="lname" required bind:value={last_name} name="lname" maxlength="50">
                                {#if invalidLname}<small class="error lname-error">Invalid Last Name!</small>{/if}
                            </div>
                        </div>
                        <div class="form-wrapper" use:clickOutside on:click_outside={onAddressBlur}>
                            <label class="form-label" for="address"> Address 1 </label>
                            <svg class="search-icon" width="19" height="19" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path fill-rule="evenodd" clip-rule="evenodd" d="M11.7867 3.75596C14.1397 6.10896 14.1397 9.92496 11.7867 12.278C9.43375 14.631 5.61775 14.631 3.26475 12.278C0.91175 9.92496 0.91175 6.10896 3.26475 3.75596C5.61775 1.40296 9.43375 1.40296 11.7867 3.75596V3.75596Z" stroke="#C3C6C8" stroke-width="2"/>
                                <path d="M13.2271 13.708L17.6801 18.161" stroke="#C3C6C8" stroke-width="2"/>
                            </svg>                                
                            <input class:error-input={invalidAddress} placeholder="Start typing your street address" type="text" class="form-input with-icon" id="address" required bind:value={address} on:input={filterOptions} on:focus={onAddressFocus} name="address" maxlength="50">
                            {#if invalidAddress}<small class="error address-error">Invalid Address!</small>{/if}
                            {#if showDropdown}
                                <div class="dropdown">
                                    <ul>
                                        {#each filteredOptions as option}
                                            <li><button on:click|preventDefault|stopPropagation={() => selectOption(option)}>{option}</button></li>
                                        {/each}
                                    </ul>
                                </div>
                            {/if}
                        </div>
                        <div class="form-wrapper">
                            <label class="form-label" for="phone"> Phone Number </label>
                            <input placeholder="e.g., 932123456" class:error-input={invalidPhone} on:focus={onPhoneFocus} type="tel" pattern="[0-9]{9}" class="form-input" id="phone" required bind:value={phone_number} name="phone" maxlength="20">
                            {#if invalidPhone}<small class="error phone-error">Invalid Phone!</small>{/if}
                            <span class="subinfo">This information will be only used to deliver your purchase</span>
                        </div>
                    </div>
                </div>
            </form>
        </div>
        <div class="order-section ol-xs-12 col-sm-5 col-lg-4">
            <div class="order-content">
                <div class="order-header">
                    <h2> SUMMARY </h2>
                    <a href="/orders" class="link"> Edit </a>
                </div>
                <hr class="divider">
                <div class="order-main">
                    <div class="pre">
                        <div class="subtotal">
                            <span>Subtotal</span>
                            <span>{subTotal}€</span>
                        </div>
                        <div class="estimated-shipping">
                            <span>Estimated Shipping</span>
                            <span>{shipping === 0 ? 'Free' : shipping}</span>
                        </div>
                    </div>
                    <hr class="divider">
                    <div class="final">
                        <div class="total">
                            <span>Total</span>
                            <span>{subTotal + shipping}€</span>
                        </div>
                    </div>
                </div>
            </div>
            <button on:click={submitOrder} class="btn-pay">Place order</button>
        </div>
    </div>
</div>

<style>
.form-label:after {
    content: "*";
    color: #d62929;
    padding-left: 5px;
    position: absolute;
}
.form-wrapper {
    display: flex;
    flex-direction: column;
    position: relative;
    margin-bottom: 1.25rem;
}
.form-input {
    padding: 0.875rem 1.125rem;
    height: 3.75rem;
    color: #2f3132;
    border-radius: 0;
    font-size: 16px;
    border: 1px solid #c3c6c8;
    background-color: #fff;
    background-clip: padding-box;
    transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
    width: 100%;
}
.form-input:disabled {
    background-color: #f9f9f9;
}
.form-input:focus {
    outline: 0.15rem solid #000;
    box-shadow: none!important;
    border-color: #c3c6c8;
}
.search-icon {
    position: absolute;
    top: 52px;
    left: 25px;
    color: #c3c6c8;
    max-width: 100%;
    max-height: 100%;
    height: auto;
    display: inline-block;
    vertical-align: middle;
    border-style: none;
}
.with-icon {
    padding-left: 60px;
}
.order-section {
    margin-block-start: 0.83em;
}
.order-content {
    border: 1px solid #c3c6c8;
    height: auto;
    padding: 25px 20px;
}
.order-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 25px;
}
.order-header > * {
    padding: 0;
    margin: 0;
}
.order-main .pre, .order-main .final {
    display: flex;
    flex-direction: column;
}
.order-main .pre > *, .order-main .final > * {
    display: flex;
    justify-content: space-between;
}
.order-main .pre {
    color: #697172;
    white-space: normal;
}
.order-main .final {
    font-size: 18px;
    font-weight: 700;
    line-height: 1.5rem;
    color: #2f3132;
}
.divider {
    padding: 0;
    margin: 0;
    margin-bottom: 0.875rem;
    border: none;
    border-bottom: 1px solid #e1e2e3;
}
.divider:not(:first-child) {
    margin-top: 0.875rem;
}
.link {
    text-decoration: underline;
    color: #697172!important;
    font-style: normal;
    font-weight: 400;
}
.subinfo {
    font-weight: 300;
    font-size: 14px;
    line-height: 1.125rem;
    color: #697172;
}
.btn-pay {
    width: 100%;
    margin-top: 38px;
    font-weight: 700;
    height: 3.75rem;
    padding: 0.875rem 1.125rem;
    font-size: 22px;
    font-family: inherit;
    letter-spacing: 1px;
    text-transform: uppercase;
    cursor: pointer;
    background: #000000;
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
.btn-pay:hover {
    background-color: #000009e4;
}
.dropdown {
    position: absolute;
    width: 100%;
    top: 100px;
    left: 0;
    z-index: 9000;
    padding-bottom: 15px;
}
.dropdown ul {
    max-height: 400px;
    overflow: auto;
    background-color: white;
    box-shadow: 0 15px 30px -10px rgba(0, 0, 0, 0.1);
    border: 1px solid #c3c6c8;
    margin: 0;
    padding: 0;
    list-style: none;
}
.dropdown li {
    display: block;
    background-color: #fff;
    cursor: pointer;
}
.dropdown li:hover {
    color: #546c84;
    background-color: #fbfbfb;
}
li button  {
    background: none;
    color: inherit;
    border: none;
    font: inherit;
    text-align: start;
    padding: 15px;
    cursor: pointer;
    width: 100%;
    height: 100%;
    outline: inherit;
}
.error {
    color: red;
    position: relative;
    bottom: 5px;
}
.error-input {
    border-color: red;
}
</style>