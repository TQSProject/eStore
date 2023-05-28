<script>
    import { onMount } from "svelte";
    import OrderCard from "./OrderCard.svelte";
    import { PUBLIC_ORDERS_PATH, PUBLIC_PICKUS_BASE_URL } from "$env/static/public";
    import { accountEmail } from "../stores/store_account";
    import { orders } from "../stores/store_orders";

    let url = `${PUBLIC_PICKUS_BASE_URL}${PUBLIC_ORDERS_PATH}?buyer=${$accountEmail}`;
    
    let pastOrders = []
    console.log(url)

    onMount(async () => {
        fetch(url)
        .then(response => response.json())
        .then(data => {
            if ($orders != data) {
                orders.set(data);
                pastOrders = data.filter(order => order.status === "PICKED_UP")
            }
        }).catch(error => {
            return [];
        });
    });
</script>

{#if pastOrders.length !== 0}
    <div class="container-fluid">
        <div class="row">
        <div class="col-md-12">
            <div class="table-wrap">
                <table class="table">
                    <thead>
                    <tr>
                        <th>Order</th>
                        <th>Product</th>
                        <th>Date</th>
                        <th>ACP</th>
                        <th>Status</th>
                    </tr>
                    </thead>
                    <tbody>
                        {#each pastOrders as order}
                            <OrderCard id="#{order.id}" count={order.count} product={order.product} date={order.createdDateTime} status={order.status} acp={order.acp}/>
                        {/each}
                    </tbody>
                </table>
            </div>
        </div>
        </div>
    </div>
 {:else}
    <div class="page-fullwidth">
        <div class="empty-outer">
            <center>
                <div class="empty">
                <p class="gutter-bottom">Your have no past orders.</p>
                <a href="/stores" class="btn-shopping">Continue Shopping</a>
                </div> 
            </center>
        </div>
    </div>
 {/if}

 <style>
.page-fullwidth {
    max-width: 100%;
    margin-top: -16px;
    padding: 40px 100px;
    color: #000;
    min-height: 60vh;
    width: auto;
    position: relative;
    margin: 20px auto 0;
    overflow: visible;
    display: block;
}
.empty-outer {
    text-align: center!important;
    margin-top: 20px;
}
.btn-shopping {
    padding: 20px;
    background-color: rgba(255, 255, 255, 0);
    border: 1px solid #e91a47;
    box-shadow: none;
    max-width: 300px;
    border-radius: 0px;
    font-weight: 700;
    cursor: pointer;
    text-align: center;
    vertical-align: middle;
    white-space: nowrap;
    appearance: none;
    line-height: 1.5;
    transition: all 0.15s ease;
    display: inline-block;
    width: 100%;
}
.btn-shopping:hover {
    background-color: #e91a47;
    border: 1px solid #e91a47;
}
.empty-outer a {
    text-decoration: none;
    color: black;
}
.btn-shopping:hover {
   background-color: #e91a47;
   border: 1px solid #e91a47;
}
.empty {
   text-align: center;
}
.gutter-bottom {
   padding-bottom: 50px;
}
.table {
    width: 100%;
    margin-bottom: 1rem;
    color: #212529;
    border-collapse: collapse;
}
.table thead tr {
    background: #fff;
    border-bottom: 4px solid #eceffa;
}
.table thead th {
    border: none;
    padding: 50px;
    font-size: 16px;
    font-weight: 500;
    color: gray;
}
.table thead th {
    vertical-align: bottom;
    border-bottom: 2px solid #dee2e6;
}
th {
    text-align: inherit;
}
.table tbody tr {
    margin-bottom: 10px;
    border-bottom: 4px solid #f8f9fd;
}
.table tbody th {
    border: none;
    padding: 50px;
    font-size: 17px;
    background: #fff;
    vertical-align: middle;
}
 </style>