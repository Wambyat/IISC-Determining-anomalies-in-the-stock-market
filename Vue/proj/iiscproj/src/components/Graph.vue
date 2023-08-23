<template>
    <div>
        <div style="width: 80%">
            <canvas ref="myChart"></canvas>
        </div>
    </div>
</template>

<script>
    import Chart from 'chart.js/auto';
    export default {
        props: {
            dataPoints: Array,
        },
        mounted() {
            this.renderStockChart();
        },
        methods: {
            renderStockChart() {
                const prices = this.dataPoints.map((point) => point.price);
                const dates = this.dataPoints.map((point) => point.date);

                const ctx = this.$refs.myChart.getContext("2d");
                const myChart = new Chart(ctx, {
                    type: "line",
                    data: {
                        labels: dates,
                        datasets: [
                            {
                                label: "Stock Prices",
                                data: prices,
                                borderColor: "green",
                                fill: false,
                            },
                        ],
                    },
                });

                this.dataPoints.forEach((point, index) => {
                    const iframe = document.createElement("iframe");
                    iframe.src = point.articleUrl;
                    iframe.width = "300";
                    iframe.height = "200";

                    // Set the position of the iframe using CSS
                    iframe.style.position = "absolute";
                    iframe.style.left =
                        myChart.chartArea.left + index * 50 + "px";
                    iframe.style.top = myChart.chartArea.top + "px";

                    this.$el.appendChild(iframe);
                });
            },
        },
    };
</script>
