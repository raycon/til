# Spring Batch Reader With Job Parameters

스프링 배치에서 잡 파라미터 사용하는 방법.

- 빈을 `@StepScope`로 등록한다.
- `@Value("#{jobParameters[parameterName]}")`으로 값을 주입받는다.
- `:parameterName` 으로 쿼리를 지정한다.
- 맵으로 값을 전달한다.

## jobParameters

```java
@Bean
@StepScope
public JpaPagingItemReader<User> reader(@Value("#{jobParameters[name]}") String name) {
  Map<String, Object> params = new HashMap<>();
  params.put("name", name);

  JpaPagingItemReader<User> reader = new JpaPagingItemReader<>();
  reader.setQueryString("select u from User u where u.name=:name");
  reader.setParameterValues(params);
  ...
}
```

## stepExecution

```java
    @StepScope
    public JpaPagingItemReader<Employee> taxCalculatorItemReader(@Value("#{stepExecution}") StepExecution stepExecution) {
        JpaPagingItemReader<Employee> employeeItemReader = new JpaPagingItemReader<>();
        employeeItemReader.setEntityManagerFactory(persistenceConfig.entityManagerFactory());
        employeeItemReader.setQueryString(TaxCalculation.GET_UNPROCESSED_EMPLOYEES_BY_YEAR_AND_MONTH_QUERY_SLAVE);
        Map<String, Object> parameters = new HashMap<>();
        parameters.put("year", stepExecution.getJobParameters().getLong("year").intValue());
        parameters.put("month", stepExecution.getJobParameters().getLong("month").intValue());
        parameters.put("jobExecutionId", stepExecution.getJobExecutionId());
        parameters.put("minId", stepExecution.getExecutionContext().getLong("minValue"));
        parameters.put("maxId", stepExecution.getExecutionContext().getLong("maxValue"));
        employeeItemReader.setParameterValues(parameters);
        return employeeItemReader;
    }
```

- <https://github.com/cegeka/batchers/blob/master/taxcalculator/taxcalculator-batch/src/main/java/be/cegeka/batchers/taxcalculator/batch/config/remotepartitioning/ItemReaderWriterConfig.java>
- <https://blog.codecentric.de/en/2013/06/spring-batch-2-2-javaconfig-part-2-jobparameters-executioncontext-and-stepscope/>
- <http://jojoldu.tistory.com/132>