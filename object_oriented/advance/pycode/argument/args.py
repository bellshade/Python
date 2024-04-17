import sys
from getopt import getopt, GetoptError
from typing import List


try:
    argv: List[str] = sys.argv[1:]
    opts, args = getopt(argv, "c:", ["create="])

except GetoptError as e:
    raise e

for opt, arg in opts:
    if opt in ["-c", "--create"]:
        with open(arg, "w") as file:
            res = file.write("Berhasil membuat berkas dengan CLI...")
            file.close()
    else:
        ...
