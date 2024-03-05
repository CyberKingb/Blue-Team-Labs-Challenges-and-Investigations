# Scenario

You are working in a newly established SOC where there is still a lot of work to do to make it fully functional. As part of gathering intelligence, you have been assigned a task to study a threat report released in 2022 and suggest some useful outcomes for your SOC.

[Link for Report File](https://blueteamlabs.online/storage/files/8c4cbf1af327dca7176473fa355e2dc29cfc527b.zip)

# Challenge Submission
## _Question 1):_  
Name the supply chain attack related to Java logging library in the end of 2021 (Format: AttackNickname) (1 points)

![image](https://imgur.com/iY6Gv6m.png)

- After Going through the report, I found the name of the supply chain attack related to Java logging library in the end of 2021 was Log4j

![](https://imgur.com/LWame50.png)

- Inputting it into the answer box its correct

![](https://imgur.com/iuhzCgA.png)

## _Question 2):_
Mention the MITRE Technique ID which affected more than 50% of the customers (Format: TXXXX) (1 points)

- Looking through the Techniques Section of the report I found that the Command and Scripting Interpreter Technique with **[MITRE ID T1059]** had 53.4% of customers affected

<img width="557" alt="Screenshot 2024-03-03 235529" src="https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/bfc7d267-f1a9-4c89-9bd6-4b92f173b3e6">

![image](https://imgur.com/Z5kalCK.png)

## _Question 3)_
Submit the names of 2 vulnerabilities belonging to Exchange Servers (Format: VulnNickname, VulnNickname) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/d0706b5b-bb86-43a9-8827-7185c9556462)

- According to the report **[ProxyLogon and ProxyShell]** targeted Microsoft Exchange servers and affected a massive number of systems, sometimes leading to ransomware deployment.

![Screenshot 2024-03-04 091242](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/44c4120e-208c-44c9-af5b-d032c0660003)

![Screenshot 2024-03-04 091549](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/cba81367-8318-498a-bf9e-3f11932432c4)

## _Question 4)_ 
Submit the CVE of the zero-day vulnerability of a driver which led to RCE and gain SYSTEM privileges (Format: CVE-XXXX-XXXXX) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/10773aaf-b2ac-47d9-be50-69ce72021f03)

- According to the Report On July 1, security researchers and Microsoft released details of a )-Day vulnerability dubbed “PrintNightmare” with (CVE-2021-34527). PrintNightmare permits an unprivileged user to remotely obtain elevated privileges on any system running the print spooler service, which is enabled by default. It abuses  a vulnerability in how the print spooler service fails to properly authenticate  users attempting to load a printer driver dynamic link library (DLL).

![Screenshot 2024-03-04 093840](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/21d8205f-afed-40f1-8282-aeb156fd068e)

![Screenshot 2024-03-04 094116](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/8f5d8fc3-0a4e-4fb2-8f6a-65997a137232)

## _Question 5)_
Mention the 2 adversary groups that leverage SEO to gain initial access (Format: Group1, Group2) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/ababb772-cf35-4ba3-9487-04b6493936d6)

According to the report Adversaries behind both **_Gootkit and Yellow Cockatoo_** abuse search engine 
optimization (SEO) to display malicious content at the top of a victim’s search results. Because compromised websites are displayed prominently and presented to the victim from a trusted search engine, victims are often easily “lured” to these sites. They are then prompted to download malicious content masquerading as legitimate content. For example, if a user searched for “this is my query,” the binary they downloaded would be named **this-is-my-query.exe**. Because the file looks familiar, users are less likely to scrutinize it closely or look for red flags. 

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/d8cc52ef-2f6b-4a29-9bfd-ae44ee2f5e0f)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/c119e83a-e631-421d-aacc-c02fc62f473b)


## _Question 6)_ 
In the detection rule, what should be mentioned as parent process if we are looking for execution of malicious js files [Hint: Not CMD] (Format: ParentProcessName.exe) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/650d113f-692f-4c66-a3a1-308aafd30a4e)

- The parent process was **wscript.exe**
```cmd
process == wscript.exe
&&
command_line_includes ( .zip && .js )
&&
has_external_netconn
```

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/83ecb861-5210-4d74-ae7a-f583d959fdc6)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/5f6d09a2-10f8-4c2e-a9f9-bfaf9f3e6e14)

## _Question 7)_ 
Ransomware gangs started using affiliate model to gain initial access. Name the precursors used by affiliates of Conti ransomware group (Format: Affiliate1, Affiliate2, Afilliate3) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/82dd038e-381e-40b9-8fac-943b465b1bfc)

- The precursors used by the affiliates of Conti were **_Qbot, Bazar and IcedID_**

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/c69f9864-b553-4845-a3b4-e90fc8c8dd94)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/a77a4519-166f-45c4-96fb-a351524d4227)


## _Question 8)_ 
The main target of coin miners was outdated software. Mention the 2 outdated software mentioned in the report (Format: Software1, Software2) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/061e1b8a-eef3-40fa-b5d3-81d2da4d3e80)

- The best defense against many of the coin miner compromises observed was patch management. Many of the coinminers seen exploited flaws in outdated applications like **_JBoss and WebLogic_**, so keeping systems updated will deter adversaries who are simply scanning for applications with known vulnerabilities. 


![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/48b878fd-466d-4c9c-9d51-6ddc78096fa7)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/2c9b709e-fe9d-4934-8235-d23cb1d59090)


## _Question 9)_ 
Name the ransomware group which threatened to conduct DDoS if they didn't pay ransom (Format: GroupName) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/926f16a3-eb59-419b-90df-87bc120ca37f)

- According to the report the adversary group **_Fancy Lazarus_** threatened to conduct DDoc if they didn't pay ransom

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/eaa76c6c-858a-4e71-a140-0cd0d7a8437f)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/4a97588a-ec96-47af-93cf-4f92e6bea285)


## _Question 10)_
What is the security measure we need to enable for RDP connections in order to safeguard from ransomware attacks? (Format: XXX) (1 points)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/9afe0baf-f621-4153-9282-d3630ce1c74e)

- The Security Measure needed to enable RDP connections to safeguard from ransomware attacks is Multi-Factor Authentication (MFA)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/2c041fbd-ed56-40fe-aec8-1c70a72f8a26)

![image](https://github.com/CyberKingb/Blue-Team-Labs-Challenges-and-Investigations/assets/161872623/4f41c900-69dd-4d71-b4fa-c5278138bed9)



And that is the end of my analysis of The Report
I hope it has an enlightening analysis 
Don't Forget to Connect With me on LinkedIn And Twitter
