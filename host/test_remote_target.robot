*** Settings ***
# Resource gets us the remote libraries "target", "common" and "security"
Resource     %{MYPROJECT_HOME}/remote_libraries.txt


*** Variables ***
# Command line has precedence over the following. I assigned a static
# IP to my raspberry PI, so I can hardcode the value in here to save
# passing command line arguments
${server_uri}=      192.168.0.122
${start_port}=      8270


*** Test Cases ***
security test
    [Documentation]     Perform security_a test!
    ${out} =    security.security_a
    Should Be Equal As Strings    ${out}    security_a called!
    Log    ${out}

target test
    ${out} =    target.set_property     security    ON
    Should Be Equal As Strings    ${out}    Property security set to ON
    Log    ${out}

    ${out} =    target.target_op_pass_or_fail   ${TRUE}
    Should Be Equal As Strings    ${out}    target_op_pass_or_fail succeeded!
    Log    ${out}

target test 2
    [Documentation]     This test is meant to always fail. Skip it with pybot
    ...                 option "-e xfail"
    [Tags]              xfail
    target.target_op_pass_or_fail   ${FALSE}

common test
    ${out} =    common.feature_a
    Should Be Equal As Strings    ${out}    feature_a called!
    Log    ${out}

    ${out} =    common.feature_b
    Should Be Equal As Strings    ${out}    feature_b called!
    Log    ${out}

    ${out} =    common.common
    Should Be Equal As Strings    ${out}    common called!
    Log    ${out}

