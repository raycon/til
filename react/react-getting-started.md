# React

사용자 인터페이스를 만들기 위한 JavaScript 라이브러리

## JSX

- 자바스크립트를 확장한 문법
- `React Element`를 정의한다.
- `Component`: 마크업과 로직이 느슨하게 결합된 유닛
- Babel은 JSX를 `React.createElement()` 호출로 변환한다.
- React는 `React.createElement()` 호출로 `React Element` 를 생성한다.
- 속성을 `camelCase` 를 사용해서 정의한다.

```js
// 한줄로 정의
const name = "Josh Perez";

// ()를 사용해서 여러줄로 정의
// {}를 사용해서 자바스크립트 표현식을 사용할 수 있다.
const element = <h1>Hello, {formatName(user)}!</h1>;

// 리턴 값으로 JSX 를 리턴할 수 있다.
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}

// ""를 사용해서 속성을 정의한다.
const element = <div tabIndex="0"></div>;

// {}를 사용해서 자바스크립트 표현식을 사용해서 속성을 정의한다.
const element = <img src={user.avatarUrl}></img>;

// 자식을 포함할 수 있다.
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

JSX 는 다음과 같이 변환된다.

```js
// JSX
const element = <h1 className="greeting">Hello, world!</h1>;

// Babel
const element = React.createElement(
  "h1",
  { className: "greeting" },
  "Hello, world!"
);

// React (단순화됨)
const element = {
  type: "h1",
  props: {
    className: "greeting",
    children: "Hello, world!"
  }
};
```

## Element

- `Componenet`의 구성요소
- 불변객체. 엘리먼트를 생성한 이후에 수정할 수 없다.
- React DOM은 렌더링을 할 때 이전 엘리먼트와 비교하고, 변경된 부분만 업데이트 한다.

```js
// Element 정의
const element = <h1>Hello, world</h1>;

// <div id="root"></div> 를 찾아서 렌더링 한다.
ReactDOM.render(element, document.getElementById("root"));
```

위 코드는 다음 HTML을 생성한다.

```html
<div id="root"><h1>Hello, world</h1></div>
```

## Component

- `props` 입력을 받은 후 화면에 어떻게 표시할지 기술하는 엘리컨트를 반환한다.
- 자바스크립트의 함수와 유사하다.
- 컴포넌트의 이름은 [항상 대문자](https://ko.reactjs.org/docs/jsx-in-depth.html#user-defined-components-must-be-capitalized)로 시작해야한다.
- `props` 는 읽기 전용이다.

```js
// 함수 컴포넌트
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

// 클래스 컴포넌트
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

React 엘리먼트는 사용자 정의 컴포넌트로도 나타낼 수 있다.

```js
// 컴포넌트 정의
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

// 컴포넌트를 사용한 엘리먼트 정의
// name="Sara" 어트리뷰트가 props 객체로 Welcome 컴포넌트에 전달된다.
const element = <Welcome name="Sara" />;

// DOM 렌더링
ReactDOM.render(element, document.getElementById("root"));
```

컴포넌트를 사용해서 컴포넌트를 정의할 수 있다.

```js
function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}
```

## State

- `props`와 유사하지만 컴포넌트에 의해 완전히 제어된다.
- `setState()`가 호출되면 React는 `render()` 메서드를 호출한다.
- `setState()`를 호출할 때 React는 제공한 객체를 현재 state로 병합한다.
- 생명주기 메서드가 state 를 설정하기 유용한 메서드다.
- 직접 값을 설정하면 안된다.

```js
// Wrong
this.state.comment = "Hello";
// Correct
this.setState({ comment: "Hello" });
```

# React

## 주요 개념

### Element

- React 앱의 가장 작은 단위로 화면에 표시할 내용을 기술한다.
- JSX를 사용해서 표현한다.

### JSX

- React Element 를 생성한다.
  ```jsx
  const element = <h1 className="greeting">Hello, world!</h1>;
  ```
- Babel은 JSX를 `React.createElement()` 호출로 컴파일한다.
  ```js
  const element = React.createElement(
    "h1",
    { className: "greeting" },
    "Hello, world!"
  );
  ```
- `React.createElement()`는 자바스크립트 객체를 생성한다.
  ```js
  // 주의: 다음 구조는 단순화되었습니다
  const element = {
    type: "h1",
    props: {
      className: "greeting",
      children: "Hello, world!"
    }
  };
  ```

### Component

- `props` 입력을 받아서 Element를 반환한다.
- 함수 컴포넌트
  ```js
  function Welcome(props) {
    return <h1>Hello, {props.name}</h1>;
  }
  ```
