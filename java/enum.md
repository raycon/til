# 자바 열거형

특징:

- 타입을 검사한다.
- 열거형 상수를 사용하면, 상수의 값이 변경되었을 때 다시 컴파일 하지 않아도 된다.

정의:

```java
enum 이름 { 상수1, 상수2, ... }
```

비교:

```java
if (type == Type.POST) ...

switch(type) {
    case GET:
    break;
    case POST:
    break;
    ...
}
```

메소드:

- `name()`: 열거형 상수의 이름을 String 으로 반환.
- `ordinal()`: 열거형 상수가 정의된 순서를 반환 (0 부터 시작).

기타 메소드:

```java
static E values() // 열거형의 모든 상수를 배열에 담아서 반환.
static E valueOf(String name) // 문자열을 상수로 변환
```

멤버 추가:

```java
enum Type {
    GET(1), POST(2), PUT(3), DELETE(4);

    private final int value;

    Type(int value) { this.value=value; }   // private 생략됨
    public int getValue() { return this.value; }
}
```

추상 메소드 추가:

```java

enum Trans {
    BUS(100) { int fare(int distance) { return distance*BASE} },
    TRAIN(150)  { int fare(int distance) { return distance*BASE} };

    protected final int BASE; // protected 로 해야 각 상수에서 접근 가능

    Trans(int base) {
        BASE = base;
    }

    abstract int fare(int distance); // 추상 메소드 선언
}
```

