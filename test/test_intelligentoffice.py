import	unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError



class TestIntelligentOffice(unittest.TestCase):
	@patch.object(GPIO, "input")
	def test_check(self, mock_object:Mock):
	#This is an example of test where I want to mock the GPIO.input() function
		pass



	@patch.object(GPIO, "input")
	def test_check_quadrant_occupancy_first_side(self, mock_object: Mock):
		io= IntelligentOffice()
		io.check_quadrant_occupancy(io.INFRARED_PIN1)
		mock_object.assert_called_once_with(io.INFRARED_PIN1)
		self.assertTrue(io.check_quadrant_occupancy)

	@patch.object(GPIO, "input")
	def test_check_quadrant_occupancy_first_side(self, mock_object: Mock):
		io = IntelligentOffice()
		io.check_quadrant_occupancy(io.INFRARED_PIN2)
		mock_object.assert_called_once_with(io.INFRARED_PIN2)
		self.assertTrue(io.check_quadrant_occupancy)

	@patch.object(GPIO, "input")
	def test_check_quadrant_occupancy_third_side(self, mock_object: Mock):
		io = IntelligentOffice()
		io.check_quadrant_occupancy(io.INFRARED_PIN3)
		mock_object.assert_called_once_with(io.INFRARED_PIN3)
		self.assertTrue(io.check_quadrant_occupancy)

	@patch.object(GPIO, "input")
	def test_check_quadrant_occupancy_fourth_side(self, mock_object: Mock):
		io = IntelligentOffice()
		io.check_quadrant_occupancy(io.INFRARED_PIN4)
		mock_object.assert_called_once_with(io.INFRARED_PIN4)
		self.assertTrue(io.check_quadrant_occupancy)

	@patch.object(GPIO, "input")
	def test_exception_check_quadrant_occupancy(self, mock_object: Mock):
		io = IntelligentOffice()
		with self.assertRaises(IntelligentOfficeError):
			io.check_quadrant_occupancy(10)

	@patch.object(SDL_DS3231, "read_datetime")
	@patch.object(IntelligentOffice, "change_servo_angle")
	def test_blind_open_on_monday_8(self, mock_change_servo_angle, mock_read_datetime):
		io = IntelligentOffice()
		mock_read_datetime.return_value = datetime(2024, 11, 25, 8, 0, 0)
		io.blinds_open = False
		io.manage_blinds_based_on_time()
		mock_change_servo_angle.assert_called_with(12.0)
		self.assertTrue(io.blinds_open)

	@patch.object(SDL_DS3231, "read_datetime")
	@patch.object(IntelligentOffice, "change_servo_angle")
	def test_blind_close_on_monday_20(self, mock_change_servo_angle, mock_read_datetime):
		io = IntelligentOffice()
		mock_read_datetime.return_value = datetime(2024, 11, 25, 20, 0, 0)
		io.blinds_open = True
		io.manage_blinds_based_on_time()
		mock_change_servo_angle.assert_called_with(2.0)
		self.assertFalse(io.blinds_open)

	@patch.object(SDL_DS3231, "read_datetime")
	@patch.object(IntelligentOffice, "change_servo_angle")
	def test_blind_close_on_saturday_20(self, mock_change_servo_angle, mock_read_datetime):
		io = IntelligentOffice()
		mock_read_datetime.return_value = datetime(2024, 11, 30, 8, 0, 0)
		io.blinds_open = False
		io.manage_blinds_based_on_time()
		mock_change_servo_angle.assert_not_called()
		self.assertFalse(io.blinds_open)

	@patch.object(SDL_DS3231, "read_datetime")
	@patch.object(IntelligentOffice, "change_servo_angle")
	def test_blind_open_on_closed_20(self, mock_change_servo_angle, mock_read_datetime):
		io = IntelligentOffice()
		mock_read_datetime.return_value = datetime(2024, 12, 1, 20, 0, 0)
		io.blinds_open = False
		io.manage_blinds_based_on_time()
		mock_change_servo_angle.assert_not_called()
		self.assertFalse(io.blinds_open)




	@patch.object(VEML7700, 'lux', new_callable=int)
	@patch.object(GPIO, 'output')
	@patch.object(IntelligentOffice, 'is_office_empty', return_value=False)
	def test_manage_light_level_office_not_empty(self, mock_is_office_empty, mock_gpio_output, mock_lux):
		io = IntelligentOffice()
		mock_lux = 300
		io.light_on = False
		io.manage_light_level()
		mock_gpio_output.assert_called_with(29, True)
		self.assertTrue(io.light_on)

	@patch.object(GPIO, 'input', return_value=True)
	@patch.object(GPIO, 'output')
	def test_monitor_air_quality_gas_detected(self, mock_gpio_output, mock_gpio_input):
		io = IntelligentOffice()
		io.monitor_air_quality()
		mock_gpio_output.assert_called_with(36, True)  #
		self.assertTrue(io.buzzer_on)


















