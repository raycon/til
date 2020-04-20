# HttpServletRequest 에서 IP 조회

```java
HttpServletRequest request = (HttpServletRequest) nativeWebRequest.getNativeRequest();

String clientIp = request.getHeader("X-Forwarded-For");
if (StringUtils.isEmpty(clientIp)|| "unknown".equalsIgnoreCase(clientIp)) {
    clientIp = request.getHeader("Proxy-Client-IP");
}
if (StringUtils.isEmpty(clientIp) || "unknown".equalsIgnoreCase(clientIp)) {
    clientIp = request.getHeader("WL-Proxy-Client-IP");
}
if (StringUtils.isEmpty(clientIp) || "unknown".equalsIgnoreCase(clientIp)) {
    clientIp = request.getHeader("HTTP_CLIENT_IP");
}
if (StringUtils.isEmpty(clientIp) || "unknown".equalsIgnoreCase(clientIp)) {
    clientIp = request.getHeader("HTTP_X_FORWARDED_FOR");
}
if (StringUtils.isEmpty(clientIp) || "unknown".equalsIgnoreCase(clientIp)) {
    clientIp = request.getRemoteAddr();
}

return clientIp;
```

출처: <https://jaehun2841.github.io/2018/08/10/2018-08-10-spring-argument-resolver>
