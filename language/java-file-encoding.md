# Java File Encoding

> jar 실행시 한글 깨짐 현상 해결

jar파일을 생성할때 소스 인코딩을 UTF-8로 지정하면 jar 파일을 실행할때도 UTF-8로 실행해야한다.
소스 파일이 UTF-8 이면 실행도 UTF-8 로, euc_kr 이면 euc_kr 로 지정해야 한다.

jar 파일을 실행할 때 `-Dfile.encoding` 옵션으로 인코딩을 지정한다.

    java -jar -Dfile.encoding=UTF-8 application.jar
