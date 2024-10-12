const fs = require('node:fs')

/**
 * @param {string} file
 * @returns {string[]}
 */
function loadPattern (file) {
  return fs.readFileSync(file, 'utf8')
    .split('\n')
    .map(line => line.trim().replace('\\#', '#'))
    .filter(line => line && !line.startsWith('#'))
}


module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: ['simple-import-sort', 'unused-imports'],
    ignorePatterns: [
    ...loadPattern('.gitignore'),
    ...loadPattern('.eslintignore')
  ],
  settings: {
    'import/resolver': {
      typescript: {
        alwaysTryTypes: true,
      },
    },
  },
  overrides: [
    {
      files: ['*.ts', '*.d.ts', '*.vue'],
      plugins: ['@typescript-eslint'],
      extends: [
        '@nuxtjs/eslint-config-typescript',
        'plugin:nuxt/recommended',
        'plugin:vue/vue3-recommended',
        'plugin:vue-pug/vue3-recommended',
        'plugin:@typescript-eslint/strict',
      ],
      parser: 'vue-eslint-parser',
      parserOptions: {
        extraFileExtensions: ['.vue'],
        parser: '@typescript-eslint/parser',
        project: './tsconfig.json',
      },
      rules: {
        'vue/multi-word-component-names': 'off',
        'vue/no-multiple-template-root': 'off',
        '@typescript-eslint/consistent-type-definitions': [
          'error',
          'interface',
        ],
        '@typescript-eslint/consistent-type-exports': 'error',
        '@typescript-eslint/consistent-type-imports': 'error',
      },
    },
  ],
}
