# Create entity class from database

> <https://stackoverflow.com/questions/46892039/intellij-idea-persistence-support-for-spring-boot-project?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa>

JPA Framework 추가

- File > Project Structure > Modules에서 모듈을 선택하고 `+` 버튼을 눌러서 JPA를 추가한다.
- Default JPA Provider를 Hibernate로 지정한다.
- Persistence 패널에서 Entity를 확인할 수 있다.

Database 추가

- Database 패널에서 `+` > Datasource > MySQL을 선택한다.
- 아이디와 암호를 넣고 `Test Connection` 버튼을 눌러서 접속을 확인한다.
- `Schemas`에서 사용할 데이터베이스를 선택한다.

Entity 생성

- Persistence 패널에서 모듈명을 선택한다.
- 마우스 우클릭으로 `Generate Persistence Mapping > By Database Schema`를 선택한다.
  - Choose Data Source: `@localhost`를 선택한다.
  - Package: Entity가 생성될 패키지를 지정한다.
  - Add to Persistence Unit: 체크 해제한다.

Entity 편집

- schema와 catalog를 지운다.
- 공통된 속성을 뽑아서 부모 클래스를 만든다.

## 참고

Cannot resolve column 해결:

- Persistence 패널에서 마우스 우클릭
- `Assign Data Sources`에서 추가한 데이터베이스를 선택한다.
