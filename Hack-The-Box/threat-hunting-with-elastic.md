# Introduction to Threat Hunting & Hunting with Elastic

## Threat Hunting Fundamentals

### Threat Hunting Definition

The median duration between an actual security breach and its detection, otherwise termed "dwell time", is usually several weeks, if not months. This implies a potential adversarial presence within a network for a span approaching three weeks, a duration that can be significantly impactful.

Threat hunting is an active, human-led, and often hypothesis-driven practice that systematically combs through network data to identify stealthy, advanced threats that evade existing security solutions. 

This strategic evolution from a conventionally reactive posture allows us to uncover insidious threats that automated detection systems or external entities such as law enforcement might not discern.

The principal objective of threat hunting is to substantially reduce dwell time by recognizing malicious entities at the earliest stage of the cyber kill chain. This proactive stance has the potential to prevent threat actors from entrenching themselves deeply within our infrastructure and to swiftly neutralize them.

The threat hunting process commences with the identification of assets – systems or data – that could be high-value targets for threat actors. Next, we analyze the TTPs (Tactics, Techniques, and Procedures) these adversaries are likely to employ, based on current threat intelligence. We subsequently strive to proactively detect, isolate, and validate any artifacts related to the abovementioned TTPs and any anomalous activity that deviates from established baseline norms.

#### Key facets of Threat Hunting

* An offensive, proactive strategy that prioritizes threat anticipation over reaction, based on hypotheses, attacker TTPs, and intelligence.
* An offensive, reactive response that searches across the network for artifacts related to a verified incident, based on evidence and intelligence.
* A solid, practical comprehension of threat landscape, cyber threats, adversarial TTPs, and the cyber kill chain.
* Cognitive empathy with the attacker, fostering an understanding of the adversarial mindset.
* A profound knowledge of the organization's IT environment, network topology, digital assets, and normal activity.
* Utilization of high-fidelity data and tactical analytics, and leveraging advanced threat hunting tools and platforms.

How does threat hunting intersect with the various phases of Incident Handling?

* In the **Preparation** phase of incident handling, a threat hunting team must set up robust, clear rules of engagement. Operational protocols must be established, outlining:
    - when and how to intervene
    - the course of action in specific scenarios
  
Organizations may choose to weave threat hunting into their existing incident handling policies and procedures, obviating the need for separate threat hunting policies and procedures.

* During the **Detection & Analysis** phase of incident handling, a threat hunter’s acumen is indispensable. They can:
    - augment investigations
    - ascertain whether the observed _indicators of compromise_ (IoCs) truly signify an incident
    - further, their adversarial mindset can help uncover additional artifacts or IoCs that might have been missed initially.

* In the **Containment, Eradication, and Recovery** phase of incident handling, the role of a hunter can be diverse. Some organizations might expect hunters to perform tasks within:
    - the Containment
    - Eradication
    - Recovery stages
    
However, this is not a universally accepted practice. The specific roles and responsibilities of the hunting team will be stipulated in the procedural documents and security policies.

* Regarding the **Post-Incident Activity** phase of incident handling, hunters, with their extensive expertise spanning various IT domains and IT Security, can contribute significantly. They can proffer recommendations to fortify the organization's overall security posture.

### A Threat Hunting Team's Structure

* **Threat Hunter**: The core role within the team, threat hunters are cybersecurity professionals with a deep understanding of the threat landscape, cyber adversaries' Tactics, Techniques, and Procedures (TTPs), and sophisticated threat detection methodologies. They proactively search for Indicators of Compromise (IoCs) and are proficient in using a variety of threat hunting tools and platforms.

* **Threat Intelligence Analyst**: These individuals are responsible for gathering and analyzing data from a variety of sources, including open-source intelligence, dark web intelligence, industry reports, and threat feeds. Their job is to understand the current threat landscape and predict future trends, providing valuable insights to threat hunters.

* **Incident Responders**: When threat hunters identify potential threats, incident responders step in to manage the situation. They investigate the incident thoroughly and they are also responsible for containment, eradication, and recovery actions, and they ensure that the organization can quickly resume normal operations.

* **Forensics Experts**: These are the team members who delve deep into the technical details of an incident. They are proficient in digital forensics and incident response (DFIR), capable of analyzing malware, reverse engineering attacks, and providing detailed incident reports.

* **Data Analysts/Scientists**: They play a pivotal role in examining large datasets, using statistical models, machine learning algorithms, and data mining techniques to uncover patterns, correlations, and trends that can lead to actionable insights for threat hunters.

* **Security Engineers/Architects**: Security engineers are responsible for the overall design of the organization's security infrastructure. They ensure that all systems, applications, and networks are designed with security in mind, and they often work closely with threat hunters to implement tools and techniques that facilitate threat hunting, as well as kill-chain defenses.

