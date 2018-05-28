# Batch chunk size

[Spring Batch Javaconfig - parameterize commit-interval aka chunksize
](https://stackoverflow.com/questions/24373110/spring-batch-javaconfig-parameterize-commit-interval-aka-chunksize)

Batch 에서 Job을 구성할 때 `chunkSize`를 `jobParameter`로부터 입력 받기 위해서는 `Step` bean 을 `@JobScope`로 선언해야 한다.

```java
@Bean
@JobScope
public Step step(@Value("#{jobParameters['chunkSize']}") Integer chunkSize) {
  ...
}
```