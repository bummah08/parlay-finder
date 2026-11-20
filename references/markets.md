# Verify the whole ticket

## Find an offer

Start at the venue's public schedule, combo builder, featured tickets or market listings. Search by a real fixture, player and market available for the requested date. When an unpriced custom build stalls, try an already listed combination that meets the user's constraints and has a trade history. Use targeted searches or bounded, date-filtered listing pages. A prebuilt ticket still needs the same sporting and settlement checks.

Match the identities of **all** legs before using a quote or trade. Verify fixture and date, player or team, statistic, direction, threshold, period, settlement variant and venue. Where possible include the permanent ticket or market link. A copied ticket with a different line, live period, promotion or protection is a different price. An odds aggregator is useful for comparison if its timestamp and venue are clear.

- **Live whole-ticket quote.** Record the positive executable price, its observation time and currency. Check the selected combination is accepted and the price covers the requested amount. For multiple book levels use the volume-weighted fill, or state the size supported. A preview may expire.
- **Last trade.** Record the price for this exact combination and side, the most recent fill time and source. Calculate a conditional payout at that price. If there is no live offer, say so.
- **Unquoted.** List the verified legs and the unavailable payout. If a model estimate is useful, show its assumptions and uncertainty separately. When allowed, try a smaller or otherwise eligible quoted ticket. Never copy its price onto the requested ticket.

## Kalshi public lookups

Use a public venue interface, search tool or read-only data fetch that is available in the current session. Confirm the current public API host and parameter names from the official guide. The documented production base is `https://external-api.kalshi.com/trade-api/v2`. [Public market data](https://docs.kalshi.com/getting_started/quick_start_market_data)

| Public request | Check |
|---|---|
| `GET /markets/{ticker}` | Read an existing combo's status and `mve_selected_legs`. Match each underlying market ticker and side to the selection. Resolve unclear player IDs or protected-market terms through the underlying contract rules. |
| `GET /markets/{ticker}/orderbook` | Inspect the **combo's** bids. A YES buy at price `p` draws on NO bids at `1 − p`, with prices in dollars. Use positive size and the proper side. An empty opposite book or a placeholder ask with zero size supplies no executable offer. |
| `GET /markets/trades?ticker={ticker}` | Match the returned ticker and sort by trade time if needed. Use the price expressed for the side being evaluated, even when the counterparty initiated the trade. Keep the fill timestamp distinct from the time of your lookup. |

A public builder may leave the payout blank while other tickets show prices. Kalshi requests a quote for the entire combination. Use the public order book or trade history for the exact ticket when the preview is blank. Check the current rules for inactive players, protected markets and fractional settlement. [Market details](https://docs.kalshi.com/api-reference/market/get-market) · [Order book](https://docs.kalshi.com/getting_started/orderbook_responses) · [Trades](https://docs.kalshi.com/api-reference/market/get-trades) · [Combo rules](https://help.kalshi.com/en/articles/13823820-combos) · [Fee schedule](https://kalshi.com/fee-schedule)

## Returns and price comparisons

Use the venue's verified total cost and winning receipt first. For a cash stake at decimal odds `d`, gross return is stake times `d`. For a binary contract that pays one dollar, gross return in dollars is the number of winning contracts. Distinguish cash spent on contracts, fees, and unused balance when rounding the number of contracts. Check full-win, full-loss and any material push, void, dead-heat or partial outcomes using the venue's rules. Promo credit can pay differently from cash.

Use the bundled helper on a **single whole-ticket price**. Change directory to the skill folder for these examples. Substitute current evidence for the example prices.

```bash
python3 scripts/payout.py --cents 40 --budget 10
python3 scripts/payout.py --american +180 --budget 10
python3 scripts/payout.py --decimal 2.8 --budget 10
python3 scripts/payout.py --fractional 9/5 --budget 10
```

Supply `--entry-fee` or `--win-fee` only for an amount established for that exact quote and size. For a cents price add `--lot` if the venue requires an observed contract increment. With unknown fees or increments label the calculation approximate and before applicable fees. For a ticket that resolves to either its win value or zero, break-even win probability is actual outlay divided by the winning receipt after applicable payout fees. Use the actual settlement distribution for voidable, partially paying or refunded outcomes.
