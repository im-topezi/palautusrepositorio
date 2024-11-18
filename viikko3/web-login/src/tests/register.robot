*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go to Register Page

*** VARIABLES ***
${good_username}    jali
${bad_username}    uh
${good_password}    kahdeksan8
${short_password}    ysi
${bad_password}    kahdeksan

*** Test Cases ***

Register With Valid Username And Password
    Register With Username And Password  ${good_username}  ${good_password}  ${good_password}
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Register With Username And Password  ${bad_username}  ${good_password}  ${good_password}
    Register Page Should Be Open
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Register With Username And Password  ${good_username}  ${short_password}  ${short_password}
    Register Page Should Be Open
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Register With Username And Password  ${good_username}  ${bad_password}  ${bad_password}
    Register Page Should Be Open
    Register Should Fail With Message  Password can not contain only letters

Register With Nonmatching Password And Password Confirmation
    Register With Username And Password  ${good_username}  ${bad_password}  ${good_password}
    Register Page Should Be Open
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Register With Username And Password  kalle  kalle987  kalle987
    Register Page Should Be Open
    Register Should Fail With Message  User with username kalle already exists

Login After Successful Registration

    Register With Username And Password  ${good_username}  ${good_password}  ${good_password}
    click link  ohtu
    click button  Logout
    Login Page Should Be Open
    Set Username  ${good_username}
    Set Password  ${good_password}
    click button  Login
    Main Page Should Be Open



Login After Failed Registration
    Register With Username And Password  ${bad_username}  ${good_password}  ${good_password}
    click link  Login
    Set Username  ${good_username}
    Set Password  ${good_password}
    click button  Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}


Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
    
Reset Application Create User And Go to Register Page
    Reset Application
    Create User  kalle  kalle123
    Go to Register Page

Register With Username And Password
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Go to Register Page
    Set Username  ${username}
    Set Password  ${password}
    Confirm Password  ${password_confirmation}
    Click Button  Register


