# @Value

기본값 `""`:

    @Value("${some.property:}")
    private String value;

기본값 `null` :

    @Value("${some.property:#{null}}")
    private String value;
