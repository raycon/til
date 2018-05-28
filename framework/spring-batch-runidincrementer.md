# RunIdIncrementer 정의

참고 : <https://github.com/codecentric/spring-boot-starter-batch-web/issues/38>

동일한 배치 작업을 반복할 때 `org.springframework.batch.core.launch.support.RunIdIncrementer`를 사용하면 이전에 전달된 파라미터가 다시 사용된다. 이를 막기 위해 다음과 같이 `RunIdIncrementer`를 정의해서 사용한다.

```java
public class RunIdIncrementer implements JobParametersIncrementer {

  private static String RUN_ID_KEY = "run.id";

  private String key = RUN_ID_KEY;

  /**
    * The name of the run id in the job parameters.  Defaults to "run.id".
    *
    * @param key the key to set
    */
  public void setKey(String key) {
    this.key = key;
  }

  /**
    * Increment the run.id parameter (starting with 1).
    */
  @Override
  public JobParameters getNext(JobParameters parameters) {

    JobParameters params = (parameters == null) ? new JobParameters() : parameters;

    long id = params.getLong(key, 0L) + 1;
    //return new JobParametersBuilder(params).addLong(key, id).toJobParameters();
    return new JobParametersBuilder().addLong(key, id).toJobParameters();
  }

}
```