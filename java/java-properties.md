# Properties

`java.util.Properties` 클래스는 자바에서 설정 값(파라미터)을 코드 외부로 분리하기 위해 사용한다.

## .properties 파일

프로퍼티 파일의 확장자는 무엇이 되든 상관 없지만 주로 `.properties`를 사용한다. 프로퍼티 파일의 각 라인은 하나의 프로퍼티를 정의한다.

프로퍼티는 다음과 같은 형식으로 정의한다. 이때, 따옴표(`"`)와 작은 따옴표(`'`)는 값의 일부로 처리된다.

```properties
key=value
key = value
key : value
key value
```

주석은 `#`이나 `!`로 시작한다.

```properties
# Sharp Comment
key1=value1
! Bang comment
key2=value2
```

값을 여러줄에 걸쳐 입력하고 싶을 때는 `\`를 사용한다. 다음 예제에서 Wikipedia 앞의 공백은 모두 제거되고 `message`는 `Welcome to Wikipedia` 값을 갖는다.

```properties
message = Welcome to \
          Wikipedia!
```

### 예제

다음과 같은 프로퍼티 파일이 있을 경우

```properties
# example.properties
message = Hello!
```

`Properties.load()` 메소드로 프로퍼티 파일을 읽고, `Properties.getProperty()` 메소드로 값을 조회한다.

```java
Properties props = new Properties();
props.load(ClassLoader.getSystemResourceAsStream("example.properties"));
// message를 조회하고 값이 없을 경우 null을 리턴한다.
String message = props.getProperty("message");
// name을 조회하고 값이 없을 경우 alex를 기본값으로 사용한다.
String name = props.getProperty("name", "alex");
// city는 null 이다.
String city = props.getProperty("city");
```

### 인코딩

프로퍼티 파일의 인코딩은 [ISO-8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1)이다. 한글은 유니코드 문자열을 `escape`한 뒤 입력해야 한다. 다음 예제에서 `message`는 `안녕하세요` 값을 갖는다.

```properties
message=\uc548\ub155\ud558\uc138\uc694
```

> IntelliJ를 사용하는 경우 `Settings > Editor > File Encodings` 메뉴에서 Properties Files 항목의 Transparent native-to-ascii conversion 을 체크해주면 한글을 자동으로 이스케이프된 유니코드 문자열로 변환해서 입력하거나 보여준다.

## XML 파일

Java 1.5부터 도입된 XML 포맷을 사용해서 유니코드 이스케이프 문자를 사용하지 않고 프로퍼티 파일을 정의할 수 있다.

```xml
<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE properties SYSTEM "http://java.sun.com/dtd/properties.dtd">
<properties>
    <comment>XML Format</comment>
    <entry key="message">안녕하세요</entry>
</properties>
```

## Java 9

Java 9부터는 프로퍼티 파일의 기본 인코딩이 UTF-8이다. 프로퍼티 파일을 읽을 때 UTF-8을 적용할 수 없을 경우 ISO-8859-1을 사용한다.

## 참고

- [GitHub 예제 코드](https://github.com/raycon/examples/blob/master/java/src/test/java/com/raegon/properties/PropertiesTest.java)