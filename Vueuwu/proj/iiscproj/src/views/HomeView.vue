<template>
    <div class="home">
        <h1>Home</h1>
        <search-bar @search="performSearch"></search-bar>
    </div>
</template>

<script>
    import SearchBar from "../components/SearchBar.vue";

    export default {
        components: {
            SearchBar,
        },
        methods: {
            performSearch(query) {
                this.$router.push({ name: 'search', params: { query } });
            },
        },
    };
</script>
