# Shell Script

## Return value in bash script

echo 사용 :

```bash
function fun1(){
  echo 34
}

function fun2(){
  local res=$(fun1)
  echo $res
}
```

$(...) captures the text sent to stdout by the command contained within

return 사용 :

```bash
function fun1(){
  return 34
}

function fun2(){
  fun1
  local res=$?
  echo $res
}
```

$? contains the result code of the last command.