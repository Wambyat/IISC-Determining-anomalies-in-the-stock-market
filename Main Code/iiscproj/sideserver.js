const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");

const app = express();

app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "http://localhost:8080");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
    res.setHeader("Access-Control-Allow-Headers", "Content-Type");
    next();
});

// Change this to whatever port you want.
const port = 3000;

// This server exists only so that we can spam NSE with requests so that it might eventually send back a proper response.

// This is just a route that MIGHT "whitelist" us before we spam.
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

// This is where we spam NSE with requests. res.json is used to send back the response to the client.
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


// This function removes all the standard company suffixes from the query.
function removeCompanySuffixes(query) {
    const companySuffixes = [
        "limited",
        "incorporated",
        "ltd",
        "inc",
        "corp",
        "corporation",
        "co",
        "pvt",
        "private",
        "plc",
        "pl",
        "llc",
        "llp",
    ];

    const newQuery = [];
    for (const word of query.split(" ")) {
        if (!companySuffixes.includes(word.toLowerCase())) {
            newQuery.push(word);
        }
    }

    return newQuery.join(" ");
}

// This is so that the POST request body can be parsed.
app.use(bodyParser.json());

// This is the route that queries the </newscatcher> API. If you use this and get an error that's something like you dont have permission or something, either get your own API key or email me at anirudhaanekal@gmail.com and I'll ask for more requests or something.
app.post("/api/news", (req, res) => {
    const requ = req.body;
    const query = removeCompanySuffixes(requ.query);

    var options = {
        method: "GET",
        url: "https://api.newscatcherapi.com/v2/search",
        params: {
            q: query,
            lang: "en",
            sort_by: "relevancy",
            page: "1",
            from_rank: "0",
            to_rank: "1000",
            countries: "IN",
            page_size: requ.page_size,
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
            var json = [];
            for (let i = 0; i < resu.articles.length; i++) {
                const date = resu.articles[i].published_date.split(" ")[0];
                const unixTimestamp = new Date(date).getTime();
                json.push({
                    title: resu.articles[i].title,
                    link: resu.articles[i].link,
                    date: unixTimestamp,
                });
            }
            res.json(json);
        })
        .catch((error) => {
            console.log(error);
            res.status(500).json({
                error: error,
            });
        });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
