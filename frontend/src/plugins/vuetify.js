import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#000000',
        secondary: '#424242',
        accent: '#000000',
        error: '#000000',
        info: '#000000',
        success: '#000000',
        warning: '#000000'
      }
    }
  },
  icons: {
    iconfont: 'mdi'
  }
}) 