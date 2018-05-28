# Auto Hot Key

> 여러 기능을 단축키, 축약어로 지정해서 사용하기 편리하게 해주는 프로그램

## 설치

[AutoHotKey](https://autohotkey.com/download) 홈페이지에서 최신 버전을 받아서 설치한다. 프로그램을 실행하면 AutoHotkey Help 화면이 뜨는데 이를 참고해서 스크립트 파일을 작성한다.

## 스크립트 작성

`example.ahk` 파일을 만들어서 아래 내용을 입력한다 :

```ahk
; 첫번째 스크립트
; Ctrl + J 를 입력하면 My First Script 가 입력된다.
^j::
   Send, My First Script
Return

; ftw 를 입력하고 Space를 누르면 Free the wales로 변환된다.
::ftw::Free the whales

```

[Hotkeys](https://autohotkey.com/docs/Hotkeys.htm) 에서 매핑에 사용되는 키를 확인할 수 있다.

    ^ : Ctrl
    ! : Alt
    # : Windows

## 스크립트 실행

`.ahk` 파일을 더블클릭 하거나, 마우스 오른쪽 버튼으로 클릭하고 `Run Script`를 선택한다. 스크립트가 실행되면서 트레이에 `H` 모양 아이콘이 표시된다. 종료시에는 트레이 아이콘을 오른쪽 버튼으로 클릭하고 `Exit`을 선택한다.

## 실행 파일 만들기

ahk 스크립트 파일을 exe로 변환해서 배포할 수 있다. `.ahk` 파일을 마우스 오른쪽 버튼으로 클릭하고 `Compile Script`를 선택하면 동일한 파일명으로 `.exe` 파일이 생성된다.

### 아이콘 변경하기

임의의 아이콘을 지정해서 `.exe`파일을 생성할 수 있다. `C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe` 프로그램을 실행한다. `Source`, `Destination`을 설정하고 `Custom Icon`에서 사용할 `ico`파일을 지정한뒤 `Convert` 버튼을 누르면 된다.

> 아이콘은 [iconfinder](https://www.iconfinder.com) 사이트에서 찾을 수 있다.

## 유용한 스크립트

```ahk
; 볼륨 조절
^!PgUp::   Send {Volume_Up 2}
^!PgDn::   Send {Volume_Down 3}
^!Pause::  Send {Volume_Mute}

; 창 항상 위에 표시
^!SPACE::  Winset, Alwaysontop, , A
```