# @EnableBatchProcessing

스프링 배치에서 `@EnableBatchProcessing`을 사용하면 발생하는 일

`Autowired`에서 사용되는 빈이 생성된다.

- `JobRepository` - bean name "jobRepository"
- `JobLauncher` - bean name "jobLauncher"
- `JobRegistry` - bean name "jobRegistry"
- `PlatformTransactionManager` - bean name "transactionManager"
- `JobBuilderFactory` - bean name "jobBuilders"
- `StepBuilderFactory` - bean name "stepBuilders"

`StepScope`로 정의된 빈이 생성된다.

## 자동 시작

`@EnableBatchProcessing`을 설정하면 정의된 Job이 모두 실행된다. 이 동작을 변경하려면

- `spring.batch.job.enabled = false`로 설정하거나
- `spring.batch.job.names = ${job.name:NONE}`으로 설정한다.

## 커맨드 라인 실행

실행 매개변수로 `spring.batch.job.names`를 전달한다.

    java -jar app.jar --spring.batch.job.names=someJob

`spring.batch.job.enabled`를 `false`로 설정해 놓은 경우 이 값도 `true`로 전달해야 한다.

    java -jar app.jar --spring.batch.job.enabled=true --spring.batch.job.names=carrySong

이때 전달된 파라미터는 모두 `BATCH_JOB_EXECUTION_PARAMS`에 저장된다.

## REST 요청으로 실행

`spring.batch.job.enabled`를 `false`로 설정하고 `RequestMapping`을 정의한 뒤 `JobLauncher`로 `Job`을 실행한다.

```java
@Autowired
JobLauncher jobLauncher;

@Autowired
Job job;

@RequestMapping("/run")
public void handle() throws Exception{
    JobParameters jobParameters =
                    new JobParametersBuilder()
                    .addLong("time",System.currentTimeMillis())
                    .toJobParameters();
    jobLauncher.run(job, jobParameters);
}
```