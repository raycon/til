# ForkJoinPool 사이즈 변경

CPU 1개인 인스턴스에서 스트림 병렬 처리를 확인하기 위해 사용한 코드.
스레드의 수를 프로세서 개수보다 많게 지정할 수 있다.
실제 환경에서는 성능 향상의 의미가 없을 것 같음.

```java
int processors = Runtime.getRuntime().availableProcessors();
System.out.println("Set forkJoinPoolSize to " + (processors * 2));
System.setProperty("java.util.concurrent.ForkJoinPool.common.parallelism", String.valueOf(processors * 2));
```