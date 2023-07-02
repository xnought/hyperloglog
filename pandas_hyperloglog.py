import pandas as pd
import duckdb


def hyperloglog(df, column: str):
    result = duckdb.query(
        f"""SELECT approx_count_distinct("{column}") as result FROM df"""
    ).df()["result"][0]
    return result


if __name__ == "__main__":
    df = pd.DataFrame({"a": [1, 2, 3, 4, 5]})
    print(hyperloglog(df, "a"))
