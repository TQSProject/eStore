<script>
    import { onMount } from "svelte";
    import { stores } from "../../stores/store_products";
    import StoreCard from "../../components/StoreCard.svelte";
    import {PUBLIC_BASE_URL, PUBLIC_STORES_PATH} from '$env/static/public'

    let url = `${PUBLIC_BASE_URL}${PUBLIC_STORES_PATH}`;

    onMount(async () => {
        const params = new URLSearchParams(window.location.search);
        const query = params.get('q');
        if (query) {
            url = `${url}?q=${query}`;
        }

        fetch(url)
        .then(response => response.json())
        .then(data => {
            stores.set(data);
        }).catch(error => {
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