<template>
    <div class="home">
        <h1>Home</h1>
        <search-bar @search="performSearch"></search-bar>
        <p id="err"></p>
    </div>
</template>

<script>
    import SearchBar from "../components/SearchBar.vue";
    export default {
        components: {
            SearchBar,
        },
        methods: {
            async performSearch(query) {
                const responce = await fetch(
                    "http://localhost:5000/api/search",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            search: query,
                        }),
                    }
                );
                const data = await responce.json();
                let name;
                if (data.error) {
                    name = data.error;
                    document.getElementById("err").innerHTML = name;
                } else {
                    name = data.ticker;
                    this.$router.push({
                        name: "search",
                        params: { query: name },
                    });
                }
            },
        },
    };
</script>
