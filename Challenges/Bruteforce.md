# Bruteforce (Can you analyze logs from an attempted RDP bruteforce attack?

[Link to Challenge](https://blueteamlabs.online/home/challenge/bruteforce-16629bf9a2)

## Tools Used 
- Grep, Text Editor, Excel

## Difficulty 
- Medium
  
## OS
- Windows/Linux

[Link to File](https://blueteamlabs.online/storage/files/00fd9853557296dd3312d4529c137f1cecb329d7.zip)

## Senario
- Can you analyze logs from an attempted RDP bruteforce attack?

- One of our system administrators identified a large number of Audit Failure events in the Windows Security Event log.

- There are a number of different ways to approach the analysis of these logs! Consider the suggested tools, but there are many others out there!

## **Questions and their Analysis**

### **Question 1: How many Audit Failure events are there? (Format: Count of Events) (3 points)**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/f56aa3a5-a55e-471a-a8ea-826bfc04cd21)

- I used the `Ctrl + F` command to find the number of **Audit Faliures** in the BTLO_Bruteforce_Challenge.csv file.
- It showed me that there are `3103` audit faliure events

<img width="651" alt="image" src="https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/a8323eeb-57aa-439a-aa15-67e875ff7a01">

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/a7efe880-ca4d-4cd4-a63d-de1ce353e0d4)


### **Question 2:  What is the username of the local account that is being targeted? (Format: Username) (2 points)**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/205568d6-1dc7-425d-8fb7-a44a11eda5be)

- Going through the BTLO_Bruteforce_Challenge.txt file I found that the account being targeted was the `administrator` account.

Account For Which Logon Failed:

Security ID:		NULL SID

`Account Name:		administrator`

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/948ce6c4-3c19-43eb-9d11-3eac23cb08c0)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/12229fed-4e02-4812-bb47-4203a2f47cd9)


### **Question 3: What is the failure reason related to the Audit Failure logs? (Format: String) (3 points)**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/fce50fcd-4e04-4046-b0d3-53daef39e6a6)

- Going through the **BTLO_Bruteforce_Challenge.txt** file i found that the failure reason was due to `Unknown username or bad password`

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/8538638d-6b29-4b6d-96d4-3339a41eca01)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/bccf0691-2ea1-4e5d-884e-cb49b88cf0b9)



### **Question 4: What is the Windows Event ID associated with these logon failures? (Format: ID) (3 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/3ae97d1c-1084-48c9-9e6d-f06556c80176)

- Going through the **BTLO_Bruteforce_Challenge.evtx** file I found the event ID for the security event was `4625`

  ![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/9e03c05c-ce1c-41c6-b578-5aab54b171c9)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/f00f72bf-a6d1-483c-82d3-c8f70bb9fa62)


### **Question 5: Question 5) What is the source IP conducting this attack? (Format: X.X.X.X)**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/bd1811df-ef15-4a2b-8665-dbb47b42f415)

- Going back to the **BTLO_Bruteforce_Challenge.txt** file in the network information section the source IP Address is `113.161.192.227`

<img width="434" alt="image" src="https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/b625d770-b6aa-42fc-8491-569ced269ec4">

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/69a2653e-dfb1-48ea-a9b5-414140eda058)


### **Question 6: What country is this IP address associated with? (Format: Country) (3 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/eda5c0f1-6f7b-4db7-b00b-865e6dea4dad)

- Navigating to (https://whatismyipaddress.com/ip-lookup) and pasting in the source IP Address `113.161.192.227`

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/cbb1a889-ce2b-4dbc-ace3-d41fe821ff0b)

- It brought out the information on the IP address including the country the IP address originates from which is `Vietnam`

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/d95175ca-e54e-4fc6-bb54-b86cb71fa900)


### **Question 7: What is the range of source ports that were used by the attacker to make these login requests?**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/a09432d6-ec0e-4f38-9774-bd0ccfd3c2c2)

- Using PowerShell I can find the lowest and highest port in the **BTLO_Bruteforce_Challenge.txt** file.

```powershell
# Read the content of the document
$content = Get-Content -Path "path\to\your\document.txt" -Raw

# Define the word you want to search for
$wordToSearch = "your_word_here"

# Use Select-String to find instances of the word
$matches = $content | Select-String -Pattern $wordToSearch -AllMatches | ForEach-Object { $_.Matches.Value }

# Convert the matches to numbers (assuming they are numerical values)
$numericValues = $matches | ForEach-Object { [double]$_ }

# Find the highest and lowest values
$highestValue = $numericValues | Measure-Object -Maximum | Select-Object -ExpandProperty Maximum
$lowestValue = $numericValues | Measure-Object -Minimum | Select-Object -ExpandProperty Minimum

```

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/e34cfa40-5d3d-4774-96b0-fd976d10aa88)
