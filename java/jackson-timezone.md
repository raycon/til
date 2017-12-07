# Jackson timezone

Jackson 은 Date, Timestamp 값을 변환할 때 타임존을 지정하지 않으면 `UTC+0`을 기준으로 변환한다. KST인 UTC+9로 변환하려면 두가지 방법이 있다.

필드에 선언, 모든 필드에 선언해야 한다 :

```java
@JsonFormat(pattern = "yyyy-MM-dd HH:mm", timezone = "Asia/Seoul")
private Timestamp date;
```

`ObjectMapper`에 선언, 모든 필드에 일괄 적용된다 :

```java
ObjectMapper mapper = new ObjectMapper();
mapper.setTimeZone(TimeZone.getTimeZone("Asia/Seoul"));
Content content = mapper.readValue(json, Content.class);
```