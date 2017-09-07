# Typescript

## Installation

    npm install -g typescript

## Type

변수, 함수 파라미터에 타입을 지정할 수 있다.

```ts
function greeter(person: string) {
    return "Hello, " + person;
}
```

## Interface

변수의 정의된 인터페이스와 내부 구조가 동일할 경우 명시적인 선언이 없더라도 인터페이스를 `implements` 한 것으로 판단한다.

```ts
interface Person {
    firstName: string;
    lastName: string;
}

var user = { firstName: "Jane", lastName: "User" };
```

위와 같이 정의된 경우 `Person`을 파라미터로 받는 함수에 `user`를 전달할 수 있다.

## Class

생성자를 갖는 클래스를 선언할 수 있다. 생성자의 파라미터로 전달되는 값은 자동으로 프로퍼티에 추가된다.

```ts
class Student {
    fullName: string;
    constructor(public firstName, public middleInitial, public lastName) {
        this.fullName = firstName + " " + middleInitial + " " + lastName;
    }
}
```

위 예제에서 `Student`는 `fullName`, `firstName`, `middleInitial`, `lastName` 프로퍼티를 갖는다. 따라서 명시적인 `implements` 선언이 없이도 `Student` 클래스는 `Person` 인터페이스를 구현했다고 볼 수 있다.

위 클래스는 다음과 같은 자바스크립트 코드로 컴파일된다.

```ts
var Student = (
    // 익명 즉시 실행 함수 (immediately-invoked function expression)
    // 변수의 Scope를 정의하기 위해 사용함
    function () {
        // 함수 선언 (function declaration)
        function Student(firstName, middleInitial, lastName) {
            this.firstName = firstName;
            this.middleInitial = middleInitial;
            this.lastName = lastName;
            this.fullName = firstName + " " + middleInitial + " " + lastName;
        }
        return Student;
    }()
);
```

## Basic Types

Boolean :

```ts
let isDone: boolean = false;
```

Number :

```ts
// Number
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
```

String :

```ts
let color: string = "blue";
color = 'red';

// Template String - 여러줄에 걸치거나 ${ 표현식 }을 포함하는 문자열
let fullName: string = `Bob Bobbington`;
let age: number = 37;
let sentence: string = `Hello, my name is ${ fullName }.

I'll be ${ age + 1 } years old next month.`

// 위의 sentence는 아래의 sentence로 변환된다
var sentence = "Hello, my name is " + fullName + ".\n\nI'll be " + (age + 1) + " years old next month.";
```

Array :

```ts
let list: number[] = [1, 2, 3];

// Generic Array<elemeType>
let list: Array<number> = [1, 2, 3];
```

Tuple :

```ts
// Declare a tuple type
let x: [string, number];
// Initialize it
x = ["hello", 10]; // OK
// Initialize it incorrectly
x = [10, "hello"]; // Error
```

Enum :

```ts
// Red: 0, Green:1, Blue:2
enum Color {Red, Green, Blue};
let c: Color = Color.Green;

// Red: 1, Green:2, Blue:3
enum Color {Red = 1, Green, Blue};
let c: Color = Color.Green;

// Manual
enum Color {Red = 1, Green = 2, Blue = 4};
let c: Color = Color.Green;
// colorName = Green
let colorName: string = Color[2];
```

Any :

```ts
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; // okay, definitely a boolean
notSure.ifItExists(); // okay, ifItExists might exist at runtime
notSure.toFixed(); // okay, toFixed exists (but the compiler doesn't check)
```

Void :

```ts
function warnUser(): void {
    alert("This is my warning message");
}
```

Null and Undefined :

```ts
// Not much else we can assign to these variables!
let u: undefined = undefined;
let n: null = null;
// As a note: we encourage the use of --strictNullChecks when possible
```

Never :

```ts
// Function returning never must have unreachable end point
function error(message: string): never {
    throw new Error(message);
}

// Inferred return type is never
function fail() {
    return error("Something failed");
}

// Function returning never must have unreachable end point
function infiniteLoop(): never {
    while (true) {
    }
}
```

## Type assertion

TypeScript에서 형 변환을 할 때 사용하는 방법. 다른 언어의 Type Cast 와 비슷한 문법을 가지지만, 다른 언어와는 다르게 데이터를 재구성하지 않으므로 런타임에 영향을 주지 않는다. Type Assertion은 컴파일 시점에만 의미를 갖는다.

```ts
let someValue: any = "this is a string";
let strLength: number = (<string>someValue).length;
// or
let strLength: number = (someValue as string).length;