# VSCode for JavaScript

Plugin

- ESLint
- Prettier

`package.json`

```json
  "eslintConfig": {
    "extends": [
      "airbnb",
      "prettier",
      "prettier/react"
    ],
    "settings": {
      "import/resolver": {
        "node": {
          "paths": [
            "node_modules",
            "./src"
          ]
        }
      }
    },
    "rules": {
      "react/prefer-stateless-function": 0,
      "react/jsx-filename-extension": 0,
      "react/jsx-one-expression-per-line": 0,
      "react/prop-types": 0,
      "no-console": 0,
      "import/prefer-default-export": 0
    },
    "env": {
      "browser": true
    }
  }
```