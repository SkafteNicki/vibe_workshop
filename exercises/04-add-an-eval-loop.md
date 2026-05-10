# Exercise 4: Add An Eval Loop

In this exercise, you will measure how well your skill or prototype performs, make one improvement, and then measure again.

This is a simple version of an evaluation workflow.

The goal is not to guess whether your AI output got better.

The goal is to check.

## What You Are Doing

You will:

1. choose the thing you built in Workshop 1
2. write a small set of test cases
3. run those test cases
4. score the results with a simple rubric
5. improve one part of the skill, prompt, or prototype
6. run the same test cases again
7. compare the before and after results

## What Success Looks Like

By the end of this exercise, you will have:

1. created a small eval set
2. measured the current quality of your output
3. made one focused improvement
4. checked whether the result actually improved

## Step 1: Start OpenCode

Open a terminal in Codespaces and run:

```bash
opencode
```

If OpenCode is already running, you can stay where you are.

## Step 2: Start In Plan Mode First

Before changing anything, make sure you are in `plan` mode.

Use `plan` mode to decide what you are evaluating and what a good result looks like.

When you are ready for OpenCode to create or edit files, press `Tab` to switch to `build` mode.

## Step 3: Choose What You Are Evaluating

Pick one of these:

1. your `meeting-to-action-items` skill
2. your `TriageAI` prototype

Then tell OpenCode what you chose.

If you built the meeting notes skill, you can type:

```text
I want to evaluate my meeting-to-action-items skill. Please help me create a small eval set and a simple scoring rubric.
```

If you built TriageAI, you can type:

```text
I want to evaluate my TriageAI prototype. Please help me create a small eval set and a simple scoring rubric.
```

## Step 4: Create A Small Eval Set

Create around 8 to 10 test cases.

Try to cover a range of realistic inputs.

For example:

- easy examples
- messy examples
- incomplete examples
- emotional examples
- ambiguous examples
- edge cases that are still realistic

If you want OpenCode to help, type:

```text
Please help me create 8 to 10 realistic test cases that cover the range of inputs this tool should handle in a workshop setting. Keep them short.
```

## Step 5: Define A Simple Scoring Rubric

Keep the rubric small and easy to use.

For the meeting notes skill, a simple rubric could be:

1. Did it produce a clear summary?
2. Did it separate decisions from action items?
3. Did it identify owners correctly?
4. Did it flag unclear ownership or missing information?

For TriageAI, a simple rubric could be:

1. Did it choose a reasonable priority?
2. Did it choose a reasonable category?
3. Did it summarize the ticket clearly?
4. Did it give a sensible first reply or escalation signal?

You do not need a perfect scoring system.

You need one that is simple enough to use consistently.

## Step 6: Switch To Build Mode

Once the eval set and rubric feel clear, press `Tab` to switch from `plan` mode to `build` mode.

Now OpenCode can help create any files you want for the eval work.

## Step 7: Run The First Pass

Run your current skill or prototype on the full eval set.

Then score the outputs using the same rubric each time.

You can ask OpenCode to help organize the results.

For example:

```text
Please run through my eval cases with me and put the results into a simple table with one row per test case and one score per rubric item.
```

## Step 8: Look For The Biggest Weak Spot

Before changing anything, ask:

1. Where does the current version fail most often?
2. Is the problem in clarity, structure, missing information, or wrong classification?
3. What is one small change most likely to help?

Try to change only one important thing.

That makes it easier to tell what helped.

## Step 9: Make One Focused Improvement

Examples of good improvements:

- tightening the prompt
- improving the skill instructions
- requiring a clearer output structure
- adding a rule for ambiguity or missing information
- adding a rule for escalation or uncertainty

If you want help, type:

```text
Please suggest one small change that is likely to improve the weakest part of my results. Keep the change focused so we can measure whether it helped.
```

## Step 10: Run The Eval Again

Run the same eval set again after the change.

Then compare the before and after results.

Ask:

1. Did the scores improve?
2. Did the improvement help the cases you expected?
3. Did anything get worse?

## Step 11: Reflect On The Result

This is the most important lesson in the exercise:

AI systems should be improved by testing and measuring, not only by instinct.

Ask yourself:

1. What did the eval tell you that you would not have noticed by casual testing?
2. Did the change actually help?
3. What would you evaluate next if you had more time?

## Helpful Reminder

This exercise is not about creating a perfect benchmark.

It is about learning a repeatable loop:

1. define good examples
2. measure current results
3. make one change
4. measure again

Also remember:

- start in `plan` mode
- decide the eval set before changing the system
- keep the rubric simple
- change one thing at a time when possible
