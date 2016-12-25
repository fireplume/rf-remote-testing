import os 
import sys
import argparse
import importlib
import subprocess
import shlex

from robotremoteserver import RobotRemoteServer

# Inspiration:
#   - https://github.com/robotframework/PythonRemoteServer/blob/master/src/robotremoteserver.py
#   - http://www.diveintopython.net/functional_programming/dynamic_import.html

# Add new libraries to this list. Note that they must be listed in the same order as
# in "set_remote_lib_uris.py" since the port is assigned incrementally depending on
# that ordering. So target will be assigned the first port and so on.
REMOTE_LIB_LIST = ["target", "common_services", "security_services"]

# If you have reserved IP address and port for your target, you 
# can override these, otherwise, use the command line options.
PORT            = 8270
SERVER_IP       = '192.168.0.122'

def parse_cmd_line():
    parser = argparse.ArgumentParser(description="Utility to start RobotRemoteServers for myproject")

    parser.add_argument('op',         choices=['start', 'stop', 'test'], help="Start, stop or test for servers running.")
    parser.add_argument('server_ip',  nargs='?', default=SERVER_IP,      help="Server IP address")
    parser.add_argument('start_port', nargs='?', default=PORT,           help="Starting port to listent to, defaults to %d" % PORT)

    args = parser.parse_args()

    return args

if __name__ == "__main__":

    args    = parse_cmd_line()

    current_port = args.start_port

    for library in REMOTE_LIB_LIST:
        uri = "%s:%d" % (args.server_ip, current_port)

        if args.op == "start":
            module  = importlib.import_module(library)
            class_  = getattr(module, library)
            # Each server must be spawn in its own process, hence the fork
            pid     = os.fork()

            if pid == 0:
                try:
                    RobotRemoteServer(class_(), host=args.server_ip, port=current_port)
                except Exception as e:
                    print("Failed to start %s or address already in use." % library)
                sys.exit(0)

        elif args.op == "stop":
            p = subprocess.Popen(shlex.split("python -m robotremoteserver stop %s" % uri), stderr=subprocess.STDOUT)
            p.communicate()

        elif args.op == "test":
            p = subprocess.Popen(shlex.split("python -m robotremoteserver test %s" % uri), stderr=subprocess.STDOUT)
            p.communicate()

        current_port += 1
