# Read Consistency

`DyanmoDB`는 여러 `AWS region`에서 사용이 가능하다. 각각의 `AWS region`은 여러 독립된 장소에 존재하는 `Availability Zone`으로 구성되어 있다. `Availibility Zone`들은 데이터의 복사본을 저장한다. `DynamoDB`에 데이터를 입력하고 HTTP 200 응답을 받은 경우 데이터는 `결과적으로` 1초 이내에 모든 저장소 위치에 저장된다. 이러한 특성으로 인해 `DynamoDB`는 두가지 타입의 읽기 방식을 지원한다.

Eventually Consistent Reads:

데이터를 읽을 때 가장 최근 수행된 입력 오퍼레이션의 결과를 반영하지 않는다.

Strongly Consistent Reads:

데이터를 읽을 때 가장 최근 수행된 입력 오퍼레이션의 결과를 반영한다.

`DynamoDB`는 `Eventurally Consistent Reads`를 기본으로 사용하고, 읽기 오퍼레이션을 수행할 때 `ConsistentRead` 파라미터를 `true`로 설정 할 경우 `Strongly Consistent Reads`를 사용한다.

## 참고

- <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html>