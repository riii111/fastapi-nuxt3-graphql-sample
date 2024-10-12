import { defineNuxtConfig } from 'nuxt/config'
import vuetify from 'vite-plugin-vuetify'

export default defineNuxtConfig({
  app: {
    baseURL: process.env.BASE_URL
  },

  ssr: true,

  build: {
    transpile: ['vuetify', 'primevue']
  },

  css: ['vuetify/styles', '@/assets/style/main.scss'],

  hooks: {
    // Vuetifyのカスタム設定が反映されるようにする。
    'vite:extendConfig': (config) => {
      config.plugins?.push(
        vuetify({
          autoImport: true,
          styles: { configFile: 'assets/style/variables.scss' }
        })
      )
    }
  },

  runtimeConfig: {
    public: {
      apiClientBase: 'http://localhost:8001'
    }
  },

  vite: {
    ssr: {
      noExternal: ['vuetify']
    },
    define: {
      'process.env.DEBUG': false
    },
    server: {
      watch: {
        usePolling: true
      },
      hmr: {
        port: Number(process.env.HMR_PORT)
      }
    }
  },

  // vuetifyのソースマップ警告がTerminalに出力されないようにする。
  sourcemap: {
    client: false,
    server: false
  },

  // ネストしたcomposableも自動でインポートするようにする
  // https://nuxt.com/docs/guide/directory-structure/composables#how-files-are-scanned
  imports: {
    dirs: ['composables/**', 'f/**']
  },

  // components内のすべてがディレクトリ名なしで利用可能。
  components: [
    {
      path: '~/components',
      pathPrefix: false
    }
  ],

  compatibilityDate: '2024-10-12'
})