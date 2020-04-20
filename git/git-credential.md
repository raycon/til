# Git Credential 사용

> 윈도우에서는 아래 내용 대신 [Git Credential Manager for Windows](https://github.com/Microsoft/Git-Credential-Manager-for-Windows) 를 사용하면 편하다.

SSH를 사용하지 않을 경우에 인증정보(Credential) 저장하는 방법

`credential.helper`를 지정해서 인증정보 저장소를 선택할 수 있다.

- 기본 : 저장하지 않는다.
- `cache` : 메모리에 저장하고 15분간 유지한다.
- `store` : 디스크의 파일에 저장한다.
- `osxkeychain` : 맥에서 제공하는 암호화된 저장소를 사용한다.
- `wincred` : 윈도우에서 제공하는 암호화된 저장소를 사용한다.

다음 명령어로 지정한다.

    git config --global credential.helper store
    protocol=https
    host=mygithost
    username=bob
    password=s3cre7
