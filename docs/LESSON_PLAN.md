# 📖 Lesson Plan — Weather-And-Air-Quality-Station

> **Chain K — Hardware & Systems Foundations** | An outdoor sensor node reporting temperature,
> humidity, pressure, rain, and optionally air quality back to a dashboard — over wifi or long-range
> LoRa.

## What This Project Is

This is the project that actually lives outside — everything else in Chain K can sit on a desk. Weather
stations force real decisions about power (no wall outlet outdoors), waterproofing (it rains on purpose
here), and long-running reliability (it has to survive weeks unattended), not just circuit theory. The
four lessons build in the order those real decisions come up: get real sensor readings first, then size
solar power for the worst realistic week (not the best), then pick a reporting connectivity that
actually reaches your mounting spot, then weatherproof it correctly for the long haul.

## Learning Objectives

By the end I can:

1. Wire and read a BME280 (temperature/humidity/pressure) and a tipping-bucket rain gauge.
2. Size a solar panel and battery for a real deficit scenario — a cloudy week, not an average day —
   and compute how many days of autonomy a given battery actually provides.
3. Choose wifi vs. LoRa for reporting, based on real range and power tradeoffs, not just what's
   familiar.
4. Weatherproof an outdoor enclosure correctly, including the detail that trips people up: a sealed
   box reads barometric pressure wrong.

## Software You Will Use

- Arduino IDE or MicroPython for the ESP32 (or LoRa32, if reporting over LoRa).
- A dashboard/logging target (a simple MQTT broker, a spreadsheet via webhook, or Home Assistant).

## Build Order

1. Wire the BME280 (I2C) and rain gauge (digital pin, reed switch); confirm you're getting believable
   readings before adding any power constraints.
   🔗 [Random Nerd Tutorials — ESP32 with BME280 using Arduino IDE](https://randomnerdtutorials.com/esp32-bme280-arduino-ide-pressure-temperature-humidity/)
2. Size the solar panel and battery for your cloudiest expected week, not your average day — compute
   your own daily consumption, harvest, and autonomy numbers before ordering hardware.
   🎥 [How To Size A Solar Charge Controller? (MPPT & PWM)](https://www.youtube.com/watch?v=32EKKl1E6iA) (KiloWatt Maker with Younes)
3. Decide wifi vs. LoRa for reporting, based on your actual mounting spot's wifi range back to the
   router, not just which radio you already have on hand.
   🔗 [LoRaWAN vs Wi-Fi for IoT Sensors: Range, Power and Gateway Comparison](https://robustel.com/lorawan-vs-wi-fi-for-iot-sensors-range-power-and-gateway-comparison/) (Robustel)
4. Weatherproof the enclosure — a vent membrane (not a sealed wall) where the BME280 sits, sealed
   cable glands everywhere else — reusing Walkie-Talkie-Build's exact waterproofing pattern.
   🔗 [How to Design an IP65/IP67 Enclosure for Outdoor Electronics](https://ohmframe.com/blog/how-to-design-enclosure-ip65-ip67) (Ohmframe)

## Common Mistakes to Avoid

- Condensation inside a sealed enclosure — needs a vent with a membrane, not a fully sealed box.
- Sizing a solar panel or battery for an average or sunny day instead of the cloudiest expected week.
- Battery undersized for winter's shorter solar days.
- Wifi range from an outdoor mounting spot back to the router — LoRa avoids this entirely if wifi
  doesn't reach.
- A fully sealed enclosure reading barometric pressure wrong — the BME280 needs a vent to the outside
  air, not an airtight box.

## Check Your Understanding

The quiz covers real solar-sizing math (harvest vs. consumption vs. autonomy), why a sealed enclosure
reads pressure wrong, the wifi-vs-LoRa tradeoff, and rain gauge calibration reasoning.

## Why This Matters (Industry Application)

This is a real IoT sensor-node deployment in miniature: power budgeting, intermittent connectivity, and
long-unattended-uptime are the same problems industrial and agricultural IoT deal with at scale.

## Reflection Questions

- If your station's battery only has 3 days of autonomy through a cloudy week, what are your actual
  options (bigger panel? bigger battery? lower duty cycle?), and how would you decide between them?
- Why does an outdoor, unattended project force real engineering decisions that a desk-bound project
  can defer indefinitely?