* **Network Security Analyst**: These professionals specialize in network behavior and traffic patterns. They understand the normal ebb and flow of network activity and can quickly identify anomalies indicative of a potential security breach.

* **SOC Manager**: The Security Operations Center (SOC) manager oversees the operations of the threat hunting team, ensuring smooth coordination among team members and effective communication with the rest of the organization.

## When Should We Hunt?

* **When New Information on an Adversary or Vulnerability Comes to Light**: The cybersecurity landscape is always evolving, with fresh intel on potential threats and system vulnerabilities being uncovered regularly. If there's a newly discovered adversary or a vulnerability associated with an application that our network utilizes, this calls for an immediate threat hunting session. It's imperative to decipher the adversary's modus operandi and scrutinize the vulnerability to evaluate the possible risk to our systems. For instance, if we stumble upon a previously unknown vulnerability in a widely utilized application, we'd promptly kickstart a threat hunting initiative to seek out any signs of exploitation.

* **When New Indicators are Associated with a Known Adversary**: Often, cybersecurity intelligence sources release new Indicators of Compromise (IoCs) tied to specific adversaries. If these indicators are associated with an adversary known for targeting networks akin to ours or if we've been a past target of the same adversary, we need to launch a threat hunting initiative. This aids in detecting any traces of the adversary's activities within our system, allowing us to ward off potential breaches.
* **When Multiple Network Anomalies are Detected**: Network anomalies might sometimes be harmless, caused by system glitches or valid alterations. However, several anomalies appearing concurrently or within a short period might hint at a systemic issue or an orchestrated attack. In such cases, it's crucial to carry out threat hunting to pinpoint the root cause of these anomalies and address any possible threats. For instance, if we observe odd network traffic behavior or unexpected system activities, we'd initiate threat hunting to probe these anomalies.
* **During an Incident Response Activity**: Upon the detection of a confirmed security incident, our Incident Response (IR) team will concentrate on containment, eradication, and recovery. Yet, while the IR process is in motion, it's vital to simultaneously conduct threat hunting across the network. This enables us to expose any connected threats that might not be readily visible, understand the full extent of the compromise, and avert further harm. For example, during a confirmed malware infiltration, while the IR team is dealing with the infected system, threat hunting can assist in identifying other potentially compromised systems.
* **Periodic Proactive Actions**: Beyond the scenarios mentioned above, it's crucial to note that threat hunting should not be simply a reactive task. Regular, proactive threat hunting exercises are key to discovering latent threats that may have slipped past our security defenses. This guarantees a continual monitoring strategy, bolstering our overall security stance and minimizing the prospective impact of an attack.

### The Relationship Between Risk Assessment & Threat Hunting

Risk assessment, as an essential facet of cybersecurity, enables a comprehensive understanding of the potential vulnerabilities and threat vectors within an organization. In the context of threat hunting, risk assessment serves as a key enabler, allowing us to prioritize our hunting activities and focus our efforts on the areas of greatest potential impact.

* **Prioritizing Hunting Efforts**: By recognizing the most critical assets (often referred to as 'crown jewels') and their associated risks, we can prioritize our threat hunting efforts on these areas. Assets could include sensitive data repositories, mission-critical applications, or key network infrastructure.
* **Understanding Threat Landscape**: The threat identification step of the risk assessment allows us to understand the threat landscape better, including the Tactics, Techniques, and Procedures (TTPs) used by potential threat actors. This understanding assists us in developing our hunting hypotheses, which are essential for proactive threat hunting.
* **Highlighting Vulnerabilities**: Risk assessment helps to highlight vulnerabilities in our systems, applications, and processes. Knowing these weaknesses enables us to look for exploitation indicators in these areas. For instance, if we know a particular application has a vulnerability that allows for privilege escalation, we can look for anomalies in user privilege levels.
* **Informing the Use of Threat Intelligence**: Threat intelligence is often used in threat hunting to identify patterns of malicious behavior. Risk assessment helps inform the application of threat intelligence by identifying the most likely threat actors and their preferred methods of attack.
* **Refining Incident Response Plans**: Risk assessment also plays a critical role in refining Incident Response (IR) plans. Understanding the likely risks helps us anticipate and plan for potential breaches, ensuring a swift and effective response.
* **Enhancing Cybersecurity Controls**: Lastly, the risk mitigation strategies derived from risk assessment can directly feed into enhancing existing cybersecurity controls and defenses, further strengthening the organization’s security posture.

## The Threat Hunting Process

**Setting the Stage**: The initial phase is all about planning and preparation. It includes
    
* laying out clear targets based on a deep understanding of the threat landscape
* our business's critical requirements
* threat intelligence insights.

### Example Summary

