# open_government
An open source platform for sourcing and distribution of public funding.

## What is the idea of an Open Government?

An open government exists on the internet. It doesn’t have an embassy, or a consulate, or public officials. It is entirely online and powered by contributors (“taxpayers”) whose money is automatically distributed to according to the rules of the government.

Our platform is a transparent and fully democratic implementation of this idea, built on an open source API (and perhaps eventually an application layer).

## How does the proposed system work?

The rules are simple. To become a *citizen*, you pay a monthly fee (your taxes) ranging anywhere from $1-50. You can create one *proposal* at a time; this proposal can enact a _policy_, _program_, or _venture_. A proposal can encompass anything from police force funding

You get three *votes* a month. Your votes determine where your taxes go. If you don’t distribute any of your three votes, a percentage of that month’s payments can go to the maintainer of the platform; with the remainder distributed either 1) equally across all proposals for that month or 2) according to voting defaults set in your profile.

You have a *profile* where you can establish your _policy preferences_. This helps the filtering algorithm surface proposals that will be of interest to you. You can even look into other citizens’ public profiles to see their non-private preferences and voting records.

The API will also provide a framework for making your own proposals. You can provide a description, estimated cost, tags, or any other “meta” information that will help you reach your target audience (vis-a-vis a the proposal-filtering algorithm). 

Proposals will also have a _“proposals like this”_ functionality to assist in uniting the common efforts of citizens.

These proposals are voted on every month by citizens. Every citizen has three votes upon which they may distribute unequal weight, thusly reflecting the relative import of certain things to the voter. The voted-upon proposals are then stack ranked and paid for in order until there is no more budget. 

If half the US used this platform, it would efficiently distribute over $7b in tax revenue every month, while engaging every citizen is a politician with equal power and stake in their government. 

## Creating Better Policy

With enough data, this platform should be able to scientifically predict the economic and social benefit of a proposed policy, program, or venture. We could even leverage machine learning algorithms to aid in policy creation; making our decisions on social engineering as data-driven and empirically rigorous as possible.

We’ve open-sourced this project in the spirit of collaboration, with the end goal of changing the way we think about government. Anyone can adopt it, modify the rules, or even just copy it and host it on their own server.
