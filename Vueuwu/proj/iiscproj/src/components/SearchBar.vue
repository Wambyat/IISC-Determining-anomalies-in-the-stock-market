<template>
    <div>
        <input v-model="searchQuery" placeholder="Search for the company" />
        <button @click="performSearch">Search</button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                searchQuery: "",
            };
        },
        methods: {
            performSearch() {
                this.$emit("search", this.searchQuery);
            },
        },
    };
</script>
