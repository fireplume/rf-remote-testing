At work, we've been using remote robot framework libraries to test our targets. I've never really known
how it was working, so I thought I'd figure it out by myself by creating a template framework from
which anybody could easily create a remote testing environment.

Thanks to https://github.com/robotframework/PythonRemoteServer for the example and remote server library.

I've tested this project on a Linux virtual machine running on Windows as the host and a Raspberry PI 3
running Ubuntu Mate as the target.

SETUP and RUNNING

- Make sure your target has the 'daemon' utility. On Ubuntu: sudo apt-get install daemon

- Target must be setup to run an SSH server and accept ssh connections (https://help.ubuntu.com/community/SSH/OpenSSH/Configuring)

- Set up your target with password less SSH login so you can run something like: 'ssh -X someuser@xxx.xxx.xxx.xxx ls' without having
to enter a password manually (http://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login).

- Clone the project both on your host and target (git clone git@github.com:fireplume/rf-remote-testing.git)

- Run setup.sh on the host and give it as parameter the path to the 'target' directory in which
are located 'server.py' and libraries on the target device (it's under the cloned project's root directory).

- Figure out the IP address of your target

- Edit the 'run' file and set the following fields:
    uname:plume                     Replace 'plume' with the username to ssh to your target
    -v server_uri:192.168.0.122     Replace '192.168.0.122' with your target's IP address
    -v start_port:8270              Replace '8270' with the starting port index range you want to assign to the
                                    remote library servers.

- Run with:
    . run

- or manually with something like:
    pybot -d results -v uname:plume -v server_uri:192.168.0.122 -v start_port:8270 host

