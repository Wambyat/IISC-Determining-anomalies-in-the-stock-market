<template>
    <div>
        <h2>Search UWU</h2>
        <p>{{ query }}</p>
        <p>:(</p>
    </div>
</template>

<script>
    export default {
        props: {
            query: String,
        },
    };
</script>
