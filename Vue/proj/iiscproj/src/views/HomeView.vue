<template>
    <div class="home">
        <h1>Home</h1>
        <search-bar @search="performSearch"></search-bar>
        <p id="err"></p>

        <!-- table -->
        <table class="newsTable">
            <tr>
                <th>Ticker</th>
                <th>Desc</th>
                <th>Company</th>
                <th>Announcement Time</th>
                <th>Full announcement</th>
            </tr>
            <tr v-for="(item, key) in news" :key="key">
                <td>{{ item.symbol }}</td>
                <td>{{ item.desc }}</td>
                <td>{{ item.sm_name }}</td>
                <td>{{ item.an_dt }}</td>
                <td>{{ item.attchmntText }}</td>
            </tr>
        </table>
        <p>
            If you can't see the news after 10 seconds, either refresh the page
            or check if nseindia.com is down
        </p>
    </div>
</template>

<style scoped>
    table {
        border: 1px solid black;
        /* border-collapse: collapse; */
        width: auto;
    }

    th,
    td {
        border: 1px solid black;
        padding: 5px;
        text-align: left;
    }
</style>

<script>
    import SearchBar from "../components/SearchBar.vue";
    import { ref, onMounted } from "vue";
    import axios from "axios";
    export default {
        data() {
            return {
                news: {},
            };
        },
        setup() {
            const news = ref({});
            onMounted(async () => {
                console.log("home mounted");

                function starter() {
                    const apiURL = "http://localhost:3000/api/starter";
                    return axios
                        .get(apiURL)
                        .then((response) => {
                            console.log(response.data);
                            return response.data;
                        })
                        .catch((error) => {
                            console.error(error);
                        });
                }

                function getNews(a) {
                    if (a > 100) {
                        return;
                    }
                    const apiUrl =
                        "http://localhost:3000/api/corporate-announcements";
                    return axios
                        .get(apiUrl)
                        .then((response) => {
                            console.log(response.data);
                            news.value = response.data;
                            return response.data;
                        })
                        .catch((error) => {
                            console.error(error);
                            getNews(a + 1);
                        });
                }
                // await starter();
                console.log("getting news");
                // await getNews(0);
            });

            return { news };
        },
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
