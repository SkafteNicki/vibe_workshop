# Exercise 2: Improve Your Skill

In this exercise, you will improve the skill you created in Exercise 1.

This is an important part of working with AI tools.

The first version is rarely perfect. The real value comes from testing, noticing weak spots, and improving the instructions.

## What You Are Doing

You will:

1. use your `meeting-to-action-items` skill on a messier note file
2. look for what it gets right and wrong
3. improve the skill so the output becomes more useful

## What Success Looks Like

By the end of this exercise, you will have:

1. tested a skill on a more difficult example
2. improved the skill instructions
3. seen a better result after making changes

## Step 1: Start OpenCode

Open a terminal in Codespaces and run:

```bash
opencode
```

If OpenCode is already running, you can stay where you are.

## Step 2: Start In Plan Mode First

Before changing the skill, make sure you are in `plan` mode.

Use `plan` mode to review the previous result, discuss what is weak, and agree on what should improve.

When you are ready for OpenCode to update the skill files, press `Tab` to switch to `build` mode.

## Step 3: Run Your Skill On A Harder Example

Use this file:

`exercises/sample-meeting-notes-2.md`

Type this in OpenCode:

```text
Use my meeting-to-action-items skill on exercises/sample-meeting-notes-2.md and show me the result.
```

## Step 4: Review The Output

Read the result and ask yourself:

1. Did it clearly separate decisions from action items?
2. Did it identify owners correctly?
3. Did it notice when an owner was missing?
4. Did it notice when a deadline was unclear?
5. Did it point out open questions?
6. Was the final format easy to read?

You are not judging yourself here.

You are judging the instructions you gave the AI.

## Step 5: Switch To Build Mode

Once you know what should change, press `Tab` to switch from `plan` mode to `build` mode.

Now OpenCode can update the skill.

## Step 6: Ask OpenCode To Improve The Skill

Type this:

```text
Please improve my meeting-to-action-items skill based on that result. Make sure it clearly separates decisions, action items, missing owners, missing deadlines, and open questions. Keep the output simple and easy to scan.
```

If you want to be more specific, you can also say:

```text
Please update the skill so it always:
1. separates confirmed action items from open questions
2. flags missing owners
3. flags missing deadlines
4. shows decisions in their own section
5. keeps the final format short and clear
```

## Step 7: Run The Improved Skill Again

Now test the improved version on the same file:

```text
Use my updated meeting-to-action-items skill on exercises/sample-meeting-notes-2.md and show me the new result.
```

## Step 8: Compare Before And After

Ask yourself:

1. Is the new output easier to read?
2. Did it catch more of the unclear parts?
3. Would this be useful in real work?

## Helpful Reminder

This exercise is not about getting a perfect answer.

It is about learning that AI tools improve when you give them clearer structure and clearer rules.

Also remember:

- start in `plan` mode
- talk through the improvements first
- press `Tab` to move to `build` mode only when you are ready to update files

## If You Want To Go Further

Try one more improvement.

For example, ask OpenCode to make the skill:

- group action items by person
- sort action items by urgency
- write a short follow-up email after the action list
- add a short section called `Risks or blockers`
