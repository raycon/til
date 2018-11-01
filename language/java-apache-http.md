# Apache Http

## Dependency

Gradle:

```gradle
  compile 'org.apache.httpcomponents:httpclient:4.5.6'
  compile 'org.apache.httpcomponents:httpcore:4.4.10'
```

## Proxy

```java
HttpClient httpclient = new HttpClient();
httpclient.getHostConfiguration().setProxy("Host", "Port");
httpclient.getState().setProxyCredentials(
    new AuthScope("Host", "Port"),
    new UsernamePasswordCredentials("ID", "Password")
);
```

## 문제 해결

`Illegal character in query at index` 오류를 방지하기 위해서 주소를 인코딩 해야 한다.

```java
try {
    String simpleUrl = "http://www.abc.com/?email=abc&pass=efg";
    String encodedurl = URLEncoder.encode(url,"UTF-8");
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}
```




