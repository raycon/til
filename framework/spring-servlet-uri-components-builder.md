# ServletUriComponentsBuilder

> org.springframework.web.servlet.support.ServletUriComponentsBuilder

``` java
// scheme, host, port, path, query string
// http://localhost:8080/car/123?query=123
ServletUriComponentsBuilder.fromCurrentRequest();

// host, port, scheme, context path
// http://localhost:8080
ServletUriComponentsBuilder.fromCurrentContextPath();

// host, port, scheme, path
// http://localhost:8080/car/123
ServletUriComponentsBuilder.fromCurrentRequestUri();

// host, port, scheme, context path, servlet mapping
// http://localhost:8080
ServletUriComponentsBuilder.fromCurrentServletMapping();
```