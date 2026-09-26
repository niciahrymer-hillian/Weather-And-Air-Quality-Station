"""
Tests for solar_power_budget.py. Values independently verified with a
reference implementation before being written here.
"""
import pytest

from solar_power_budget import (
    daily_consumption_mah,
    daily_harvest_mah,
    net_daily_balance_mah,
    autonomy_days,
)


def test_daily_consumption_mah():
    assert daily_consumption_mah(30) == 720


def test_daily_consumption_mah_zero_current():
    assert daily_consumption_mah(0) == 0


def test_daily_harvest_mah_sunny_day():
    assert daily_harvest_mah(1, 6, 3.7) == pytest.approx(1216.22, abs=0.01)


def test_daily_harvest_mah_cloudy_week():
    assert daily_harvest_mah(1, 1, 3.7) == pytest.approx(202.70, abs=0.01)


def test_net_daily_balance_mah_surplus():
    assert net_daily_balance_mah(1216.22, 720) == pytest.approx(496.22, abs=0.01)


def test_net_daily_balance_mah_deficit():
    assert net_daily_balance_mah(202.70, 720) == pytest.approx(-517.30, abs=0.01)


def test_autonomy_days_with_real_deficit():
    assert autonomy_days(2000, 517.3) == pytest.approx(3.09, abs=0.01)


def test_autonomy_days_no_deficit_is_infinite():
    assert autonomy_days(2000, -5) == float('inf')


def test_autonomy_days_zero_deficit_is_infinite():
    assert autonomy_days(2000, 0) == float('inf')
