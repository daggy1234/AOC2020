import os
import subprocess

def read_output(stream,callback):
  mstr = ""
  for line in iter(stream.readline,b''):
    mstr += line.decode()
  return mstr

if __name__ == "__main__":
  print("Building Outupt.........")
  for item in os.listdir("."):
    if not "." in item:
      for file in os.listdir(item):
        res = subprocess.Popen(["/bin/bash","-c",f"cd {item} && cargo build"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  print("Starting RUn")

  for item in os.listdir("."):
    if not "." in item:
      for file in os.listdir(item):
        if file.endswith(".py"):
          print(f'{33*"="} PROBLEM {item.upper()} {33*"="}')

          print("PYTHON:")
          sequence = ["/bin/bash","-c",f"cd {item} && python {file}"]
          process = subprocess.Popen(sequence, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          res = read_output(process.stdout,process.stderr)
          print(res)
        elif file.endswith(".rs"):
          print("RUST:")
          sequence = ["/bin/bash","-c",f"cd {item} && cargo run"]
          process = subprocess.Popen(sequence, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
          res = read_output(process.stdout,process.stderr)
          print(res)
  print(100 * "=")