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
            res.status(500).json({ error: "An error occurred", error: error });
        });
});

// Start the proxy server
app.listen(port, () => {
    console.log(`Proxy server listening at http://localhost:${port}`);
});
