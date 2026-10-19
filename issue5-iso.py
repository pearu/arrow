import pyarrow as pa
pa.array(["2020-12-31 23:59:60"]).cast(pa.timestamp("s"))
