# Case: TriageAI

TriageAI is a small internal tool for support teams.

The idea is simple:

A support agent pastes in a messy customer ticket and quickly gets back a more structured view of it.

That structured view might include:

- how urgent the ticket seems
- what kind of problem it is
- the customer's tone or sentiment
- a short summary
- a suggested first reply
- whether the ticket should be escalated

## Why This Matters

Support teams often spend time on the same first-step work again and again:

- reading long messages
- guessing urgency
- sorting tickets into categories
- deciding whether a manager or specialist should step in
- writing the first reply

TriageAI is meant to speed up that first pass.

The goal is not to replace human judgment.

The goal is to give support teams a useful starting point.

## Who It Is For

This tool is for internal support agents.

It is not a full customer support platform.

It is just a lightweight prototype that helps with early ticket triage.

## What A Good First Version Could Do

A useful first version might let a user:

1. paste in a raw support ticket
2. click a button
3. receive a structured result on screen

That result could include:

- `priority`: Critical / High / Medium / Low
- `category`: Billing / Bug / Feature Request / Account / Other
- `sentiment`: Frustrated / Neutral / Positive
- `summary`: a short plain-English summary
- `draft_reply`: a professional first response
- `escalate`: yes or no
- `escalate_reason`: a short explanation

## Your Job In This Exercise

You are not being asked to build a perfect product.

You are being asked to decide what a sensible prototype should include, write that down as a PRD, and then build it.

## Important: You Decide The Scope

This part matters.

Do not assume the case has already decided everything for you.

During planning, you and the agent should decide things like:

- what the smallest useful version is
- what implementation language to use
- whether to build only a backend, or a backend and a simple interface
- whether the prototype should only handle one language or multiple ticket languages
- how polished the interface needs to be
- what is clearly out of scope for this workshop

One simple choice might be Python plus a very small web interface.

But that is only a suggestion, not a rule.

## Helpful Note On Sample Data

This repository includes `exercises/data_downloader.py`.

You can ask OpenCode to run it and show you some sample support ticket data.

That is a good early step because seeing real examples can help you decide how broad or narrow the prototype should be.

## Helpful Note On Build Hints

This repository also includes `exercises/triageai-hints.md`.

You can ask OpenCode to read that file for extra guidance.

It includes workshop-friendly suggestions and a reminder that direct AI calls in code should use the OpenRouter API.

## Helpful Sample Ticket

If you want a concrete example to discuss during planning, use this one:

> "I was charged twice this month and nobody has responded to my last three emails. This is completely unacceptable. I want a refund immediately or I'm disputing with my bank."

A reasonable triage result would probably mark this as:

- high urgency
- billing-related
- frustrated
- likely worth escalating

## What Is Deliberately Missing

This case does not fully specify the product.

That is intentional.

Part of the exercise is deciding:

- what to build now
- what to leave out
- what should wait for a future version

That planning conversation is part of the work.
