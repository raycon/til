# Spring 에서 Rest 요청 보내기

<http://stackoverflow.com/questions/4075991/post-request-via-resttemplate-in-json>

```java
// create request body
JSONObject request = new JSONObject();
request.put("username", name);
request.put("password", password);

// set headers
HttpHeaders headers = new HttpHeaders();
headers.setContentType(MediaType.APPLICATION_JSON);
HttpEntity<String> entity = new HttpEntity<String>(request.toString(), headers);

// send request and parse result
ResponseEntity<String> loginResponse = restTemplate
  .exchange(urlString, HttpMethod.POST, entity, String.class);
if (loginResponse.getStatusCode() == HttpStatus.OK) {
  JSONObject userJson = new JSONObject(loginResponse.getBody());
} else if (loginResponse.getStatusCode() == HttpStatus.UNAUTHORIZED) {
  // nono... bad credentials
}
```

Proxy 설정 : <http://stackoverflow.com/questions/3687670/using-resttemplate-how-to-send-the-request-to-a-proxy-first-so-i-can-use-my-jun>

```java
@Bean
public RestTemplate restTemplate() {
    SimpleClientHttpRequestFactory requestFactory = new SimpleClientHttpRequestFactory();

    Proxy proxy= new Proxy(Type.HTTP, new InetSocketAddress("my.host.com", 8080));
    requestFactory.setProxy(proxy);

    return new RestTemplate(requestFactory);
}
```