# 윈도우 실행 시 NumLock 켜지는 동작 바꾸기

- `시작 > 실행 > regedit` 입력해서 레지스트리 편집기 실행
- `HKEY_USERS > .Default > Control Panel > Keyboard` 에서 `InitialKeyboardIndicators` 값을 다음과 같이 설정
  - `0` : NumLock OFF
  - `1` : NumLock ON
