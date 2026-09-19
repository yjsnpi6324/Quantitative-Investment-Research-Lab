import unittest
from datetime import date

from src.evaluation.a_share_calendar import AShareTradingCalendar
from src.evaluation.trading_calendar import horizon_targets


class TradingCalendarTests(unittest.TestCase):
    def setUp(self):
        self.calendar = AShareTradingCalendar()

    def test_mid_autumn_2026_is_closed(self):
        self.assertFalse(self.calendar.is_trading_day(date(2026, 9, 25)))
        self.assertTrue(self.calendar.is_trading_day(date(2026, 9, 28)))

    def test_sep18_targets_skip_mid_autumn(self):
        targets = horizon_targets(
            date(2026, 9, 18), self.calendar.is_trading_day
        )
        self.assertEqual(targets["T+1"], date(2026, 9, 21))
        self.assertEqual(targets["T+3"], date(2026, 9, 23))
        self.assertEqual(targets["T+5"], date(2026, 9, 28))

    def test_sep16_targets_are_strict_future_trading_days(self):
        targets = horizon_targets(
            date(2026, 9, 16), self.calendar.is_trading_day
        )
        self.assertEqual(targets["T+1"], date(2026, 9, 17))
        self.assertEqual(targets["T+3"], date(2026, 9, 21))
        self.assertEqual(targets["T+5"], date(2026, 9, 23))

    def test_unknown_year_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "UNSUPPORTED_TRADING_CALENDAR_YEAR"):
            self.calendar.is_trading_day(date(2027, 1, 4))


if __name__ == "__main__":
    unittest.main()
