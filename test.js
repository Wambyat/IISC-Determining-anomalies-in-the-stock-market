Highcharts.stockChart("container", {
    series: [
        {
            name: "Stock",
            data: [
                {
                    x: 1234567890000,
                    y: 50,
                    articleLink: "https://example.com/article1",
                },
                {
                    x: 1234567900000,
                    y: 55,
                    articleLink: "https://example.com/article2",
                },
                {
                    x: 1234567910000,
                    y: 60,
                    articleLink: "https://example.com/article3",
                },
            ],
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
