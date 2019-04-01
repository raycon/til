# Heap Pollution

`heap pollution`이란 `parameterized type`의 변수가 해당하는 타입을 참조하지 않는 경우를 말한다.

예를들어:

```java
List ln = new ArrayList<Number>();
List<String> ls = ln;  // unchecked warning
String s = ls.get(0); // ClassCastException
```

`ln`을 `ls`에 대입하면 `List<String>` 타입의 변수 `ls`는 `List<Number>`를 가리키게 된다. 이러한 상황이 `heap pollution`이다. `heap pollution`은  `ClassCastException`을 초래한다.

위 코드를 컴파일 하면 `unchecked warning`이 발생하는데, 이런류의 경고가 없도록 컴파일 하면 `help pollution`을 예방할 수 있다.

## 참고

- Wikipedia, [Heap polution](https://en.wikipedia.org/wiki/Heap_pollution)
- [What is heap pollution?](http://www.angelikalanger.com/GenericsFAQ/FAQSections/TechnicalDetails.html#Topic2)