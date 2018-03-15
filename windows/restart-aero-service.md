# Restart aero service

윈도우 시작시 창 불투명 효과가 적용되지 않을 경우 아래 내용을 `aero.bat`으로 저장해서 실행한다.

  @echo off
  :main
  cls
  echo.Stopping Windows UX Manager...
  net stop uxsms
  echo.Restarting Windows UX Manager...
  net start uxsms