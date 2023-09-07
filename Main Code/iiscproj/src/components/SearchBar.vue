<template>
    <div>
        <input
            v-model="searchQuery"
            @input="genList"
            placeholder="Search for the company"
            id="compIn"
            style="min-width: 40%; border: none" />
        <button @click="performSearch">Search</button>
        <div class="search-list">
            <p v-if="filteredData.error">{{ filteredData.error }}</p>
            <!-- This is what makes the dynamic list -->
            <ul v-else v-for="(item, key) in filteredData" :key="key">
                <router-link
                    style="text-decoration: none"
                    :to="{ name: 'search', params: { query: key } }">
                    <li class="st">{{ key }}: {{ item }}</li>
                </router-link>
            </ul>
        </div>
    </div>
</template>

<style scoped>
    .st {
        color: black;
        cursor: pointer;
        /* no underlined */
        text-decoration: none;
    }

    .search-list ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
        border-bottom: 1px solid #ddd;
        padding: 10px;
        cursor: pointer;
    }
    .search-list ul:hover {
        background-color: #f1f1f1;
    }
    .search-list::-webkit-scrollbar {
        width: 20px;
        background-color: #f1f1f1;
        border-bottom-right-radius: 15px;
    }
    .search-list::-webkit-scrollbar-thumb {
        background-color: #888;
        border: 5px solid transparent;
        width: 50px;
        border-radius: 50px;
        background-color: #8070d4;
        background-clip: content-box;
    }

    .search-list::-webkit-scrollbar-track {
        background-color: #e4e4e4;
        border-bottom-right-radius: 15px;
    }
    .search-list {
        max-height: 300px;
        max-width: 40%;
        overflow-y: scroll;
        border-radius: 15px;
        box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25),
            0 10px 10px rgba(0, 0, 0, 0.22);
    }
</style>

<script>
    import { onMounted } from "vue";
    let all_company_list;
    export default {
        setup() {
            onMounted(async () => {
                const getAllCompany = async function () {
                    try {
                        const response = await fetch(
                            "http://localhost:5000/api/all"
                        );
                        const data = await response.json();
                        return data;
                    } catch (error) {
                        console.error(error);
                    }
                };
                all_company_list = await getAllCompany();
            });
        },
        data() {
            return {
                searchQuery: "",
                filteredData: {},
            };
        },
        methods: {
            performSearch() {
                this.$emit("search", this.searchQuery);
            },
            genList() {
                function filterJson(jsonData, input) {
                    const filteredJson = {};
                    // This minimum requirement is only here because the resulting json is large and makes my computer lag. Test without the limit if you wish.
                    if (input.length < 3) {
                        return { error: "Please enter more than 2 characters" };
                    }
                    for (const key in jsonData) {
                        // This checks if the input is in either the ticker or the company name.
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
                this.filteredData = filterJson(all_company_list, userInput);
            },
        },
    };
</script>
