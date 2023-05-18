<script>
    import axios from 'axios';
    import { onMount } from 'svelte';
    import { PUBLIC_BASE_URL, PUBLIC_REGISTER_PATH } from '$env/static/public'
    import { getCookie, setCookie } from '../../stores/store_cookies';
    import { navigate } from '../../utils';
    import { updateAccount } from '../../stores/store_account';
    import { afterNavigate } from '$app/navigation';
    import { page } from "$app/stores";
    
    const url = `${PUBLIC_BASE_URL}${PUBLIC_REGISTER_PATH}`;

    let previousPage = '/' ;

    afterNavigate(({from}) => {
        previousPage = from?.url.pathname || previousPage
    }) 

    let firstName = '';
    let lastName = '';
    let email = '';
    let password = '';

    const registerUser = async () => {
        try {
        const response = await axios.post(url, {
            first_name: firstName,
            last_name: lastName,
            email,
            password,
        });

        const { access: access_token } = response.data;

        // Store the access token in a cookie
        setCookie('access_token', access_token);

        updateAccount();

        // Redirect to the previous page or '/' if no previous page is available
        const newPage = previousPage === $page.url.pathname ? '/' : previousPage;

        navigate(newPage);
        } catch (error) {
            // Handle any errors during registration
            console.error('Registration error:', error);
        }
    };

    onMount(() => {
        // Check if the user is already logged in
        const access_token = getCookie('access_token')
            if (access_token) {
                navigate()
            }
    });
</script>

<svelte:head>
	<title>ShopHub - Sign Up Page</title>
</svelte:head>

