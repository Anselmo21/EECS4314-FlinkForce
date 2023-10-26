import json
import argparse

def load_subsystems(filename="subsystems.json"):
    with open(filename, "r") as f:
        return json.load(f)

def format_subsystems(subsystems):
    return "\n".join([f"$INSTANCE {instance} cSubSystem" for instance in subsystems.values()])

def filter_and_format_content(content, subsystems):
    content_lines = content.replace('"', '').replace("\\", "/").split('\n')
    return "\n".join([line for line in content_lines if any(pattern in line for pattern in subsystems.keys())])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate contain file for dependencies in .raw.ta file')
    parser.add_argument('ta_file', type=str, metavar='ta_file', help='The .raw.ta file to read dependencies from')
    args = parser.parse_args()
    ta_file = args.ta_file

    with open(ta_file, 'r') as file:
        content = file.read()

    subsystems = load_subsystems()
    subsys_content = format_subsystems(subsystems)
    modified_content = filter_and_format_content(content, subsystems)
    
    modified_content = f"FACT TUPLE :\n{subsys_content}\n{modified_content}"
    
    with open(ta_file, 'w') as file:
        file.write(modified_content)