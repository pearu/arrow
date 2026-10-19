import pyarrow as pa
import pyarrow.compute as pc

for value, fmt in [
    ("15-Feb-2015", "%d-%b-%Y"),
    ("15 February 2015", "%d %B %Y"),
    ("Sun 15 Feb 2015", "%a %d %b %Y"),
    ("02/15/2015 02:30 PM", "%m/%d/%Y %I:%M %p"),
]:
    try:
        print(pc.strptime(pa.array([value]), format=fmt, unit="s")[0])
    except pa.ArrowInvalid as e:
        print(e)
