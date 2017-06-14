# Eclipse Content Assist

이클립스에서 `Ctrl+Space`를 누르면 입력 가능한 변수나 메소드가 표시된다. 적당한 값을 찾아서 선택을 하면 자동으로 입력이 되는데, 이 때 동작이 살짝 이상하다.

```java
  public String getSomeValue() {
    return value;
  }

  public void doSomething() {
    String value = getOtherValue();
  }
```

위 같은 코드에서 `get|OtherValue()` 와 같이 커서를 이동하고 `Ctrl+Space`를 눌러서 어시스트 창을 띄운 다음 `S` 를 입력해서 `getSomeValue()`를 자동입력하면 다음과 같이 변경된다.

```java
  public String getSomeValue() {
    return value;
  }

  public void doSomething() {
    String value = getSomeValue()OtherValue();
  }
```

`-_-`

커서 오른쪽의 텍스트도 다 변경하려면, 어시스트 창이 떠있는 상태에서 `Ctrl` 키를 누른 상태로 `Enter`를 입력하면 된다.

어시스트 기본값을 변경하려면, `Window > Preferences > Java > Editor > Content Assist` 메뉴의 `Insertion` 항목을 `Completion overwrites`로 설정하면 된다.