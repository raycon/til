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
const name = 'Josh Perez';

// ()를 사용해서 여러줄로 정의
// {}를 사용해서 자바스크립트 표현식을 사용할 수 있다.
const element = (
  <h1>
    Hello, {formatName(user)}!
  </h1>
);

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
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);

// Babel
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);

// React (단순화됨)
const element = {
  type: 'h1',
  props: {
    className: 'greeting',
    children: 'Hello, world!'
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
ReactDOM.render(element, document.getElementById('root'));
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
ReactDOM.render(
  element,
  document.getElementById('root')
);
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
this.state.comment = 'Hello';
// Correct
this.setState({comment: 'Hello'});
```