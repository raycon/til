# IntelliJ Settings

## Gradle Wrapper 인증서 오류 해결

IntelliJ는 자체 jre를 사용한다. 다음 파일에 `인증서.crt`를 추가한다.

    C:\Program Files\JetBrains\IntelliJ IDEA 2018.1.1\jre64\lib\security\cacerts

인증서 관리 프로그램은 [KeyStore Explorer](http://keystore-explorer.org/)를 사용하면 편리하다.

## Proxy

- `Settings > Appearance & Behavior > System Settings > HTTP Proxy` 에서 프록시를 설정한다.

## Plugins

- `.ignore`: ignore 파일 문법 강조. 트리에서 색 지정
- `Lombok Plugin`: Lombok을 사용하려면 필요하다.
- `CodeGlance`: 미니맵 스타일의 스크롤바를 사용할 수 있다.

## Settings

- `Settings > Build, Execution, Deployment > Compiler`에서 `Build project automatically`를 체크한다.
- `Settings > Inspections`에서 `Spelling`을 체크 해제한다.
- `Settings > Editor > General > Editor Tabs`에서
    - `Tab Appearance > Placement`를 `Never`로 설정
    - `Tab Closing Policy > Tab limit`을 `2`로 설정
- `Settings > Editor > General > Breadcrumbs` 에서 `Show breadcrumbs` 해체
- `View > Toolbar` 체크 설정
- `View > Navigation Bar` 체크 해제

## Keymap

`Settings > Keymap`

- Split Vertically : `Alt + \`
- Goto Next Splitter : `Alt + →`
- Goto Previous Splitter : `Alt + ←`
- Fully Expand Tree Node: `Ctrl+Wheel down`
- Collapse Tree Node: `Ctrl+Wheel up`

## Code Style

`Settings > Code Style > Java`

- Chained method calls : Chop down if long
- Blank Lines > Keep Maximum Blank Lines : 모두 1로 설정

## Color Scheme

- [Oblivion](https://github.com/raycon/oblivion) 적용

## Encoding

`Settings > Editor > File Encodings` 에서 다음과 같이 설정

- Global Encoding : `UTF-8`
- Project Encoding : `UTF-8`
- Default encoding for properties files: `UTF-8`
- Transparent native-to-ascii conversion 체크

## 유용한 단축키

- `F2` : 다음 에러로 점프