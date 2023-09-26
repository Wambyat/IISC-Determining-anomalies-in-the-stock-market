# Stock Market Analysis Interface

This is project is made in Vue.
Refer to the flow diagram (flow.png) in root folder for a visual understanding of the project.

It is a stock market analysis based project with social media posts and news integrated. News integration to be done using [ \</newscatcher> ](https://newscatcherapi.com/)

Reddit and 𝕏 (twitter) integration code is ready and will work and can be integrated as soon as the companies change their API rules.

### Folder Structure

* [LaTeX_Documentation](#latex_documentation)
  * [Main doc.pdf](.\LaTeX_Documentation\Main_doc.pdf")
* [Main Code](#main-code)
  * [Flask](#flask)
    * [app.py](#app.py)
  * [iiscproj](#iiscproj)
    * [public]
    * [src](/Main%20Code/iiscproj/src)
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
  * [General Tests](.\Tools\General Tests)
    * [graph_test.html](.\Tools\General Tests\graph_test.html)
    * [graph_test.js](.\Tools\General Tests\graph_test.js)
    * [selenium_Test.py](.\Tools\General Tests\selenium_Test.py)
  * [image](.\Tools\image)
    * [capture.png](.\Tools\image\capture.png)
    * [capture2.png](.\Tools\image\capture2.png)
    * [csv_merger.py](.\Tools\image\csv_merger.py)
    * [gDrive_uploader.py](.\Tools\image\gDrive_uploader.py)
    * [image.py](.\Tools\image\image.py)
    * [image_checker.py](.\Tools\image\image_checker.py)
    * [image_cutter.py](.\Tools\image\image_cutter.py)
    * [image_gradient_exponential_maker.py](.\Tools\image\image_gradient_exponential_maker.py)
    * [image_organiser.py](.\Tools\image\image_organiser.py)
    * [image_renamer.py](.\Tools\image\image_renamer.py)
  * [NSE](.\Tools\NSE)
    * [nse.py](.\Tools\NSE\nse.py)
    * [selenium_cookie.py](.\Tools\NSE\selenium_cookie.py)
    * [selenium_get.py](.\Tools\NSE\selenium_get.py)
    * [unix_to_normal_time_converter.py](.\Tools\NSE\unix_to_normal_time_converter.py)
  * [reddit_twitter](.\Tools\reddit_twitter)
    * [reddit_pushshift.py](.\Tools\reddit_twitter\reddit_pushshift.py)
    * [reddit_tester.py](.\Tools\reddit_twitter\reddit_tester.py)
    * [twitter.py](.\Tools\reddit_twitter\twitter.py)

#### LaTeX_Documentation:
Contains the LaTeX documentation of the project. This is only basic documnetaion that explains why we have used the various tools and frameworks.