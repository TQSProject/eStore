<script>
    import { onMount } from "svelte";
    import { products } from "../../../stores/store_products";
    import ProductCard from "../../../components/ProductCard.svelte";
    import {PUBLIC_BASE_URL, PUBLIC_STORES_PATH} from '$env/static/public'

    const url = `${PUBLIC_BASE_URL}${PUBLIC_STORES_PATH}`;

    export let data;

    onMount(async () => {
        fetch(`${url}${data.slug}/products`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            products.set(data);
        }).catch(error => {
            console.log(error);
            return [];
        });
    });
</script>

<svelte:head>
	<title>ShopHub - Products Page</title>
</svelte:head>

<section>
    <div class="container-fluid">
        <div class="row row-cols-5">
            {#each $products as product}
                <ProductCard object={product} />
            {/each}
        </div>
     </div>
</section>

<style>
</style>