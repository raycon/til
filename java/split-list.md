# 자바 리스트 나누는 코드 예제

```java
// 리스트를 N 개의 리스트로 나눈다
// 리스트에 포함되는 항목의 갯수가 변함
static <T> List<List<T>> convertToNList(List<T> list, int numberOfList) {
    int countPerList = 1;
    while (countPerList * numberOfList < list.size()) {
        countPerList++;
    }
    return convertToNContainingList(list, countPerList);
}

// 리스트를 N개의 항목을 갖는 리스트로 나눈다.
// 결과 리스트의 갯수가 변함
static <T> List<List<T>> convertToNContainingList(List<T> list, final int countPerList) {
    List<List<T>> result = new ArrayList<List<T>>();
    final int N = list.size();
    for (int i = 0; i < N; i += countPerList) {
        result.add(new ArrayList<T>(list.subList(i, Math.min(N, i + countPerList))));
    }
    return result;
}
```