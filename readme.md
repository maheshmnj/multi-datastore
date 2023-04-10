### Delete all nodes

```bash
MATCH (n) DETACH DELETE n;
```

### Create nodes

```bash
CREATE (n:Person {name: 'John Doe', age: 33});
```

### Create nodes with labels

```bash
CREATE (n:Person:Developer {name: 'John Doe', age: 33});
```

/// Match nodes

```bash
MATCH (n) RETURN n;
```
