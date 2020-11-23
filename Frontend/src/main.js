import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ToastService from 'primevue/toastservice';

import 'primevue/resources/themes/bootstrap4-light-purple/theme.css';

import 'primevue/resources/primevue.min.css';

import 'primeicons/primeicons.css';

import 'primeflex/primeflex.css';

const Vue = createApp(App)

Vue.use(router)
Vue.use(ToastService)
Vue.mount('#app')
