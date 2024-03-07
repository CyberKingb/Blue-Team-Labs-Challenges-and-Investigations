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

## Questions and their Analysis

**Question 1: How many Audit Failure events are there? (Format: Count of Events) (3 points)**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/f56aa3a5-a55e-471a-a8ea-826bfc04cd21)

- I used the **Ctrl + F** command to find the number of **Audit Faliures** in the BTLO_Bruteforce_Challenge.csv file.
- It showed me that there are **3103** audit faliure events

<img width="651" alt="image" src="https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/a8323eeb-57aa-439a-aa15-67e875ff7a01">

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/a7efe880-ca4d-4cd4-a63d-de1ce353e0d4)


**Question 2:  What is the username of the local account that is being targeted? (Format: Username) (2 points)**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/205568d6-1dc7-425d-8fb7-a44a11eda5be)

- Going through the BTLO_Bruteforce_Challenge.txt file i found that the 

Account For Which Logon Failed:
Security ID:		NULL SID
**Account Name:		administrator**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/948ce6c4-3c19-43eb-9d11-3eac23cb08c0)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/12229fed-4e02-4812-bb47-4203a2f47cd9)

