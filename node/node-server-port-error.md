# EADDRINUSE :::8080 (이미 사용하고 있는 포트) 에러 해결법

서버에서 node 실행 시 아래와 같은 에러거 발생했을 경우 :

```bash
$ node server.js
...
error: uncaughtException: listen EADDRINUSE :::8080 ...
```

`netstat`으로 포트를 사용하고 있는 프로세스를 찾는다 :

```bash
$ netstat -tulpn | grep :8080
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 :::8080                     :::*                        LISTEN      2930/node
```

`ps` 로 2930/node 프로세스를 찍어보면 다음과 같다 :

```bash
$ ps u 2930
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
id        2930  0.0  0.8 1244668 71508 pts/1   Sl   Nov27   0:03 node server.js
```

`kill -9 PID` 명령어로 프로세스를 종료한다 :

```bash
kill -9 2930
```