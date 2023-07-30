import subprocess, sys, json

# ////////////////////

def run_git_command(command, data):
   try:
      result = subprocess.run(command, cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
      print(result.stdout.strip())
   except subprocess.CalledProcessError as e:
      if "Error executing command: ['git', 'merge'" in e.stderr:
         subprocess.run(["code"])
      print(f"Error executing command: {command}\n{e.stderr}")
      sys.exit(1)

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

# CIAO
# CIAO
# CIAO
# ////////////////////
# CIAO

if __name__ == "__main__":
   main()