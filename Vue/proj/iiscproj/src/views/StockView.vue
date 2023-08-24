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
    export default {
        data() {
            return {
                news: {},
                dataToday: {},
                compName: "",
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
