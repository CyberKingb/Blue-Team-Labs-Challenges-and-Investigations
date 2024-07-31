## Challenge Senario
You’re a senior cyber security engineer and during your shift, we have intercepted/noticed a high privilege actions from unknown source that could be identified as malicious. We have got you the ticket that made these actions.
You are the one who created the secret for these tickets. Please fix this and submit the low privilege ticket so we can make sure that you deserve this position.

### ***Here is the ticket:***

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiQlRMe180X0V5ZXN9IiwiaWF0Ijo5MDAwMDAwMCwibmFtZSI6IkdyZWF0RXhwIiwiYWRtaW4iOnRydWV9.jbkZHll_W17BOALT95JQ17glHBj9nY-oWhT1uiahtv8 

## Challenge Submission
### **1) Can you identify the name of the token? (Format: String) (2 points)**

From the ticket we can see that the text is in base 64 format.
So heading on to `cyberchef` I used the from Base 64 recepie and got the true output of the ticket, from the output i saw `JWT` which is short for JSON Web Token.

So the token name should be `JWT`

![cyberchef base 64 decoded](https://github.com/user-attachments/assets/8a9650cc-4a55-4e97-b5f9-e608efddb74d)

![Solved!](https://github.com/user-attachments/assets/8e6df22e-8cad-4e8f-9b25-4ea0189a145f)


### **#2) What is the structure of this token? (Format: Section.Section.Section) (2 points)**

The structure of a JSON Web Token is `header-token-signature`

![Solved!](https://github.com/user-attachments/assets/8e6df22e-8cad-4e8f-9b25-4ea0189a145f)


### **#3) What is the hint you found from this token? (Format: String) (2 points)**

From the cyberchef output in the second line there is `"flag":"BTL{_4_Eyes}"` which should be a hint since the question asked for a string our answer should be `_4_Eye`

![image](https://github.com/user-attachments/assets/c9215a0a-886d-4b2a-a45f-014268536b31)

![image](https://github.com/user-attachments/assets/c61c7afe-c9de-4725-a8c8-41202d85f4c3)


### **#4) What is the Secret? (Format: String) (2 points)**

To find the secret we need to crack the jwt token by bruteforcing it with hashcat.

For this we firstly copy the token and put it into a `.txt` file. I put mine into `secret.txt`.

![Saving the Token into a file](https://github.com/user-attachments/assets/935b10b3-9b6e-4924-bc37-dad965ce2bad)

Now on our command line `- hashcat secret.txt -m 16500 -a 3 ?a?a?a?a`


