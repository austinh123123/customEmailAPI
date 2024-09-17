## Notes
1. You must inject custom_code.xml into B2C_1A_SignInSignUp here: 
```xml
<TechnicalProfile Id="PolicyProfile">
    <DisplayName>Policy Profile</DisplayName>
    <Protocol Name="SAML2" />
    <!-- Code goes here -->
    <OutputClaims>
```
2. You must register a saml application in your tenant to use this policy
https://learn.microsoft.com/en-us/azure/active-directory-b2c/saml-service-provider?tabs=windows&pivots=b2c-custom-policy

3. The run now link will be:
https://gpdevb2c.b2clogin.com/gpdevb2c.onmicrosoft.com/B2C_1A_SignInSignUp/generic/login?EntityId=https://azureadb2ctests.onmicrosoft.com/samlAPPUITest