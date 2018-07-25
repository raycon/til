# IntelliJ Settings

## Gradle Wrapper 인증서 오류 해결

IntelliJ는 자체 jre를 사용한다. 다음 파일에 `인증서.crt`를 추가한다.

    C:\Program Files\JetBrains\IntelliJ IDEA 2018.1.1\jre64\lib\security\cacerts

인증서 관리 프로그램은 [KeyStore Explorer](http://keystore-explorer.org/)를 사용하면 편리하다.

## Plugins

- `Markdown Navigator` : 마크다운 프리뷰, PDF 출력

## Settings

- `Settings > Build, Execution, Deployment > Compiler`에서 `Build project automatically`를 체크한다.
- `Settings > Inspections`에서 `Spelling`을 체크 해제한다.
- `Settings > Code Style > Alignment and Braces`에서 `Simple methods in one line`을 체크 해제한다.
- `Settings > Editor > General > Editor Tabs`에서
    - `Tab Appearance > Placement`를 `Never`로 설정
    - `Tab Closing Policy > Tab limit`을 `2`로 설정
- `Settings > Editor > General > Breadcrumbs` 에서 `Show breadcrumbs` 해체

## Keymap

`Settings > Keymap`

- Split Vertically : `Alt + \`
- Goto Next Splitter : `Alt + →`
- Goto Previous Splitter : `Alt + ←`

## Code Style

`Settings > Code Style > Java`

- Chained method calls : Chop down if long
- Blank Lines > Keep Maximum Blank Lines : 모두 1로 설정

## Color Scheme

- [Oblivion](http://color-themes.com/?view=theme&id=563a1a6180b4acf11273ae3c) 다운로드
- General > Code > Line number : Foreground `#606366`
- General > Editor > Gutter background : Background `#313335`
- General > Editor > Tear line : Foreground `#555555`
- General > Editor > Tear line selection : Foreground `#787878`
- General > Text > Default text : Background `#2B2B2B`
- General > Editor > Selection background : Background `#214283`
- General > Editor > Selection Foreground : 모두 체크 해제
- General > Editor > Guides > Indent guide : Background `#373737`

## 유용한 단축키

- `F2` : 다음 에러로 점프