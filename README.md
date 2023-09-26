# Stock Market Analysis Interface

This is project is made in Vue. Run the file `RUNME.bat` to start all the servers. Run `npm install` once before.
Refer to the flow diagram (flow.png) in root folder for a visual understanding of the project.

It is a stock market analysis based project with social media posts and news integrated. News integration to be done using [ \</newscatcher> ](https://newscatcherapi.com/)

Reddit and 𝕏 (twitter) integration code is ready and will work and can be integrated as soon as the companies change their API rules. The github action will work if there is more than 2 branches (excluding legacy)

## Folder Structure
### Clicking on a folder will take you to an explanation. Clicking on a file will take you to the code.

* [LaTeX_Documentation](#latex_documentation)
  * [Main doc.pdf](/LaTeX_Documentation/Main_doc.pdf")
* [Main Code](#main-code)
  * [Flask](#flask)
    * [app.py](./Main%20Code/Flask/app.py)
  * [iiscproj](#iiscproj)
    * [public](#public)
    * [src](#src)
      * [assets](#assets)
      * [components](#components)
        * [Graph.vue](./Main%20Code/iiscproj/src/components/Graph.vue)
        * [SearchBar.vue](./Main%20Code/iiscproj/src/components/SearchBar.vue)
      * [router](#router)
        * [index.js](./Main%20Code/iiscproj/src/router/index.js)
      * [views](#views)
        * [HomeView.vue](./Main%20Code/iiscproj/src/views/HomeView.vue)
        * [ModelView.vue](./Main%20Code/iiscproj/src/views/ModelView.vue)
        * [StockView.vue](./Main%20Code/iiscproj/src/views/StockView.vue)
      * [App.vue](./Main%20Code/iiscproj/src/App.vue)
      * [main.js](./Main%20Code/iiscproj/src/main.js)
    * [sideserver.js](./Main%20Code/iiscproj/sideserver.js)
* [Tools](#tools)
  * [General Tests](./Tools/General%20Tests)
    * [graph_test.html](./Tools/General%20Tests/graph_test.html)
    * [graph_test.js](./Tools/General%20Tests/graph_test.js)
    * [selenium_Test.py](./Tools/General%20Tests/selenium_Test.py)
  * [image](#image)
    * [csv_merger.py](./Tools/image/csv_merger.py)
    * [gDrive_uploader.py](./Tools/image/gDrive_uploader.py)
    * [image_checker.py](./Tools/image/image_checker.py)
    * [image_cutter.py](./Tools/image/image_cutter.py)
    * [image_gradient_exponential_maker.py](./Tools/image/image_gradient_exponential_maker.py)
    * [image_organiser.py](./Tools/image/image_organiser.py)
    * [image_renamer.py](./Tools/image/image_renamer.py)
    * [image.py](./Tools/image/image.py)
  * [NSE](#nse)
    * [nse.py](./Tools/NSE/nse.py)
    * [selenium_cookie.py](./Tools/NSE/selenium_cookie.py)
    * [selenium_get.py](./Tools/NSE/selenium_get.py)
    * [unix_to_normal_time_converter.py](./Tools/NSE/unix_to_normal_time_converter.py)
  * [reddit_twitter](#reddit_twitter)
    * [reddit_pushshift.py](./Tools/reddit_twitter/reddit_pushshift.py)
    * [reddit_tester.py](./Tools/reddit_twitter/reddit_tester.py)
    * [twitter.py](./Tools/reddit_twitter/twitter.py)

### [LaTeX_Documentation:](/LaTeX_Documentation)
Contains the LaTeX documentation of the project. This is only basic documentation that explains why we have used the various tools and frameworks.

### [Main Code:](/Main%20Code)
Contains the main code of the project. The code is divided into two parts:
### [Flask:](/Main%20Code/Flask)
This is the backend of the project. It is made using Flask and is used to run the python scripts and send the data to the frontend. This calls nse_lib.

### [iiscproj:](/Main%20Code/iiscproj)
This is the frontend of the project. It is made using Vue and is used to display the data. It calls the Flask backend to get the data.
* #### [public:](/Main%20Code/iiscproj/public)
    This has some base Vue project file.
* #### [src:](/Main%20Code/iiscproj/src)
    This has the main code of the frontend.
    * #### [assets:](/Main%20Code/iiscproj/src/assets)
        This is where you can add some global css or images.
    * #### [components:](/Main%20Code/iiscproj/src/components)
        This has the components of the project. There are 2 of these. [Graph.vue](./Main%20Code/iiscproj/src/components/Graph.vue) and [SearchBar.vue](./Main%20Code/iiscproj/src/components/SearchBar.vue).
        * Graph.vue: This is the component that displays the graph. It is made using HighChart.js.
        * SearchBar.vue: This is the component that displays the search bar. It is the dynamic search bar that is used to search for companies. It is made using some json filtering.
    * #### [router:](/Main%20Code/iiscproj/src/router)
        This has the [router](/Main%20Code/iiscproj/src/router/index.js) of the project. It is used to navigate between the different views.
    * #### [views:](/Main%20Code/iiscproj/src/views)
        This has the various "pages" of the project. There are 3 of these. [HomeView.vue](./Main%20Code/iiscproj/src/views/HomeView.vue), [ModelView.vue](./Main%20Code/iiscproj/src/views/ModelView.vue) and [StockView.vue](./Main%20Code/iiscproj/src/views/StockView.vue).
        * HomeView.vue: This is the home page of the project. It has the search bar and corporate announcements.
        * ModelView.vue: This is the page that displays the model. It doesn't have anything as the model was incomplete.
        * StockView.vue: This is the page that displays the stock data. It has the graph and the news and social media posts. The social media posts are removed as the reddit and twitter APIs have changed.
    * #### [App.vue:](/Main%20Code/iiscproj/src/App.vue)
        This is the main Vue file. It has the navbar.
    * #### [main.js:](/Main%20Code/iiscproj/src/main.js)
        This is the main js file. It is the starter file.
    * #### [sideserver.js:](/Main%20Code/iiscproj/sideserver.js)
        This is the server that pings corporate announcements from NSE. It also calls the newscathcer API.
* ### [Tools](/Tools/)
    * #### [General Tests:](/Tools/General%20Tests)
        This has some general ests that were used to test the project.
        * [graph_test.html](/Tools/General%20Tests/graph_test.html): This is a html file that was used to test the graph.
        * [graph_test.js](/Tools/General%20Tests/graph_test.js): This is a js file that was used to test the graph.
        * [selenium_Test.py](/Tools/General%20Tests/selenium_Test.py): This was a selenium test that was used to try to circumvent the NSE cookie problem.
    * #### [image:](/Tools/image)
        There are a lot of files in here. These are small scripts I wrote for debugging the model. They are not important.
    * #### [NSE:](/Tools/NSE)
        * [nse.py](/Tools/NSE/nse.py): This is a file where I was testing the NSE library.
        * [selenium_cookie.py](/Tools/NSE/selenium_cookie.py): This is a file where I was testing the selenium cookie problem.
        * [selenium_get.py](/Tools/NSE/selenium_get.py): This is another file where I was testing the selenium cookie problem.
        * [unix_to_normal_time_converter.py](/Tools/NSE/unix_to_normal_time_converter.py): This is script to convert unix timetamp to normal time.
    * #### [reddit_twitter:](/Tools/reddit_twitter)
        * [reddit_pushshift.py](/Tools/reddit_twitter/reddit_pushshift.py): This is a file where I was testing the reddit pushshift API. This is a public databse. Try this before testing the official reddit API.
        * [reddit_tester.py](/Tools/reddit_twitter/reddit_tester.py): This is a file where I was testing the reddit API.
        * [twitter.py](/Tools/reddit_twitter/twitter.py): This is a file where I was testing the twitter API.
