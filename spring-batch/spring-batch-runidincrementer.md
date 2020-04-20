# Spring Batch RunIdIncrementer

> 스프링 배치에서 동일한 파라미터로 잡을 새로 생성하고 싶을 경우에 사용한다.

## JobInstance

![job](https://docs.spring.io/spring-batch/4.0.x/reference/html/images/job-heirarchy.png)

    JobInstance = Job + JobParameter

파라미터가 달라야 인스턴스가 새로 생성된다. `RunIdIncrementer`를 사용하면 매번 실행 할 때 마다 run.id를 증가시킬 수 있다.

```java
@Bean
public Job sampleJob(JobBuilderFactory jobBuilderFactory, Step sampleStep) {
    return jobBuilderFactory.get("jobName").incrementer(new RunIdIncrementer()).start(sampleStep).build();
}
```

`BATCH_JOB_EXECUTION_PARAMS` 테이블에서 전달된 파라미터를 확인할 수 있다.

## 이전 파라미터를 읽어들이는 문제

[optional/omitted jobParameters are reloaded from previous jobs](https://github.com/codecentric/spring-boot-starter-batch-web/issues/38) 참조

`RunIdIncrementer`를 사용하면 이전 `run.id`를 읽어들이기 위해서 이전에 전달받은 JobParameters를 모두 다시 읽어들인다. 이를 해결하기 위해 다음과 같이 수정한 `RunIdIncrementer`를 사용한다.

```java
public class RunIdIncrementer implements JobParametersIncrementer {
    private static String RUN_ID_KEY = "run.id";
    private String key = RUN_ID_KEY;

    public void setKey(String key) {
        this.key = key;
    }

    public JobParameters getNext(JobParameters parameters) {
        JobParameters params = (parameters == null) ? new JobParameters() : parameters;
        long id = params.getLong(key, 0L) + 1;
        // return new JobParametersBuilder(params).addLong(key, id).toJobParameters();
        return new JobParametersBuilder().addLong(key, id).toJobParameters();
    }
}
```