During the planning and preparation phase, a threat hunting team might conduct in-depth research on the latest threat intelligence reports, analyze industry-specific vulnerabilities, and study the tactics, techniques, and procedures (TTPs) employed by threat actors. They may also identify critical assets and systems within the organization that are most likely to be targeted. As part of the preparation, extensive logging mechanisms can be implemented across servers, network devices, and endpoints to capture relevant data for analysis. Threat hunting tools like SIEM, EDR, and IDS are configured to collect and correlate logs, generate alerts, and provide visibility into potential security incidents. Additionally, the team stays updated on emerging cyber threats by monitoring threat feeds, subscribing to relevant security mailing lists, and participating in information sharing communities.


### Formulating Hypothesis

The next step involves making educated predictions that will guide our threat hunting journey. These hypotheses can stem from various sources, like recent threat intelligence, industry updates, alerts from security tools, or even our professional intuition. We strive to make these hypotheses testable to guide us where to search and what to look for.


### Example Hypothesis

A hypothesis might be that an attacker has gained access to the network by exploiting a particular vulnerability or through phishing emails. This hypothesis could be derived from recent threat intelligence reports that highlight similar attack vectors. It could also be based on an alert triggered by an intrusion detection system indicating suspicious network traffic patterns. The hypothesis should be specific and testable, such as "An advanced persistent threat (APT) group is leveraging a known vulnerability in the organization's web server to establish a command-and-control (C2) channel."

### Data Gathering and Examination

This phase is where the active threat hunt occurs. It involves collecting necessary data, such as log files, network traffic data, endpoint data, and then analyzing this data using the predetermined methodologies and tools. Our goal is to find evidence that either supports or refutes our initial hypothesis. This phase is highly iterative, possibly involving refinement of the hypothesis or the investigation approach as we uncover new information.

### Example Data Gathering and Examination

The threat hunting team might examine web server access logs to identify unusual or unauthorized access patterns, analyze network traffic captures to detect suspicious communications with external domains, or investigate endpoint logs to identify anomalous behavior or signs of compromise. They apply data analysis techniques such as statistical analysis, behavioral analysis, or signature-based detection to identify potential threats. They might employ tools like log analyzers, packet analyzers, or malware sandboxes to extract information from the collected data and uncover hidden indicators of compromise.

### Evaluating Findings and Testing Hypotheses

After analyzing the data, we need to interpret the results. This could involve confirming or disproving the hypothesis, understanding the behavior of any detected threats, identifying affected systems, or determining the potential impact of the threat. This phase is crucial, as it will inform the next steps in terms of response and remediation.

### Example Evaluating Findings and Testing Hypotheses

The threat hunting team might discover a series of failed login attempts from an IP address associated with a known threat actor, confirming the hypothesis of an attempted credential brute-force attack. They might also find evidence of suspicious outbound network connections to known malicious domains, supporting the hypothesis of a command-and-control (C2) communication channel. The team conducts deeper investigations to understand the behavior of the identified threats, assess the scope of the compromise, and determine the potential impact on the organization's systems and data.

### Mitigating Threats

If we confirm a threat, we must undertake remediation actions. This could involve:

*  isolating affected systems
* eliminating malware
* patching vulnerabilities
* modifying configurations. 

Our goal is to:

* eradicate the threat
* limit any potential damage.

### Example Mitigating Threats

If the threat hunting team identifies a compromised system communicating with a C2 server, they may isolate the affected system from the network to prevent further data exfiltration or damage. They may deploy endpoint protection tools to remove malware or perform forensic analysis on the compromised system to gather additional evidence and determine the extent of the breach. Vulnerabilities identified during the threat hunting process can be patched or mitigated to prevent future attacks. Network configurations can be adjusted to restrict unauthorized access or to strengthen security controls.

### After the Hunt

Once the threat hunting cycle concludes, it's crucial to document and share the findings, methods, and outcomes. This might involve updating threat intelligence platforms, enhancing detection rules, refining incident response playbooks, or improving security policies. It's also vital to learn from each threat hunting mission to enhance future efforts.


### Example 'After the Hunt'

Once the threat hunting cycle concludes, the team documents the findings, methodologies, and outcomes of the investigation. They update threat intelligence platforms with newly discovered indicators of compromise (IoCs) and share relevant information with other teams or external partners to enhance the collective defense against threats. They may improve detection rules within security tools based on the observed attack patterns and refine incident response playbooks to streamline future incident handling. Lessons learned from the hunt are incorporated into security policies and procedures, and training programs are adjusted to enhance the organization's overall security posture.

### Continuous Learning and Enhancement

Threat hunting is not a one-time task, but a continuous process of learning and refinement. Each threat hunting cycle should feed into the next, allowing for continuous improvement of hypotheses, methodologies, and tools based on the evolving threat landscape and the organization's changing risk profile.

### Example Continuous Learning and Enhancement

