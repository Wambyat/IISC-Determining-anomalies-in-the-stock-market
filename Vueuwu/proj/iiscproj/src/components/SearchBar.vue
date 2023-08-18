<template>
    <div>
        <input
            v-model="searchQuery"
            @input="genList"
            placeholder="Search for the company"
            id="compIn" />
        <button @click="performSearch">Search</button>
    </div>
</template>

<script>
    import { ref, onMounted } from "vue";
    let comp;
    export default {
        setup() {
            onMounted(async () => {
                console.log("search mounted");
                const abc = async function () {
                    try {
                        console.log("try");
                        const response = await fetch(
                            "http://localhost:5000/api/all"
                        );
                        console.log("first");
                        const data = await response.json();
                        return data;
                    } catch (error) {
                        console.error(error);
                    }
                };
                console.log("waiting");
                comp = await abc();
                console.log("done");
                console.log(comp);
            });
        },
        data() {
            return {
                searchQuery: "",
            };
        },
        methods: {
            async firstList() {
                try {
                    const response = await fetch(
                        "http://localhost:5000/api/all"
                    );
                    const data = await response.json();
                } catch (error) {
                    console.error(error);
                }
            },
            performSearch() {
                this.$emit("search", this.searchQuery);
            },
            genList() {
                function filterJson(jsonData, input) {
                    const filteredJson = {};
                    for (const key in jsonData) {
                        if (
                            key.includes(input) ||
                            jsonData[key]
                                .toLowerCase()
                                .includes(input.toLowerCase())
                        ) {
                            filteredJson[key] = jsonData[key];
                        }
                    }
                    return filteredJson;
                }

                const userInput = document.getElementById("compIn").value;
                console.log("Filtering based on: ", userInput);
                const filteredData = filterJson(comp, userInput);
                console.log(filteredData);
                console.log("genList");
            },
        },
    };
</script>