- 클래스 컴포넌트
  ```js
  class Welcome extends React.Component {
    render() {
      return <h1>Hello, {this.props.name}</h1>;
    }
  }
  ```

### State

- 컴포넌트는 각각 고유한 상태를 가질 수 있다.
- 상태가 변경되면 컴포넌트를 다시 렌더링 한다.

### Event

- JSX 를 사용해서 함수를 이벤트 핸들러로 전달한다.
  ```js
  <button onClick={activateLasers}>Activate Lasers</button>
  ```

### Condition

- 조건부 연산자로 표시할 엘리먼트를 정의할 수 있다.
  ```js
  function Greeting(props) {
    const isLoggedIn = props.isLoggedIn;
    if (isLoggedIn) {
      return <UserGreeting />;
    }
    return <GuestGreeting />;
  }
  ```
- `&&` 뒤의 엘리먼트는 조건이 `true`일때 출력되고, 조건이 `false`라면 React가 무시한다.
  ```js
  function Mailbox(props) {
    const unreadMessages = props.unreadMessages;
    return (
      <div>
        <h1>Hello!</h1>
        {unreadMessages.length > 0 && (
          <h2>You have {unreadMessages.length} unread messages.</h2>
        )}
      </div>
    );
  }
  ```
- inline 으로 표현할 수 있다.
  ```js
  render() {
    const isLoggedIn = this.state.isLoggedIn;
    return (
      <div>
        The user is <b>{isLoggedIn ? 'currently' : 'not'}</b> logged in.
      </div>
    );
  }
  ```
- 컴포넌트가 `null`을 반환하면 렌더링 하지 않는다.

### List

- 컴포넌트의 리스트(배열)를 중괄호`{}`를 사용해서 JSX 에 포함시킬 수 있다.
- 배열 내부의 엘리먼트에 `Key`를 지정한다.
- key는 React 가 항목을 변경, 추가, 삭제할때, 각 항목을 식별하는 것을 돕는다.
- key는 형제 사이에서만 유일하면 되고, 전역에서 유일할 필요는 없다.
- `map()` 함수 내부에 있는 엘리먼트에 key를 넣어 주는 게 좋다.
- key는 `props`로 전달되지 않는다.

### Form

- 제어 컴포넌트(Controlled Component): React에 의해 값이 제어되는 입력 폼 엘리먼트
- `value`를 사용해서 값을 표시한다.
- `onChange`를 사용해서 값을 갱신한다.
  - `input` 엘리먼트에 `name`을 추가하고 `event.target.name` 을 사용해서 구별할 수 있다.
- `onSubmit`을 사용해서 값을 제출한다.
- 제어 컴포넌트에 `value`를 설정할 경우, `onChange`를 설정하지 않으면사용자가 변경할 수 없다.

### State 끌어 올리기

- 동일한 데이터에 대한 변경사항을 여러 컴포넌트에 반영해야 할 필요가 있습니다. 이럴 때는 가장 가까운 공통 조상으로 state를 끌어올리는 것이 좋다.
- 공통 조상은 `진리의 원천`이 되어서 데이터를 제공한다.

### 합성

- `props.children`을 사용해서 자식 엘리먼트를 출력할 수 있다.
- `구체적인` 컴포넌트가 `일반적인` 컴포넌트를 렌더링하고 `props`를 통해 내용을 구성한다.

### React로 생각하기

- 각 컴포넌트가 데이터 모델의 한 조각을 나타내도록 분리해주세요.
- state 가 아닌 경우
  - 부모로부터 props를 통해 전달되는 값
  - 시간이 지나도 변하지 않는 값
  - 컴포넌트 안의 다른 state나 props를 가지고 계산 가능한 값

## 접근성

### ref

- `createRef`로 `ref`를 생성하고 포커스를 지정하는데 사용할 수 있다.

  ```js
  this.textInput = React.createRef();

  <input type="text" ref={this.textInput}/>

  focus() {
    this.textInput.current.focus();
  }
  ```

## 코드 분할

- 동적 `import`를 사용해서 앱 로딩 속도를 향상시킬 수 있다.
- 여러 js 를 묶어서 bundle로 만들어주는 툴인 Webpack이 코드 분할을 지원한다.
- `React.lazy` 함수를 사용하면 동적 import를 사용해서 컴포넌트를 렌더링 할 수 있다.
  - SSR 에서는 사용할 수 없다.
  - `Suspend`를 사용해서 로딩할 때 보여줄 컴포넌트를 지정할 수 있다.

여기서부터 다시 시작
https://ko.reactjs.org/docs/context.html

## Context

