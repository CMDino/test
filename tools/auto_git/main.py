import subprocess, json, os

# AAAAAA

def is_vscode_running():
   for process in os.popen('tasklist').readlines():
      if 'code.exe' in process.lower():
         return True
   return False

def run_git_command(command, data, msg):
   try:
      result = subprocess.run(command, cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
      print(result.stdout.strip())
   except subprocess.CalledProcessError as e:
      print(f"Error executing command: {command}\n{e.stderr} --- Trying to solve...")
      if "CONFLICT (content): Merge conflict" in e.stdout:
         if not is_vscode_running():
            subprocess.run(["code"], shell=True)
         while True:
            try:
               result = subprocess.run(["git", "merge", data["branch"]], cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
               break
            except subprocess.CalledProcessError as e:
               if "(MERGE_HEAD exists)" in e.stderr:
                  result = subprocess.run(["git", "commit", "-m", f"\"{msg}\""], cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
                  break

def main():
   with open("configuration.json", "r") as file:
      data = json.load(file)
   msg = input("Enter comment for commit: ")
   run_git_command(["git", "checkout", data["branch"]], data, msg)
   run_git_command(["git", "add", "*"], data, msg)
   run_git_command(["git", "commit", "-m", f"\"{msg}\""], data, msg)
   run_git_command(["git", "push"], data, msg)
   run_git_command(["git", "checkout", "develop"], data, msg)
   run_git_command(["git", "merge", data["branch"]], data, msg)
   run_git_command(["git", "push"], data, msg)
   run_git_command(["git", "checkout", data["branch"]], data, msg)
   run_git_command(["git", "merge", "develop"], data, msg)
   run_git_command(["git", "push"], data, msg)

if __name__ == "__main__":
   main()