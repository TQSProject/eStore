<script>
    export let options = [];
    export let x = 0;
    export let y = 0;
</script>

<style>
    .dropdown {
        padding-bottom: 100px;
    }
    ul {
        position: absolute;
        width: 100%;
        top: var(--x);
        left: var(--y);
        z-index: 9000;
        background-color: white;
        box-shadow: 0 15px 30px -10px rgba(0, 0, 0, 0.1);
        border: 1px solid #c3c6c8;
        margin: 0;
        padding: 0;
        list-style: none;
    }
    li {
        display: block;
        padding: 15px;
        background-color: #fff;
        cursor: pointer;
    }
    li:hover {
        color: #546c84;
        background-color: #fbfbfb;
    }
</style>