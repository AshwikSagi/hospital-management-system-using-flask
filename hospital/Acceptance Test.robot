*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${username}       ashwik
${password}       ashwik
${pid}            123456789

*** Test Cases ***
test_login_logout
    Goto Login Page
    Sleep    2s
    Click Link    Logout
    Close Browser

test_view_patient
    Goto Login Page
    Click Link    Patient
    Click Link    view
    Set Selenium Speed    0.2s
    Click Link    Patient
    Click Link    view
    Sleep   0.5s
    Element Should Contain    id:tt    Patient SSN ID
    Sleep    1s
    Click Link    Logout
    Close Browser

test_update
    Goto Login Page
    Click Link    Patient
    Click Link    update
    Set Selenium Speed    0.2s
    Sleep    1s
    Click Link    Patient
    Click Link    update
    Input Text    name:pid    ${pid}
    Click Button    get
    Input Text    name:name    dummy name
    Execute Javascript    location.href = "#address"
    Input Text    name:address    Sainikpuri
    Execute Javascript    location.href = "#submit"
    Click Button    Update
    Click Link    Logout
    Close Browser

test_search_patient
    Goto Login Page
    Click Link    Patient
    Click Link    search
    Set Selenium Speed    0.2s
    Click Link    Patient
    Click Link    search
    Input Text    name:pid    ${pid}
    Click Button    get
    Sleep    1s
    Click Link    Logout
    Close Browser

test_pharmacy
    Goto Login Page
    Click Link    Pharmacy
    Click Link    Issue medicines to patient
    Set Selenium Speed    0.2s
    Click Link    Pharmacy
    Click Link    Issue medicines to patient
    Input Text    name:pid    ${pid}
    Click Button    get
    Sleep    0.5s
    Click Button    Issue Medicines
    Input Text    name:name    dolo
    Input Text    name:qty    5
    Click Button    Add medicine
    Execute Javascript    location.href = "#update"
    Click Button    Buy medicines
    Sleep    1s
    Close Browser

test_delete
    Goto Login Page
    Click Link    Patient
    Click Link    delete
    Set Selenium Speed    0.2s
    Sleep    1s
    Click Link    Patient
    Click Link    delete
    Input Text    name:pid    ${pid}
    Click Button    get
    Execute Javascript    location.href = "#submit"
    #Click Button    Delete
    Sleep    1s
    Close Browser

*** Keywords ***
Goto Login Page
    Open Browser    http://127.0.0.1:5000    chrome
    Maximize Browser Window
    Input Text    name:username    ${username}
    Input Text    name:password    ${password}
    Click Button    Login
    Title Should Be    Hospital Management
