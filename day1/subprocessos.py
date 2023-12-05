import os
import time

def main():
    name = "bruno"  # stack

    pid_filho = os.fork()
    if pid_filho == 0:
        time.sleep(100)  # demora
        print("Processo filho", os.getpid(), name)
        os.execl("/bin/ls", "ls", "-la")
    else:
        print("Processo pai PID", os.getpid(), name)
        print("Meu filho é o", pid_filho)


if __name__ == "__main__":
    main()
