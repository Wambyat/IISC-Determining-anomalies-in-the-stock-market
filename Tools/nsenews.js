const axios = require("axios");

const url =
    "https://www.nseindia.com/api/corporate-announcements?index=equities";

axios
    .get(url)
    .then((response) => {
        // Handle the response data
        const data = response.data;
        console.log(data);
    })
    .catch((error) => {
        // Handle the error
        console.error(error);
    });
