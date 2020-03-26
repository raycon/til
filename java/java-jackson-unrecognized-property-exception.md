# Jackson UnrecognizedPropertyException

Jackson을 사용해서 JSON 을 객체로 변환 할 때, JSON에 있는 키값이 객체의 프로퍼티에 존재하지 않을 경우 `UnrecognizedPropertyException`이 발생한다. 두가지 방법으로 해결할 수 있다.

`ObjectMapper` 설정 값 지정 :

    mapper.configure(DeserializationConfig.Feature.FAIL_ON_UNKNOWN_PROPERTIES, false);

클래스에 어노테이션 추가 :

    @JsonIgnoreProperties(ignoreUnknown = true)