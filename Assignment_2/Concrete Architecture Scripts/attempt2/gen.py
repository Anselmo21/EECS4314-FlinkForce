import os
import re

# Read ta_dependency_file dependencies
sep = os.sep
ta_file = "fd.raw.ta"
contain_file = "fd.contain"
dependencies = []
with open(ta_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        type, from_file, _ = line.split()
        # We only care about the concrete files
        if type == "$INSTANCE":
            dependencies.append(from_file.strip("\""))

with open(contain_file, "w") as out:

    for d in dependencies:
        expl = d.split(sep)
        directory = sep.join(expl[:-1])
        out.write(f"contain {directory} {d}\n")