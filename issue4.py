import pyarrow as pa
import pyarrow.compute as pc

for value in ["1584282600", "1000000000000000", "67768036000000000"]:
    result = pc.strptime(pa.array([value]), format="%s", unit="s")
    print(pc.strftime(result, format="%Y-%m-%d %H:%M:%S")[0])
