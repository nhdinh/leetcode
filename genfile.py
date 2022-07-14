import sys
from pathlib import Path
import re

if __name__ == '__main__':
    sol_name = sys.argv[1]
    
    filename = sol_name.lower().strip()
    x = re.sub("[^0-9a-z]", "_", filename)
    while "__" in x:
        x = x.replace("__", "_")

    fh = Path(f"{x}.py")
    fh.touch(exist_ok=True)
    f = open(fh, 'w')
    f.write(f"# {sol_name}\n")
    f.close()