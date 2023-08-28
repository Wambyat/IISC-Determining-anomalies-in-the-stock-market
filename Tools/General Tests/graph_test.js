Highcharts.stockChart("container", {
    series: [
        {
            name: "Stock",
            "data": [
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
