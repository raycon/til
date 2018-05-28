# ObjectValidation

`@NotNull`, `@Min`, `@Max` 같은 제한사항을 사용했을 때, violation을 검출하는 방법

```java
ValidatorFactory factory = Validation.buildDefaultValidatorFactory();
Validator validator = factory.getValidator();
Set<ConstraintViolation<User>> violations = validator.validate(user);
for (ConstraintViolation<User> violation : violations) {
    System.out.println(violation);
}
```