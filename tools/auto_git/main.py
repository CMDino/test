import subprocess, sys, json

# ////////////////////

def run_git_command(command, data):
   try:
      result = subprocess.run(command, cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
      print(result.stdout.strip())
   except subprocess.CalledProcessError as e:
      if "CONFLICT (content): Merge conflict" in e.stdout:
         openVSCode = False
         if openVSCode == False:
            # subprocess.run(["code"], shell=True)
            openVSCode = True
         while True:
            try:
               print("riga 18")
               result = subprocess.run(["git", "merge", data["branch"]], cwd=data["path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
               print(f"riga 20 {result.stdout}")
               break
            except subprocess.CalledProcessError as e:
               print(f"riga 23 {e.stdout}")
               pass
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

# PRRROVVVA
# CIAOOOOOOOOOOA
# CIIIIAAAAAAOOOO
# CIAIAOIAOAIOIAOA
# CIAIAOIAOAIOIAOA

if __name__ == "__main__":
   main()