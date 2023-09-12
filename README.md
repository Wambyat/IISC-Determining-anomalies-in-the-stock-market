# Stock Market Analysis Interface

This is project is made in Vue.
Refer to the flow diagram (flow.png) in root folder for a visual understanding of the project.

It is a stock market analysis based project with social media posts and news integrated. News integration to be done using [ \</newscatcher> ](https://newscatcherapi.com/)

Reddit and 𝕏 (twitter) integration code is ready and will work and can be integrated as soon as the companies change their API rules.

### Folder Structure

* [LaTeX_Documentation](#latex_documentation)
* [Main Code](#main-code)
  * [Flask](#flask)
    * [app.py]
  * [iiscproj](#iiscproj)
    * [public]
    * [src]
      * [assets]
      * [components]
        * [Graph.vue](#graph.vue)
        * [SearchBar.vue](#searchbar.vue)
      * [router](#router)
        * [index.js]
      * [views](#views)
        * [HomeView.vue](#homeview.vue)
        * [ModelView.vue](#modelview.vue)
        * [StockView.vue](#stockview.vue)
      * [App.vue](#app.vue)
      * [main.js](#main.js)
    * [README.md]
    * [sideserver.js](#sideserver.js)
* [Tools](#tools)
  * [General Tests](.\IISC-Summer-Internship\Tools\General Tests)
    * [graph_test.html](.\IISC-Summer-Internship\Tools\General Tests\graph_test.html)
    * [graph_test.js](.\IISC-Summer-Internship\Tools\General Tests\graph_test.js)
    * [selenium_Test.py](.\IISC-Summer-Internship\Tools\General Tests\selenium_Test.py)
  * [image](.\IISC-Summer-Internship\Tools\image)
    * [capture.png](.\IISC-Summer-Internship\Tools\image\capture.png)
    * [capture2.png](.\IISC-Summer-Internship\Tools\image\capture2.png)
    * [csv_merger.py](.\IISC-Summer-Internship\Tools\image\csv_merger.py)
    * [gDrive_uploader.py](.\IISC-Summer-Internship\Tools\image\gDrive_uploader.py)
    * [image.py](.\IISC-Summer-Internship\Tools\image\image.py)
    * [image_checker.py](.\IISC-Summer-Internship\Tools\image\image_checker.py)
    * [image_cutter.py](.\IISC-Summer-Internship\Tools\image\image_cutter.py)
    * [image_gradient_exponential_maker.py](.\IISC-Summer-Internship\Tools\image\image_gradient_exponential_maker.py)
    * [image_organiser.py](.\IISC-Summer-Internship\Tools\image\image_organiser.py)
    * [image_renamer.py](.\IISC-Summer-Internship\Tools\image\image_renamer.py)
  * [NSE](.\IISC-Summer-Internship\Tools\NSE)
    * [nse.py](.\IISC-Summer-Internship\Tools\NSE\nse.py)
    * [selenium_cookie.py](.\IISC-Summer-Internship\Tools\NSE\selenium_cookie.py)
    * [selenium_get.py](.\IISC-Summer-Internship\Tools\NSE\selenium_get.py)
    * [unix_to_normal_time_converter.py](.\IISC-Summer-Internship\Tools\NSE\unix_to_normal_time_converter.py)
  * [reddit_twitter](.\IISC-Summer-Internship\Tools\reddit_twitter)
    * [reddit_pushshift.py](.\IISC-Summer-Internship\Tools\reddit_twitter\reddit_pushshift.py)
    * [reddit_tester.py](.\IISC-Summer-Internship\Tools\reddit_twitter\reddit_tester.py)
    * [twitter.py](.\IISC-Summer-Internship\Tools\reddit_twitter\twitter.py)

#### LaTeX_Documentation:
Contains the LaTeX documentation of the project. This is only basic documnetaion that explains why we have used the various tools and frameworks.