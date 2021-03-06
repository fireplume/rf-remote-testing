# Robot Framework remote target testing using remote libraries

A template framework from which anybody could easily create a remote testing environment. This project is about launching a test suite on the host which will start a remote library server on the target, connect to it and run library keywords on the target. The Robot Framework keywords allow, amongst other things, to execute binaries directly on the target.

Thanks to https://github.com/robotframework/PythonRemoteServer for the example and remote server library.

I've tested this project on a Linux virtual machine running on Windows as the host and a Raspberry PI 3
running Ubuntu Mate as the target.

## Inspiration
Some time ago, at work, we had to test remote targets, cell phones. We opted for Robot Framework. I was not personally involved in the setup of that environment, but I was curious to see if I could reproduce it on my own, which is what this project is about. It allows to run tests locally on the target from a remote host and to generate a detailed report of the outcome. For more information on Robot Framework, see http://robotframework.org/.

__!!! Don't pull releases v1.0 and v1.1 as they are broken !!!__

## SETUP

- Install Robot Framework and the PythonRemoteServer on your host (http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#installation-instructions, https://github.com/robotframework/PythonRemoteServer)

- Make sure your target has the 'daemon' utility. On Ubuntu: sudo apt-get install daemon

- Target must be setup to run an SSH server and accept ssh connections (https://help.ubuntu.com/community/SSH/OpenSSH/Configuring)

- Set up your target with password less SSH login so you can run something like: 'ssh -X someuser@xxx.xxx.xxx.xxx ls' without having
to enter a password manually (http://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login).

- Clone the project both on your host and target (git clone git@github.com:fireplume/rf-remote-testing.git)

- Run setup.sh on the host and give it as parameter the path to the 'target' directory in which
are located 'server.py' and libraries on the target device (it's under the cloned project's root directory).

- Figure out the IP address of your target

- Edit the 'run' file and set the following fields:
    - uname:plume                  Replace 'plume' with the username to ssh to your target
    - server_uri:192.168.0.122     Replace '192.168.0.122' with your target's IP address
    - start_port:8270              Replace '8270' with the starting port index range you want to assign to the
                                   remote library servers.

## RUNNING
- In the host project's root directory, run with one of:
    - . run
    - pybot -d results -v uname:plume -v server_uri:192.168.0.122 -v start_port:8270 host # adapt to your environment

## TINKERING WITH THE LIBRARIES
If you want to add, remove or modify the libraries, inspect and modify the following files:
- Library management:
    - target/server.py
    - host/remote_libraries.txt
    - host/set_remote_lib_uris.py
- The test itself:
    - host/test_remote_target.robot
- Current libraries:
    - target/{common_services.py,security_services.py,target.py}
