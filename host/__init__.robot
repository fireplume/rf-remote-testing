##################################################################################
*** Settings ***
Library         Process    WITH NAME   PROC
Documentation   This init file is used to start and stop the remote library servers.
Suite Setup     Start remote servers
Suite Teardown  Stop remote servers

##################################################################################
*** Variables ***

# Command line variables have precedence over file variables. I assigned a static
# IP to my raspberry PI, so I can hardcode the value in here to save
# passing command line arguments. A much better alternative than hard coding
# such values would be to have a utility which can get the IP address
# of your target automatically and pass it on the command line.

# Target IP address:
${server_uri}=     192.168.0.122

# Port range starting index to assign to remote libraries.
${start_port}=     8270

# Username configured for ssh on remote target
${uname}=          plume

# If you have installed the remote libraries elsewhere on your target, adjust
# the following variable accordingly (ex: /home/test_account/github/rf-remote-testing/target).
${REMOTE_ROOT_PROJECT}=     REMOTE_PROJECT_PATH_TAG

##################################################################################
*** Keywords ***

start remote servers
    PROC.Start process     ssh  -X  ${uname}@${server_uri}  daemon python ${REMOTE_ROOT_PROJECT}/server.py start ${server_uri} ${start_port}
    Sleep   10

stop remote servers
    PROC.Terminate All Processes
    PROC.Run process       ssh  -X  ${uname}@${server_uri}  daemon python ${REMOTE_ROOT_PROJECT}/server.py stop ${server_uri} ${start_port}

