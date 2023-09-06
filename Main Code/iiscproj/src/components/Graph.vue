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
            const data = props.data;
            const chartOptions = ref({
                series: [
                    {
                        name: "Stock",
                        data: data,
                        useHTML: true,
                        tooltip: {
                            pointFormatter: function () {
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
