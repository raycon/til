# Import static methods

테스트를 위해 `assertj`와 `Mockito`를 사용하다보면 다음과 같은 `static` 메소드를 import 해서 사용해야 한다.

    import static org.assertj.core.api.Assertions.assertThat
    import static org.mockito.BDDMockito.given;
    import static org.mockito.Matchers.any;
    import static org.mockito.Mockito.mock;
    import static org.mockito.Mockito.times;
    import static org.mockito.Mockito.verify;

이클립스는 static 메소드를 검색 대상에 포함하지 않기 때문에 이를 자동으로 입력할 수 있게 설정이 필요하다.

`Window » Preferences » Java » Editor » Content Assist » Favorites` 에서 `New Type...`을 누르고 다음을 입력한다.

    org.mockito.Matchers
    org.mockito.Mockito
    org.mockito.BDDMockito
    org.assertj.core.api.Assertions

`given()`, `assertThat()`과 같은 메소드를 호출 할 때 자동완성이 지원된다.