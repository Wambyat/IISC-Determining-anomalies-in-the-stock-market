const express = require("express");
const axios = require("axios");

const app = express();

app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "http://localhost:8080");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");
    next();
});
const port = 3000;

app.get("/api/starter/", (req, res) => {
    const url = "https://www.nseindia.com/";
    axios
        .get(url)
        .then((response) => {
            res.json(response.data);
        })
        .catch((error) => {
            res.status(500).json({
                error: "An error occurred",
                error: error,
                url: url,
            });
        });
});

// Proxy route
app.get("/api/corporate-announcements", (req, res) => {
    const url =
        "https://www.nseindia.com/api/corporate-announcements?index=equities";
    axios
        .get(url)
        .then((response) => {
            res.json(response.data);
        })
        .catch((error) => {
            res.status(500).json({
                error: "An error occurred",
                error: error,
                url: url,
            });
        });
});

// accept post request
app.post("/api/news", (req, res) => {
    const requ = req.body;
    var options = {
        method: "GET",
        url: "https://api.newscatcherapi.com/v2/search",
        params: {
            q: requ.query,
            lang: requ.lang,
            sort_by: "relevancy",
            page: "1",
            from_rank: "0",
            to_rank: "1000",
            countries: "IN",
            page_size: "3",
            from: requ.from,
            to: requ.to,
        },
        headers: {
            "x-api-key": "oAulWCneqCcjaTq5JH58zE7VsvjH32s-7zkqBK5axIc",
        },
    };

    axios
        .request(options)
        .then(function (response) {
            const resu = response.data;
            // make json with title, link
            var json = [];
            for (let i = 0; i < resu.articles.length; i++) {
                json.push({
                    title: resu.articles[i].title,
                    link: resu.articles[i].link,
                });
            }
            res.json(json);
        })
        .catch((error) => {
            res.status(500).json({
                error: "An error occurred",
                error: error,
                url: url,
            });
        });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
