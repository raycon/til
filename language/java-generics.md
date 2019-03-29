# Generics

    generic [dʒəˈnerɪk]  
    형용사
    포괄적인, 총칭[통칭]의


`Generics`를 도입하기 전에는 명시적인 형 변환 과정에서 런타임 에러가 발생하는 가능성이 있었다. `Generics`를 사용하면 클래스나 인터페이스에서 쓰이는 타입을 파라미터화 한다. 이를 통해 엄격한 타입 검사가 가능해져서 컴파일 시점에 더 많은 버그를 탐지할 수 있다.

- [Generics](#generics)
  - [Generic Types](#generic-types)
    - [Type Parameter, Variable, Argument](#type-parameter-variable-argument)
  - [Type Parameter Naming Conventions](#type-parameter-naming-conventions)
  - [Generic Methods](#generic-methods)
  - [Bounded Type Parameters](#bounded-type-parameters)
    - [Upper Bound](#upper-bound)
    - [Multiple Bounds](#multiple-bounds)
  - [Generics, Inheritance, and Subtypes](#generics-inheritance-and-subtypes)
  - [Wildcards](#wildcards)
    - [Upper Bounded Wildcards](#upper-bounded-wildcards)
    - [Unbounded Wildcards](#unbounded-wildcards)
    - [Lower Bounded Wildcards](#lower-bounded-wildcards)
    - [Wildcards and Subtyping](#wildcards-and-subtyping)
    - [Wildcard Capture and Helper Methods](#wildcard-capture-and-helper-methods)
    - [Wildcard Guidelines](#wildcard-guidelines)
  - [Type Erasure](#type-erasure)
    - [Erasure of Generic Types](#erasure-of-generic-types)
    - [Erasure of Generic Methods](#erasure-of-generic-methods)
    - [Bridge Methods](#bridge-methods)
    - [Non-Reifiable Types](#non-reifiable-types)
  - [Restrictions on Generics](#restrictions-on-generics)
  - [참고](#%EC%B0%B8%EA%B3%A0)

## Generic Types

`Generic Type`은 파라미터화된 타입을 사용하는 `Generic Class`나 `Generic Interface`를 의미한다.

`Generic Class`는 다음과 같이 정의한다:

```java
class Name<T1, T2, ..., Tn> {
    /* ... */
}
```

`<>`안에 정의된 클래스 이름을 `Type Parameter`라고 부르며, `Type Variable` 이라고도 한다. 여기서 `T1`, `T2` 등의 타입 변수는 `primitive` 타입을 제외한 모든 타입(클래스, 인터페이스, 배열, 또 다른 타입 변수)이 될 수 있다.

`Type Parameter`는 `,`로 구분해서 여러개를 정의할 수 있다.

```java
public interface Pair<K, V> {
    public K getKey();
    public V getValue();
}
```

### Type Parameter, Variable, Argument

`Type Variable`은 `Type Parameter` 정의를 통해 선언된다.

> A type variable is introduced by the declaration of a type parameter of a generic class, interface, method, or constructor

다음과 같은 클래스 정의가 있을 때:

```java
public class Box<T extends Product> {
    private T t;
    public void set(T t) { this.t = t; }
    public T get() { return t; }
}
```

`T extends Product`는 Box 클래스의 `Type Parameter`를 정의하고, `Type Variable`로 `T`를 선언한다. `extends` 키워드는 아래에서 설명한다.

`Type Argument`는 제네릭 클래스의 인스턴스를 생성할 때 파라미터로 전달 된 실제 타입을 의미한다. 다음 예제에서 `Type Argument`는 `Cake`다.

```java
Box<Cake> cakeBox = new Box<Cake>();
```

자바7 이후에 도입된 타입추론을 사용하면 다음과 같은 형태로 인스턴스를 생성할 수 있다.

```java
Box<Cake> cakeBox = new Box<>();
```

이때 사용하는 `<>`를 `Diamond`라고 부른다.

## Type Parameter Naming Conventions

일반적인 변수 선언 방식과 다르게 타입 변수는 주로 대문자 하나를 사용한다. 가장 보편적으로 사용되는 타입 변수는 다음과 같다:

    E - Element (used extensively by the Java Collections Framework)
    K - Key
    N - Number
    T - Type
    V - Value
    S,U,V etc. - 2nd, 3rd, 4th types

## Generic Methods

`Generic Method`는 자신만의 타입 파라미터를 정의하는 메소드를 의미한다. 제네릭 타입 정의와 유사하지만 타입 파라미터의 유효 범위는 해당 메소드 내부로 제한된다.

제네릭 메소드는 메소드의 리턴 타입 앞부분에 타입 파라미터를 선언한다.

```java
public class Util {
    public static <K, V> boolean compare(Pair<K, V> p1, Pair<K, V> p2) {
        // ...
    }
}
```

다음과 같이 사용한다:

```java
boolean same = Util.<Integer, String>compare(p1, p2);
```

이때 컴파일러가 타입 추론을 할 수 있으므로, 타입 아규먼트는 생략 가능하다.

```java
boolean same = Util.compare(p1, p2);
```

## Bounded Type Parameters

`Bounded Type Parameter`는 `Type Argument`로 사용되는 타입의 종류를 제한하기 위해 사용된다.

### Upper Bound

`extends` 키워드를 사용해서 `Type Argument`를 특정 클래스를 상속받거나 특정 인터페이스를 구현한 타입으로 한정할 수 있다.

```java
class Product { ... }
interface Company { ... }

public class Box<T extends Product> {
    ...
    public <C extends Company> void setCompany(C c) {
        ...
    }
}
```

위 예제에서 `T`는 `Product`를 상속받아야 하며, `C`는 `Company`를 구현해야 한다.

### Multiple Bounds

`&`를 사용해서 여러 클래스나 인터페이스를 지정할 수 있다. 이때, 클래스 타입이 인터페이스보다 먼저 선언되어야 한다.

```java
class A { ... }
interface B { ... }
interface C { ...}

class D <T extends A & B & C> { ... }
class D <T extends B & A & C> { ... } // 에러. 클래스 A는 인터페이스 사이에 선언될 수 없다.
```

## Generics, Inheritance, and Subtypes

자바에서 `Integer`는 `Number`에 대입할 수 있다.

```java
public void someMethod(Number n) { ... }
someMethod(new Integer(10));   // OK
```

하지만 `Box<Integer>`는 `Box<Number>`에 대입할 수 없다.

```java
public void boxTest(Box<Number> n) { ... }
boxTest(new Box<Integer>(10));   // Error
```

`Integer`는 `Number`를 상속받지만, `Box<Integer>`는 `Box<Number>`를 상속받지 않기 때문이다.

![subtypes](https://docs.oracle.com/javase/tutorial/figures/java/generics-subtypeRelationship.gif)

이를 해결하기 위해 `Wildcard`를 사용한다.

## Wildcards

제네릭 코드에서 물음표 `?`는 `Unknown Type`을 나타내는 `wildcard`로 쓰인다. 파라미터, 필드, 로컬 변수의 타입으로 쓰이며 가끔은 리턴 타입으로 쓰이기도 한다. `Type Argument`, 제네릭 인스턴스 생성, `supertype`으로는 쓰이지 않는다.

### Upper Bounded Wildcards

    <? extends SomeType>

위 문법에서 `?`는 `SomeType`과 `SomeType`을 상속받거나 구현한 타입을 의미한다.

예를들면

- `List<Number> list`: `Number`의 인스턴스만 추가될 수 있다.
- `List<? extends Number> list`: `Number`를 상속받은 클래스의 인스턴스가 추가될 수 있다.

### Unbounded Wildcards

    <?>

바운더리가 지정되지 않은 와일드카드는 모든 타입을 의미한다.

List의 모든 요소를 출력하는 제네릭 메소드를 다음과 같이 작성할 경우 `List<Number>`나 `List<String>`은 파라미터로  전달할 수 없다.

```java
public static void printList(List<Object> list) {
    for (Object elem : list)
        System.out.println(elem + " ");
    System.out.println();
}
```

이때 와일드카드를 써서 다음과 같이 선언할 수 있다.

```java
public static void printList(List<?> list) {
    for (Object elem: list)
        System.out.print(elem + " ");
    System.out.println();
}
```

### Lower Bounded Wildcards

    <? super SomeType>

위 문법에서 `?`는 `SomeType`과 `SomeType`의 부모 타입을 의미한다.

예를들면

- `List<Integer> list`: `Integer`의 인스턴스만 추가될 수 있다.
- `List<? super Integer> list`: `Integer`, `Number`, `Object`의 인스턴스가 추가될 수 있다.

### Wildcards and Subtyping

와일드카드를 사용할 경우 다음과 같은 상속 관계가 정의된다.

                         List<?>
                        ↑       ↑
    List<? extends Number> ←┐┌→ List<? super Integer>
        ↑                   ││      ↑
    List<? extends Integer> └│┐ List<? super Number>
        ↑                    ││     ↑
    List<Integer> ───────────┘└ List<Number>

### Wildcard Capture and Helper Methods

컴파일러는 코드로부터 와일드카드의 특정 타입을 추론하는데, 이렇게 추론된 타입을 `Wildcard Capture`라고 한다.

```java
void foo(List<?> i) {
    i.set(0, i.get(0));
}
```

위 코드에서 `i`는 `Object`의 리스트로 처리된다. `set(int, CAP#1)` 시그니쳐를 사용해서 메소드를 호출해야 하는데, `i.get(0)`은 `Object`를 리턴하므로 다음과 같은 에러가 발생한다.

    WildcardError.java:6: error: method set in interface List<E> cannot be applied to given types;
        i.set(0, i.get(0));
        ^
    required: int,CAP#1
    found: int,Object

이때 `helper`메소드를 만들어서 `CAP#1`이 타입변수 `T`라고 지정해주면 문제를 해결할 수 있다.

```java
void foo(List<?> i) {
    fooHelper(i);
}

private <T> void fooHelper(List<T> l) {
    l.set(0, l.get(0));
}
```

위 코드에서 `List<T> l`은 `T` 타입의 리스트이고, `get`, `set` 모두 `T` 타입을 처리하기 때문에 에러가 발생하지 않는다.

Q: 그럼 fooHelper 메소드만 있으면 되는거 아닌가?

A: 맞다. `helper`메소드는 제네릭 도입 이전의 코드를 사용하기 위해 정의한다. 제네릭이 도입되면서 `List`는 `List<?>`가 되었다. 예전 코드를 제네릭이 도입된 이후의 컴파일러로 컴파일 할 경우 에러가 발생한다. 메소드의 시그니쳐를 바꿀 수 없을 경우, 헬퍼 메소드를 추가해서 오류를 해결할 수 있다.

와일드카드 캡쳐는 각각의 파라미터에 대해 추론된다. 다음 코드에서 `l1`은 `CAP#1` 타입이고, `l2`는 `CAP#2` 타입이다.

```java
void swapFirst(List<? extends Number> l1, List<? extends Number> l2) {
    Number temp = l1.get(0);
    // 기대값: CAP#1 extends Number
    // 실제값: CAP#1 extends Number
    l1.set(0, l2.get(0));
    // Number != CAP#2 extends Number
    l2.set(0, temp);
}
```

따라서 위 코드는 컴파일 에러를 발생한다.

### Wildcard Guidelines

다음과 같은 2가지 성격의 변수가 있다.

- `In` 변수: 코드에 데이터를 제공한다.
- `Out` 변수: 다른 곳에서 사용되는 데이터를 갖는다.
- `copy(src, dest)` 에서 `src`는 `In` 변수이고, `dest`는 `Out` 변수이다.

와일드카드를 어떤 경우에 어떻게 써야 하는가?

- `in` 변수는 `upper bounded wildcard <? extends Type>`를 사용해서 정의한다.
- `out` 변수는 `lower bounded wildcard <? super Type>`를 사용해서 정의한다.
- `in`변수에 정의된 메소드 중 `Object`의 메소드만 사용할 경우 `unbounded wildcard <?>`를 사용해서 정의한다.
- 코드에서 `in`변수와 `out`변수의 내부 변수에 접근하는 경우 와일드카드를 사용하지 않는다.

## Type Erasure

제네릭은 컴파일 시점에 타입 체크를 하기 위해 도입되었다. 제네릭과 관련된 코드는 컴파일 시점에 사용되고 제거된다. 따라서 생성된 바이트코드는 일반적인 클래스, 인터페이스, 메소드만 포함하게 된다. 이 과정을 `Type Erasure`라고 부른다. 자바 컴파일러는 다음과 같은 순서로 제네릭 타입을 제거한다.

- 제네릭 타입의 `Type Parameter`들을 파라미터의 `Bound`로 대체한다. `Unbounded Type Parameter <?>`는 `Object`로 대체된다. 
- 필요한 경우 형 변환 코드를 삽입한다.
- 상속된 제네릭 타입의 다형성을 위해서 `Bridge Method`를 생성한다.

### Erasure of Generic Types

다음 예제를 컴파일 할 경우:

```java
public class Node<T extends Comparable<T>> {

    private T data;
    private Node<T> next;

    public Node(T data, Node<T> next) {
        this.data = data;
        this.next = next;
    }

    public T getData() { return data; }
    // ...
}
```

`T` 는 `Comparable`로 대체된다.

```java
public class Node {

    private Comparable data;
    private Node next;

    public Node(Comparable data, Node next) {
        this.data = data;
        this.next = next;
    }

    public Comparable getData() { return data; }
    // ...
}
```

### Erasure of Generic Methods

다음 예제를 컴파일 할 경우:

```java
public static <T> int count(T[] anArray, T elem) {
    int cnt = 0;
    for (T e : anArray)
        if (e.equals(elem))
            ++cnt;
        return cnt;
}
```

`T`는 `Unbounded Type Parameter`이므로 `Object`로 교체된다.

```java
public static int count(Object[] anArray, Object elem) {
    int cnt = 0;
    for (Object e : anArray)
        if (e.equals(elem))
            ++cnt;
        return cnt;
}
```

다음과 같은 제네릭 메소드의 경우:

```java
public static <T extends Shape> void draw(T shape) { ... }
```

`T`는 `Shape`로 교체된다.

```java
public static void draw(Shape shape) { ... }
```

### Bridge Methods

다음과 같은 코드가 있을 때:

```java
public class Node<T> {

    public T data;

    public Node(T data) { this.data = data; }

    public void setData(T data) {
        System.out.println("Node.setData");
        this.data = data;
    }
}

public class MyNode extends Node<Integer> {
    public MyNode(Integer data) { super(data); }

    public void setData(Integer data) {
        System.out.println("MyNode.setData");
        super.setData(data);
    }
}
```

`Type Erasure`가 적용되면 `Node`와 `MyNode`는 다음과 같이 대체된다:

```java
public class Node {

    public Object data;

    public Node(Object data) { this.data = data; }

    public void setData(Object data) {
        System.out.println("Node.setData");
        this.data = data;
    }
}

public class MyNode extends Node {

    public MyNode(Integer data) { super(data); }

    public void setData(Integer data) {
        System.out.println("MyNode.setData");
        super.setData(data);
    }
}
```

이때 `MyNode`의 `setData(Integer data)`는 `Node`의 `setData(T data)`를 오버라이드 하고 있었지만, 변경된 코드에서는 이런 관계가 없어진다.

이 문제를 해결하기 위해 자바 컴파일러는 `Bridge Method`를 추가한다.

```java
class MyNode extends Node {

    // Bridge method generated by the compiler
    public void setData(Object data) {
        setData((Integer) data);
    }

    public void setData(Integer data) {
        System.out.println("MyNode.setData");
        super.setData(data);
    }

}
```

### Non-Reifiable Types

[Non-Refiable Types](https://docs.oracle.com/javase/tutorial/java/generics/nonReifiableVarargsType.html#non-reifiable-types) 요약 필요

## Restrictions on Generics

- 원시 타입을 사용해서 제네릭 타입의 인스턴스를 만들 수 없다.

      Pair<int, char> p;  // Error

- 타입 파라미터의 인스턴스를 만들 수 없다

      T t = new T();  // Error

- 타입 파라미터를 사용해서 정적 필드를 선언할 수 없다.

      private static T t;  // Error

- `instanceof`에 타입 파라미터를 사용할 수 없다.

      if(list instanceof ArrayList<Integer>)  // Error

- 형 변환을 할 수 없다

      List<Integer> li = new ArrayList<>();
      List<Number>  ln = (List<Number>) li; // Error

- 제네릭 타입의 배열을 생성할 수 없다.

      List<Integer>[] arrayOfLists = new List<Integer>[2];  // compile-time error

- 제네릭 타입은 `Exception`이나 `Throwable`을 상속받을 수 없다.

      // Extends Throwable indirectly
      class MathException<T> extends Exception { /* . */ }    // compile-time error
      // Extends Throwable directly
      class QueueFullException<T> extends Throwable { /* ... */ // compile-time error

- 타입 파라미터는 `catch` 구문에서 사용할 수 없다.

      try {
          ...
      } catch(T e) {    // Error
          ...
      }

- `Type Erasure` 이후 같은 시그니쳐를 갖는 메소드를 선언할 수 없다.

      public class Example {
          public void print(Set<String> strSet) { }
          public void print(Set<Integer> intSet) { }
      }

## 참고

- [The Java Tutorials - Generics](https://docs.oracle.com/javase/tutorial/java/generics/index.html)
- [Lesson: Generics](https://docs.oracle.com/javase/tutorial/extra/generics/index.html)
- [What is the difference between a wildcard bound and a type parameter bound?](http://www.angelikalanger.com/GenericsFAQ/FAQSections/TypeArguments.html#FAQ203)
- [Difference between class and type](https://stackoverflow.com/questions/16600750/difference-between-class-and-type)
- [Type Variables](https://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.4)
- [Definition of type variable and parameter](https://stackoverflow.com/questions/7075363/definition-of-type-variable-and-parameter)
- [Why use a wild card capture helper method?](https://stackoverflow.com/questions/30763895/why-use-a-wild-card-capture-helper-method)