<template>
    <div class="home">
        <h1>Home</h1>
        <search-bar @search="performSearch"></search-bar>
        <p id="err"></p>
        <!-- loop thru symbol, desc, sm_name, an_dt and attchmntTest from news array. every element is a dictionary-->
        <div v-for="(item, key) in news" :key="key">
            <p>TICKER: {{ item.symbol }}</p>
            <p>Desc: {{ item.desc }}</p>
            <p>Company: {{ item.sm_name }}</p>
            <p>Announcement Time: {{ item.an_dt }}</p>
            <p>Full announcement: {{ item.attchmntText }}</p>
        </div>
        <p>If you can't see the news after 10 seconds, either refresh the page or check if nseindia.com is down</p>
    </div>
</template>

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
