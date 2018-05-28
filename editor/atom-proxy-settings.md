# ATOM proxy

> ATOM에 패키지를 설치하려는데 네트워크 커넥션 에러가 발생해서 프록시를 설정했다.

`C:\Users\[사용자]\.atom\.apm\.atomrc` 파일을 `C:\Users\[사용자]\.atom\.atomrc` 로 복사하고 아래 내용을 추가한다.

    proxy=http://[IP]:[PORT]
    https-proxy=http://[IP]:[PORT]
    strict-ssl=false
