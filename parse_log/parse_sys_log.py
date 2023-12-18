from subprocess import run, PIPE
import os


class UsersProcesses:

    def __init__(self):
        pass

    def analyze_logs(self, log_path):
        if os.path.isfile(log_path):
            run(["grep", "HTTP/1.1\" 200", log_path])
        elif os.path.isdir(log_path):
            run(["find", log_path, "-name", "*.txt", "-exec", "grep",
                 "HTTP/1.1\" 200", "{}", ";"])
