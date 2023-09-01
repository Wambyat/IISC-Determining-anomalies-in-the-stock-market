<template>
    <div>
        <div v-if="compName" class="newsClass">
            <h2>{{ compName }}</h2>
        </div>
        <div v-else>loading</div>
        <div v-if="Object.keys(dataToday).length === 0">
            <p>Loading</p>
        </div>
        <div v-else>
            <table class="tableClass">
                <tr>
                    <th>Average Price</th>
                    <th>High Price</th>
                    <th>Low Price</th>
                    <th>Latest Price</th>
                    <th>Deliverable Quantity</th>
                    <th>No of trades</th>
                </tr>
                <tr>
                    <td>{{ dataToday["AveragePrice"] }}</td>
                    <td>{{ dataToday["HighPrice"] }}</td>
                    <td>{{ dataToday["LowPrice"] }}</td>
                    <td>{{ dataToday["LastPrice"] }}</td>
                    <td>{{ dataToday["DeliverableQty"] }}</td>
                    <td>{{ dataToday["No.ofTrades"] }}</td>
                </tr>
            </table>
        </div>
        <div v-if="chartData.length === 0">Loading</div>
        <div v-else>
            <Graph :data="chartData" class="newsClass graphClass" />
        </div>
        <div v-if="news" class="newsClass">
            <h2>News</h2>
            <div v-for="article in news">
                <component
                    :is="article.link.startsWith('http') ? 'a' : 'router-link'"
                    :key="article.link"
                    :to="article.link"
                    :href="article.link"
                    target="_blank">
                    {{ article.title }}
                </component>
            </div>
        </div>
    </div>
</template>

<style scoped>
    table {
        /* border: 1px solid rgb(255, 255, 255); */
        border-collapse: collapse;
        width: auto;
    }
    /* only divide inside no border */
    th,
    td {
        /* border: 1px solid rgb(255, 255, 255); */
        border-radius: 15px;
        padding: 5px;
        text-align: center;
    }
    a {
        text-decoration: none;
        color: black;
    }
    /* on hover underline and make little larger with a small animation */
    a:hover {
        text-decoration: underline;
        font-size: 1.1em;
        transition: 0.2s;
    }
    /* newsClass should be centered  make borders rounded and some gap on bottom*/
    .newsClass {
        background-color: aliceblue;
        margin: auto;
        width: 50%;
        /* border: 3px solid rgb(0, 0, 0); */
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 20px;
        margin-top: 20px;
    }

    .graphClass {
        width: 95%;
    }
    /* tableClass inherite from newsClass */
    .tableClass {
        background-color: aliceblue;
        margin: auto;
        width: 50%;
        /* border: 3px solid rgb(0, 0, 0); */
        padding: 10px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
</style>

<script>
    import axios from "axios";
    import { ref, onMounted, isRef } from "vue";
    import Graph from "../components/Graph.vue";
    export default {
        components: {
            Graph,
        },
        data() {
            return {
                news: {},
                dataToday: {},
                compName: "",
                chartData: [],
            };
        },
        props: {
            query: String,
        },
        setup(props) {
            // news and dataToday are like global variables. They will be used in the template. query is from the prev page.
            const news = ref({});
            const dataToday = ref({});
            const compName = ref("");
            const chartData = ref([]);
            const query = ref(props.query);
            fetch("http://localhost:5000/api/all").then((response) => {
                const data = response.json().then((data) => {
                    console.log(data);
                    compName.value = data[query.value];
                    GetNews();
                    console.log(news.value);
                });
            });

            onMounted(async () => {
                try {
                    const latestData = await getLatest();
                    console.log(latestData);
                    dataToday.value = latestData;
                    chartData.value = await getStockValues();
                    console.log(chartData.value);
                } catch (error) {
                    console.error(error);
                }
            });

            async function getLatest() {
                try {
                    const apiURL = "http://localhost:5000/api/stock/";
                    const response = await axios.post(apiURL, {
                        ticker: query.value,
                    });
                    return response.data;
                } catch (error) {
                    throw error;
                }
            }

            async function getStockValues() {
                try {
                    const apiURL = "http://localhost:5000/api/stock/data/";
                    const response = await axios.post(apiURL, {
                        ticker: query.value,
                    });
                    return response.data;
                } catch (error) {
                    throw error;
                }
            }

            function today() {
                const today = new Date();
                const yesterday = new Date();

                // check if today is sat, sun or mon. if it is then return friday's date
                if (today.getDay() == 0) {
                    today.setDate(today.getDate() - 2);
                } else if (today.getDay() == 6) {
                    today.setDate(today.getDate() - 1);
                } else if (today.getDay() == 1) {
                    today.setDate(today.getDate() - 3);
                }
                yesterday.setDate(today.getDate() - 1);
                const dd = String(today.getDate()).padStart(2, "0");
                const mm = String(today.getMonth() + 1).padStart(2, "0");
                const yyyy = today.getFullYear();
                const date_today = yyyy + "-" + mm + "-" + dd;

                const dd1 = String(yesterday.getDate()).padStart(2, "0");
                const mm1 = String(yesterday.getMonth() + 1).padStart(2, "0");
                const yyyy1 = yesterday.getFullYear();
                const date_yesterday = yyyy1 + "-" + mm1 + "-" + dd1;

                return [date_yesterday, date_today];
            }
            async function GetNews() {
                try {
                    // today's date
                    const days = today();
                    console.log(days[0], days[1], compName.value);
                    const apiURL = "http://localhost:3000/api/news";
                    const response = await axios
                        .post(apiURL, {
                            query: compName.value,
                            from: days[0],
                            to: days[1],
                        })
                        .then((response) => {
                            console.log(response.data);
                            news.value = response.data;
                        });
                } catch (error) {
                    // throw error;
                    console.log(error);
                }
            }
            return { dataToday, compName, news,chartData };
        },
    };
</script>
