# Java Run Command

자바에서 외부 프로세스 실행하는 방법

## Runtime 사용

```java
String command = "echo \"hello\"";
Process process = Runtime.getRuntime().exec(command);
```

만약 윈도우에서 사용할 경우 `cmd /c`를 명령어 앞에 추가해야 한다.

```java
if (SystemUtils.IS_OS_WINDOWS) {
    command = "cmd /c " + command;
}
Process process = Runtime.getRuntime().exec(command);
```

프로세스의 InputStream을 읽어서 System.out 으로 출력할 수 있다.

```java
process.waitFor();
try (InputStream psout = process.getInputStream()) {
    byte[] buffer = new byte[1024];
    int n = 0;
    while ((n = psout.read(buffer)) != -1) {
        System.out.write(buffer, 0, n);
    }
}
```

위 방식은 프로세스에서 출력하는 메시지 양이 많을 경우 문제가 발생할 수 있다. 쓰레드를 생성해서 프로세스의 InputStream을 읽는 방식을 사용할 수 있다.

```java
new Thread(() -> {
    BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
    String line;
    try {
        while ((line = input.readLine()) != null)
            System.out.println(line);
    } catch (IOException e) {
        e.printStackTrace();
    }
}).start();
p.waitFor();
```

## ProcessBuilder 사용

ProcessBuilder를 사용하면 간단하게 실행이 가능하다.

```java
ProcessBuilder builder = new ProcessBuilder("echo", "hello");
// ProcessBuilder builder = new ProcessBuilder("cmd", "/c", "echo", "hello"); // Windows
builder.redirectOutput(Redirect.INHERIT);
builder.redirectError(Redirect.INHERIT);
builder.start();
```

`inheritIO` 메소드를 사용해서 동일한 기능을 하도록 설정할 수 있다.

```java
ProcessBuilder builder = new ProcessBuilder(commands).inheritIO();
builder.start();
```

`process.waitFor` 메소드를 사용해서 exitCode를 리턴할 수 있다.

```java
private int execute(String command) {
    return execute(command.split(" "));
}

private int execute(String... command) {
    try {
        ProcessBuilder builder = new ProcessBuilder(decorate(command)).inheritIO();
        Process process = builder.start();
        return process.waitFor();
    } catch (IOException | InterruptedException e) {
        e.printStackTrace();
    }
    return -1;
}

private List<String> decorate(String... command) {
    List<String> commands = new ArrayList<>(Arrays.asList(command));
    if (SystemUtils.IS_OS_WINDOWS) {
        commands.addAll(0, Arrays.asList("cmd", "/c"));
    }
    return commands;
}
```