<section>
    <div class="auth-wrapper">
        <div class="auth-box">
            <div class="top"></div>
            <div class="auth-content">
                <div class="auth-form-wrapper">
                    <h2 class="theme">Register</h2>
                    <form class="auth-form" on:submit|preventDefault={registerUser}>
                        <div class="form-field">
                            <label for="first-name">First Name</label>
                            <div class="input-ctn">
                                <svg class="icn" xmlns="http://www.w3.org/2000/svg" width="43.84" height="43.84" viewBox="0 0 45.587 45.587">
                                    <path d="M25.918,9.206a5.754,5.754,0,1,1-5.754,5.754,5.753,5.753,0,0,1,5.754-5.754m0,24.658c8.137,0,16.713,4,16.713,5.754v3.014H9.206V39.617c0-1.753,8.576-5.754,16.713-5.754M25.918,4A10.959,10.959,0,1,0,36.878,14.959,10.956,10.956,0,0,0,25.918,4Zm0,24.658C18.6,28.658,4,32.33,4,39.617v8.219H47.837V39.617C47.837,32.33,33.234,28.658,25.918,28.658Z" transform="translate(-3.125 -3.125)" fill="#1f1e21" stroke="#fff" stroke-width="1.75"></path>
                                </svg>
                                <input type="text" bind:value="{firstName}" name="first-name" id="first-name" class="large" size="30" placeholder="Type your first name">                            
                            </div>
                        </div>
                        <div class="form-field">
                            <label for="last-name">Last Name</label>
                            <div class="input-ctn">
                                <svg class="icn" xmlns="http://www.w3.org/2000/svg" width="43.84" height="43.84" viewBox="0 0 45.587 45.587">
                                    <path d="M25.918,9.206a5.754,5.754,0,1,1-5.754,5.754,5.753,5.753,0,0,1,5.754-5.754m0,24.658c8.137,0,16.713,4,16.713,5.754v3.014H9.206V39.617c0-1.753,8.576-5.754,16.713-5.754M25.918,4A10.959,10.959,0,1,0,36.878,14.959,10.956,10.956,0,0,0,25.918,4Zm0,24.658C18.6,28.658,4,32.33,4,39.617v8.219H47.837V39.617C47.837,32.33,33.234,28.658,25.918,28.658Z" transform="translate(-3.125 -3.125)" fill="#1f1e21" stroke="#fff" stroke-width="1.75"></path>
                                </svg>
                                <input type="text" bind:value="{lastName}" name="last-name" id="last-name" class="large" size="30" placeholder="Type your last name">                            
                            </div>
                        </div>
                        <div class="form-field">
                            <label for="email">Email</label>
                            <div class="input-ctn">
                                <svg width="29" height="20" viewBox="0 0 29 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                      <path d="M27.2099 0.360535H1.66668C0.863837 0.360535 0.207031 1.01728 0.207031 1.82V17.8744C0.207031 18.677 0.863837 19.3339 1.66668 19.3339H27.2099C28.0127 19.3339 28.6696 18.6772 28.6696 17.8744V1.82C28.6695 1.01728 28.0127 0.360535 27.2099 0.360535ZM26.6621 1.45508L15.2779 9.99319C15.0732 10.1489 14.759 10.2464 14.4382 10.2449C14.1175 10.2464 13.8033 10.1489 13.5986 9.99319L2.21436 1.45508H26.6621ZM20.5811 10.5566L26.7844 18.2189C26.7907 18.2266 26.7983 18.2324 26.8049 18.2394H2.07166C2.07822 18.2321 2.08589 18.2266 2.09212 18.2189L8.2955 10.5566C8.48556 10.3216 8.44954 9.97712 8.21411 9.78663C7.97913 9.59658 7.63463 9.6326 7.44451 9.86762L1.30173 17.4552V2.13923L12.9421 10.8688C13.3797 11.1946 13.912 11.338 14.4382 11.3395C14.9636 11.3384 15.4964 11.195 15.9342 10.8688L27.5746 2.13923V17.455L21.432 9.86762C21.2419 9.63266 20.897 9.59653 20.6624 9.78663C20.427 9.97668 20.3909 10.3216 20.5811 10.5566Z" fill="#151515"></path>
                                </svg>
                                <input type="email" bind:value="{email}" name="email" id="email" placeholder="Type your email address" spellcheck="false" autocomplete="off" autocapitalize="off">
                            </div>
                        </div>
                        <div class="form-field">
                            <label for="password">Password</label>
                            <div class="input-ctn">
                                <svg width="29" height="29" viewBox="0 0 29 29" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <g>
                                    <path opacity="0.5" d="M22.4441 28.9463H6.43398C4.96342 28.9463 3.76562 27.7498 3.76562 26.2782V13.8269C3.76562 12.3553 4.96342 11.1588 6.43398 11.1588H22.4441C23.9147 11.1588 25.1125 12.3553 25.1125 13.8269V26.2782C25.1125 27.7498 23.9147 28.9463 22.4441 28.9463ZM6.43398 12.9376C5.94419 12.9376 5.54453 13.336 5.54453 13.8269V26.2782C5.54453 26.7691 5.94419 27.1676 6.43398 27.1676H22.4441C22.9339 27.1676 23.3336 26.7691 23.3336 26.2782V13.8269C23.3336 13.336 22.9339 12.9376 22.4441 12.9376H6.43398Z" fill="#151515"></path>
                                    <path opacity="0.5" d="M20.6641 12.9376C20.1731 12.9376 19.7746 12.5391 19.7746 12.0482V7.60133C19.7746 4.65928 17.3802 2.26508 14.4379 2.26508C11.4956 2.26508 9.10117 4.65928 9.10117 7.60133V12.0482C9.10117 12.5391 8.7027 12.9376 8.21172 12.9376C7.72074 12.9376 7.32227 12.5391 7.32227 12.0482V7.60133C7.32227 3.67741 10.5136 0.486328 14.4379 0.486328C18.3622 0.486328 21.5535 3.67741 21.5535 7.60133V12.0482C21.5535 12.5391 21.155 12.9376 20.6641 12.9376Z" fill="#151515"></path>
                                    </g>
                                    <defs>
                                    <clipPath>
                                    <rect width="28.4625" height="28.46" fill="white" transform="translate(0.207031 0.486328)"></rect>
                                    </clipPath>
                                    </defs>
                                </svg>
                                <input type="password" bind:value="{password}" name="password" id="password" placeholder="Type your password">
                            </div>
                        </div>
                        <div class="form-field action-bottom">
                            <input class="btn" type="submit" value="Register">              
                        </div>
                    </form>
                    <p class="auth-option">
                        Already have an account? 
                        <a href="/login">Login</a> here.
                    </p>
                </div>
            </div>
        </div>
    </div>
