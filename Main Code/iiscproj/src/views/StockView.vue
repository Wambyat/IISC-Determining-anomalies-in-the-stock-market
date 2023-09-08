<template>
    <div>
        <div v-if="company_name" class="newsClass">
            <h2>{{ company_name }}</h2>
        </div>
        <div v-else>loading</div>
        <div v-if="Object.keys(stock_data_today).length === 0">
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
                    <td>{{ stock_data_today["AveragePrice"] }}</td>
                    <td>{{ stock_data_today["HighPrice"] }}</td>
                    <td>{{ stock_data_today["LowPrice"] }}</td>
                    <td>{{ stock_data_today["LastPrice"] }}</td>
                    <td>{{ stock_data_today["DeliverableQty"] }}</td>
                    <td>{{ stock_data_today["No.ofTrades"] }}</td>
                </tr>
            </table>
        </div>
        <div v-if="chart_data.length === 0">Loading</div>
        <div v-else>
            <Graph :data="chart_data" class="newsClass graphClass" />
        </div>
        <div v-if="news" class="newsClass">
            <h2>News</h2>
            <!-- There are other details available. Add acoording to the requirements. Refer to </newscatcher> documentation for full details. -->
            <div v-for="article in news">
                <component
                    :is="article.link.startsWith('http') ? 'a' : 'router-link'"
                    :key="article.link"
                    :to="article.link"
                    :href="article.link"
                    target="_blank">
                    {{ article.title }}
                    <br />
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
                stock_data_today: {},
                company_name: "",
                chart_data: [],
            };
        },
        props: {
            query: String,
        },
        setup(props) {
            const news = ref({});
            const stock_data_today = ref({});
            const company_name = ref("");
            const chart_data = ref([]);
            const query = ref(props.query);
            fetch("http://localhost:5000/api/all").then((response) => {
                response.json().then((data) => {
                    company_name.value = data[query.value];
                    GetNews();
                });
            });

            onMounted(async () => {
                try {
                    const latestData = await getTodayStockData();
                    stock_data_today.value = latestData;
                    chart_data.value = await getStockValues();
                } catch (error) {
                    console.error(error);
                }
            });

            // This gets data from NSE about the stock. It will be today's live data. It has been filtered in the flask server.
            async function getTodayStockData() {
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

            // This gets data from NSE about the stock prices only. It will be one year's worth of data. It has been formatted, by flask, as required by highcharts, already.
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

            // This is a helper function for today()
            function formatDate(date) {
                const year = date.getFullYear();
                const month = (date.getMonth() + 1).toString().padStart(2, "0");
                const day = date.getDate().toString().padStart(2, "0");
                return `${year}-${month}-${day}`;
            }

            // This function returns an array of dates for the last 30 days, excluding weekends.
            function today() {
                const dates = [];
                const currentDate = new Date();

                for (let i = 0; i < 30; i++) {
                    const date = new Date();
                    date.setDate(currentDate.getDate() - i);

                    if (date.getDay() >= 1 && date.getDay() <= 5) {
                        dates.push(formatDate(date));
                    }
                }
                return dates;
            }

            // This function gets news from </newscatcher>. It should be unfiltered. It has been set to get news from the last 5ish days.
            async function GetNews() {
                try {
                    const days = today();
                    const apiURL = "http://localhost:3000/api/news";
                    const response = await axios
                        .post(apiURL, {
                            query: company_name.value,
                            from: days[5],
                            to: days[0],
                            page_size: 5,
                        })
                        .then((response) => {
                            news.value = response.data;
                        });
                } catch (error) {
                    console.log(error);
                }
            }
            return { stock_data_today, company_name, news, chart_data };
        },
    };
</script>
