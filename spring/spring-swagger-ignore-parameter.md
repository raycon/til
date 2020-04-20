# Swagger 문서에서 특정 파라미터 제외하기

`io.swagger.annotations.ApiParam` 사용:

```
public String someMethod(@ApiParam(hidden = true) String parameter) {
    ...
}
```

`springfox.documentation.annotations.ApiIgnore` 사용:

```
public String someMethod(@ApiIgnore String parameter) {
    ...
}
```
