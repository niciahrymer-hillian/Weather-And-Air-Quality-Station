# Weather-And-Air-Quality-Station

### An outdoor sensor node reporting temperature, humidity, pressure, rain, and optionally air quality back to a dashboard — over wifi or long-range LoRa.

![Chain K](https://img.shields.io/badge/Chain%20K-64748B?style=for-the-badge) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge)](LICENSE-GPL) [![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue?style=for-the-badge)](LICENSE-AGPL)

[🎮 Interactive Tour](docs/interactive/index.html) · [📋 Cheat Sheet](docs/CHEATSHEET.pdf) · [📖 Full Lesson](docs/LESSON.pdf) · [🔗 Resources](docs/RESOURCES.pdf) · [📖 Lesson Plan](docs/LESSON_PLAN.md)

<!-- SCREENSHOT PLACEHOLDER: docs/screenshots/overview.png -->

Real-hardware build with an emulation/planning-first path. Part of **Chain K — Hardware & Systems
Foundations**. Can reuse **Walkie-Talkie-Build**'s LoRa hardware for reporting, and its waterproofing
approach directly; sensor/soldering skills come from **Electronics-Circuits-Bench**.

## What this is

This is the project that actually lives outside — everything else in Chain K can sit on a desk. Weather
stations force real decisions about power (no wall outlet outdoors), waterproofing (it rains on purpose
here), and long-running reliability (it has to survive weeks unattended), not just circuit theory. The
four lessons build in the order those real decisions come up: get real sensor readings first, then size
solar power for the worst realistic week (not the best), then pick a reporting connectivity that
actually reaches your mounting spot, then weatherproof it correctly for the long haul. Compute a real
daily energy balance and a real battery-autonomy number — sunny day vs. cloudy week — in the **Solar &
Battery Sizing Simulator** tab before your station is 20 feet up a pole with no wall outlet nearby.

## Prerequisites

| Requirement | Notes |
|---|---|
| A modern browser | Chrome, Firefox, Safari, or Edge — the interactive tour is a single HTML file, no install |
| Python 3.8+ (for the exercises) | Check with `python3 --version` |
| A BME280 + microcontroller (optional for the tour/exercises) | Only needed for a real build — the tour and exercises need nothing but a browser and Python |

## Items Needed

- [ ] A BME280 breakout (temperature/humidity/pressure) — see [Hardware Buying Guide](#hardware-buying-guide-what-to-look-for--red-flags) below (check for a real datasheet, avoid undocumented clones)
- [ ] A tipping-bucket rain gauge with a stated mm-per-tip calibration figure
- [ ] A microcontroller — ESP32 (wifi) or a LoRa32 (LoRa)
- [ ] A solar panel + LiPo + charge controller with low-voltage cutoff, for outdoor power
- [ ] A waterproof enclosure with a vent membrane (not fully sealed)
- [ ] Nothing else required for the tour or exercises — just a browser and Python

## Quick Start

1. **Open the interactive tour.** Double-click `docs/interactive/index.html` — no server, no build step.
2. **Work Lesson 1 (Sensors & real-world data)**, and confirm your rain gauge's mm-per-tip calibration
   figure before treating any tip count as a real measurement.
3. **Do the skeleton-code exercise.**
   ```bash
   cd exercises
   python3 -m venv .venv && source .venv/bin/activate
   pip install pytest
   pytest -v
   ```
   You'll see 9 failing tests. Open `exercises/solar_power_budget.py` and implement the four functions
   — full instructions in [`exercises/README.md`](exercises/README.md).
4. **Work Lesson 2 (Solar power & battery sizing)**, then open the **Solar & Battery Sizing
   Simulator** tab and compare the "Sunny day" and "Cloudy week" presets on the same hardware.
   > ⚠️ **You may get stuck here:** a setup that looks perfectly fine on a sunny-day preset can flip to
   > a real deficit on the cloudy-week preset with nothing else changed — that's the actual lesson, not
   > a bug in the simulator.
5. **Work Lesson 3 (Connectivity)** and test your real wifi signal at the actual mounting spot before
   committing to a board.
6. **Work Lesson 4 (Weatherproofing & reliability)** and confirm your enclosure has an explicit vent
   membrane for the BME280.
7. **Then the Quiz**, then Flashcards/Match/Pop Quiz for review.
8. **Check the Report Card tab** any time. Click **Print / Save as PDF** to keep a dated copy in `docs/`.

## Exercise Overview

| # | Lesson | Concept | Solar & Battery Sizing Simulator tie-in |
|---|---|---|---|
| 1 | Sensors & real-world data | Rain gauge calibration, sensor trust | *(hands-on wiring — no simulator panel)* |
| 2 | Solar power & battery sizing | Daily balance, autonomy | The whole simulator — sunny vs. cloudy presets |
| 3 | Connectivity | Wifi vs. LoRa tradeoffs | *(design decision — no simulator panel)* |
| 4 | Weatherproofing & reliability | Vent membrane, pressure reading, condensation | *(hands-on build — no simulator panel)* |

**Learning path:**
```
Lesson 1 (sensors)  →  Lesson 2 (solar & battery)  →  Lesson 3 (connectivity)  →  Lesson 4 (weatherproofing)
                              ↓
             Solar & Battery Sizing Simulator + exercises/ (solar_power_budget.py)
                              ↓
             Quiz → Flashcards/Match/Pop Quiz → Report Card
```

## Hardware Buying Guide (What to look for & red flags)

**Parts list:** a BME280 (temperature/humidity/pressure, one cheap breakout covers all three), a tipping-
bucket rain gauge sensor, optionally a PMS5003 (PM2.5 particulate) or SCD40 (CO2) sensor for air quality, a
microcontroller (ESP32 is the easy choice — wifi built in), a solar panel + LiPo + charge controller for
outdoor power, and a waterproof enclosure.

**What to look for:** a solar charge controller with **low-voltage cutoff** (protects the LiPo from
over-discharge on cloudy weeks) is worth paying for over a bare panel+battery. Size the solar panel for
your cloudiest expected week, not your average day.

**Red flags:** "solar power bank" listings with no actual charge-controller IC specified, generic humidity
sensors with no datasheet (BME280 clones exist that drift badly), and rain gauges sold with no calibration
figure (mm per tip).

**Common failure points:** condensation inside a sealed enclosure (needs a vent with a membrane, not a
fully sealed box), battery undersized for winter's shorter solar days, and wifi range from an outdoor
mounting spot back to the router — LoRa avoids this entirely if wifi doesn't reach.

**Waterproofing** reuses the exact same pattern as **Walkie-Talkie-Build**'s waterproof option: IP67
enclosure, sealed cable glands, vented (not open) membrane where air needs to get in.

## Wiring Diagrams

**Core build, with the solar variant called out.** ESP32 (or a LoRa32 if reporting over LoRa instead of
wifi) reads the BME280 over I2C and the rain gauge's reed switch on a digital pin; the solar branch (dashed,
yellow) is a drop-in replacement for USB power — panel → charge controller (low-voltage cutoff) → LiPo →
ESP32:

![Weather station wiring diagram](docs/diagrams/wiring.svg)

**Waterproof enclosure, cross-section.** Everything inside an IP67 box, wires crossing the wall only through
sealed cable glands, and — the detail that trips people up — the BME280 sits behind a vent membrane rather
than a sealed wall, because a fully sealed box reads barometric pressure wrong:

![Weather station waterproof enclosure diagram](docs/diagrams/waterproof-enclosure.svg)

## Parts & Pricing

Pulled from the chain-wide [Hardware Shopping List](../HARDWARE_SHOPPING_LIST.md#weather-and-air-quality-station)
— check there for current links; prices drift. **Budget/Mid/Luxury are the same tiers the shopping list
calls Budget/Mid/Premium.**

| Item | Budget | Mid | Luxury |
|---|---|---|---|
| Sensor | BME280 breakout (~$8) — temp/humidity/pressure | + basic rain gauge (~$15) | + PMS5003 particulate (~$25) or SCD40 CO2 (~$35) |
| Microcontroller | ESP32 dev board (~$8–12) | Same | Heltec LoRa32 V3 (~$20–25) if reporting over LoRa instead of wifi |
| **Solar power** *(optional variant)* | Generic 5W panel + basic controller (~$20) | Panel + controller **with low-voltage cutoff** (~$30–35) | Adafruit/Victron-class charge controller (~$20–40) + panel sized for your cloudiest week |
| **Waterproof enclosure** *(optional variant)* | Generic IP67 box + shared cable gland kit | [TICONN IP67 junction box, ~$25](https://www.amazon.com/TICONN-Waterproof-Electrical-Junction-Enclosure/dp/B0B87THLGC) | [Adafruit flanged weatherproof enclosure, ~$15–20](https://www.adafruit.com/product/3931) — glands pre-installed |

Running total, core build only: **~$16–17 budget → ~$23 mid → ~$55–60 luxury** (microcontroller + sensor).
Add the solar and waterproof rows if you're building the full outdoor version — most people building this
project want both, since it's the one project in the chain that has to survive outside unattended.

## Why This Matters (Industry Application)

This is a real IoT sensor-node deployment in miniature: power budgeting, intermittent connectivity, and
long-unattended-uptime are the same problems industrial and agricultural IoT deal with at scale.

## Topics Covered

| Area | What this project covers |
|------|--------------------------|
| Sensors | Temperature, humidity, pressure, rain, optionally air quality |
| Power | Solar charging, battery sizing, and low-voltage cutoff |
| Connectivity | Wifi vs. LoRa for a remote, low-bandwidth node |
| Weatherproofing | A real outdoor enclosure that survives rain and condensation |
| Data | Logging and dashboarding sensor readings over time |
| Reliability | Building something that runs unattended for months |

## How This Connects

Chain K (Hardware & Systems Foundations). Can reuse **Walkie-Talkie-Build**'s LoRa hardware for reporting,
and its waterproofing approach directly; sensor/soldering skills come from **Electronics-Circuits-Bench**.

## Project Layout

```
Weather-And-Air-Quality-Station/
├── docs/
│   ├── interactive/index.html   # tour: lessons, quiz, flashcards, match, pop quiz, solar/battery simulator, report card
│   ├── LESSON_PLAN.md           # short build-plan reference
│   ├── LESSON.pdf               # the full written lesson, printable
│   ├── CHEATSHEET.pdf           # one-page recap, printable
│   ├── RESOURCES.pdf            # further-reading links, printable
│   └── diagrams/                # wiring.svg + waterproof-enclosure.svg
├── exercises/
│   ├── solar_power_budget.py    # skeleton — implement the 4 functions
│   ├── test_solar_power_budget.py
│   └── README.md
└── README.md                    # this file
```

---
Dual licensed — [GPL v3](LICENSE-GPL) and [AGPL v3](LICENSE-AGPL).
