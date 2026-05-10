# Exercise 1: Create And Improve A Skill

In this exercise, you will teach OpenCode a repeatable way to turn meeting notes into clear action items — and then make it better.

You do not need to know how to code to do this exercise.

## What You Are Making

A skill is a small reusable instruction pack for the AI assistant.

You will create a skill that can:

- read meeting notes
- pull out decisions, owners, and next steps
- turn them into a clean action list

Then you will test it on a harder example and improve it based on what you find.

## What Success Looks Like

By the end of this exercise, you will have:

1. created a new skill using the `skill-creator` skill
2. tested it on a simple meeting note file
3. tested it on a messier file and found its weak spots
4. improved the skill so the output becomes more useful

---

## Part 1: Create The Skill

### Step 1: Start OpenCode

Open a terminal in Codespaces and run:

```bash
opencode
```

If OpenCode is already running, you can stay where you are.

### Step 2: Start In Plan Mode First

Before you ask OpenCode to create anything, make sure you are in `plan` mode.

`plan` mode is for thinking, clarifying, and shaping the work before any files are changed.

Spend a few minutes going back and forth with the agent there first.

When you are ready for OpenCode to actually create files, press `Tab` to switch to `build` mode.

### Step 3: Ask OpenCode To Use The Skill Creator

Type this in OpenCode:

```text
Use the skill-creator skill to help me create a new skill.
```

### Step 4: Describe The Skill You Want To Build

Then type this:

```text
I want to create a skill called meeting-to-action-items. The skill should help turn messy meeting notes into a clear list of action items, owners, deadlines, decisions, and follow-ups. Please guide me step by step and keep the language simple.
```

OpenCode will usually ask a few follow-up questions. That is expected.

### Step 5: Keep The Scope Small

If OpenCode asks what the skill should do, you can reply with this:

```text
Keep it simple. The skill should read meeting notes and produce:
1. a short summary
2. key decisions
3. action items with owners
4. any missing information or unclear ownership
```

### Step 6: Switch To Build Mode

Once the goal is clear, press `Tab` to switch from `plan` mode to `build` mode.

Now OpenCode can create the skill files in the repository.

### Step 7: Let OpenCode Build The Skill

OpenCode should now guide you through creating the skill. If it seems unsure, type:

```text
Please continue using the skill-creator workflow. Create the new skill in this repository and keep the output short and practical.
```

### Step 8: Test The Skill On Sample Notes

Once the skill is created, test it using the sample file in this repository:

`exercises/sample-meeting-notes.md`

Type this:

```text
Use my new meeting-to-action-items skill on exercises/sample-meeting-notes.md and show me the result.
```

### Step 9: Review The Result

Look at the output and ask:

1. Did it find the action items?
2. Did it assign the right owners?
3. Did it notice anything unclear or missing?
4. Is the result easy to read?

---

## Part 2: Improve The Skill

The first version is rarely perfect. The real value comes from testing on harder examples, noticing weak spots, and improving the instructions.

### Step 10: Test On A Harder Example

Now use this messier file:

`exercises/sample-meeting-notes-2.md`

Type this:

```text
Use my meeting-to-action-items skill on exercises/sample-meeting-notes-2.md and show me the result.
```

### Step 11: Review The Output

Read the result and ask yourself:

1. Did it clearly separate decisions from action items?
2. Did it identify owners correctly?
3. Did it notice when an owner was missing?
4. Did it notice when a deadline was unclear?
5. Was the final format easy to read?

You are not judging yourself here. You are judging the instructions you gave the AI.

### Step 12: Switch Back To Plan Mode

Before changing the skill, switch back to `plan` mode.

Use it to discuss what was weak and agree on what should improve.

When you are ready for OpenCode to update the files, press `Tab` to switch to `build` mode again.

### Step 13: Ask OpenCode To Improve The Skill

Type this:

```text
Please improve my meeting-to-action-items skill based on that result. Make sure it clearly separates decisions, action items, missing owners, missing deadlines, and open questions. Keep the output simple and easy to scan.
```

### Step 14: Run The Improved Skill Again

Test the updated version on the same file:

```text
Use my updated meeting-to-action-items skill on exercises/sample-meeting-notes-2.md and show me the new result.
```

### Step 15: Compare Before And After

Ask yourself:

1. Is the new output easier to read?
2. Did it catch more of the unclear parts?
3. Would this be useful in real work?

---

## Helpful Reminder

You are not trying to get a perfect result on the first try.

The point of the exercise is to experience two things:

1. You can teach the AI a repeatable way of working
2. AI tools improve when you give them clearer rules and better examples

Also remember:

- start in `plan` mode
- talk through the task before making changes
- press `Tab` to move to `build` mode only when you are ready to change files

## If You Want To Go Further

Once the improved version works, try adding one more rule. For example, ask OpenCode to make the skill:

- group action items by person
- sort action items by urgency
- write a short follow-up email after the action list
- add a short section called `Risks or blockers`
