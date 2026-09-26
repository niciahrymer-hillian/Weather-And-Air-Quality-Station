# Exercises — Solar Power Budget

A hands-on companion to Lesson 2 in the interactive tour: the real math behind the Solar &amp; Battery
Sizing Simulator tab, and this project's own buying-guide advice to size for your cloudiest expected
week, not your average day.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 9 failing tests — every function in `solar_power_budget.py` currently raises
`NotImplementedError`.

## What to do

Open `solar_power_budget.py`. Implement in this order:

1. `daily_consumption_mah` — the station's real daily energy draw.
2. `daily_harvest_mah` — what a panel actually delivers, with real-world efficiency loss included.
3. `net_daily_balance_mah` — the number that actually matters: does today gain or lose charge.
4. `autonomy_days` — if running a real deficit, how many days until the battery hits its cutoff.

## When you're done

All 9 tests passing means you can answer the actual question this project's Common Mistakes list warns
about: not "does my panel work on a sunny day," but "how many cloudy days in a row can this station
survive before it goes dark" — and whether that number is actually good enough for a real winter.
