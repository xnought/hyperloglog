# hyperloglog

HyperLogLog algorithm from scratch. Count the cardinality of an array with with basically no memory usage.

You could get perfect count, but it takes a lot of memory (hashmap).

```python
from hyperloglog import hyperloglog

estimated_num_elements = hyperloglog(array)
```

Check out the [`example.ipynb`](example.ipynb) for a real example on a 100 million elements array with around 10 million unique elements.

## Todo

- [ ] implement in faster language
- [ ] have more max_leading_zeros than just 1
- [ ] implement distributed/parallel version
- [ ] improve hash function
