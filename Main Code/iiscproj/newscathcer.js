function fun() {
    var axios = require("axios").default;

    var options = {
        method: "GET",
        url: "https://api.newscatcherapi.com/v2/search",
        params: {
            q: "maruti",
            lang: "en",
            sort_by: "relevancy",
            page: "1",
            from_rank: "0",
            to_rank: "1000",
            countries: "IN",
            page_size: "3",
            from: "2023-08-28",
            to: "2023-08-29",
        },
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
                console.log(
                    res.articles[i].title,
                    ": ",
                    res.articles[i].published_date
                );
                console.log(res.articles[i].link);
                console.log("\n");
            }
        })
        .catch(function (error) {
            console.error(error);
        });
}

// today's date in yyyy-mm-dd format
function today() {
    const today = new Date();
    
    // check if today is sat, sun or mon. if it is then return friday's date
    if (today.getDay() == 0) {
        today.setDate(today.getDate() - 2);
    } else if (today.getDay() == 6) {
        today.setDate(today.getDate() - 1);
    } else if (today.getDay() == 1) {
        today.setDate(today.getDate() - 3);
    }
    const dd = String(today.getDate()).padStart(2, "0");
    const mm = String(today.getMonth() + 1).padStart(2, "0");
    const yyyy = today.getFullYear();

    return [yyyy + "-" + mm + "-" + (parseInt(dd) - 1), yyyy + "-" + mm + "-" + dd ]
}

console.log(today());