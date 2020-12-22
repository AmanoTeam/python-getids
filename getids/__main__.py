import sys
from . import get_age

if len(sys.argv) <= 1:
    print("You must specify the target IDs as argument to get their creation dates.", file=sys.stderr)
    sys.exit(1)
else:
    sys.argv.pop(0)
    for uid in sys.argv:
        print(f"{uid}:", " ".join(get_age(int(uid))))