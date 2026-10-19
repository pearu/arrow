import platform
import sys

import pyarrow as pa
import pyarrow.compute as pc

print(sys.version.split()[0], platform.platform(), "pyarrow", pa.__version__)

CASES = [
    # (item, value, format)
    ("1 %b", "15-Feb-2015", "%d-%b-%Y"),
    ("1 %B", "15 February 2015", "%d %B %Y"),
    ("1 %a", "Sun 15 Feb 2015", "%a %d %b %Y"),
    ("1 %p", "02/15/2015 02:30 PM", "%m/%d/%Y %I:%M %p"),
    ("2 Feb 30", "2021-02-30", "%Y-%m-%d"),
    ("2 Apr 31", "2021-04-31", "%Y-%m-%d"),
    ("3 day 00", "2021-02-00", "%Y-%m-%d"),
    ("4 %s ok", "1584282600", "%s"),
    ("4 %s wrap", "1000000000000000", "%s"),
    ("4 %s int overflow", "67768036000000000", "%s"),
    ("5 sec 60", "2020-12-31 23:59:60", "%Y-%m-%d %H:%M:%S"),
    ("5 sec 61", "2020-12-31 23:59:61", "%Y-%m-%d %H:%M:%S"),
]

for item, value, fmt in CASES:
    try:
        result = pc.strptime(pa.array([value]), format=fmt, unit="s")
        # strftime, not as_py(): datetime cannot hold years outside 1..9999
        out = pc.strftime(result, format="%Y-%m-%d %H:%M:%S")[0].as_py()
    except Exception as e:
        out = f"{type(e).__name__}: {e}"
    print(f"{item:18} {value!r:24} {fmt!r:22} -> {out}")
