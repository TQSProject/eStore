<script>
	import shop from '$lib/images/shop.png';
	import cart from '$lib/images/cart.png';
	import { account, accountFirstName, logoutAccount } from '../stores/store_account';
	import { orderCount } from '../stores/store_cart';
    import { PUBLIC_BASE_URL, PUBLIC_STORES_PATH } from '$env/static/public';

	let mobileActive = false;
</script>

<header class="header">
	<div class="wrapper">
		<div class="header-item-left">
			<a href="/" class="brand">
				<img src={shop} alt="logo">
			</a>
		</div>
		<div class="header-item-center">
			<button type="button" class="menu-mobile-trigger" on:click={() => mobileActive = true}>
				<span></span>
				<span></span>
				<span></span>
			</button>
			<div class="overlay" class:active={mobileActive}></div>
			<nav class="menu" class:active={mobileActive}>
				<div class="menu-mobile-header">
					<div class="menu-mobile-title"></div>
					<button type="button" class="menu-mobile-close" on:click={() => mobileActive = false}>×</button>
				</div>
				<ul class="menu-section">
					<li><a href="/stores">Stores</a></li>
					<div class="m-info">
						<form method="get" class="search-form" action="/stores">
							<input type="search" placeholder="Search..." name="q" value="">
						</form>
						<a href="/register" class="auth-button">Sign Up</a>
						<a href="/login" class="auth-button">Login</a>					 
					</div>
          		</ul>
			</nav>
			<form method="get" class="search-form" action="/stores">
				<input type="search" placeholder="Search..." name="q" value="">
			</form>
		</div>
		<div class="header-item-right">
			<div class="cart-icon">
				<a href="/orders">
				  <img src={cart} alt="cart">
				  <span class="order-count">{$orderCount >= 10 ? '9+' : $orderCount}</span>
				</a>
			</div>
			{#if $account}
				<span class="username">{$accountFirstName}</span> 
				<button on:click={logoutAccount} class="auth-button">Logout</button>
			{:else}
				<a href="/register" class="auth-button">Sign Up</a>
				<a href="/login" class="auth-button">Login</a>
			{/if}
		</div>
	</div>
</header>

<style>
	header {
		position: fixed;
		width: 100%;
		top: 0;
		left: 0;
		padding: 0;
		z-index: 99999;
		border: none;
		outline: none;
		background: #000000;
		margin: 0 auto;
		height: auto;
		box-shadow: 0 4px 6px -1px #0000001a, 0 2px 4px -1px #0000000f;
	}

	header .wrapper {
		padding-left: 20px;
		padding-right: 20px;
		padding-top: 6px;
		padding-bottom: 6px;
		max-width: 1920px;
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: space-between;
	}
	.header-item-left {
		display: flex;
		order: 2;
		align-items: center;
		justify-content: center;
	}
	.header-item-center {
		align-items: center;
		display: flex;
		order: 1;
		width: 40%;
	}
	.header-item-right {
		display: flex;
		align-items: center;
		order: 3;
		justify-content: flex-end;
		width: 40%;
	}
	.header .menu > ul > li {
		display: inline-block;
		margin-left: 0;
		color: #fff;
		padding-right: 5px;
		margin-left: 15px;
	}
	.header .menu > ul > li > a {
		position: relative;
		font-size: 22px;
		letter-spacing: 1px;
		font-weight: 400;
		border: none;
		outline: none;
		color: #fefbff;
		text-transform: uppercase;
		text-rendering: optimizeLegibility;
		transition: color .3s ease-in-out;
	}
	.header .menu > ul > li > a:hover {
		color: #e91a47;
	}
	.brand {
		line-height: inherit;
	}
	a.brand img {
		max-width: 60px;
		padding: 5px;
	}
	form.search-form {
    	margin-left: 40px;
	}
	.search-form input {
		font-family: inherit;
		height: 36px;
		border-color: #feffff!important;
		background-color: #000;
		border-style: solid;
		letter-spacing: 1px;
		font-size: 16px;
		color: #fff!important;
		border-radius: 0;
		margin-top: 0;
		margin-bottom: 0!important;
		width: 260px;
		max-width: 100%;
		outline: none;
	}
	.cart-icon {
		padding-right: 40px;
		line-height: 0;
		position: relative;
	}
	.order-count {
		position: absolute;
		top: -2px;
		right: 31px;
		text-align: center;
		border: 1px solid black;
		height: 17px;
		line-height: 14px;
		width: 17px;
		border-radius: 50%;
		font-size: 12px;
		font-weight: 200;
		background-color: #e91a47;
		color: #fff;
		margin: 0;
		text-decoration: none;
	}
	.auth-button {
		font-family: inherit;
		letter-spacing: 1px;
		width: 100px;
		height: 36px;
		line-height: 36px;
		font-size: 16px;
		font-weight: 400;
		margin-right: 15px;
		margin-left: 5px;
		display: inline-block;
		text-align: center;
		vertical-align: middle;
		white-space: nowrap;
		border: 0;
		border-radius: 0px;
		cursor: pointer;
		background: #e91a47;
		color: #fff;
		transition: 0.2s cubic-bezier(0.05,0,0,1)
	}
	.auth-button:hover {
		background: white;
		color: #e91a47;
	}
	.menu-mobile-header, .menu-mobile-trigger {
		display: none;
	}
	.header .m-info {
		display: none;
	}
	.username {
		color: white;
		letter-spacing: 1px;
		height: 36px;
		line-height: 36px;
		font-size: 20px;
		font-weight: 400;
		margin-right: 15px;
		margin-left: 5px;
		display: inline-block;
		text-align: center;
		vertical-align: middle;
		white-space: nowrap;
	}
	@media only screen and (max-width: 992px) {
		.header-item-center, .header-item-right {
			width: initial;
		}
		.header-item-right .auth-button, .header-item-center .search-form {
			display: none;
		}
		.header .menu-mobile-trigger span:nth-child(1) {
			top: 0;
		}
		.header .menu-mobile-trigger span:nth-child(2) {
			top: 0.5rem;
		}
		.header .menu-mobile-trigger span:nth-child(3) {
			top: 1rem;
		}
		.header .menu-mobile-trigger {
			position: relative;
			display: block;
			cursor: pointer;
			width: 1.75rem;
			height: 1rem;
			border: none;
			outline: none;
			margin-left: 0;
			background: 0 0;
			transform: rotate(0);
			transition: .35s ease-in-out;
		}
		.header .menu-mobile-trigger span {
			display: block;
			position: absolute;
			width: 100%;
			height: 2px;
			left: 0;
			border: none;
			outline: none;
			opacity: 1;
			border-radius: 0.25rem;
			background: #feffff;
			transform: rotate(0);
			transition: .25s ease-in-out;
		}
		.header .menu {
			position: fixed;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			z-index: 1099;
			overflow: hidden;
			background: #000000;
			transform: translate(-100%);
			transition: all .5s ease-in-out;
		}
		.overlay {
			position: fixed;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			z-index: 1098;
			opacity: 0;
			visibility: hidden;
			background: rgba(0,0,0,.55);
			transition: all .5s ease-in-out;
		}
		.header .header-item-center {
			order: 1;
		}
		.header .menu.active {
			transform: translate(0);
		}
		.header .menu .menu-section {
			height: 100%;
			overflow-y: auto;
			overflow-x: hidden;
			position: relative;
			text-align: center;
			padding: 0;
		}
		.header .menu .menu-mobile-header {
			position: sticky;
			display: flex;
			align-items: center;
			justify-content: space-between;
			top: 0;
			height: 3.125rem;
			z-index: 501;
			border-bottom: 1px solid rgba(0,0,0,.1);
			background: #000000;
		}
		.header .menu .menu-section {
			padding: 0;
		}
		.header .menu .menu-mobile-header .menu-mobile-title {
			font-size: 24px;
			font-weight: 500;
			line-height: inherit;
			color: #fff;
			text-transform: uppercase;
			text-rendering: optimizeLegibility;
		}
		.header .menu .menu-mobile-header .menu-mobile-close {
			font-size: 2.25rem;
			line-height: 3.125rem;
			cursor: pointer;
			width: 3.125rem;
			height: 3.125rem;
			border-left: 1px solid rgba(0,0,0,.1);
			color: #fff;
			text-align: center;
			background: black;
			border: none;
		}
		.cart-icon {
			padding-right: 9px;
		}
		.order-count {
			right: 0;
		}
		.header .m-info {
			display: flex;
			flex-direction: column;
			align-items: center;
			gap: 16px;
			padding: 0 3.125rem 0 1rem;
			margin-top: 17px;
			min-height: 200px;
		}
		.header .m-info .search-form {
			display: block;
			padding: 0;
			margin: 0;
			width: 75%;
		}
		.header .m-info .search-form input {
			width: 100%;
		}
		.header .m-info .auth-button {
			width: 75%;
			height: 36px;
			line-height: 36px;
			margin: 0;
			padding: 0;
		}
	}
</style>
