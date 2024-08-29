# Custom email API calls with the Editor
The following is an example of how to inject custom code into the IEF-Editor generated policies.
This is specifically an example for a rest api call to send an email OTP
1. Build the policy 
2. Identify the parts of the flowchart where injection is necessary
3. In the Editor, add and rename the nodes to represent the place where your custom code will go. Make sure they have a unique name; this is so the parts of the policy are named consistently by the generation step.
In our case, we will name the send email node "Send_Email_OTP_SignIn"
4. Now, identify the parts of the generated XML that need to be overwritten
In this example, we find the TechnicalProfile "Send_Email_OTP_SignIn" which sends the REST-API request and the ClaimsTransformation "Send_Email_OTP_SignIn_BuildRequestBody" which builds the JSON body for the request.
5. Add the injected code to the Relying Party file. In our case, this is called "B2C_1A_SignInSignUp.xml", make sure to name it exactly as it appears in the base policy.
The injected code will be run instead of the in the base policy file.

## Note: 
This example uses policy inheritance where a base policy's elements are overwritten by a child policy. If there are multiple child policies, only the children in the subtree will be effected.

## Relevent docs: 
- This is the documenations for the JSON transformation: https://learn.microsoft.com/en-us/azure/active-directory-b2c/json-transformations