# IntelliJ HotSwap

> <https://github.com/dmitry-zhuravlev/hotswap-agent-intellij-plugin#dcevm-installation> 참고

IntelliJ에서 HotSwap을 사용하면 어플리케이션을 재시작 하지 않고 수정사항을 반영할 수 있다.

- `Debug` 모드로 어플리케이션 실행
- 코드 수정
- Rebuild (`Ctrl+Shift+F9`)
- HotSwap으로 class 파일이 다시 로드됨

이 기능은 Java SDK의 기능적인 제약으로 인해 메소드의 시그니쳐가 변경하는 경우 에러가 발생한다.

해결 방법:

1. JRebel: 유료. 연 $550로 엄청나게 비싸다.
1. Spring-Loaded: 2018-08-07 기준 최근 커밋이 2017-11-30으로 업데이트가 안되고 있다.
1. **DCEVM: 무료, 오픈소스**

## DCEVM (Dynamic Code Evolution VM)

- 최신버전을 [다운로드](https://github.com/dcevm/dcevm/releases)한다.
- `java -jar DCEVM-8u181-installer.jar` 명령으로 실행한다.
- 현재 사용하는 Java를 선택하고 `Install DCEVM as altjvm` 버튼을 누른다.

### Hotswap Agent

> <http://hotswapagent.org/mydoc_setup_intellij_idea.html> 참고

- 최신버전을 [다운로드](https://github.com/HotswapProjects/HotswapAgent/releases)한다.
- IntelliJ에 `HotSwapAgent` 플러그인을 설치한다.
- `Settings > Tools > HotSwapAgent` 에서 `Enable HotSwapAgent in all configurations`에 체크한다.
- `Agent installation`에 다운로드한 jar 파일을 지정한다.

어플리케이션을 디버그 모드로 실행하면 `HOTSWAP AGENT` 로그가 출력된다. 이제 메소드 이름을 변경하고 `Ctrl+Shift+F9`를 눌러도 에러가 발생하지 않고 수정사항이 바로 반영된다.

### Tips

IntelliJ는 파일을 저장할 때 컴파일 하는 기능을 제공하지 않는다. 따라서 `Ctrl+S`로 저장하고 `Ctrl+Shift+F9`를 매번 눌러야해서 불편하다. `Settings > Keymap`에서 `Main menu > Build > Rebuild`에 `Ctrl+S`를 지정한다. `Save All`단축키는 사라지지만 `Rebuild` 동작을 수행하면서 파일이 저장되고 빌드도 새로 된다. **꼼수**다. ~~묘하게 불편할 수 있음~~