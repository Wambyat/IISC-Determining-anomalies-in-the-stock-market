<template>
    <div class="home">
        <h1>Home</h1>
        <Graph :dataPoints="dataPoints" />
        <search-bar @search="performSearch"></search-bar>
        <p id="err"></p>
        <div v-for="(item, key) in news" :key="key">
            <p>TICKER: {{ item.symbol }}</p>
            <p>Desc: {{ item.desc }}</p>
            <p>Company: {{ item.sm_name }}</p>
            <p>Announcement Time: {{ item.an_dt }}</p>
            <p>Full announcement: {{ item.attchmntText }}</p>
        </div>
        <p>
            If you can't see the news after 10 seconds, either refresh the page
            or check if nseindia.com is down
        </p>
    </div>
</template>

<script>
    import SearchBar from "../components/SearchBar.vue";
    import Graph from "../components/Graph.vue";
    import { ref, onMounted } from "vue";
    import axios from "axios";
    export default {
        data() {
            return {
                news: {},
                dataPoints: [
                    {
                        date: "2023-08-01",
                        price: 150.25,
                        articleUrl: "https://example.com/article1",
                    },
                    {
                        date: "2023-08-02",
                        price: 155.5,
                        articleUrl: "https://example.com/article2",
                    },
                    {
                        date: "2023-08-03",
                        price: 160.75,
                        articleUrl: "https://example.com/article3",
                    },
                    {
                        date: "2023-08-04",
                        price: 162.1,
                        articleUrl: "https://example.com/article4",
                    },
                    {
                        date: "2023-08-05",
                        price: 158.9,
                        articleUrl: "https://example.com/article5",
                    },
                    {
                        date: "2023-08-06",
                        price: 157.25,
                        articleUrl: "https://example.com/article6",
                    },
                    {
                        date: "2023-08-07",
                        price: 154.75,
                        articleUrl: "https://example.com/article7",
                    },
                    {
                        date: "2023-08-08",
                        price: 153.0,
                        articleUrl: "https://example.com/article8",
                    },
                    {
                        date: "2023-08-09",
                        price: 150.75,
                        articleUrl: "https://example.com/article9",
                    },
                    {
                        date: "2023-08-10",
                        price: 149.5,
                        articleUrl: "https://example.com/article10",
                    },
                ],
            };
        },
        setup() {
            const news = ref({});
            onMounted(async () => {
                console.log("home mounted");
                function getNews(a) {
                    if (a > 50) {
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
                await getNews(0);
            });

            return { news };
        },
        components: {
            SearchBar,
            Graph,
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
