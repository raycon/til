# Tomcat 포트 변경

Apache Tomcat 9 버전:

- `C:\Program Files\Apache Software Foundation\Tomcat 9.0\conf\server.xml`

```xml
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
```

위 내용을 찾아서 `8080`을 원하는 포트로 변경한다.