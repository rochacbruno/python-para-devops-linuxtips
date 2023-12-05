import os

os.mkfifo("/tmp/pythonqueue", 0o600)

print("hello", file=open("/tmp/pythonqueue", "w"))
