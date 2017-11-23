# Handling soft deletes

- `@SQLDelete`를 사용하는 방법
- Custom Repository를 정의해서 사용하는 방법

## CustomRepository

> [Customize the base repository](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.customize-base-repository)를 참고해서 CustomRepository를 구현한다.

`@MappedSuperclass`를 사용해서 모든 Entity가 상속받아 사용할 부모 클래스를 정의한다.

```java
@MappedSuperclass
public class BaseEntity {
    @Basic
    @Column(name = "deleted")
    private Boolean deleted;
    ...
}
```

`SimpleJpaRepository`를 상속받은 Repository를 정의한다. `delete` 메소드를 재정의해서 삭제시에 `deleted`값을 `true`로 설정한다.

```java
public class CustomRepositoryImpl<T extends BaseEntity, ID extends Serializable>
        extends SimpleJpaRepository<T, ID> {

    public CustomRepositoryImpl(JpaEntityInformation<T, ?> entityInformation, EntityManager entityManager) {
        super(entityInformation, entityManager);
    }

    @Override
    @Transactional
    public void delete(T entity) {
        Assert.notNull(entity, "The entity must not be null!");
        entity.setDeleted(true);
    }
}
```

어플리케이션 설정에서 `@EnableJpaRepositories`에 생성한 Repository를 지정한다.

```java
@SpringBootApplication
@EnableJpaRepositories(repositoryBaseClass=CustomRepositoryImpl.class)
public class MyApplication {
  ...
}
```

`@OneToMany`나 `@ManyToOne` 사용시에 `@Where` 어노테이션을 추가해서 삭제되지 않은 Entity만 조회할 수 있다.

```java
@Where(clause = "deleted = false")
@OneToMany(mappedBy = "team")
List<User> users;
```

### CustomRepository 단점

- 조회시 `deleted`가 `true`인 데이터도 함께 조회된다. [Query Method](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.query-methods)를 사용하거나 [Customizing Indivisual repositories](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.single-repository-behavior)를 사용해서 필터링 할 수 있다.
- `cascade`, `orphanRemoval = true`를 사용할 경우 **레코드가 실제로 삭제되므로 사용할 수 없다.**

## SQLDelete

- `@SQLDelete` : Entity가 삭제시 사용되는 쿼리. `delete` 대신 `update`를 사용해서 `deleted`를 설정한다.

```java
@Entity
@Table(name = "user")
@SQLDelete(sql = "UPDATE user SET deleted = true WHERE id = ?")
public class UserEntity {
    @Id
    @Column(name = "id")
    private String id;
    @Column(name = "deleted")
    private Boolean deleted;
    @ManyToOne()
    @JoinColumn(name = "team_id", referencedColumnName = "id")
    private Team team;
    ...
}
```

**주의** : Entity 클래스에 `@Where(clause = "deleted = false")`를 사용할 경우 insert 할 때 키 중복 에러가 발생하면서 입력되지 않는다.

### SQLDelete - Cascade 적용

- `@Where` 조건을 사용해서 리스트 조회시 삭제되지 않은 Entity 만 조회한다. (UserEntity 클래스에 선언된 조건과는 별도로 선언이 필요하다.)
- `cascade = CascadeType.ALL`을 지정해서 team이 삭제되면 리스트의 user도 한다.
- `orphanRemoval = true`로 지정해서 리스트에서 삭제된 user를 삭제한다.

```java
@Entity
@Table(name = "team")
@SQLDelete(sql = "UPDATE team SET deleted = true WHERE id = ?")
public class TeamEntity {
    @Id
    @Column(name = "id")
    private String id;

    @Column(name = "deleted")
    private Boolean deleted;

    @Where(clause = "deleted = false")
    @OneToMany(mappedBy = "team", cascade = CascadeType.ALL, orphanRemoval = true)
    List<User> users;
}
```

**주의** : `@OneToOne` 관계에서는 `@Where` 조건이 적용되지 않는다.

### SQLDelete - 단점

- 모든 Entity 클래스에 `@SQLDelete`를 지정해주어야한다.
- 조회시 `deleted`가 `true`인 데이터도 함께 조회된다.