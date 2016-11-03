# VSCode 에서 node.js 개발환경 설정하기

> 원문 : https://code.visualstudio.com/Docs/runtimes/nodejs

## 설치

`https://nodejs.org/en/download/`

운영체제에 맞는 Node.js를 설치하고, 환경변수를 설정한다.

## 터미널

VSCode 는 터미널을 내장하고 있다. `` Ctrl+` `` 키로 실행한다. `` Ctrl+Shift+` ``키를 눌러서 창을 추가할 수 있다.

## 디버깅

VSCode 는 노드 디버거를 기본으로 제공한다. `Ctrl+Shift+Z` 키로 디버거를 실행한다. 톱니바퀴 아이콘을 눌러서 실행 환경(`.vscode/launch.json`)을 설정한다. 이 파일에서 실행할 코드를 지정해준다.

```json
    "program": "${workspaceRoot}\\bin\\www",
```

초록색 화살표 혹은 `F5` 키를 눌러서 디버깅을 시작한다. 브레이크 포인트는 `F9`로 설정한다.

## jsconfig.json

자바스크립트를 편집할 때 VS Code는 `jsconfig.js` 파일을 찾는다. 이 파일이 없으면 Status Bar 오른쪽에 초록 아이콘이 표시되는데, 이를 누르면 `jsconfig.js` 파일을 생성할 수 있다.

이 파일이 존재하면 VS Code 는 현재 폴더에 포함된 모든 파일이 동일한 프로젝트의 파일이라고 인식하게 된다.

## Typings

IntelliSense 에 사용되는 모듈. 아래 명령어로 설치한다.

```bash
    npm install -g Typings
```

### Typings Proxy Settings

`~/.typingsrc` 파일을 만들고 아래 내용을 추가한다.

```rc
    proxy="http://xxx.xxx.xxx.xxx:80"
    rejectUnauthorized=false
```

### Node, Express, AWS 타입 정의 설치

**프로젝트 루트**에서 아래 명령어를 실행한다.

```bash
    typings install dt~node --global --save
    typings install dt~express dt~serve-static dt~express-serve-static-core --global --save
    typings install dt~aws-sdk --global --save
```

프로젝트 루트에 `typings.json`파일과 `typings`폴더가 생성된다.
VS Code 를 종료하고 다시 시작하면 js 파일에서 node와 express관련 IntelliSense를 사용할 수 있다.

## ESLint

JavaScript 문법을 검사하는 확장

## process.env

`launch.json` 파일에서 `process.env.KEY` 값으로 전달되는 값을 설정할 수 있다.

```json
"env": {
    "NODE_ENV": "development",
}
```