##################################################################################
*** Settings ***
Library         Process    WITH NAME   PROC
Documentation   This init file is used to start and stop the remote library servers.
Suite Setup     Start remote servers
Suite Teardown  Stop remote servers


##################################################################################
*** Variables ***

# If you have installed the remote libraries elsewhere on your target, adjust
# the following variable accordingly.
${REMOTE_ROOT_PROJECT}=     /opt/robot/my-project

# Command line has precedence over the following. I assigned a static
# IP to my raspberry PI, so I can hardcode the value in here to save
# passing command line arguments.
${server_uri}=              192.168.0.122
${start_port}=              8270


##################################################################################
*** Keywords ***

start remote servers
    PROC.Start process     ssh  -X  ${uname}@${server_uri}  daemon python ${REMOTE_ROOT_PROJECT}/server.py start
    Sleep   10

stop remote servers
    PROC.Terminate All Processes
    PROC.Run process       ssh  -X  ${uname}@${server_uri}  daemon python ${REMOTE_ROOT_PROJECT}/server.py stop

