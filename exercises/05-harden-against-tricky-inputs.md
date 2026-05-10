# Exercise 5: Harden Against Tricky Inputs

In this exercise, you will test how your skill or prototype behaves when the input is confusing, incomplete, or intentionally difficult.

This helps you make your AI workflow more reliable.

The goal is not to make it impossible to break.

The goal is to make it fail more safely and more clearly.

## What You Are Doing

You will:

1. take the thing you built in Workshop 1
2. test it with tricky or adversarial inputs
3. look for weak spots
4. improve the skill, prompt, or instructions
5. test again
6. if possible, swap with a partner and try to break each other's setup

## What Success Looks Like

By the end of this exercise, you will have:

1. tested your system on bad or unusual inputs
2. found at least one failure mode
3. improved how the system handles that situation
4. seen how other people use unexpected inputs

## Step 1: Start OpenCode

Open a terminal in Codespaces and run:

```bash
opencode
```

If OpenCode is already running, you can stay where you are.

## Step 2: Start In Plan Mode First

Before changing anything, make sure you are in `plan` mode.

Use `plan` mode to think about what could go wrong and what a safe response should look like.

When you are ready for OpenCode to create or edit files, press `Tab` to switch to `build` mode.

## Step 3: Choose What You Are Hardening

Pick one of these:

1. your `meeting-to-action-items` skill
2. your `TriageAI` prototype

Then tell OpenCode what you chose.

If you built the meeting notes skill, you can type:

```text
I want to harden my meeting-to-action-items skill against tricky inputs. Please help me test weak spots and improve the instructions.
```

If you built TriageAI, you can type:

```text
I want to harden my TriageAI prototype against tricky inputs. Please help me test weak spots and improve the instructions or prompt.
```

## Step 4: Try A Few Tricky Inputs

Use around 4 to 6 inputs.

You can make your own, or start from examples like these.

### If You Built The Meeting Notes Skill

Try inputs such as:

1. notes with missing owners and no clear decisions
2. notes with mixed languages or unusual wording
3. notes that include unrelated chat or jokes
4. notes that are extremely short and missing context
5. notes where questions sound like decisions

Example prompt:

```text
Please generate 5 tricky meeting note examples that could confuse my meeting-to-action-items skill, but still look realistic.
```

### If You Built TriageAI

Try inputs such as:

1. a ticket with almost no detail
2. a ticket with mixed problems in one message
3. a ticket written in a different language
4. a ticket with emotional language but unclear facts
5. a malformed or oddly formatted ticket

Example prompt:

```text
Please generate 5 tricky support ticket examples that could confuse my TriageAI prototype, but still look realistic.
```

## Step 5: Observe How It Fails

Run your current version on the tricky inputs.

Then ask:

1. Did it stay calm and clear?
2. Did it make up details that were not in the input?
3. Did it pretend to know things that were actually unclear?
4. Did it give an answer when it should have flagged uncertainty?
5. Did the output stay readable?

If you want help, type:

```text
Please help me identify the biggest failure modes in these results. Focus on places where the system sounds confident but should be more careful.
```

## Step 6: Switch To Build Mode

Once you understand the weak spots, press `Tab` to switch from `plan` mode to `build` mode.

Now OpenCode can update the skill, prompt, or prototype.

## Step 7: Improve The Safeguards

Make one or two focused improvements.

Examples:

- tell the system to say when information is missing
- separate facts from guesses
- require an `unclear` or `needs review` signal when confidence is low
- keep the output short when the input is messy
- avoid inventing owners, deadlines, categories, or causes

If you want help, type:

```text
Please update my instructions so the system handles unclear or messy input more safely. It should avoid making things up and should clearly flag uncertainty.
```

## Step 8: Run The Tricky Inputs Again

Run the same tricky inputs again after your update.

Then compare the old and new results.

Ask:

1. Did the system become more careful?
2. Did it handle uncertainty more honestly?
3. Did it stay useful, or did it become too vague?

## Step 9: If Possible, Swap With A Partner

If you are working with someone else, swap systems.

Each person should try to find one more weak spot in the other person's setup.

Then share:

1. the input you used
2. what went wrong
3. one change that might help

This part is useful because other people often think of cases you would not think of yourself.

## Step 10: Reflect On The Result

Ask yourself:

1. What kind of input caused the biggest problem?
2. What safeguard helped most?
3. What should the system do when it is unsure?

## Helpful Reminder

This exercise is not about blocking every strange input.

It is about improving how the system behaves when the input is weak, messy, or confusing.

Also remember:

- start in `plan` mode
- test bad inputs on purpose
- look for overconfidence
- make small changes and test again
