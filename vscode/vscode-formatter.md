# VSCode Formatter

> VSCode는 내부적으로 js-beautify를 사용한다. 

## 단축키

기본 단축키는 아래와 같다.

`파일 > 기본 설정 > 바로 가기 키` 에서 `keybindings.json` 파일을 열고 이 항목을 변경할 수 있다. 

```json
[
    { "key": "ctrl+b", "command": "editor.action.format" }
]
```

`Ctrl+b` 는 사이드바를 토글하는 단축키인데 잘 사용하지 않으므로 포매팅 하는 단축키로 설정했다.

## 파일 저장할 때 포매터 적용

`파일 > 기본 설정 > 사용자 설정` 에서 `settings.json` 파일을 열고 아래 내용을 입력한다.

```json
"editor.formatOnSave":true,
```

## [Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify)

> 포매터 옵션을 설정할 수 있는 확장

`beautify`는 `프로젝트 루트`나 `사용자 홈디렉토리`에 있는 `.jsbeautifyrc` 파일을 통해 포매터 옵션을 설정할 수 있다.