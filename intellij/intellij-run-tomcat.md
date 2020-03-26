# 톰캣에서 스프링 어플리케이션 실행

- `Edit Configuration`
- `Templates` > `Tomcat Server` > `Local`
- `Server` 탭
  - Application server에 톰캣이 설치된 경로를 지정한다.
  - VM options에 `-Dspring.profiles.active=PROFILE_NAME` 값을 지정해서 프로필을 지정한다.
- `Deployment` 탭
  - `+` 버튼을 누른다.
  - `war`, `war exploded`를 선택한다.
  - `war exploded`를 선택할 경우 `▶` 버튼에서 다음 옵션이 활성화된다.
    - Update resources, Update classes and resources
    - 클래스 수정하고 Update classes... 를 선택해도 수정 사항 반영은 되지 않는다.
    - TODO: 어떻게 작동하는지 알아볼 필요 있음
