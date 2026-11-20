---
name: parlay-finder
description: Find, research, or evaluate a sports parlay, accumulator, same-game parlay, or Kalshi combo on demand. Use for upcoming or in-play events across sports, player props or team markets, requests for researched picks, and questions about the price, chances, or cash return of a multi-leg ticket.
---

# Parlay Finder

## Choose the slate

- Honor the requested sport, league, venue, date or time window, player vs team markets, number of legs, and stake. Resolve “tonight,” “Sunday,” and “next” using the user's timezone and give the calendar date. Use a stated timezone if the user's is unknown.
- For an unqualified request, search the next open pregame slate across in-season sports. Start with player props on Kalshi and look for a ten-leg ticket when the board supports it. If Kalshi was only a default, consider an available venue with a verified whole-ticket price. Honor an explicit venue. Use $10 as an illustrative budget when the stake is unspecified. If ten credible legs are unavailable, give the strongest supported shorter option and its actual count.
- For “any sport,” select a well-covered available slate. Use multiple sports when requested or when it materially improves an unrestricted search, and say which sports are included. Preserve an explicit date, sport or player-only constraint if the slate is empty. Report the gap and, when helpful, identify the next posted opportunity separately.
- Verify official start times and current status on each invocation. For live requests, record the score, clock or period, player's accumulated stat and market state, then refresh before replying. A locked line, postponed fixture, completed event or stale pregame price cannot support a current play. For historical requests, reconstruct the requested as-of time and exclude later information.

## Research and select

1. Discover actual lines on the chosen venue. Sample viable candidates beyond the first featured ticket. Compare thresholds and prices, including alternatives that change the chance of cashing. Use official schedules, game logs and team or tournament updates. Use credible beat reporters or analysts for consequential late news and cite the original report when available. Use [the sport-specific checks](references/sports.md) for inputs and settlement definitions.
2. For each candidate verify identity, opponent, event, side, metric, threshold and period. Check starter or entry status, availability, expected opportunity, matchup and material conditions. Flag a pending lineup as provisional. Prioritize players whose role remains supported. For live props include how much of the target remains and how much play is left.
3. Calculate hits at the exact threshold from a comparable, named sample with an as-of cutoff. Apply the market's tie, participation and stat definitions. Count zeros in qualifying appearances and report pushes, voids or partial settlements separately. Keep the season or comparable baseline visible when using a recent streak. Describe missing history or role changes and avoid a precise hit rate without a defensible denominator.
4. Check overlap and eligibility. Identify teammates, shared game scripts, nested thresholds and other dependencies. Use joint results from matched games where helpful. Avoid multiplying correlated leg probabilities or presenting the product of singles prices as a tradeable parlay. Remove duplicates, contradictions or combinations the venue rejects.
5. Distinguish a higher chance of cashing from a larger return and from positive expected value. When value is the goal, compare an independently supported joint probability range with the fee-adjusted break-even rate. A past hit rate, price or winning streak cannot establish an edge on its own. If the evidence doesn't justify the price, say so. For a long card, include a shorter option only if it helps the user's stated goal, and price it independently.

## Verify the price and deliver

- Follow [the venue and payout guide](references/markets.md). Seek a **live quote for the exact whole ticket** first. If the custom combo has no quote, look for a previously traded or published ticket within the request and verify every leg before using its price. If neither is available, report the missing quote. Label any hypothetical calculation and give its assumptions. An odds board listing ten individual markets proves only that the legs exist.
- Keep the work read-only. Use public prices or a nonbinding preview. Leave orders, trades and wagers to the user. Check current official location and age eligibility if it affects a real-money venue recommendation. Use the user's stated constraints without inferring eligibility from an account age minimum alone.
- Lead with the ticket, venue, event date, and quote status with time and timezone. Show gross winning return, profit and the amount at risk at the stated stake. Use the verified preview or [the payout calculator](scripts/payout.py) with the whole-ticket price. Identify fees, contract rounding, or special settlement that affects the example.
- List each leg in a compact table with its exact line and observed hits out of qualifying appearances or the most relevant evidence. Name the strongest rationale, the most vulnerable leg or shared dependency, and any pending report that would change the pick. Link the exact ticket or trade record when available and cite the game logs and material news. Treat every future outcome as uncertain.
