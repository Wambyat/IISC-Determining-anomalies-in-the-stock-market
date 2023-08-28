<template>
    <div>
        <h2>{{ query }}</h2>
        <div v-if="compName">
            <h2>{{ compName }}</h2>
        </div>
        <div v-else>loading</div>
        <div v-if="dataToday">
            <table>
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
        <div v-else>
            <p>Loading</p>
        </div>
        <Graph :data="chartData" />
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
    import axios from "axios";
    import { ref, onMounted, isRef } from "vue";
    import Graph from '../components/Graph.vue';
    export default {
        components: {
            Graph,
        },
        data() {
            return {
                news: {},
                dataToday: {},
                compName: "",
                chartData: [
                {
                    "x": 1234567890000,
                    "y": 50,
                    "articleLink": "https://example.com/article1"
                },
                {
                    "x": 1234567900000,
                    "y": 55,
                    "articleLink": "https://example.com/article2"
                },
                {
                    "x": 1234567910000,
                    "y": 60,
                    "articleLink": "https://example.com/article3"
                },
                {
                    "x": 1234567920000,
                    "y": 15,
                    "articleLink": "https://example.com/article4"
                },
                {
                    "x": 1234567930000,
                    "y": 85,
                    "articleLink": "https://example.com/article5"
                },
                {
                    "x": 1234567940000,
                    "y": 37,
                    "articleLink": "https://example.com/article6"
                },
                {
                    "x": 1234567950000,
                    "y": 70,
                    "articleLink": "https://example.com/article7"
                },
                {
                    "x": 1234567960000,
                    "y": 5,
                    "articleLink": "https://example.com/article8"
                },
                {
                    "x": 1234567970000,
                    "y": 90,
                    "articleLink": "https://example.com/article9"
                },
                {
                    "x": 1234567980000,
                    "y": 25,
                    "articleLink": "https://example.com/article10"
                },
                {
                    "x": 1234567990000,
                    "y": 42,
                    "articleLink": "https://example.com/article11"
                },
                {
                    "x": 1234568000000,
                    "y": 78,
                    "articleLink": "https://example.com/article12"
                },
                {
                    "x": 1234568010000,
                    "y": 91,
                    "articleLink": "https://example.com/article13"
                },
                {
                    "x": 1234568020000,
                    "y": 18,
                    "articleLink": "https://example.com/article14"
                },
                {
                    "x": 1234568030000,
                    "y": 63,
                    "articleLink": "https://example.com/article15"
                },
                {
                    "x": 1234568040000,
                    "y": 47,
                    "articleLink": "https://example.com/article16"
                },
                {
                    "x": 1234568050000,
                    "y": 32,
                    "articleLink": "https://example.com/article17"
                },
                {
                    "x": 1234568060000,
                    "y": 76,
                    "articleLink": "https://example.com/article18"
                },
                {
                    "x": 1234568070000,
                    "y": 8,
                    "articleLink": "https://example.com/article19"
                },
                {
                    "x": 1234568080000,
                    "y": 53,
                    "articleLink": "https://example.com/article20"
                },
                {
                    "x": 1234568090000,
                    "y": 67,
                    "articleLink": "https://example.com/article21"
                }
            ],
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
            const query = ref(props.query);
            fetch("http://localhost:5000/api/all").then((response) => {
                const data = response.json().then((data) => {
                    console.log(data);
                    compName.value = data[query.value];
                });
            });

            onMounted(async () => {
                try {
                    const latestData = await getLatest();
                    console.log(latestData);
                    dataToday.value = latestData;
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
            return { dataToday, compName };
        },
    };
</script>
