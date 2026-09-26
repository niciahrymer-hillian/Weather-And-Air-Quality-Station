"""
Solar Power Budget -- fill in the four functions below.

The real math behind the Solar & Battery Sizing Simulator tab, and
the actual reasoning behind this project's own buying-guide advice:
"size the solar panel for your cloudiest expected week, not your
average day." A panel that comfortably covers a sunny day can still
leave the station running a real daily deficit through a cloudy
winter week -- these functions are how you'd actually catch that
before it happens outdoors, unattended.

Run the tests as you go:  pytest exercises/test_solar_power_budget.py -v
All four start failing. Implement one function, re-run, watch it turn
green, move to the next.
"""


def daily_consumption_mah(avg_current_ma):
    """A sensor node's total daily energy draw, in mAh, given its
    average current draw in mA (most of a real station's day is spent
    asleep, with brief wake-ups to sample sensors and report over
    wifi/LoRa -- avg_current_ma already accounts for that duty cycle).

    >>> daily_consumption_mah(30)
    720
    """
    # TODO: return avg_current_ma * 24
    raise NotImplementedError


def daily_harvest_mah(panel_watts, sun_hours, battery_voltage, efficiency=0.75):
    """How much energy a solar panel actually delivers to the battery
    in a day, in mAh. panel_watts * sun_hours gives watt-hours;
    efficiency derates that for real-world losses (angle, dust,
    temperature -- a panel never delivers its full rated output in
    practice); dividing by battery_voltage converts watt-hours to
    milliamp-hours at that voltage.

    >>> round(daily_harvest_mah(1, 6, 3.7), 2)
    1216.22
    """
    # TODO: return (panel_watts * sun_hours * efficiency * 1000) / battery_voltage
    raise NotImplementedError


def net_daily_balance_mah(harvest_mah, consumption_mah):
    """The actual day's energy balance: positive means the battery
    gains charge that day, negative means it's draining -- the number
    that matters is whether THIS stays positive through your cloudiest
    expected week, not just on an average day.

    >>> round(net_daily_balance_mah(1216.22, 720), 2)
    496.22
    """
    # TODO: return harvest_mah - consumption_mah
    raise NotImplementedError


def autonomy_days(battery_capacity_mah, deficit_mah_per_day, usable_fraction=0.8):
    """If the station is running a real daily deficit (harvest doesn't
    cover consumption), how many days can the battery sustain it before
    hitting the low-voltage cutoff? usable_fraction accounts for the
    fact that a LiPo shouldn't be run all the way to empty -- only a
    fraction of its rated capacity is safely usable. If there's no
    deficit (harvest already covers consumption), the station can run
    indefinitely -- return float('inf').

    >>> round(autonomy_days(2000, 517.3), 2)
    3.09
    >>> autonomy_days(2000, -5)
    inf
    """
    # TODO: if deficit_mah_per_day <= 0, return float('inf'). Otherwise
    # return (battery_capacity_mah * usable_fraction) / deficit_mah_per_day
    raise NotImplementedError
