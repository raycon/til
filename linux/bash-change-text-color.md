# Bash 출력 글자 색상 변경

> StackOverflow : [how to change the output color of echo inlinux](http://stackoverflow.com/questions/5947742/how-to-change-the-output-color-of-echo-in-linux)

[ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) 를 사용해서 색상을 지정할 수 있다.

```text
Black        0;30     Dark Gray     1;30
Red          0;31     Light Red     1;31
Green        0;32     Light Green   1;32
Brown/Orange 0;33     Yellow        1;33
Blue         0;34     Light Blue    1;34
Purple       0;35     Light Purple  1;35
Cyan         0;36     Light Cyan    1;36
Light Gray   0;37     White         1;37
```

다음과 같이 변수를 선언해서 사용한다 :

```bash
#    .---------- constant part!
#    vvvv vvvv-- the code from above
RED='\033[0;31m'
NC='\033[0m' # No Color
printf "I ${RED}love${NC} Stack Overflow\n"
echo -e "I ${RED}love${NC} Stack Overflow"
```

```bash
BLA='\033[0;30m'
RED='\033[0;31m'
GRE='\033[0;32m'
ORA='\033[0;33m'
BLU='\033[0;34m'
PUR='\033[0;35m'
CYA='\033[0;36m'
LGY='\033[0;37m'
GRY='\033[1;30m'
LRE='\033[1;31m'
LGR='\033[1;32m'
YEL='\033[1;33m'
LBL='\033[1;34m'
LPU='\033[1;35m'
LCY='\033[1;36m'
WHI='\033[1;37m'
NOC='\033[0m'
```