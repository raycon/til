# DAO, DTO, VO

## DAO

- `Data Access Object`의 약자.
- Database에 접근하는 로직과 비지니스 로직을 분리하는데 사용

## DTO

> <https://martinfowler.com/eaaCatalog/dataTransferObject.html>

- `Data Transfer Object`의 약자.
- 프로세스 간 통신이 일반적으로 원격 인터페이스(예: 웹 서비스)를 통해 이루어진다.
- 각각의 요청을 하나씩 보내는 것은 비효율적이다.
- `DTO`를 사용해서 여러 호출에 의해 전달되던 데이터를 한번에 전송할 수 있다.
- `DTO`는 비지니스 로직을 포함하지 않는 단순한 객체이다.
- 데이터를 전달하는 객체

### 장점

> <https://stackoverflow.com/questions/36174516/rest-api-dtos-or-not> 참고

- 데이터베이스에 저장된 값을 원하는 목적에 맞도록 가공할 수 있다.
- Entity에 영속성과 관련이 없는 어노테이션이 함께 쓰이는 것을 방지할 수 있다.
- Entity와 연관이 없으므로 리소스를 생성하거나 삭제할 때 전달받는 값을 원하는대로 다룰 수 있다.
- `Swagger`를 사용할 경우 `@ApiModel`이나 `@ApiModelProperty`와 같은 문서화를 위한 어노테이션을 사용해도 Entity에는 영향이 없다.
- 여러 버전의 API에 다른 DTO를 사용할 수 있다.
- 릴레이션을 만드는데 있어서 자유롭다.
- 여러 MediaType에 대해 그에 대응하는 DTO를 가질 수 있다.
- DTO는 `HATEOAS`를 위한 링크를 가질 수 있다. 이 링크는 Entity에 추가될 수 없다.

### 변환

ORM 사용시 서비스 레이어와 퍼시스턴트 레이어 사이에서 변환된다. (다양한 의견이 있음)

    클라이언트 ← DTO → 컨트롤러 ← DTO → 서비스 ← Domain Model → 퍼시스턴트 ←→ 데이터베이스
    클라이언트 ← DTO → 컨트롤러 ← Domain Model → 서비스 ← Domain Model → 퍼시스턴트 ←→ 데이터베이스


DTO를 Domain Model 로 변환하는 과정을 도와주는 툴을 사용할 수 있다.

> <https://stackoverflow.com/questions/1432764/any-tool-for-java-object-to-object-mapping/1432956#1432956>  
> <https://www.baeldung.com/java-performance-mapping-frameworks>

## VO

- 상태가 있는 것이 아닌 값으로 취급하는 객체
- 값을 표현하는 객체
- 불변(immutable) 객체
- 가격, String 등
