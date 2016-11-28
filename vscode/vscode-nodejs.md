# VSCode 에서 node.js 개발환경 설정하기

> 원문 : <https://code.visualstudio.com/Docs/runtimes/nodejs>

## node.js 설치

`https://nodejs.org/en/download/`

운영체제에 맞는 Node.js를 설치하고, 환경변수를 설정한다.

## Extensions

`Ctrl+Shift+X` 로 확장 패널을 열어서 설치한다.

- ESLint : 자바스크립트 문법 검사
- npm (by egamma) : package.json 검사 및 스크립트 실행

## process.env

`.vscode/launch.json` 파일에서 `process.env.KEY` 값으로 전달되는 값을 설정할 수 있다.

```json
    "configurations": [
        {
            "env": {
                "NODE_ENV": "development",
            }
        }
    ]
```

## Debugging

VSCode 는 노드 디버거를 기본으로 제공한다. `Ctrl+Shift+Z` 키로 디버거를 실행한다. 톱니바퀴 아이콘을 눌러서 실행 환경(`.vscode/launch.json`)을 설정한다. 이 파일에서 실행할 코드를 지정해준다.

```json
    "configurations": [
        {
            "program": "${workspaceRoot}\\bin\\www",
        }
    ]
```

초록색 화살표 혹은 `F5` 키를 눌러서 디버깅을 시작한다. 브레이크 포인트는 `F9`로 설정한다.

### Breakpoint Validation

성능을 위해서 Node.js는 함수에 접근할 때 그 함수를 로드한다. 디버거에서 설정한 BreakPoint는 Node.js가 해당 소스를 파싱하기 전에는 작동하지 않는다. 이를 막기 위해서 VSCode 는 `--nolazy` 옵션을 추가해서 Node.js를 실행한다.

`--nolazy` 옵션은 최초 실행 시간을 증가시킬 수 있는데, 이 옵션은 `launch.json` 파일의 `runtimeArgs` 속성에 `--lazy` 값을 전달함으로써 끌 수 있다.

```json
    "configurations": [
        {
            "runtimeArgs": [
                "--lazy"
            ]
        }
    ]
```

`--lazy` 값을 주고 Breakpoint 를 설정 하면 요청한 라인에 설정되지 않고 수행 중단이 가능한 이미 파싱된 코드로 Breakpoint가 `점프`한다. 이 항목은 `file.js 6->10` 과 같이 표시가 된다.

Node.js 가 모든 코드를 파싱하고 난 다음에 Breakpoints 섹션 헤더에 있는 `Reapply` 버튼을 누르면 요청했던 라인으로 Breakpoint가 돌아온다.

### Attaching VS Code to Node.js

> 디버그 모드로 실행되고 있는 Node.js 프로세스에 VS Code 디버거를 붙일 수 있다.

커맨드 라인에서 아래 명령어로 노드를 실행한다.

```cmd
node --debug program.js
or
node --debug-brk program.js // 첫번째 라인에서 멈춤
```

VS Code 의 디버그 화면에서 초록색 화살표 옆의 콤보박스를 누르면 `연결(Attach to Node)` 옵션이 있다. 이 항목을 선택하고 디버거를 실행하면 현재 실행되어 있는 프로세스에 디버거가 연결된다. 이 항목과 관련된 실행 환경 설정은 다음과 같다.

```json
    "configurations": [
        {
            "name": "Attach to Node",
            "type": "node",
            "request": "attach",
            "port": 5858,
            "restart": true,
            "timeout": 10000
        }
    ]
```

`Attach to Node` 기능은 [nodemon](http://nodemon.io/) 을 사용할 때 유용하다. nodemon은 실행 도중 파일이 수정되면 Node.js 를 다시 실행한다. VS Code의 디버그 실행 환경에서 `restart` 속성을 `true`로 설정하면 VS Code 디버거는 새로 실행된 Node.js의 디버거에 자동으로 연결된다.

### nodemon

`` Ctrl+` `` 를 눌러서 터미널을 실행하고 아래 명령어로 nodemon을 설치한다.

> VSCode 는 터미널을 내장하고 있다. `` Ctrl+` `` 키로 실행한다. `` Ctrl+Shift+` ``키를 눌러서 창을 추가할 수 있다.

```cmd
npm install -g nodemon
```

nodemon 을 디버그 모드로 실행한다.

```cmd
nodemon --debug server.js
```

npm 확장을 설치한 경우 `package.json` 에 아래 내용을 추가하면, `Ctrl+R, Shift+R` 버튼으로 스크립트를 실행할 수 있다.

```json
"scripts": {
    "start": "node app.js",
    "nodemon": "nodemon --debug app.js"
}
```

디버그 화면에서 Attach To Node 를 실행한다.

> `Stop` 버튼은 디버그 세션만 종료하고 `nodemon` 은 종료하지 않는다.

> 문법 오류가 있는 경우 `nodemon`은 Node.js를 재시작 할 수 없다. VS Code는 10초 안에 `Attach to Node`가 실패할 경우 연결을 포기한다. 이를 막기 위해서 `timeout` 값(ms)을 더 큰 값으로 변경설정해주면 된다.