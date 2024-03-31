Explain operators in Fast Expression used on WorldQuantBrain platform.

**SOME NOTES ARE ONLY APPLICABLE ON THE worldquantbrain platform**
### Notes copied from https://platform.worldquantbrain.com/learn/data-and-operators/operators:

1. All operator calls are to be made using the following order of arguments:

    - Required amount of data fields
    - Group (optional)
    - Lookback days (optional)
    - Keyword arguments (optional)
        - In the “Operator” column, they are shown as   `key=default_value`.
        - They are passed in the form `key=value`.
        - Keyword argument may be omitted, in this case its default value will be passed to operator.

    - Examples:
        - `ts_delta(close, 21)`
        - `ts_regression(close, ts_step(1), 21, lag = 63, rettype = 1)`
        - `ts_regression(close, ts_step(1), 21)`
            - same as `ts_regression(close, ts_step(1), 21, lag=0, rettype=0)`
        - `ts_covariance(close, vwap, 20)`
        - `group_rank(close, industry)`
        - `group_backfill(sales / assets, subindustry, 252, std = 3)`

2. Variable assignment is possible in the following form:

    `a = sales / assets; ts_delta(a, 252)`

    Variable re-assignment is not permitted.

3. Underscores in operator names can be omitted for ease of typing.