After each threat hunting cycle, the team reviews the effectiveness of their hypotheses, methodologies, and tools. They analyze the results and adjust their approach based on lessons learned and new threat intelligence. For example, they might enhance their hunting techniques by incorporating machine learning algorithms or behavioral analytics to detect more sophisticated threats. They participate in industry conferences, attend training sessions, and collaborate with other threat hunting teams to stay updated on the latest attack techniques and defensive strategies.

## The Threat Hunting Process VS Emotet

[Emotet Malware](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-280a)

**Setting the Stage**: During the planning and preparation phase, the threat hunting team extensively researches the Emotet malware's tactics, techniques, and procedures (TTPs) by studying previous attack campaigns, analyzing malware samples, and reviewing threat intelligence reports specific to Emotet. They gain a deep understanding of Emotet's infection vectors, such as malicious email attachments or links, and the exploitation of vulnerabilities in software or operating systems. The team identifies critical assets and systems that are commonly targeted by Emotet, such as endpoints with administrative privileges or email servers.

**Formulating Hypotheses**: Hypotheses in the context of Emotet threat hunting might be based on known Emotet IoCs or patterns observed in previous attacks. For example, a hypothesis could be that Emotet is using a new phishing technique to distribute malicious payloads via compromised email accounts. This hypothesis could be derived from recent threat intelligence reports highlighting similar Emotet campaigns or based on alerts triggered by email security systems detecting suspicious email attachments. The hypothesis should be specific, such as "Emotet is using compromised email accounts to send phishing emails with malicious Word documents containing macros."

**Designing the Hunt**: In the design phase, the threat hunting team determines the relevant data sources and collection methods to validate or invalidate the Emotet-related hypotheses. They may decide to analyze email server logs, network traffic logs, endpoint logs, or sandboxed malware samples. They define search queries, filters, and correlation rules to extract information related to Emotet's specific characteristics, such as email subject lines, attachment types, or network communication patterns associated with Emotet infections. They leverage threat intelligence feeds to identify Emotet-related IoCs, such as known command-and-control (C2) server addresses or file hashes associated with Emotet payloads.

**Data Gathering and Examination**: During the active threat hunting phase, the team collects and analyzes data from various sources to detect Emotet-related activities. For example, they might examine email server logs to identify patterns of suspicious email attachments or analyze network traffic captures to detect communication with known Emotet C2 servers. They apply data analysis techniques, such as email header analysis, network traffic pattern analysis, or behavioral analysis, to identify potential Emotet infections. They utilize tools like email forensics software, network packet analyzers, or sandbox environments to extract relevant information from the collected data and uncover hidden indicators of Emotet activity.

**Evaluating Findings and Testing Hypotheses**: In this phase, the team evaluates the findings from data analysis to confirm or refute the initial Emotet-related hypotheses. For example, they might discover a series of emails with similar subject lines and attachment types associated with Emotet campaigns, confirming the hypothesis of ongoing Emotet phishing activities. They might also find evidence of network connections to known Emotet C2 servers, supporting the hypothesis of an active Emotet infection. The team conducts deeper investigations to understand the behavior of the identified Emotet infections, assess the scope of the compromise, and determine the potential impact on the organization's systems and data.

**Mitigating Threats**: If Emotet infections are confirmed, the team takes immediate remediation actions. They isolate affected systems from the network to prevent further spread of the malware and potential data exfiltration. They deploy endpoint protection tools to detect and remove Emotet malware from compromised systems. Additionally, they analyze compromised email accounts to identify and remove unauthorized access. They patch or mitigate vulnerabilities exploited by Emotet to prevent future infections. Network configurations are adjusted to block communication with known Emotet C2 servers or malicious domains.

**After the Hunt**: Once the Emotet threat hunting cycle concludes, the team documents their findings, methodologies, and outcomes. They update threat intelligence platforms with new Emotet-related IoCs and share relevant information with other teams or external partners to enhance their collective defense against Emotet. They improve detection rules within security tools based on the observed Emotet attack patterns and refine incident response playbooks to streamline future incident handling. Lessons learned from the Emotet hunt are incorporated into security policies and procedures, and training programs are adjusted to enhance the organization's overall defenses against Emotet and similar malware.

**Continuous Learning and Enhancement**: Threat hunting for Emotet is an ongoing process that requires continuous learning and improvement. After each Emotet threat hunting cycle, the team reviews the effectiveness of their hypotheses, methodologies, and tools. They analyze the results and adjust their approach based on lessons learned and new Emotet-related threat intelligence. For example, they might enhance their hunting techniques by incorporating advanced behavior-based detection mechanisms or machine learning algorithms specifically designed to identify Emotet's evolving TTPs. They actively participate in industry conferences, attend training sessions, and collaborate with other threat hunting teams to stay updated on the latest Emotet attack techniques and defensive strategies.

---

↩️: [Home](../../index.md)
