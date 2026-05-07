# Exercise 1: Create Your First Skill

In this exercise, you will teach OpenCode a repeatable way to turn meeting notes into clear action items.

You do not need to know how to code to do this exercise.

## What You Are Making

A skill is a small reusable instruction pack for the AI assistant.

In this exercise, you will create a skill that can:

- read meeting notes
- pull out decisions, owners, and next steps
- turn them into a clean action list

## What Success Looks Like

By the end of this exercise, you will have:

1. used the `skill-creator` skill
2. created a new skill for a simple workflow
3. tested it on a sample meeting note file

## Step 1: Start OpenCode

Open a terminal in Codespaces and run:

```bash
opencode
```

If OpenCode is already running, you can stay where you are.

## Step 2: Start In Plan Mode First

Before you ask OpenCode to create anything, make sure you are in `plan` mode.

`plan` mode is for thinking, clarifying, and shaping the work before files are changed.

Spend a few minutes going back and forth with the agent there first.

When you are ready for OpenCode to actually create or edit files, press `Tab` to switch to `build` mode.

## Step 3: Ask OpenCode To Use The Skill Creator

Type this in OpenCode:

```text
Use the skill-creator skill to help me create a new skill.
```

This tells OpenCode to switch into a mode where it helps you design a new reusable workflow.

## Step 4: Describe The Skill You Want To Build

Then type this:

```text
I want to create a skill called meeting-to-action-items. The skill should help turn messy meeting notes into a clear list of action items, owners, deadlines, decisions, and follow-ups. Please guide me step by step and keep the language simple.
```

OpenCode will usually ask a few follow-up questions. That is expected.

## Step 5: Keep The Scope Small

If OpenCode asks what the skill should do, you can reply with this:

```text
Keep it simple. The skill should read meeting notes and produce:
1. a short summary
2. key decisions
3. action items
4. who owns each action item
5. any missing information or unclear ownership
```

This keeps the exercise focused and easier to finish.

## Step 6: Switch To Build Mode

Once you feel the goal is clear, press `Tab` to switch from `plan` mode to `build` mode.

Now OpenCode can create the skill files in the repository.

## Step 7: Let OpenCode Build The Skill

OpenCode should now guide you through creating the new skill folder and writing the skill instructions.

If it seems unsure, type this:

```text
Please continue using the skill-creator workflow. Create the new skill in this repository and keep the output short and practical.
```

## Step 8: Test The Skill On Sample Notes

Once the skill is created, test it using the sample file in this repository:

`exercises/sample-meeting-notes.md`

Type this in OpenCode:

```text
Use my new meeting-to-action-items skill on exercises/sample-meeting-notes.md and show me the result.
```

## Step 9: Review The Result

Look at the output and ask:

1. Did it find the action items?
2. Did it assign the right owners?
3. Did it notice anything unclear or missing?
4. Is the result easy to read?

If not, improve the skill by telling OpenCode what to change.

For example:

```text
Please improve the skill so it always separates confirmed action items from open questions.
```

## Helpful Reminder

You are not trying to get a perfect result on the first try.

The point of the exercise is to experience that you can teach the AI assistant a repeatable way of working.

Also remember:

- start in `plan` mode
- talk through the task first
- press `Tab` to move to `build` mode only when you are ready to make changes

## If You Want To Go Further

After the basic version works, try adding one more rule.

For example:

- highlight deadlines
- flag missing owners
- group action items by person
- create a follow-up email draft from the notes
