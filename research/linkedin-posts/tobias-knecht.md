# Tobias Knecht — Manually Collected LinkedIn Posts

These posts were **manually collected** (LinkedIn scraping is restricted) to preserve authentic, advanced email security and anti-abuse insights for our B2B Email Playbook.

## Post 1: Abuse at Scale (Why IP Reputation Persists)

**Core Insight:** Large-scale phishing operations succeed because **reputation and infrastructure signals lag the abuse**—deliverability and security teams should treat real-time abuse telemetry as the leading indicator, not law enforcement outcomes or after-the-fact incident reports.

700,000 phishing emails a day. 3,000 compromised machines a day. 24 months in prison.

The sentencing of Ilya Angelov last week — leader of the "Mario Kart" group (TA-551, Shathak) — put numbers on what abuse operations look like at scale. His crew ran phishing-as-infrastructure: flood inboxes, compromise endpoints, sell botnet access to ransomware operators. BitPaymer. Then IcedID. The email channel was the entry point for the entire chain.

What's unglamorous about this story is what it took to stop it: years of investigation, international cooperation, and a criminal willing to get caught. The infrastructure ran from at least 2018 to 2021. Three years of 700K emails a day.

For every operation like this that ends in a courtroom, there are dozens still running. The math doesn't change: volume abuse at this scale is possible because compromised IP reputation persists, malicious senders keep finding their way onto legitimate infrastructure, and abuse teams get too many reports to act on every one.

Law enforcement is a lagging indicator. Real-time abuse data is the leading one.

## Post 2: The 48-Hour Credential Theft Window

**Core Insight:** Email-borne infostealers compress the breach timeline to **<48 hours**—the most effective “fix” is upstream: blocking malicious sending infrastructure using historical IP reputation and abuse signals *before* the email is delivered.

From inbox to dark web in under 48 hours.

New research from Whiteintel (March 2026) tracked the full lifecycle of infostealer malware: a single malicious email attachment results in corporate credentials listed for sale on dark web marketplaces within 48 hours of infection — well before most security teams detect the breach. Infostealer delivery via email rose 84% in 2025.

The gap isn't just a detection problem. It starts earlier: the email should never have arrived. An IP that's been observed distributing malicious payloads doesn't get a fresh start with every new campaign. The sending infrastructure has history. That history is visible — if you're looking at the right signals.

By the time a detection rule fires, the credential is already being sold. The only layer that closes the gap before it opens is blocking malicious sending infrastructure before delivery, not after infection.

We see that infrastructure in real time. That's the 48-hour problem worth solving.

## Post 3: SPF/DKIM/DMARC Passed — Still Phishing

**Core Insight:** Authentication verifies sender identity, **not trustworthiness**—advanced filtering must incorporate infrastructure and behavioral signals (domain age, registration patterns, IP history, sending velocity) to catch campaigns that are “legitimate” by SPF/DKIM/DMARC yet malicious in intent.

1.6 million phishing emails. Every single one passed SPF, DKIM, and DMARC.

The "Quish Splash" campaign (Feb 26–Mar 18) embedded phishing links inside BMP image attachments — standard content scanners don't inspect pixel data. Microsoft Defender missed all of it. The sending domain was properly authenticated. The emails were, technically, legitimate by every standard authentication check.

Authentication tells you who sent the email. It doesn't tell you whether you should trust them. Those are two different questions, and conflating them is how 1.6 million phishing emails land in inboxes unchallenged.

The signals that would have caught this aren't in the content: they're in the infrastructure. Domain age. Registration patterns. IP history. Sending velocity. A domain set up two weeks before a campaign looks different from one with years of clean sending history — regardless of whether SPF and DKIM are configured correctly.

Authentication is a floor, not a ceiling. The ceiling is behavioral signals on the infrastructure that sent it.
