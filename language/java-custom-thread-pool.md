# Custom Thread Pool

자바의 `parallelStream()`을 사용해서 병렬 처리를 할 경우 스레드는 `availableProcessors`보다 1개 적은 숫자로 생성된다. 스레드 수를 지정하려면 `ForkJoinPool`을 써서 아래와 같이 작성한다.

```java
ForkJoinPool forkJoinPool = new ForkJoinPool(2);
forkJoinPool.submit(() ->
    //parallel task here, for example
    IntStream.range(1, 1_000_000).parallel().filter(PrimesPrint::isPrime).collect(toList())
).get();
```

참고:

- <https://stackoverflow.com/questions/21163108/custom-thread-pool-in-java-8-parallel-stream>