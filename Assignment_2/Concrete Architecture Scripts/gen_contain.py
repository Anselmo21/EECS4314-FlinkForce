import argparse
import json

def loadSubsystems() -> dict:
    with open("subsystems.json", "r") as f:
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

def printContainment(dependencies: list, contain_file: str, subsystems: dict):
    with open(contain_file, "w") as out:
        [out.write(f"contain {sys} {d}\n") 
         for d in dependencies 
         for pattern, sys in subsystems.items() if pattern in d]

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