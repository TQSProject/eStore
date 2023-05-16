<script>
    import { onMount } from "svelte";
    import { stores } from "../../stores/store_products";
    import StoreCard from "../../components/StoreCard.svelte";
    import {PUBLIC_BASE_URL, PUBLIC_STORES_PATH} from '$env/static/public'

    const url = `${PUBLIC_BASE_URL}${PUBLIC_STORES_PATH}`;

    onMount(async () => {
        fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            stores.set(data);
        }).catch(error => {
            console.log(error);
            return [];
        });
    });
</script>

<svelte:head>
	<title>ShopHub - Home Page</title>
</svelte:head>

<section>
	{#each $stores as store}
		<StoreCard object={store} />
	{/each}
</section>

<style>
</style>