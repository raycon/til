# Creact React App

Node.js를  [설치](https://nodejs.org/ko/)한다.

`create-react-app` 명령어로 새로운 프로젝트를 만든다. (시간이 꽤 걸린다.)

    > npx create-react-app my-app

`start` 명령어로 실행할 수 있다. (개발용)

    > npm start

## Structure

    my-app/
    README.md
    node_modules/
    package.json
    public/
        index.html          // 페이지 템플릿
        favicon.ico
    src/
        App.css
        App.js              // 자바스크립트 진입 지점
        App.test.js
        index.css
        index.js
        logo.svg

- `src` 폴더 안에 있는 파일들만 처리된다. js, css 파일은 `src` 폴더에 넣어야 한다.
- `public` 폴더 안에 있는 파일들만 `public/index.html` 에서 접근할 수 있다.
- 다른 폴더를 추가할 수 있지만 운영용 빌드에 포함되지는 않는다.

## Dependencies

- [BABEL](https://babeljs.io/docs/en/) : 자바스크립트 컴파일러, 오래된 브라우저에서 호환 가능하도록 컴파일 한다.
    - JSX 도 변환한다.
- [Webpack](https://webpack.js.org/)
    - Static Module Bundler
    - [Module](https://webpack.js.org/concepts/modules/): 분리된 기능의 덩어리
    - Bundle: 소프트웨어 및 일부 하드웨어와 함께 작동하는 데 필요한 모든 것을 포함하는 Package

## Styles and Assets

### Adding Stylesheets

자바스크립트에서 쓸 CSS 파일을 import 할 수 있다.

`src/Button.css`

```css
.Button {
    padding: 20px;
}
```

`src/Button.js`

```js
import React, { Component } from 'react';
import './Button.css'; // Tell Webpack that Button.js uses these styles

class Button extends Component {
render() {
    // You can use them as regular CSS styles
    return <div className="Button" >Button</div>;
}
}

export default Button;
```

`src/App.js`

```js
import React from 'react';
import './App.css';
import Button from './Button.js';

function App() {
  return <Button/>
}

export default App;
```

### Adding CSS Modules

[CSS Module](https://github.com/css-modules/css-modules)은 클래스 이름의 범위를 지정해줘서, 충돌 걱정 없이 동일한 이름을 여러 파일에서 사용할 수 있도록 한다. 클래스 이름은 `[filename]_[classname]__[hash]` 로 변환된다.

`.module.css` 확장자를 지정해서 css 파일을 생성한다.

`Button.module.css`

```css
.error {
    background-color: red;
}
```

`Button.js`

```js
import React, { Component } from 'react';
import styles from './Button.module.css'; // Import css modules stylesheet as styles

class Button extends Component {
  render() {
    // reference as a js object
    return <button className={styles.error}>Error Button</button>;
  }
}

export default Button;
```

결과

```html
<button class="Button_error__1N7J7">Error Button</button>
```

### CSS Reset

`index.css` 에 다음 라인을 추가한다.

```css
@import-normalize; /* bring in normalize.css styles */

/* rest of app styles */
```

### Images, Fonts, and Files

Webpack을 사용하면 CSS 를 사용하는 것과 비슷한 방식으로 정적 리소스를 사용할 수 있다. 자바스크립트 파일 안에서 `import` 로 파일을 가져올 수 있다. 파일을 import 할 경우 CSS를 import 할 때와는 경로 값을 전달한다.


```js
import logo from './logo.png'; // Tell Webpack this JS file uses this 
function Header() {
  // Import result is the URL of your image
  return <img src={logo} alt="Logo" />;
}
export default Header;
```

CSS 파일에서도 사용할 수 있다. `./`로 시작하는 경로를 처리한다.

```css
.Logo {
  background-image: url(./logo.png);
}
```

SVG 파일을 리액트 컴포넌트로 변환해서 import 할 수 있다.

```js
import { ReactComponent as Logo } from './logo.svg';
const App = () => (
  <div>
    {/* Logo is an actual React component */}
    <Logo />
  </div>
);
```

### Public Folder

`public` 폴더에 저장된 리소스는 Webpack 에 의해 처리되지 않고 `build` 폴더로 복사된다. 이 파일들은 `%PUBLIC_URL%` 변수를 통해 사용할 수 있다.

```html
<link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
```

`public` 폴더에 파일을 저장하는 방식은 `src`에 저장하고 `js` 에서 `import` 하는 방식에 비해 다음과 같은 단점이 있어서 추천하지 않는다.

- `public`폴더에 저장된 파일은 사후처리나 용량 최적화의 대상이 되지 않는다.
- 파일이 존재하지 않을 경우 컴파일 타임에 에러를 발견하지 못하고, 사용자에게 404 에러를 보여준다.
- 파일 이름이 해시값을 갖지 않기 때문에 캐시된 파일을 업데이트 하기 위해 쿼리 변수를 설정하거나 파일 이름을 매번 변경해야 한다.

다음과 같은 경우 `public` 폴더를 사용한다.

- 특정 이름을 갖는 파일이 필요할 때. (`manifest.webmanifest`)
- 이미지가 수천개쯤 되고 동적으로 참조할 경우(?)
- 작은 사이즈의 스크립트를 포함시킬 경우
- Webpack 과 호환되지 않는 라이브러리를 사용할 경우


### Code Splitting

`import()` 함수를 사용하면 `Promise`를 리턴하는데 이를 통해서 코드를 나누고, 사용자의 요청이 있을 때에만 특정 파일을 로드할 수 있다.

[공식문서](https://create-react-app.dev/docs/code-splitting) 참고

## IDE

- `Babel JavaScript` [설치](https://marketplace.visualstudio.com/items?itemName=mgmcdermott.vscode-language-babel)

## 참고자료

- [difference between default and named exports](https://stackoverflow.com/questions/36795819/when-should-i-use-curly-braces-for-es6-import/36796281#36796281)

## Production Deploy

`build` 명령어로 산출물을 작성한다.

    > npm run build
    Creating an optimized production build...
    Compiled successfully.

    File sizes after gzip:

    39.84 KB  build\static\js\2.f7f722d9.chunk.js
    775 B     build\static\js\runtime-main.94075b70.js
    612 B     build\static\js\main.39090ed5.chunk.js
    547 B     build\static\css\main.d1b05096.chunk.css

`serve` 명령어로 정적 서버를 실행할 수 있다.

    npm install -g serve
    serve -s build
