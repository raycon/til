# JSON 출력하기

기본 :

```java
ObjectMapper mapper = new ObjectMapper();
System.out.println(mapper.writeValueAsString(object));
```

Pretty print 적용 :

```java
ObjectMapper mapper = new ObjectMapper();
System.out.println(mapper.writerWithDefaultPrettyPrinter().writeValueAsString(object));
```

Array 요소를 줄마다 표시 :

```java
DefaultPrettyPrinter pp = new DefaultPrettyPrinter();
pp.indentArraysWith(DefaultIndenter.SYSTEM_LINEFEED_INSTANCE);
System.out.println(mapper.writer(pp).writeValueAsString(object));
```

toString 적용 :

```java
@Override
public String toString() {
    ObjectMapper mapper = new ObjectMapper();
    try {
        return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(this);
    } catch (JsonProcessingException e) {
        return e.getMessage();
    }
}
```

