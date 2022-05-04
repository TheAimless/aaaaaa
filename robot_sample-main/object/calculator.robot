*** Settings ***
Resource        ..${/}resources${/}imports.robot

*** Variables ***
${number_1}         com.google.android.calculator:id/digit_1
${number_2}         com.google.android.calculator:id/digit_2
${number_3}         com.google.android.calculator:id/digit_3
${number_4}         com.google.android.calculator:id/digit_4
${number_5}         com.google.android.calculator:id/digit_5
${number_6}         com.google.android.calculator:id/digit_6
${number_7}         com.google.android.calculator:id/digit_7
${number_8}         com.google.android.calculator:id/digit_8
${number_9}         com.google.android.calculator:id/digit_9
${number_0}         com.google.android.calculator:id/digit_0
${multiply}         com.google.android.calculator:id/op_mul
${minus}            com.google.android.calculator:id/op_sub
${divide}           com.google.android.calculator:id/op_div
${plus}             com.google.android.calculator:id/op_add
${equal}            com.google.android.calculator:id/eq
${AC}               com.google.android.calculator:id/clr
${result}           com.google.android.calculator:id/result_final


*** Keywords ***
Input number
    [Arguments]    ${input_no}
    AppiumLibrary.click element             ${number_${input_no}}
#    AppiumLibrary.click element         ${AC}
#    FOR    ${i}    IN RANGE    9999999
#        ${input_no}=      evaluate    ${no}%10
#        AppiumLibrary.click element             ${number_${input_no}}
#        ${no}=      evaluate    ${no}/10
#        ${no}=      evaluate    "%.0f" % ${no}
#        EXIT FOR LOOP IF        "${no}"=="0"
#    END

Click multiply
    AppiumLibrary.click element             ${multiply}
Click divide
    AppiumLibrary.click element             ${divide}
Click minus
    AppiumLibrary.click element             ${minus}
Click plus
    AppiumLibrary.click element             ${plus}
Click equal
    AppiumLibrary.click element             ${equal}
Verify result
    [Arguments]    ${value}
    Element text should be      ${result}           ${value}