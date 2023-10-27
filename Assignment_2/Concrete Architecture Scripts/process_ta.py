import json
import argparse

def loadSubsystems(filename="system_structure.json"):
    with open(filename, "r") as f:
        return json.load(f)
    
def subsystemPatterns(subsystems):
    if 'children' not in subsystems:
        patterns = [subsystems['pattern'].replace('*', '')]
    else:
        patterns = []
        for child in subsystems['children']:
            patterns += subsystemPatterns(child)
    return patterns

def formatSubsystems(subsystems):
    formatted_subsystems = f"$INSTANCE {subsystems['name']} cSubSystem\n"
    if 'children' in subsystems:
        for child in subsystems['children']:
            formatted_subsystems += formatSubsystems(child)
    return formatted_subsystems

def filterAndFormatContent(content, subsystems):
    content_lines = content.replace('"', '').replace("\\", "/").split('\n')
    subsystem_patterns = subsystemPatterns(subsystems)
    return "\n".join([line for line in content_lines if len(line) >= 2 and any(pattern in line.split(" ")[1] for pattern in subsystem_patterns)])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate contain file for dependencies in .raw.ta file')
    parser.add_argument('ta_file', type=str, metavar='ta_file', help='The .raw.ta file to read dependencies from')
    args = parser.parse_args()
    ta_file = args.ta_file

    with open(ta_file, 'r') as file:
        content = file.read()

    subsystems = loadSubsystems()
    subsys_content = formatSubsystems(subsystems)
    modified_content = filterAndFormatContent(content, subsystems)
    
    modified_content = f"FACT TUPLE :\n{subsys_content}\n{modified_content}"
    
    with open(ta_file, 'w') as file:
        file.write(modified_content)