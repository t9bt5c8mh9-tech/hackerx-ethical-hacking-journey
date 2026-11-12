# Updated Defensive Methods for Every Course Topic

This guide maps all 22 topics in the repository’s course overview to current defensive learning goals and authoritative references. It is curriculum content—not an executable hacking agent. Activities use synthetic records, fictional organizations, static reports, or purpose-built local training targets. Do not test real systems or collect real user data.

> **Keeping this guide current:** Standards and vendor guidance change. Check the linked official source for its latest version before teaching or applying a recommendation. This guide was prepared on 2026-11-12; links are reference starting points, not a claim that every document was revalidated on that date.

## Safety boundaries for the AI tutor

- Use fictional/synthetic data or an intentionally prepared local lab only.
- No real Wi-Fi capture or password cracking, credential collection, phishing, keylogging, fraud, denial-of-service traffic, or scanning of public systems.
- No general shell, arbitrary code execution, host-file access, secrets, or unrestricted network access.
- Show the proposed lesson action and expected scope; require learner approval for any lab operation; log activity and provide stop/reset.
- Teach dual-use topics through prevention, detection, incident response, and harmless simulations.
- Treat model output as untrusted; validate facts against linked primary sources and never let generated text override the lab boundaries.

## Topic-by-topic lessons and current defensive practice

