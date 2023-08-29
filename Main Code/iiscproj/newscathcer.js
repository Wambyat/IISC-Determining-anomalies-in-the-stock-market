var axios = require("axios").default;

var options = {
    method: "GET",
    url: "https://api.newscatcherapi.com/v2/search",
    params: { q: "maruti", lang: "en", sort_by: "relevancy", page: "1", from_rank: "0", to_rank: "1000", countries: "IN", page_size: "3", from: "2023-08-28", to: "2023-08-29"},
    headers: {
        "x-api-key": "oAulWCneqCcjaTq5JH58zE7VsvjH32s-7zkqBK5axIc",
    },
};

axios
    .request(options)
    .then(function (response) {
        const res = response.data;
        //  print titles of the json
        for (let i = 0; i < res.articles.length; i++) {
            console.log(res.articles[i].title,": ",res.articles[i].published_date);
            console.log(res.articles[i].link)
            console.log("\n");
        }
    })
    .catch(function (error) {
        console.error(error);
    });
