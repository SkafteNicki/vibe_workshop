# Exercise 4: Bring Your Own Idea

In this exercise, there is no case file and no prompt to copy.

You bring the idea. The AI helps you shape it, stress-test it, and build it.

This is the closest thing to real work you will do today.

---

## What This Exercise Is About

You are going to use two new skills:

- **brainstorming** — helps you turn a rough idea into a clear design, one question at a time
- **grill-me** — pushes back on your plan and asks hard questions until the design is solid

Together, they help you think before you build.

---

## What Success Looks Like

By the end of this exercise, you will have:

1. turned your own idea into a clear, written design
2. stress-tested that design by letting the AI challenge your assumptions
3. built a small working prototype based on what survived the process

---

## Step 1: Pick An Idea

Think of something small and useful you would actually want to exist.

It does not need to be technical. It just needs to be something a computer could help with.

Some examples to get you started (but use your own if you have one):

- A tool that reads a messy email and drafts a polite reply
- A simple quiz generator from a block of text
- A daily summary of your calendar in plain English
- A tool that checks whether a job description matches a resume
- A mood tracker that gives you a short reflection at the end of the day

Write your idea down in one or two sentences before you start.

---

## Step 2: Start OpenCode In Plan Mode

Open a terminal and run:

```bash
opencode
```

Make sure you are in `plan` mode before continuing.

`plan` mode is for thinking and designing. No files will change yet.

---

## Step 3: Use The Brainstorming Skill

Tell OpenCode your idea and ask it to use the brainstorming skill.

For example:

```text
I have an idea for a tool that [describe your idea in one sentence]. Please use the brainstorming skill to help me shape it.
```

The AI will ask you questions one at a time. Answer them honestly. There are no wrong answers.

You are working toward a short, written design document — a clear description of what you are building and why.

**Take your time here.** This is the most important step.

---

## Step 4: Use The Grill-Me Skill

Once the brainstorming session feels complete and you have a design in mind, it is time to stress-test it.

Ask OpenCode:

```text
Please use the grill-me skill to challenge my design.
```

The AI will now ask harder questions — about edge cases, assumptions, things you may not have thought through.

This is not meant to discourage you. It is meant to make the final build better.

For each question, answer as best you can. The AI will offer its own recommendation if you are not sure.

---

## Step 5: Write A PRD

Once you have worked through the brainstorming and grilling, use the `to-prd` skill to lock in your plan.

```text
Use the to-prd skill to turn our current design into a PRD and write it to PRD.md.
```

Read the PRD when it is done. Ask yourself:

1. Does it match what you actually want to build?
2. Is the scope small enough to finish today?
3. Is anything missing or unclear?

If something feels off, ask OpenCode to revise it before moving on.

---

## Step 6: Switch To Build Mode

When the PRD looks right, press `Tab` to switch from `plan` mode to `build` mode.

Now OpenCode can start creating files.

---

## Step 7: Build It

Ask OpenCode to implement the prototype based on the PRD.

A good starting prompt:

```text
Please implement the PRD in small steps. After each step, explain what changed in plain English.
```

If you want to stay in control of the pace:

```text
Please implement just the first milestone and stop. I will review before we continue.
```

---

## Step 8: Try It

Once something is working, test it with a real example from your own life or work.

Then ask:

```text
Please show me how to run this and test it.
```

---

## Step 9: Reflect

When you are done, think about these questions:

1. How did the final prototype compare to your original idea?
2. Did the brainstorming step change what you wanted to build?
3. Did the grill-me step catch anything you had not thought of?
4. What would the next version include?

---

## A Note On Scope

The goal is not to build something impressive. The goal is to build something **real** — even if it is tiny.

A tool that does one thing well is better than a tool that tries to do five things and does none of them.

If your idea feels too big, ask OpenCode to help you cut it down:

```text
My idea feels too large for a workshop. Please help me find the smallest version that still feels useful.
```
