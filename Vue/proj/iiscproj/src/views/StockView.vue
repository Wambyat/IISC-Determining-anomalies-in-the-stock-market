<template>
    <div>
        <h2>Search UWU</h2>
        <p>{{ query }}</p>
        <div v-for="(item, key) in news" :key="key">
            <p>TICKER: {{ item.symbol }}</p>
            <p>Desc: {{ item.desc }}</p>
            <p>Company: {{ item.sm_name }}</p>
            <p>Announcement Time: {{ item.an_dt }}</p>
            <p>Full announcement: {{ item.attchmntText }}</p>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import { ref, onMounted } from "vue";
    export default {
        data() {
            return {
                news: {},
                dataToday: {},
            };
        },
        props: {
            query: String,
        },
        setup(props) {
            // news and dataToday are like global variables. They will be used in the template. query is from the prev page.
            const news = ref({});
            const dataToday = ref({});
            const query = ref(props.query);
            onMounted(async () => {
                console.log("getting data");

                // This gets the latest data about the stock from nse. This is calling flask.
                function getLatest() {
                    const apiURL = "http://localhost:5000/api/stock";
                    return axios
                        .post(apiURL, {
                            ticker: query.value,
                        })
                        .then((response) => {
                            console.log(response.data);
                            dataToday.value = response.data;
                            return response.data;
                        })
                        .catch((error) => {
                            console.error(error);
                        });
                }
                await getLatest();
                console.log(dataToday.value);

                // This gets the news about the stock from nse. This is calling express.
                function getNews(a) {
                    if (a > 5) {
                        return;
                    }
                    const apiUrl =
                        "http://localhost:3000/api/corporate-announcements/"+query.value;
                    return axios
                        .get(apiUrl)
                        .then((response) => {
                            console.log(response.data);
                            news.value = response.data;
                            return response.data;
                        })
                        .catch((error) => {
                            console.error(error);
                            console.log("retrying");
                            getNews(a + 1);
                        });
                }
                await getNews(0);
                console.log(news.value);
            });
            return { news, dataToday };
        },
    };
</script>
