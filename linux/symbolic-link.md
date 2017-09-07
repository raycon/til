# 심볼릭 링크

## 명령어

```text
링크생성 : ln -s TARGET LINK_NAME
업데이트 : ln -sfn TARGET LINK_NAME
```

옵션 의미 :

```text
s, --symbolic       : 심볼릭 링크를 의미함
f, --force          : 현재 존재하는 파일을 덮어씀
n, --no-dereference : 심볼릭 링크를 일반 파일처럼 취급함
```

## 하드 링크와 차이

```bash
$ echo hello > test.txt
$ ln -s test.txt sym.txt
$ ln test.txt hard.txt
$ ls -i hard.txt
529066 hard.txt
$ ls -i sym.txt
529068 sym.txt
$ ls -i test.txt
529066 test.txt
```

- 하드링크(`hard.txt`) 와 원본(`test.txt`)은 inode number가 동일하다.
- 하드링크를 지워도 원본에 영향은 없다.
- 원본을 지우면 하드링크에는 영향이 없지만, 심볼릭 링크는 `No such file or directory` 오류가 발생한다.