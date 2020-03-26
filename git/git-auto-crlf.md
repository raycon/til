# AutoCRLF

    warning: LF will be replaced by CRLF

git 에서 변경사항을 추가할 때 CRLF -> LF, LF -> CRLF 변환이 일어날 수 있다. `core.autocrlf` 옵션이 `true`로 설정되어 있기 때문인데 이 메시지를 보지 않으려면 다음과 같이 설정한다.

    git config --global core.autocrlf input

`core-autocrlf`는 값에 따라 다음과 같이 동작한다.

- `true`: Checkout Windows-style, commit Unix-style
- `input`: Checkout as-is, commit Unix-style
- `false`: Checkout as-is, commit as-is

요즘 IDE나 에디터들은 CRLF, LF 가리지 않고 모두 지원하므로 다른 사람들과 협력하려면 LF만 사용하는게 편리하다.

이미 clone 한 저장소의 설정을 변경하려면 다음 명령어로 캐시를 지운다.

    git rm -rf --cached .
    git reset --hard HEAD

## 참고

- <https://git-scm.com/book/ko/v1/Git%EB%A7%9E%EC%B6%A4-Git-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0>
- <https://stackoverflow.com/questions/2517190/how-do-i-force-git-to-use-lf-instead-of-crlf-under-windows>
