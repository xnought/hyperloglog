# hyperloglog

HyperLogLog algorithm from scratch. Count the cardinality of an array with with basically no memory usage.

You could get perfect count, but it takes a lot of memory (hashmap). Instead, leverage statistics with hyperloglog.

```python
from hyperloglog import hyperloglog

estimated_num_elements = hyperloglog(array)
```

Check out the [`example.ipynb`](example.ipynb) for a real example on a 100 million elements array with around 10 million unique elements.

Or check out the [`pandas_example.ipynb`](pandas_example.ipynb) for the pandas example that uses the `approx_count_distinct` [DuckDB](https://duckdb.org/) function under the hood (a superior implementation to mine).
