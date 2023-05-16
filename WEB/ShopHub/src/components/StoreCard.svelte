
<script>
    export let object;
</script>

<div class="store-card">
    <a class="content" href="stores/{object.slug}">
        <div class="banner">
            <div class="image" style="background-image: url({object.image})">
            </div>
            <span class="title"></span>
        </div>
        <div class="legend">
            <span class="name">{object.name}</span>
            <span class="location">({object.address})</span>
        </div>
    </a>
</div>

<style>
    .store-card {
        padding: 2em;
    }
    .store-card .banner {
        width:100%;
        height: 280px;
        text-align:center;
        position:relative;
    }
    .store-card .banner .image {
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
    .store-card .banner .title {
        color:rgb(0, 0, 0);
        font-size:50px;
        font-weight:bold;
        position:relative;
        position:absolute;
        line-height: 260px;
        z-index:9999;
        filter: blur(0px);
    }
    .store-card .legend {
        font-size: 10px;
    }
    @media only screen and (min-width: 992px) {
        .store-card .legend {
            font-size: 40px;
        }
    }

    @media only screen and (min-width: 768px) and (max-width: 992px) {
        .store-card .legend {
            font-size: 30px;
        }
    }

    @media only screen and (min-width: 576px) and (max-width: 768px) {
        .store-card .legend {
            font-size: 20px;
        }
    }

    @media only screen and (min-width: 436px) and (max-width: 576px) {
        .store-card .legend {
            font-size: 18px;
        }
    }

    @media only screen and (max-width: 576px) {
        .store-card {
            padding-left: 1em;
            padding-right: 1em;
        }
    }

    @media only screen and (min-width: 380px) and (max-width: 436px) {
        .store-card .legend {
            font-size: 15px;
        }
    }

    @media only screen and (min-width: 320px) and (max-width: 380px) {
        .store-card .legend {
            font-size: 12px;
        }
    }
</style>