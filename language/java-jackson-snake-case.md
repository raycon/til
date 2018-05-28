# Jackson Snake Case

`ObjectMapper`를 사용할 때 필드 이름을 `camelCase`에서 언더스코어(`_`)로 연결한 이름으로 변경해야하는 경우

    camelCaseFieldName -> camel_case_field_name

## @JsonProperty

`@JsonProperty`를 사용해서 각 필드별로 매핑되는 이름을 지정할 수 있다.

```java
class User {
    @JsonProperty("camel_case_field_name")
    protected String camelCaseFieldName;
}
```

모든 필드에 대해 지정해주기 번거롭다.

## PropertyNamingStrategy

`PropertyNamingStrategy` 를 사용하면 모든 필드에 대해서 적용된다.

```java
objectMapper.setPropertyNamingStrategy(PropertyNamingStrategy.SNAKE_CASE);
```

도메인에 정의할 수도 있다.

```java
@JsonNaming(PropertyNamingStrategy.SnakeCaseStrategy.class)
class User {
    protected String camelCaseFieldName;
}
```

