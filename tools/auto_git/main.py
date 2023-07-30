import subprocess, sys, json

# ////////////////////

def run_git_command(command, data):
   try:
      result = subprocess.run(command, cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
      print(result.stdout.strip())
   except subprocess.CalledProcessError as e:
      print(f"Error executing command: {command}\n{e.stderr} --- Trying to solve...")
      if "CONFLICT (content): Merge conflict" in e.stdout:
         while True:
            try:
               print("riga 18")
               result = subprocess.run(["git", "merge", data["branch"]], cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
               print(f"riga 20 {result.stdout}")
               break
            except subprocess.CalledProcessError as e:
               print(f"riga 23 {e.stdout} ----- {e.stderr}")
               if "(MERGE_HEAD exists)" in e.stderr:
                  result = subprocess.run(["git", "commit", "-m", "test"], cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
                  break
      input()
      #sys.exit(1)

def main():
   with open("configuration.json", "r") as file:
      data = json.load(file)
   msg = input("Enter comment for commit: ")
   run_git_command(["git", "checkout", data["branch"]], data)
   run_git_command(["git", "add", "*"], data)
   run_git_command(["git", "commit", "-m", f"\"{msg}\""], data)
   run_git_command(["git", "push"], data)
   run_git_command(["git", "checkout", "develop"], data)
   run_git_command(["git", "merge", data["branch"]], data)
   run_git_command(["git", "push"], data)
   run_git_command(["git", "checkout", data["branch"]], data)
   run_git_command(["git", "merge", "develop"], data)
   run_git_command(["git", "push"], data)

# delta
# delta
# delta
# delta
# weeeeee

if __name__ == "__main__":
   main()