import pyarrow as pa
import pyarrow.compute as pc

for value in ["2021-02-30", "2021-04-31", "2021-02-00"]:
    try:
        print(pc.strptime(pa.array([value]), format="%Y-%m-%d", unit="s")[0])
    except pa.ArrowInvalid as e:
        print(e)
