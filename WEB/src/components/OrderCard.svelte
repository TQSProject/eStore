<script>
    import { orderCount } from "../stores/store_cart";
    import { navigate } from "../utils";

export let id;
export let date;
export let status;
export let acp;
export let product;
export let count;
</script>

<tr class="alert" on:click={navigate(`order/${id}`)}>
    <td>{id}</td>
    <td><span>{product}</span> <span class="count">x{count}</span></td>
    <td>{date.split("T")[0]}</td>
    <td>{acp.name}, {acp.city}</td>
    <td class="status">
        {#if status === "WAITING_ADMIN_APPROVAL"}
            <span class="waiting">Waiting for approval</span>
        {:else if status === "DELIVERING"}
            <span class="shipping">Shipping</span>
        {:else if status === "DELIVERED_AND_WAITING_FOR_PICKUP"}
            <span class="active">Available for pick up</span>
        {:else}
            <span class="waiting">Unknown</span>
        {/if}
    </td>
 </tr>

<style>
.count {
    background: #f1ecec;
    color: #010101; 
    border-radius: 26px;
    padding: 2px 8px 2px 8px;
    margin-left: 15px;
}
.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
    cursor: pointer;
}
tr {
    margin-bottom: 10px;
    border-bottom: 4px solid #f8f9fd!important;
}
td {
    border: none;
    padding: 50px;
    font-size: 17px;
    background: #fff;
    vertical-align: middle;
    position: relative;
}
.active {
    background: #cff6dd;
    color: #1fa750;
}
td.status span {
    position: relative;
    border-radius: 30px;
    padding: 4px 10px 4px 25px;
}
.active:after {
    background: #23bd5a;
}
td.status span:after {
    position: absolute;
    top: 12px;
    left: 10px;
    width: 10px;
    height: 10px;
    content: '';
    border-radius: 50%;
}
.waiting {
    background: #fddddd;
    color: #cf0c0c;
}
.waiting:after {
    background: #f21d1d;
}
.shipping {
    background: #fdf5dd;
    color: #cfa00c;
}
.shipping:after {
    background: #f2be1d;
}
</style>