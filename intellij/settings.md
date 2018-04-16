# IntelliJ Settings

## Gradle Wrapper 인증서 오류 해결

IntelliJ는 자체 jre를 사용한다. 다음 파일에 `인증서.crt`를 추가한다.

    C:\Program Files\JetBrains\IntelliJ IDEA 2018.1.1\jre64\lib\security\cacerts

인증서 관리 프로그램은 [KeyStore Explorer](http://keystore-explorer.org/)를 사용하면 편리하다.