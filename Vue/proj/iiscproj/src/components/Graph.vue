<template>
    <div>
        <highcharts :constructor-type="'stockChart'" :options="chartOptions" />
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
            });
            return {
                chartOptions,
            };
        },
    };
</script>
