<script>
    import { addToOrders } from "../stores/store_order";
    export let object;
</script>

<div class="product-card">
    <div class="content">
        <div class="banner">
            <div class="image" style="background-image: url({object.image})"></div>
        </div>
        <div class="overlay"></div>
        <div class="details">
            <span class="name">{object.name}</span>
            <span class="money">{object.price}€</span>
        </div>
    </div>
    <button class="order-button" on:click={() => addToOrders(object)}>
        add to cart
    </button>
</div>

<style>
    .product-card {
        padding: 10px;
        border-radius: 0;
        position: relative;
        height: 460px;
    }
    .product-card .content {
        padding: 10px;
        border: 1px solid #d1d5db;
        background: linear-gradient(0deg, #000 0, rgba(0,0,0,0) 60%);
    }
    .product-card .banner {
        width:100%;
        height: 280px;
        text-align:center;
        position:relative;
    }
    .product-card .banner .image {
        position: absolute;
        top: 0;
        left: 0;
        padding: 0;
        background-size:cover;
        background-repeat: no-repeat;
        background-position: center;
        height: 100%;
        width: 100%;
    }
    .overlay {
        display: flex;
        padding: 190px 0;
        background: linear-gradient(0deg, #000 0, rgba(0,0,0,0) 60%);
        bottom: 54px;
        left: 10px;
        opacity: 1;
        z-index: 6000;
        width: calc(100% - 20px);
        position: absolute;
    }
    .details {
        position: relative;
        z-index: 6001;
        display: flex;
        font-size: 2em;
        font-weight: 500;
        color: white;
        justify-content: flex-end;
        align-items: flex-start;
        width: 100%;
        flex-direction: column;
    }
    .details .name {
        text-transform: uppercase;
        text-align: left;
        font-weight: 400;
        z-index: 502;
        font-size: 20px;
        padding-right: 12px;
    }
    .order-button {
        background-color: #E91A47;
        color: #fff;
        z-index: 6002;
        width: 100%;
        text-align: center;
        margin-left: auto;
        text-transform: uppercase;
        position: relative;
        font-size: 20px;
        margin-right: auto;
        height: 54px;
        padding-top: 12px 0;
        line-height: 54px;
        outline: none;
        border: 0;
        appearance: none;
        font-family: inherit;
        cursor: pointer;
        letter-spacing: 1px;
    }
    .order-button:hover {
        background-color: #cc0632;
	}
    @media only screen and (max-width: 1200px) {
        .product-card {
            flex:0 0 25%;
            max-width:25%
        }
    }
    @media only screen and (max-width: 992px) {
        .product-card {
            flex:0 0 33.333333%;
            max-width:33.333333%;
        }
    }
    @media only screen and (max-width: 576px) {
        .product-card {
            flex:0 0 50%;
            max-width:50%;
        }
    }
    @media only screen and (max-width: 380px) {
        .product-card {
            flex:0 0 100%;
            max-width:100%;
        }
    }
</style>