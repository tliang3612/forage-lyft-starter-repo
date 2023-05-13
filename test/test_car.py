import unittest
from datetime import datetime

from car_factory import CarFactory

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        calliope = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        calliope = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(calliope.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        calliope = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(calliope.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        calliope = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage,
                                               last_service_mileage)
        self.assertFalse(calliope.engine.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0

        glissade = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        glissade = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glissade.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        glissade = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(glissade.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        glissade = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(glissade.engine.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        palindrome = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        palindrome = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(palindrome.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        palindrome = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on)
        self.assertTrue(palindrome.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        palindrome = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on)
        self.assertFalse(palindrome.engine.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        rorschach = CarFactory.create_rorschach(today, last_service_date, current_mileage,
                                               last_service_mileage)
        self.assertTrue(rorschach.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        rorschach = CarFactory.create_rorschach(today, last_service_date, current_mileage,
                                                 last_service_mileage)
        self.assertFalse(rorschach.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        rorschach = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage,
                                                 last_service_mileage)
        self.assertTrue(rorschach.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        rorschach = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage,
                                                 last_service_mileage)
        self.assertFalse(rorschach.engine.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        thovex = CarFactory.create_thovex(today, last_service_date, current_mileage,
                                                 last_service_mileage)
        self.assertTrue(thovex.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        thovex = CarFactory.create_thovex(today, last_service_date, current_mileage,
                                           last_service_mileage)
        self.assertFalse(thovex.battery.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        thovex = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage,
                                           last_service_mileage)
        self.assertTrue(thovex.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        thovex = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage,
                                           last_service_mileage)
        self.assertFalse(thovex.engine.needs_service())


if __name__ == '__main__':
    unittest.main()
