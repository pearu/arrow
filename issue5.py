import pyarrow as pa
import pyarrow.compute as pc

for value in ["2020-12-31 23:59:60", "2020-12-31 23:59:61"]:
    try:
        print(pc.strptime(pa.array([value]), format="%Y-%m-%d %H:%M:%S", unit="s")[0])
    except pa.ArrowInvalid as e:
        print(e)
