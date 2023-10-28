import subprocess
import os
import glob
import shutil

# cleanup
patterns = ['*.raw.ta', '*.con.ta', '*.ls.ta', '*.contain']

for pattern in patterns:
    files_to_delete = glob.glob(pattern)
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f'Successfully deleted {file}')
        except Exception as e:
            print(f'Error while deleting {file}: {e}')

# copy in the raw.ta
shutil.copy2("./source/dependencies.raw.ta", "./flink_UnderstandFileDependency.raw.ta")  

# generate contain
subprocess.run(["python", "gen_contain.py", "flink_UnderstandFileDependency.raw.ta"])

# process ta
subprocess.run(["python", "process_ta.py", "flink_UnderstandFileDependency.raw.ta"])

# createContainment.bat
result = subprocess.run(["createContainment.bat"], shell=True, text=True, capture_output=True)
print(f"Create Containment Output:\n{result.stdout}\n")
print(f"Create Containment Errors:\n{result.stderr}\n")

# runLSEdit.bat
result = subprocess.run(["runLSEdit.bat"], shell=True, text=True)