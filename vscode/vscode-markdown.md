# VSCode Markdown

> 참고 : [Build an Amazing Markdown Editor Using Visual Studio Code and Pandoc](http://thisdavej.com/build-an-amazing-markdown-editor-using-visual-studio-code-and-pandoc/)

## 미리보기

VSCode 에서는 Markdown 문서를 작성하고 `미리보기(Ctrl+Shift+V)` 버튼을 누르면 미리보기가 열린다. `Ctrl+K V` 를 누르면 Markdown 문서의 오른쪽에 미리보기 화면이 열린다. Markdown 문서를 수정하면 미리보기도 실시간으로 갱신된다.

## 문법 검사

[markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) 를 설치하면 에러가 있는 문구에 표시가 된다. 에러의 자세한 사항은 [Rules.md](https://github.com/DavidAnson/markdownlint/blob/v0.3.1/doc/Rules.md) 파일에서 확인할 수 있다.

## HTML로 변환

[Pandoc](http://pandoc.org) 과 [vscode-pandoc](https://github.com/dfinke/vscode-pandoc) 확장을 설치하고 `Settings.json` 을 아래와 같이 수정한다 :

    "pandoc.htmlOptString": "-s -f markdown_github -t html5 -H [PATH]/markdown-github-pandoc.html",

각각의 옵션은 아래 의미를 갖는다 :

* `-s` : 하나의 파일로 변환
* `-f markdown_github` : 깃헙 마크다운 문법 사용
* `-t` : 타입을 지정
* `-H` : 변환된 파일의 헤더에 들어갈 내용을 지정한다. (내용이 복사되서 들어감)
* `-c` : css 지정 (css 파일이 링크로 들어감)

> [markdown-github-pandoc.html](https://github.com/raycon/vscode-markdown-css/blob/master/markdown-github-pandoc.html)은 마크다운 스타일시트를 적용하는 파일이다.

`F1` > `Pandoc Render` > `html` 을 선택하면 변환 작업이 수행된다.