</section>


<style>
    .auth-wrapper {
        min-height: 529px;
        padding-top: min(4.1%,77.5px);
        padding-bottom: min(4.1%,77.5px);
        display: flex;
        align-items: center;
    }
    .auth-box {
        background-color: #fff;
        margin-left: auto;
        margin-right: auto;
        width: min(88%, 759px);
        border: 1px solid black;
    }
    .top {
        padding-top: 20px;
        padding-bottom: 20px;
        background-color: #000000;
        position: relative;
    }
    .auth-content {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        padding-top: 0px;
        padding-bottom: 0px;
        padding-left: min(8.8%,66.41px);
        padding-right: min(8.8%,66.41px);
        margin-top: min(5%,30px);
        margin-bottom: min(6%,40px);
        max-width: 1160px;
    }
    .auth-form-wrapper {
        width: 100%;
        display: inline-block;
    }
    .auth-form {
        padding: 0;
    }
    .form-field {
        width: 100%;
        margin-bottom: min(5%,30px);
        line-height: 1;
        text-align: left;
    }
    .form-field label {
        font-style: normal;
        font-weight: 400;
        font-size: 28px;
        line-height: 1.43;
        color: #151515;
        left: 0px;
        opacity: 1;
        padding: 0;
        position: relative;
        top: 0em;
        transition: unset;
        z-index: 1;
        margin-bottom: 5px;
        display: block;
    }
    .input-ctn {
        display: flex;
        align-items: center;
        position: relative;
    }
    .input-ctn svg {
        position: absolute;
        left: 0px;
        opacity: 0.5;
        max-width: 29px;
    }
    .form-field input {
        margin: 0;
        border-top: 0;
        border-left: 0;
        border-right: 0;
        font-style: normal;
        font-weight: 300;
        font-size: 18px;
        display: block;
        width: 100%;
        line-height: 1;
        color: #151515 !important;
    }
    .form-field input:focus {
        outline: none;
    }
    .form-field .btn {
        padding-top: 13.25px;
        padding-bottom: 9.25px;
        font-weight: 600;
        font-size: 36px;
        line-height: 1.22;
        color: #FFFFFF !important;
        padding-left: 0;
        padding-right: 0;
        width: 100%;
        text-transform: uppercase;
        appearance: none;
        transition: all 0.15s ease;
        display: inline-block;
        text-decoration: none;
        text-align: center;
        vertical-align: middle;
        white-space: nowrap;
        border: 0;
        border-radius: 0px;
        background: #e91a47;
        font-family: inherit;
        letter-spacing: 1px;
        cursor: pointer;
    }
    .form-field .btn:hover {
        background: #d5143e;
    }
    h2.theme {
        font-style: normal;
        font-weight: 600;
        font-size: 4rem;
        line-height: 1.44;
        text-transform: capitalize;
        color: #151515;
        margin: 0;
        margin-bottom: min(5%,30px);
        text-align: center;
        position: relative;
        z-index: 11;
    }
    .auth-option {
        font-style: normal;
        font-weight: 300;
        font-size: 18px;
        line-height: 1.22;
        text-align: center;
        color: #151515;
        padding-top: min(5%,30px);
        font-family: 'Montserrat';
    }
    .auth-option a {
        color: #e91a47;
        font-weight: 500;
    }
    @media only screen and (min-width: 750px) {
        .auth-option {
            font-size: min(18px,calc(15px + (18 - 15) * ((100vw - 750px) / (1920 - 750)))) !important;
        }
        h2.theme {
            font-size: min(64px,calc(40px + (64 - 40) * ((100vw - 750px) / (1920 - 750)))) !important;
        }
        .form-field input {
            padding-left: 44px;
            padding-top: 15px;
            padding-bottom: 15px;
        }
        .form-field label {
            font-size: min(28px,calc(20px + (28 - 20) * ((100vw - 750px) / (1920 - 750)))) !important;
        }
        .nlogin .form-field .btn {
            font-size: min(36px,calc(24px + (36 - 24) * ((100vw - 750px) / (1920 - 750)))) !important;
        }
    }
</style>