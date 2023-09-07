<template>
    <div>
        <highcharts
            :constructor-type="'stockChart'"
            :options="chartOptions"
            class="graphBaby" />
    </div>
</template>

<script>
    import { ref } from "vue";
    export default {
        name: "Graph",
        props: {
            data: Array,
            chartOptions: Object,
        },
        setup(props) {
            // This is coming from StockView.
            const data = props.data;

            // This is how we pass our options and data to Highcharts.
            const chartOptions = ref({
                series: [
                    {
                        name: "Stock",
                        // This is the data we're plotting. Should be in the format {x: unix timestamp(milliseconds), y: price, articleTitle: <optional> title, articleLink: <optional> link}
                        data: data,
                        useHTML: true,
                        tooltip: {
                            pointFormatter: function () {
                                // This is where we are creating the tooltip. This is what is rendered when we hover over a point.
                                if (
                                    this.articleLink === "No News" ||
                                    this.articleLink === undefined
                                ) {
                                    return (
                                        "Price: " +
                                        this.y +
                                        "<br> No News" +
                                        "</a>"
                                    );
                                }
                                if (this.articleTitle) {
                                    return (
                                        "Price: " +
                                        this.y +
                                        '<br> <a href="' +
                                        this.articleLink +
                                        '">' +
                                        this.articleTitle +
                                        "</a>"
                                    );
                                }
                                return (
                                    "Price: " +
                                    this.y +
                                    '<br> <a href="' +
                                    this.articleLink +
                                    '">' +
                                    this.articleLink +
                                    "</a>"
                                );
                            },
                        },
                    },
                ],
                title: {
                    text: "Stock Price",
                },
                theme: "brand-dark",
                // other themes can be found here: https://github.com/highcharts/highcharts/tree/master/ts/masters/themes. change accordingly here and in main.js (This is present two folder up from this file.)
            });
            return {
                chartOptions,
            };
        },
    };
</script>

<style>
    .graphBaby {
        border-radius: 15px;
    }
</style>