- context를 이용하면, 데이터를 props로 넘겨주지 않고 여러 컴포넌트에서 사용할 수 있다.
- 선호 로케일, 테마, 데이터 캐시 등을 관리하는 데 사용하면 편리하다.
- 클래스 컴포넌트에서 하나의 Context 구독하기
  - `MyClass.contextType = MyContext` 로 컨텍스트를 지정
  - `this.context` 로 사용
- 함수 컴포넌트에서 구독
  ```
  <MyContext.Consumer>
    {value => /* context 값을 이용한 렌더링 */}
  </MyContext.Consumer>
  ```
  - `Context.Consumer`의 자식은 함수여야 한다.

## Error Boundary

https://ko.reactjs.org/docs/error-boundaries.html

## Forwarding Refs

https://ko.reactjs.org/docs/forwarding-refs.html

## Fragments

- Fragments는 DOM에 별도의 노드를 추가하지 않고 여러 자식을 그룹화할 수 있다.
  ```html
  <table>
    <tr>
      <!-- 이 부분을 컴포넌트로 분리하려고 할 때-->
      <td>Hello</td>
      <td>World</td>
    </tr>
  </table>
  ```
  ```js
  // <React.Fragment> 나 <> 를 사용해서 그룹화 한다.
  return (
    <>
      <td>Hello</td>
      <td>World</td>
    </>
  );
  ```
- Fragments에 key가 있다면 <React.Fragment> 문법으로 명시적으로 선언해야 한다.
  ```js
  props.items.map(item => (
    // React는 `key`가 없으면 key warning을 발생한다.
    <React.Fragment key={item.id}>
  ...
  ```

## HOC

- HOC는 컴포넌트를 받아서 새로운 컴포넌트를 반환하는 함수다.
  - `const EnhancedComponent = higherOrderComponent(WrappedComponent);`
- Higher-order component 는 React API가 아니며, 리액트에서 컴포넌트가 쓰이는 방식에 따라 나타나는 패턴이다.
- 컴포넌트는 props 를 컴포넌트로 변환하는 것과 다르게, HOC는 컴포넌트를 컴포넌트로 변환한다.
- 여러 컴포넌트에서 사용하는 로직을 추상화 해서 HOC 로 분리할 수 있다.
- HOC 에서 사용하지 않는 props 값은 Wrapped Component 로 전달해주는게 좋다.

  ```js
  render() {
    // Filter out extra props that are specific to this HOC and shouldn't be
    // passed through
    const { extraProp, ...passThroughProps } = this.props;

    // Inject props into the wrapped component. These are usually state values or
    // instance methods.
    const injectedProp = someStateOrInstanceMethod;

    // Pass props to wrapped component
    return (
      <WrappedComponent
        injectedProp={injectedProp}
        {...passThroughProps}
      />
    );
  }
  ```

- HOC 는 주로 다음과 같은 모습을 갖는다.
  ```js
  // 1
  const NavbarWithRouter = withRouter(Navbar);
  // 2
  const CommentWithRelay = Relay.createContainer(Comment, config);
  // 3 React Redux's `connect`
  const ConnectedComment = connect(
    commentSelector,
    commentActions
  )(CommentList);
  ```
  3번을 나눠서 보면 다음과 같다.
  ```js
  // connect 는 HOC를 리턴하는 HOF. (Higher-order function)
  const enhance = connect(commentListSelector, commentListActions);
  // enhance 는 컴포넌트를 전달받는 HOC
  const ConnectedComment = enhance(CommentList);
  ```
  이러한 방식은 함수를 compose 해서 사용하는 라이브러리를 사용할 때 유용한다. 여러 HOF를 조합해서 하나의 HOC를 만들어서 사용할 수 있다.
- displayName 을 지정해서 dev tool 에서 디버깅할 때 볼 수 있다.
- 경고
  - HOC 를 render 함수 안에서 사용하지 말것. 렌더링 할 때 마다 새로운 컴포넌트가 생성되어서 이전 컴포넌트가 언마운트 되고 새로운 컴포넌트가 마운트된다. 성능 문제 뿐만 아니라 state 가 유실 되어서 문제가 된다.
  - props 를 자식 컴포넌트에 전달해도 `key`와 비슷하게 `ref`도 전달되지 않는다.

## JSX 이해하기

- JSX 는 BABEL에 의해 `React.createElement(...)` 호출로 변환된다.
- 따라서 `import React from 'react'` 가 코드에 존재해야 한다.

## Ref와 DOM

- `ref`는 자식 엘리먼트를 제어하기 위해서 사용한다.
- 생성: `this.myRef = React.createRef()`
- 지정: `<div ref={this.myRef}>`
- 사용: `const node = this.myRef.current;`

https://ko.reactjs.org/docs/higher-order-components.html#convention-wrap-the-display-name-for-easy-debugging
