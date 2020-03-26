# Spring Batch System Exit Code

스프링 배치의 Job을 실행하는 도중 에러가 발생하면 다음과 같은 로그와 함께 종료된다.

    Job: [SimpleJob: [name=sample-job]] completed with the following parameters: [{-job.name=sample.job}] and the following status: [FAILED]

    Process finished with exit code 0

Job의 [BatchStatus](http://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte2:brte:batch_core:flow_control)는 `FAILED`이지만 `exitCode`는 0이 되었다.

이럴 경우 Jenkins 에서 빌드가 성공했다고 표시되는 문제가 있다.

다음과 같이 `SpringApplication.run(...)`의 결과를 받아서 `System.exit(exitCode)`로 지정하면 `BatchStatus`를 `exitCode`로 전달할 수 있다.

```java
public class SampleBatchApplication {

    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(SampleBatchApplication.class, args);
        int exitCode = SpringApplication.exit(context);
        System.exit(exitCode);
    }

}
```