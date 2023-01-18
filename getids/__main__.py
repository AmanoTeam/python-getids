import sys

from . import get_date_as_string

if len(sys.argv) <= 1:
    print(
        "You must specify the target IDs as arguments to get their creation dates.",
        file=sys.stderr,
    )
    sys.exit(1)
else:
    sys.argv.pop(0)
    for uid in sys.argv:
        print(f"{uid}:", " ".join(get_date_as_string(int(uid))))
