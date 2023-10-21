import subprocess
import sys
import locale
from typing import Optional


def run(
    no: int,
    encoding: Optional[str],
    input: str,
    options: list[str] = [],
) -> None:
    print(no)
    cmd = [sys.executable, "-I"] + options + ["-"]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            input=input,
            check=True,
            text=True,
            encoding=encoding,
        )
        print("stdout:")
        print(proc.stdout)
    except Exception:
        print("exc_info:")
        print(sys.exc_info()[1])


print(f"{locale.getencoding()=}")
run(1, None, 'print("a")')  # OK
run(2, None, 'print("中")')  # NG
run(3, "utf-8", 'print("中")')  # NG
run(4, "utf-8", 'print("中")', options=["-X", "utf8"])  # OK
