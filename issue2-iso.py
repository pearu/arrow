import pyarrow as pa
pa.array(["2021-02-30"]).cast(pa.timestamp("s"))
