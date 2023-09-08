<template>
    <div class="model">
        <h1>IG model goes here</h1>
        <button @click="modelRun">Run Model</button>
        <p id="modelRes"></p>
    </div>
</template>

<script>
    export default {
        name: "ModelView",
        methods: {
            async modelRun() {
                // Change this to whatever the model will output.
                const responce = await fetch("http://localhost:5000/model");
                const data = await responce.json();
                if (data.error) {
                    document.getElementById("modelRes").innerHTML = data.error;
                } else {
                    document.getElementById("modelRes").innerHTML = data.data;
                }
            },
        },
    };
</script>
