# Jesse Ouellette — Manually Collected LinkedIn Posts

These posts were **manually collected** (LinkedIn scraping is restricted) to preserve authentic, high-signal deliverability insights for our B2B Email Playbook.

## Post 1: AI Agent Factories

**Core Insight:** Treating AI like a coordinated “agent factory” (not a chatbot) is a repeatable way to scale technical output and operational leverage without scaling headcount—useful when building marketing + outbound systems.

Stop prompting AI one-by-one.  
Start orchestrating Agent Factories.

Most people treat Claude, Cursor, and Codex like chatbots.  
But the smartest SaaS founders and Agencies are using OpenClaw to run "Swarm Agents."

We built the OpenClaw architecture entirely on edge containers to run massive multi-agent pipelines with zero human bottlenecks.

Here is why the tech stack is an absolute cheat code:

- **Firecracker VMs**: Providers like Fly, Cloudflare, and Vercel give us isolated microVMs so agents can safely write, execute, and test code without breaking production.
- **Cloudflare Workers**: Zero-latency agent routing at the edge.
- **Durable Objects**: Stateful, persistent memory so agents never lose context or hallucinate.
- **Vectorize**: Sub-millisecond RAG across our entire codebase and ICP data.

We are running these Agent Factories across three core areas:

1) **THE CODE FACTORY**  
We have agents that write, test, and ship their own PRs autonomously.
   - **A1 (Spec Architect)** reads Linear tickets and writes technical specs.
   - **A2 (The Builder)** writes the actual code.
   - **A3 (The Reviewer)** lints, tests, and approves the PR.

2) **PROGRAMMATIC SEO & MARKETING**  
We aren't spamming ChatGPT. We run a structured Swarm.
   - **M1** scrapes real-time search engine trends.
   - **M2** builds the schema and semantic architecture.
   - **M3** generates highly optimized, interlinked SEO pages at scale.
   - **M4** watches our paid ad spend and continually optimizes the output.

3) **GTM & OUTBOUND**  
Instead of hiring 10 more VAs for list building and inbox triage:
   - A **Scraper Agent** pulls 10-K and hiring signals 24/7.
   - A **Context Agent** cross-references it with our ICP via Vectorize.
   - A **Writer Agent** drafts hyper-personalized outbound sequences.

If you are a technical founder, operator, or agency owner, you need to spin this up today.  
It is how you scale output without scaling headcount.

## Post 2: The HTML Signature Trap

**Core Insight:** Deliverability isn’t just “subject lines”—small implementation details like HTML signatures, logos, and tracking pixels can materially increase spam risk; keeping email payloads lean is a practical safeguard for outbound reliability.

I got fired for refusing to change my email signature.  
Best day of my life.

Here's what happened:

I was a sales leader at a top SaaS company. Privacy/security space. Big growth fund portfolio.

My CEO mandated HTML signatures:

- Logos
- Tracking pixels
- Social buttons
- Legal disclaimers

The problem?

All of that DESTROYS email deliverability.

I had the data:

- ☑ HTML bloat triggers spam filters
- ☑ Images don't load 60% of the time
- ☑ Tracking pixels get flagged
- ☑ More code = higher spam score

My CRO backed me. He understood.  
The CEO didn't care. "Brand consistency."  
I got fired for "not being aligned."

The irony?  
A privacy/security company fired me for understanding email security.

So I did what any sane person would do:

I built a 7-figure SaaS helping people with email deliverability.  
No investors.  
No board meetings.  
No permission needed.  
Just me, shipping.

The CEO who fired me?  
Still wondering why his team's emails go to spam.

Getting fired was the best thing that ever happened.

What's your "signature moment"?

## Post 3: Catch-All Domains

**Core Insight:** “Catch-all” domains can poison outbound with false positives; robust validation and cautious enrichment vendor selection protect sender reputation and prevent bad data from cascading into poor deliverability and wasted pipeline.

🚨 I thought we had a problem…  
But it turns out it wasn’t as bad as it looked.

Take a look at this 👇

We tested multiple “email finder” tools side-by-side on the exact same list.

Some came back with nothing.  
Others came back with completely wrong emails.

Why? Because the domain was a catch-all.  
That means the mail server accepts any email you throw at it — whether the inbox actually exists or not.

And here’s the real danger:

- ❌ Tools that don’t validate properly will happily “find” an email, slap a ✅ on it, and hand it back to you.
- ❌ You think it’s deliverable.
- ❌ But when you send, it bounces or doesn't bounce and the person doesn't work there.

GHOST CATCH ALL EMAILS.

This is plaguing the email world right now and I've cracked the code on this.

That’s how “transferred issues” creep into your campaigns:  
bad data → bad delivery → bad outcomes.

👉 This is exactly why I wouldn’t trust FullEnrich or Wiza for email finding.  
If a tool can’t handle catch-alls with rigor, it’s setting you up for expensive mistakes.

The lesson?  
Don’t trust every green checkmark ✅ you see.

Catch-all detection is hard.  
Sloppy enrichment leads to bad data, and bad data kills outbound.

If you’re serious about outbound, you need validation that tells you the truth not just a guess.

We have our challenges, but our overall accuracy is the best in the world.  
None of these presidents work at company's with Catch-All Domains.

Watch out for the "schill" agencies who promote these tools blindly without the best judgement.  
Watch out for the catch-all guarantees which imply you will get a refund.  
My guess is they won't refund you for any of them.

What's your waterfall look like?
