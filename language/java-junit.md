# JUnit 기초

기본적인 JUnit 설치 및 사용법은 [Getting started](https://github.com/junit-team/junit4/wiki/Getting-started)를 참고한다.

## 테스트 선언

테스트 메소드는 `public` `void` 이면서 `입력 인자가 없어야 한다`. 다음의 테스트는 두개의 인자가 같은지 확인한다.

```java
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class SampleTest {
  @Test
  public void testMethod() {
    assertEquals(5, 2+3);
  }
}
```

## 단언문

`assert~` 형태의 메소드를 말한다. `org.junit.Assert` 클래스에 `public static` 메서드로 정의되어 있다.

```java
// 첫번째 인자는 테스트가 실패할 경우 출력되는 메시지다. (생략 가능)
assertArrayEquals("failure - byte arrays not same", "trial".getBytes(), "trial".getBytes());
assertEquals("failure - strings are not equal", "text", "text");
assertFalse("failure - should be false", false);
assertNotNull("should not be null", new Object());
assertNotSame("should not be same Object", new Object(), new Object());
assertNull("should be null", null);
Integer aNumber = Integer.valueOf(768);
assertSame("should be same", aNumber, aNumber);
```

자세한 예제는 [Assertions](https://github.com/junit-team/junit4/wiki/Assertions)와 [Assert JavaDoc](http://junit.sourceforge.net/javadoc/org/junit/Assert.html)문서를 참고한다.

## assertThat

`assertThat` 메소드와 `Hamcrest`를 사용해서 기본 단언문을 확장할 수 있다. `Hamcrest`는 테스트에 유용한 다양한 `Matcher`를 제공한다. 자세한 사항은 [Tutorial](https://code.google.com/archive/p/hamcrest/wikis/Tutorial.wiki)을 참고한다.

```java
  // Core Hamcrest Matchers with assertThat
  @Test
  public void testAssertThatHamcrestCoreMatchers() {
    assertThat("good", allOf(equalTo("good"), startsWith("good")));
    assertThat("good", not(allOf(equalTo("bad"), equalTo("good"))));
    assertThat("good", anyOf(equalTo("bad"), equalTo("good")));
    assertThat(7, not(CombinableMatcher.<Integer> either(equalTo(3)).or(equalTo(4))));
    assertThat(new Object(), not(sameInstance(new Object())));
  }
```

## @Before, @After

 `@BeforeClass, @Before, @After, @AfterClass` 어노테이션을 사용해서 테스트를 수행하기 전과 후에 수행되는 메소드를 지정할 수 있다.

```java
@BeforeClass
public static void setUpClass() throws Exception {
  // 클래스에 정의된 테스트가 실행되기 전에 한번 실행된다.
}

@AfterClass
public static void tearDownClass() throws Exception {
  //클래스에 정의된 테스트가 실행된 후에 한번 실행된다.
}

@Before
public void setUpTest() throws Exception {
  //각각의 테스트 메소드가 수행되기 전에 실행된다.
}

@After
public void tearDownTest() throws Exception {
  //각각의 테스트 메소드가 수행된 후에 실행된다.
}
```

각각의 테스트 메소드는 다음과 같은 순서로 실행된다 :

    @BeforeClass
       ↓
    @Before → @Test → @After
    @Before → @Test → @After
    @Before → @Test → @After
       ↓
    @AfterClass

## @Rule

규칙을 사용하면 테스트 클래스에서 각 테스트 메소드의 동작을 유연하게 추가하거나 재정의 할 수 있다. 자세한 내용은 [Rules](https://github.com/junit-team/junit4/wiki/Rules)를 참고한다.

자주 사용되는 유용한 규칙 :

    ExpectedException : 에러를 수집한다.
    Timeout : 테스트 메소드의 타임아웃을 설정한다.
    TemporaryFolder : 임시 파일이나 폴더를 만들 수 있게 해주고, 테스트가 끝나면 자동으로 삭제한다.

## 예외 처리 설정

`expected` 구문 사용하는 방법. 간단히 사용하기 좋다.

```java
@Test(expected = IllegalAragumentException.class)
public void exceptionTest() {
  String number = "invalidPhoneNumber";
  Phone phone = new Phone();
  phone.call(number);
}
```

`try-catch` 구문을 사용하는 방법. Exception 처리 코드를 작성할 수 있다.

```java
@Test
public void exceptionTest() {
  String number = "invalidPhoneNumber";
  Phone phone = new Phone();
  try {
    phone.call(number);
    fail("invalid phone number");
  } catch (IllegalArgumentException e) {
    assertThat(e.getMessage(), containsString(number));
  }
}
```

`@Rule` 어노테이션 사용하는 방법. 코드가 간결해진다.

```java
public class ExceptionTest {

  @Rule
  public final ExpectedException exception = ExpectedException.none();

  @Test
  public void thisTestPasses() {
    // exception이 아무런 Exception을 expect 하고 있지 않을므로 이 테스트는 통과한다.
  }

  @Test
  public void throwsExceptionWithCorrectMessage() {
    // RuntimeException이 발생해야 한다.
    exception.expect(RuntimeException.class);
    // Exception의 메시지는 Hello 라는 문자열을 포함해야 한다.
    exception.expectMessage("Hello");
    // Hi 와 Hello 가 다르므로 이 테스트는 실패한다.
    throw new NullPointerException("Hi");
  }
}
```

## 시간 제한 설정

`@Test` 어노테이션의 `timeout` `attribute`를 설정해서 테스트 메소드의 수행 시간을 제한할 수 있다.

```java
@Test(timeout=3000)
public void timeoutTest() {
}
```

`@Rule`을 사용해서 모든 테스트 메소드에 같은 타임아웃을 설정할 수 있다. 다음의 두 테스트는 JUnit에 의해 강제 종료된다.

```java
@Rule
public MethodRule timeout = new Timeout(20);

@Test
public void loop1() {
  while (true) {};
}

@Test
public void loop2() {
  while (true) {};
}
```

## 참고자료

- [Test runners](https://github.com/junit-team/junit4/wiki/test-runners)
- [JUnit Cookbook](http://junit.sourceforge.net/doc/cookbook/cookbook.htm)