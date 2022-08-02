import sys
from pathlib import Path
import re

cmt_marks = {
    "py": "#",
    "java": "//",
    "c": "//",
    "c++": "//",
}

if __name__ == '__main__':
    sol_name = sys.argv[1]

    extension = "py"
    if len(sys.argv) > 2:        
        extension = sys.argv[2]
    
    filename = sol_name.lower().strip()
    x = re.sub("[^0-9a-z]", "_", filename)
    while "__" in x:
        x = x.replace("__", "_")

    fh = Path(f"{x}.{extension}")
    fh.touch(exist_ok=True)
    f = open(fh, 'w')

    comment_mark = cmt_marks.get(extension, "//")
    f.write(f"{comment_mark} {sol_name}\n")
    f.close()