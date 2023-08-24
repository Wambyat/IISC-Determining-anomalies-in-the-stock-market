<template>
    <div>
        <h2>{{ query }}</h2>
        <h2 id="compName">before</h2>
        <p>grrr</p>
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
            compName: String,
        },
        setup(props) {
            // news and dataToday are like global variables. They will be used in the template. query is from the prev page.
            const news = ref({});
            const dataToday = ref({});
            let compName = ref(props.compName);
            const query = ref(props.query);
            let comp = fetch("http://localhost:5000/api/all").then(
                (response) => {
                    const data = response.json().then((data) => {
                        console.log(data);
                        document.getElementById("compName").innerHTML =
                            data[query.value];
                    });
                }
            );
            onMounted(async () => {
                // This gets the latest data about the stock from nse. This is calling flask.
                function getLatest() {
                    console.log(query.value);
                    const apiURL = "http://localhost:5000/api/stock/";
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
            });
            return { dataToday };
        },
    };
</script>
