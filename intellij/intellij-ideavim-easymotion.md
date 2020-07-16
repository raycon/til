# IdeaVim에서 EasyMotion 사용하는 방법

`h`, `j`, `k`, `l` 키로 왔다갔다 귀찮을 때 쓰면 좋은 방법: [IdeaVim-EasyMotion](https://github.com/AlexPl292/IdeaVim-EasyMotion)을 사용한다.

- IntelliJ IDEA에 `IdeaVim`, `AceJump`, `IdeaVim-EasyMotion` 플러그인을 설치한다.
- `~/.ideavimrc`에 아래 내용을 추가한다.

```vim
set easymotion
```

- `\\s` 를 누르면 점진적 검색을 하면서 원하는 위치를 탐색할 수 있다.
- 전체 목록은 아래 표와 같다.

```
Default Mapping |  <Plug> command       |
-----------------------------------------------------------------
<ll>f{char}    |  <Plug>(easymotion-f) |  mapped to fn
<ll>F{char}    |  <Plug>(easymotion-F) |  mapped to Fn
<ll>t{char}    |  <Plug>(easymotion-t) |  mapped to tn
<ll>T{char}    |  <Plug>(easymotion-T) |  mapped to Tn

<ll>w          |  <Plug>(easymotion-w) |
<ll>W          |  <Plug>(easymotion-W) |
<ll>b          |  <Plug>(easymotion-b) |
<ll>B          |  <Plug>(easymotion-B) |
<ll>e          |  <Plug>(easymotion-e) |
<ll>E          |  <Plug>(easymotion-E) |
<ll>ge         |  <Plug>(easymotion-ge |
<ll>gE         |  <Plug>(easymotion-gE |
<ll>j          |  <Plug>(easymotion-j) |
<ll>k          |  <Plug>(easymotion-k) |
<ll>n          |  <Plug>(easymotion-n) |
<ll>N          |  <Plug>(easymotion-N) |
<ll>s          |  <Plug>(easymotion-s) |  mapped to sn
```

- `Space`를 `\\s`로 매핑해서 쉽게 사용할 수 있다.

```vim
nmap <Space> <Plug>(easymotion-s)
```
