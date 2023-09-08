import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import Highcharts from "highcharts";
import StockModule from "highcharts/modules/stock";
import HighchartsVue from "highcharts-vue";

// This is where you set the highcharts style.
import brandDark from "highcharts/themes/brand-dark";
brandDark(Highcharts);
StockModule(Highcharts);

const app = createApp(App);

app.use(HighchartsVue);
app.use(router);
app.mount("#app");
