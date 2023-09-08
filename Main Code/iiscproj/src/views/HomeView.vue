<template>
    <div class="home">
        <h1>Home</h1>
        <search-bar @search="performSearch"></search-bar>
        <p id="err"></p>

        <!-- This table renders the results from NSE -->
        <div v-if="Object.keys(news).length !== 0">
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
        </div>
        <div v-else>
            <p>
                If you can't see the news after 10 seconds, either refresh the
                page or check if nseindia.com is down.
            </p>
        </div>
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
                // This is run with the hopes that NSE somehow whitelists us or somehting
                function starter() {
                    const apiURL = "http://localhost:3000/api/starter";
                    return axios
                        .get(apiURL)
                        .then((response) => {
                            // console.log(response.data);
                            return response.data;
                        })
                        .catch((error) => {
                            console.error(error);
                        });
                }

                // This is run to spam NSE with requests. It will stop after 100 requests.
                function getNews(a) {
                    if (a > 100) {
                        return;
                    }
                    const apiUrl =
                        "http://localhost:3000/api/corporate-announcements";
                    return axios
                        .get(apiUrl)
                        .then((response) => {
                            // console.log(response.data);
                            news.value = response.data;
                            return response.data;
                        })
                        .catch((error) => {
                            console.error(error);
                            getNews(a + 1);
                        });
                }
                await starter();
                // This will recursivley call itself until it gets a response from NSE or it has tried 100 times. The only reason it is recursive is because I made it recursive and I am too lazy to change it.
                await getNews(0);
            });

            return { news };
        },
        components: {
            SearchBar,
        },
        methods: {
            // This makes a request to the flask server to search for the ticker. If it is found, it will redirect to the search page. If not, it will display an error.
            // This is the only place where a (non direct/button) redirect has been implimented.
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
                    // This is how the redirect is done.
                    this.$router.push({
                        name: "search",
                        params: { query: name },
                    });
                }
            },
        },
    };
</script>
