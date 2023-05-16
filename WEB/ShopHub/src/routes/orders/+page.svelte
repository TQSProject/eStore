<script>
    import Cart from "../../components/Cart.svelte";
	let activeTab = 0;
</script>

<svelte:head>
	<title>ShopHub - Orders Page</title>
</svelte:head>

<section>
	<div class="select-status">
		<button on:click={() => activeTab = 0} class:active={activeTab === 0} class="btn-status cart">Cart</button>
		<button on:click={() => activeTab = 1} class:active={activeTab === 1} class="btn-status ongoing">Ongoing</button>
		<button on:click={() => activeTab = 2} class:active={activeTab === 2} class="btn-status past">Past</button>
	</div>
	<section class="orders-section">
		{#if activeTab === 0}
			<Cart />
		{:else if activeTab === 1}
			<!-- <Ongoing /> -->
		{:else if activeTab === 2}
			<!-- <Past /> -->
		{/if}
	</section>
</section>

<style>
	.select-status:after { 
		content: " "; 
		display: block;
		clear: both;
		padding-bottom: 10px;
		border-bottom: 1px solid #dedede;
	} 
	.btn-status {
		height: 36px;
		line-height: 36px;
		float: left;
		text-align: center;
		width: 100px;
		border: none;
		outline: none;
		appearance: none;
		background-color: rgba(0, 0, 0, .05);
		color: black;
		margin-right: 10px;
		letter-spacing: 1px;
		cursor: pointer;
	}
	.btn-status.active {
		color: white!important;;
		background-color: black!important;;
	}
	.btn-status:hover {
		color: black;
		background-color: rgba(0, 0, 0, .1);
	}
	.past {
		float: right;
		margin-right: 0;
	}
	@media only all and (max-width: 576px) {
		.select-status {
			display: flex;
			flex-direction: column;
			align-items: center;
		}
		.btn-status {
			width: 100%;
			margin-right: 0!important;
			margin-bottom: 10px;
		}
		.past {
			margin-bottom: 0;
		}
	}
</style>