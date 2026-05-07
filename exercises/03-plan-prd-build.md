# Exercise 3: Plan, Write A PRD, And Build

In this exercise, you will work from a product case instead of a fully defined task.

This is closer to real work.

You will:

1. read a case
2. discuss what should be built
3. ask OpenCode to write a PRD
4. review the PRD
5. build the prototype

## What Success Looks Like

By the end of this exercise, you will have:

1. turned a rough idea into a clearer plan
2. created a `PRD.md` file using the `to-prd` skill
3. built a working prototype based on your chosen scope

## Step 1: Start OpenCode

Open a terminal in Codespaces and run:

```bash
opencode
```

If OpenCode is already running, you can stay where you are.

## Step 2: Start In Plan Mode First

Before building anything, make sure you are in `plan` mode.

`plan` mode is for thinking, shaping the work, and making choices before files change.

Stay in `plan` mode while you discuss the case with the agent.

When you are later ready to implement, press `Tab` to switch to `build` mode.

## Step 3: Read The Case

Open this file:

`exercises/case.md`

Then ask OpenCode:

```text
Please read exercises/case.md and explain the case to me in simple language.
```

This repository also includes an optional hint file:

`exercises/triageai-hints.md`

If you want extra guidance before scoping, you can ask OpenCode to read that too.

## Step 4: Look At Sample Data Early

Before you decide the final scope, it can help to look at some real sample tickets.

This repository includes a helper script:

`exercises/data_downloader.py`

You can ask OpenCode to run it for you and show you the output.

For example:

```text
Please run exercises/data_downloader.py and show me the sample data so I can use it to help scope the prototype.
```

This is useful because it gives you a more realistic sense of what the prototype should handle.

## Step 5: Scope The Prototype Together

Now discuss what the first version should include.

This is the most important part of the exercise.

Do not rush into building.

Type something like this:

```text
Let's stay in plan mode and decide what the smallest useful prototype should be. Please help me choose the scope, the implementation language, whether the prototype should support one language or multiple ticket languages, and what should be out of scope.
```

You can also ask:

```text
Please give me 2 or 3 reasonable ways to scope this prototype, from simplest to more ambitious, and recommend one for a workshop.
```

If you want extra help, you can also say:

```text
Please read exercises/triageai-hints.md and use it as guidance while we decide the scope. If the prototype uses direct AI calls in code, we should use the OpenRouter API.
```

## Step 6: Ask OpenCode To Write A PRD

Once you have gone back and forth with the agent and the scope feels clear, ask it to use the `to-prd` skill.

Type this:

```text
Use the to-prd skill to turn our current plan into a PRD and write it to PRD.md.
```

## Step 7: Review The PRD

Read `PRD.md` and ask yourself:

1. Does it match the scope you agreed on?
2. Does it stay small enough for a workshop?
3. Does it clearly say what is in scope and out of scope?
4. Does it reflect your language and implementation choices?

If needed, ask OpenCode to revise it.

For example:

```text
Please tighten the PRD so it stays small enough for a workshop and clearly reflects our chosen implementation language and scope.
```

## Step 8: Switch To Build Mode

When the PRD looks right, press `Tab` to switch from `plan` mode to `build` mode.

Now OpenCode can start creating files.

## Step 9: Build The Prototype In Small Steps

Ask OpenCode to implement the prototype milestone by milestone.

A good prompt is:

```text
Please implement the PRD in small steps. Keep the scope tight. After each meaningful step, explain what you changed in plain English.
```

If the agent needs direction, ask it to build in this order:

1. the core logic first
2. then a simple API or backend
3. then a simple user interface, if that is part of your scope

## Step 10: Try The Prototype

Once something works, test it with a sample ticket.

You can use this one:

```text
I was charged twice this month and nobody has responded to my last three emails. This is completely unacceptable. I want a refund immediately or I'm disputing with my bank.
```

Then ask:

```text
Please show me how to run the prototype and test it with the sample ticket.
```

## Step 11: Reflect On The Result

When you are done, ask yourself:

1. Did the final prototype match the PRD?
2. Did the planning step improve the build?
3. Was the chosen scope realistic for the time available?
4. What would you improve next if this became a real product?

## Helpful Reminder

This exercise is not about building the most advanced version.

It is about learning a useful workflow:

1. plan first
2. write the plan down
3. build from the plan

Also remember:

- start in `plan` mode
- discuss the case before building
- use `to-prd` only after the plan is clear
- press `Tab` to move to `build` mode when you are ready to make changes
