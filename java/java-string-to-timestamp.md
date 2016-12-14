# String to Timestamp


String 을 Timestamp 로 변환하는 일반적인 방법 :

```java
SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss.SSS");
Date parsedDate = dateFormat.parse(yourString);
Timestamp timestamp = new java.sql.Timestamp(parsedDate.getTime());
```

자바에서 시간 관련 코딩 할때는 이것 저것 할 것 없이 요다타임 쓰면 넘나 편한것. 예를 들면 Timezone 변경같은게 필요할 경우.

Gradle 디펜던시 추가 :

```gradle
dependencies {
    compile('joda-time:joda-time')
}
```

Import 하고 :

```java
import org.joda.time.DateTime;
import org.joda.time.DateTimeZone;
import org.joda.time.format.DateTimeFormat;
import org.joda.time.format.DateTimeFormatter;
```

UTC "2016-12-08 01:00:00" > Timestamp 로 변경 :

```java
DateTimeFormatter formatter = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss").withZone(DateTimeZone.UTC);
DateTime dt = DateTime.parse("2016-12-08 01:00:00", formatter);
Timestamp timestamp = new Timestamp(dt.getMillis());
```

KST "2016-12-08 10:00:00" > Timestamp 로 변경 :

```java
DateTimeZone seoul = DateTimeZone.forID("Asia/Seoul");
DateTimeFormatter formatter = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss").withZone(seoul);
DateTime dt = DateTime.parse("2016-12-08 10:00:00", formatter);
Timestamp timestamp = new Timestamp(dt.getMillis());