# Eric Nowoslawski — Manually Collected LinkedIn Posts

These posts were **manually collected** (LinkedIn scraping is restricted) to preserve authentic outbound systems and cold email execution insights for our B2B Email Playbook.

## Post 1: The Data-Driven Intent Framework

**Core Insight:** Don’t guess which intent signal works—run parallel campaigns (baseline vs. single-signal segments vs. real-time triggers), then back-test every positive response against *all* signals to discover the true predictors and generate your next 10 campaigns from evidence.

Last quarter a client asked me which intent signal they should use. Hiring data? Funding? Website visits?

I told them to use all of them, but not how they expected.

Most people pick one signal, build a campaign around it, and pray. That's backwards. You don't know which signal predicts a response until you let the data tell you.

Here's the framework we use across 50+ clients.

Run 3 campaigns at once:

1. Entire TAM. No signals. Just firmographics. This is your baseline — and sometimes it wins.
2. Focused segments. One signal per campaign. Hiring SDRs. Recently funded. Using a competitor tool.
3. Trigger-based. Real-time events. Job posting today. Funding this week. Website visit yesterday.

Now here's the move nobody talks about.

Every positive response across all 3, take that company and run it through every signal source you have. Pull hiring data, tech stack, funding history, news, social activity. Everything.

Look for patterns.

Maybe the companies that respond all hired a VP of Sales in the last 90 days. Maybe they all use HubSpot. Maybe they all posted about a specific pain point on LinkedIn.

You wouldn't have found that by guessing upfront.

We also run a catchall workflow in Clay with Clayagent, every signal we can think of, just "what's notable about this company right now?" Sometimes the signal that predicts responses is something you'd never think to look for.

Sometimes you genuinely don't know WHY someone responded. That's fine. Not every response has a readable signal. But the ones that do give you your next 10 campaigns.

Stop picking signals from a menu. Let the data tell you what works.

## Post 2: Troubleshooting a Failing Campaign

**Core Insight:** When reply rates collapse, isolate variables fast—start by segmenting deliverability (Google Workspace only), validate DNS/auth (SPF/DKIM/DMARC + blacklist/inbox tests), then increase testing velocity with tighter segmentation and simpler offers that earn “yes” before a meeting ask.

Your campaigns have been running for two weeks. Reply rate is 0.3%. Zero positive responses.

Here are the next steps we take.

1. Peel back everything and only send to Google accounts.
Strip your list to Google Workspace, not Gmail, just Google Workspace.
Right now Outlook is harder to get into the inbox, and we don't want to send to any Proofpoint, Microsoft, or other email inboxes.
We want to isolate the variable. Your Google deliverability might be fine while Outlook is putting you straight to spam, and you'd never know if you're sending to both.
Check blacklists and run inbox placement tests while you're at it. Verify your domain setup. DKIM, SPF, and DMARC.

2. Hyper-segment the list.
Take your lead list and whittle it down to a thousand prospects as focused as you possibly can. Let the list become the message and add whatever filters you need to get them as close to your current customers as possible.

3. Increase testing velocity.
A lot of times we try to set up campaigns that will work long-term. You can't be thinking about long-term here.
Keep the lead list tight and speed up the testing velocity.
Launch multiple campaigns with different angles.
Pain-based versus value-based.
Different CTAs.
Different target personas. T
ry to make your email easier to say yes to.
Include more lead magnets or free offers delivered by AI, competitive intelligence reports, anything that provides value before asking for a meeting.

4. Test campaigns that generate meeting-ready leads versus hand raisers.
If your direct ask isn't working, test an offer that generates hand raisers instead. Sometimes people aren't ready to book a meeting but will say yes to something valuable.
Don't add complexity. Remove it. Find the one thing that's broken.

## Post 3: The Zero-to-Scale Cold Email Stack

**Core Insight:** Outbound has four solvable constraints (deliverability, list building, copywriting, sending); you can start with a “scrappy” stack and upgrade in tiers—what matters is shipping campaigns now, then investing into domains/inboxes, verification, and enrichment as ROI appears.

If there are first-time founders out there that need to start cold email for zero dollars, this is how I would do it.

There are four problems you need to solve: deliverability, list building, copywriting, and sending. Let's take each as a checklist.

1. Deliverability.
It's not best practice, and I wouldn't even say it comes across as professional, but if you want to do cold email for zero dollars, sending from your personal email address will do the trick until you close enough deals to invest. Your personal email likely has years of reputation on it, and it will work fine for the low-volume use case we're going to do here.

2. List building.
You need a way to build lists and store them. You could save files locally and use the free tiers of Codex or Claude Code to do research and find 50 contacts to reach out to. If you need their emails, most email platforms have great free trials you could work between. Start a Prospeo free trial, for instance.

3. Copywriting.
Any ChatGPT or Claude instance can help you get started for free. I would suggest creating cold emails in the style of Josh Braun if you really don't know what to do here. His frameworks are simple and they work.

4. Sending.
A new repo was just dropped that controls your browser, and you could use the "send later" function inside of Gmail to do the sending. It cuts a couple corners here and there, but if you have absolutely no money to get started, this is how you'd be able to do it.

Now here's the progression when you're ready to invest:

- $50/month: Smartlead or Instantly for sending + scheduling. They have built-in lead databases.
- $200/month: Add 3-5 domains and inboxes. Buy a list from Prospeo or Clay. Use Million Verifier to clean it.
- $500/month: I'd just invest in more domains and inboxes at this level. A/B testing across segments.
- $2,000+/month: Waterfall enrichment. Intent signals. 50+ domains. Multiple campaigns. This is where agencies like us operate.

Start sending. Upgrade later.