| # | README topic | Updated defensive learning objective and safe exercise | Primary references |
|---|---|---|---|
| 1 | Know the OS | Use a fictional asset/configuration inventory to practice supported-version inventory, timely security updates, least privilege, secure configuration, disk protection, and recovery planning. | [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) |
| 2 | Hack the MAC | Explain MAC addresses, local-network scope, and address randomization/privacy limits. Classify fabricated addresses and review defensive device inventory; do not spoof or impersonate a real device. | [Apple: Use private Wi-Fi addresses](https://support.apple.com/en-us/102509); [Android: MAC randomization](https://source.android.com/docs/core/connect/wifi-mac-randomization) |
| 3 | Information Gathering | Analyze a fictional organization’s synthetic records. Minimize collection, distinguish facts from guesses, protect personal information, document authorization and scope, and redact sensitive findings. | [NIST Privacy Framework](https://www.nist.gov/privacy-framework); [NIST SP 800-122](https://csrc.nist.gov/pubs/sp/800/122/final) |
| 4 | Leveraging AI for Hacking | Use AI for defensive summarization of fabricated alerts and reports. Verify claims, identify hallucinations, protect sensitive inputs, maintain human review, and assess AI risks before deployment. | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework); [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) |
| 5 | Prompt Guide for Hacking | Practice bounded prompts for defensive tasks. Use inert examples to identify prompt injection and data leakage; keep untrusted content separate from instructions and require validation before tool use. | [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) |
| 6 | Hiding Messages | Explain steganography and its legitimate/privacy context using a provided toy artifact and a conceptual detection exercise. Do not hide malware, credentials, or harmful payloads or teach evasion. | [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework); [CISA Secure Our World](https://www.cisa.gov/secure-our-world) |
| 7 | Surfing Anonymously | Teach browser privacy, tracker reduction, safe updates, HTTPS limitations, and realistic anonymity expectations with a fictional settings checklist. Do not frame privacy tools as a way to conceal abuse. | [EFF: Cover Your Tracks](https://coveryourtracks.eff.org/); [CISA Secure Our World](https://www.cisa.gov/secure-our-world) |
| 8 | Social Media Hacking | Recognize account takeover and social-engineering indicators in fictional messages; practice MFA/passkeys where available, recovery hygiene, privacy settings, reporting, and account recovery. No impersonation or phishing. | [CISA: Secure Our World](https://www.cisa.gov/secure-our-world); [NIST Digital Identity Guidelines](https://pages.nist.gov/800-63-4/) |
| 9 | Credit & Debit Card Frauds | Use synthetic transaction alerts to learn fraud indicators, payment-data minimization, account notifications, safe reporting, and response. Never generate or test usable payment details. | [PCI Security Standards Council](https://www.pcisecuritystandards.org/standards/); [FTC: Identity theft](https://www.identitytheft.gov/) |
| 10 | Keyboard Spying | Review a static, fabricated endpoint alert and learn prevention/detection: trusted software, patching, endpoint protection, least privilege, and incident response. Do not capture keystrokes or create a keylogger. | [CISA: Malware, Phishing, and Ransomware](https://www.cisa.gov/topics/cyber-threats-and-advisories/malware); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) |
| 11 | WiFi Hacking (WEP Cracking) | Use a fictional router profile to explain why WEP is obsolete. Recommend retiring legacy equipment and using modern supported Wi-Fi security; no radio capture or cracking. | [CISA: Securing Wireless Networks](https://www.cisa.gov/resources-tools/resources/securing-wireless-networks); [Wi-Fi Alliance: Wi-Fi security](https://www.wi-fi.org/discover-wi-fi/security) |
| 12 | WiFi Hacking (WPA/WPA2 Cracking) | Analyze a synthetic configuration checklist: prefer WPA3 where supported (or WPA2-AES when necessary), strong unique passphrases, current firmware, disabled WPS when not needed, guest-network separation, and router admin protection. Simulate risk scoring only; no handshake capture or password attacks. | [CISA: Securing Wireless Networks](https://www.cisa.gov/resources-tools/resources/securing-wireless-networks); [Wi-Fi Alliance: Wi-Fi security](https://www.wi-fi.org/discover-wi-fi/security) |
| 13 | Network Spying | Interpret fabricated flow summaries to identify unusual access patterns and discuss segmentation, encryption, monitoring, retention limits, and privacy. No live packet capture or interception. | [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework); [CIS Critical Security Controls](https://www.cisecurity.org/controls) |
| 14 | Database Hacking | Use a toy schema and fictional rows to practice least-privilege accounts, parameterized queries, safe error handling, patching, encryption, backup/restore, and audit review. No access to real databases. | [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html); [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) |
| 15 | Android Hacking | Inspect a fictional app permission manifest and identify excessive permissions, outdated dependencies, unsafe data handling, and missing updates. Recommend supported OS versions, minimal permissions, and verified app sources; no device compromise. | [Android Security](https://source.android.com/docs/security); [OWASP MASVS](https://mas.owasp.org/MASVS/) |
| 16 | Bringing Down a Website (DDoS Concepts) | Study a precomputed fictional traffic graph and tabletop outage. Practice capacity planning, provider coordination, rate limiting, resilient architecture, communications, and incident response. Generate no traffic and do not load-test a live service. | [CISA: Understanding and Responding to DDoS Attacks](https://www.cisa.gov/news-events/news/understanding-and-responding-distributed-denial-service-attacks); [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) |
| 17 | Cross-Site Scripting (XSS) | In a deliberately local, inert training page, demonstrate the defensive difference between untrusted text and safely rendered text. Focus on context-aware output encoding, safe templating, and defense-in-depth; never target a real site or collect data. | [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html); [OWASP Top 10](https://owasp.org/www-project-top-ten/) |
| 18 | Making Data Secure | Classify synthetic records; practice data minimization, access control, encryption in transit/at rest, key/secret management, backups, retention, and secure deletion appropriate to the scenario. | [NIST Privacy Framework](https://www.nist.gov/privacy-framework); [NIST SP 800-122](https://csrc.nist.gov/pubs/sp/800/122/final) |
| 19 | Password Hacking | Use fake examples to teach long unique passwords, password managers, MFA/passkeys, breached-password screening in a defensive policy context, and safe recovery. No hash cracking or login attempts. | [NIST SP 800-63-4](https://pages.nist.gov/800-63-4/); [CISA: Secure Our World](https://www.cisa.gov/secure-our-world) |
| 20 | WordPress Scanning | Review a static fictional WordPress audit report. Practice supported core/plugin/theme updates, backups, least privilege, trusted extensions, MFA for administrators, and monitoring. Do not scan live WordPress sites. | [WordPress: Hardening WordPress](https://wordpress.org/documentation/article/hardening-wordpress/); [WordPress Security](https://wordpress.org/about/security/) |
| 21 | Vulnerability Scanning & Reporting | Prioritize a pre-generated fictional findings list using severity, exposure, exploitability, and business impact; map remediation and retesting to an authorized scope. Do not run scans outside a purpose-built local lab. | [NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final); [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog); [NIST NVD](https://nvd.nist.gov/) |
| 22 | Interview Questions | Practice explaining authorization, risk, defensive controls, incident handling, privacy, and responsible AI through mock interviews. Use feedback that distinguishes verified facts from uncertainty. | [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework); [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) |

## Repeatable lesson format

For each topic, the tutor should:

1. State the defensive learning goal and lab boundary.
2. Present a short explanation with links to primary references.
3. Load only the lesson’s included synthetic scenario or static artifact.
4. Show the planned simulation and ask before running it.
5. Explain the result, limitations, and recommended mitigation.
6. Offer a reset and a short knowledge check.
7. Avoid claiming a simulation proves a real system is secure.

## Important implementation note

This guide adds updated defensive methods and references; it does not create an AI agent, a Wi-Fi hacking capability, or a runnable cyber range. A future implementation must keep all actions allowlisted and isolated, use synthetic data, deny real network access by default, and be reviewed for safety before use.
