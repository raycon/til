# VSCode Markdown

> 참고 : [Build an Amazing Markdown Editor Using Visual Studio Code and Pandoc](http://thisdavej.com/build-an-amazing-markdown-editor-using-visual-studio-code-and-pandoc/)

## 마크다운 소개

[Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## VSCode 설치

[VSCode](https://code.visualstudio.com)

## 미리보기

VSCode 에서는 Markdown 문서를 작성하고 `미리보기(Ctrl+Shift+V)` 버튼을 누르면 미리보기가 열린다. `Ctrl+K V` 를 누르면 Markdown 문서의 오른쪽에 미리보기 화면이 열린다. Markdown 문서를 수정하면 미리보기도 실시간으로 갱신된다.

## 자동완성

`Ctrl+Space` 를 누르면 자동완성 기능을 사용할 수 있다. 예를 들어 `Ctrl+Space` > `link` 를 입력 하고 vscode-markdown 항목을 선택하면 링크 Snippet이 입력된다.

## 문법 검사

[markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) 를 설치하면 에러가 있는 문구에 표시가 된다. 에러의 자세한 사항은 [Rules](https://github.com/DavidAnson/markdownlint#rules--aliases) 에서 확인할 수 있다.

## HTML 변환

[Pandoc](http://pandoc.org) 과 [vscode-pandoc](https://github.com/dfinke/vscode-pandoc) 확장을 설치하고 `Settings.json` 을 아래와 같이 수정한다 :

    "pandoc.htmlOptString": "-s -f markdown_github -t html5",

각각의 옵션은 아래 의미를 갖는다 :

- `-s` : 하나의 파일로 변환
- `-f markdown_github` : 깃헙 마크다운 문법 사용
- `-t` : 타입을 지정
- `-c` : css 지정 (css 파일이 링크로 들어감)

`F1` > `Pandoc Render` > `html` 을 선택하면 변환 작업이 수행된다.

## VSCode Settings

`F1 > Configure language specific settings > Markdown` 선택해서 다음 내용 입력:

    "[markdown]": {
        // Note: The following settings are not currently supported
        //  but will be in the next release.
        // Please refer to #19511 for more information.
        // editor.tabSize
        // editor.insertSpaces
        // editor.detectIndentation
        // editor.trimAutoWhitespace

        //저장할 때 마크다운 포매터를 적용한다.
        "editor.formatOnSave": true,
        // 공백 문자를 표시할지 여부를 설정한다.
        "editor.renderWhitespace": "boundary",
        // 'Tab' 키 외에도 'Enter' 키를 사용한 제안도 허용할지 제어한다.
        // 마크다운 편집시에는 false로 설정하는 것이 편하다.
        "editor.acceptSuggestionOnEnter": false,
        // 긴 문장을 wrapping 해서 보여주도록 설정
        "editor.wrappingColumn": 0
    }

## Lint Settings

불필요한 Warning 을 없애기 위해서 프로젝트 루트에 `.markdownlint.json` 파일을 만들고 아래 내용을 입력한다 :

    {
        "default": true,
        "MD007": { "indent": 4 },
        "MD013": false
    }

각각의 옵션은 아래 의미를 갖는다 :

- `default` : 기본 정의 사용
- `MD007` : 리스트 indent 사이즈 정의
- `MD013` : 라인 길이 경고 무시

## 스타일 변경

[vscode-markdown-css](https://github.com/raycon/vscode-markdown-css)를 다운로드 한다.

### Preview 스타일 변경

`Settings.json` 을 아래와 같이 수정한다 :

    "markdown.styles": [
        "[PATH]/markdown-light.css",
        "[PATH]/markdown-dark-material.css"
    ],

### Pandoc HTML 스타일 변경

`Settings.json` 을 아래와 같이 수정한다 :

    "pandoc.htmlOptString": "-s -f markdown_github -t html5 -H [PATH]/markdown-github-pandoc.html",

- `-H` : 변환된 파일의 헤더에 들어갈 내용을 지정한다. (내용이 복사되서 들어감)