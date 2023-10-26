import argparse
import json

def loadSubsystems() -> dict:
    with open("system_structure.json", "r") as f:
        return json.load(f)
    
def buildDependencies(ta_file: str) -> list:
    # read ta_file dependencies
    dependencies = []
    with open(ta_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            type, from_file, _ = line.split()
            # only care about instance dependencies
            if type == "$INSTANCE":
                dependencies.append(from_file.strip("\"").replace("\"", ""))
    return dependencies

def matchSubsystem(dependency, subsystems):
    match = None
    
    # Check if current subsystem has children, if so go through them to leafs and check for matches bottom up
    if 'children' in subsystems:
        for child in subsystems['children']:
            match = matchSubsystem(dependency, child)
            if match:
                break
    
    # If no match was found in the children, or there are no children, 
    # try to match the current subsystem pattern
    if not match and dependency.startswith(subsystems['pattern'].replace('*', '')):
        match = subsystems['name']
    
    return match

def printContainment(dependencies: list, contain_file: str, subsystems: dict):
    with open(contain_file, "w") as out:
        for d in dependencies:
            ss = matchSubsystem(d, subsystems)
            if ss:
                out.write(f"contain {ss} {d}\n")

if __name__ == "__main__":
    # get ta file
    parser = argparse.ArgumentParser(description='Generate contain file for dependencies in .raw.ta file')
    parser.add_argument('ta_file', type=str, metavar='ta_file', help='The .raw.ta file to read dependencies from')
    args = parser.parse_args()

    # specify output
    ta_file = args.ta_file
    contain_file = ta_file.replace(".raw.ta", ".contain")

    subsystems = loadSubsystems()
    dependencies = buildDependencies(ta_file)
    printContainment(dependencies, contain_file, subsystems)
