#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from code_source import get_lineas, parseCuenta, \
	checksum_cuenta, ERR_ILL, formatear_cuenta, fixDigit

class KataBankTest(unittest.TestCase):
	"""docstring for Kata"""

	def test_parse_cuenta(self):
		lineas = get_lineas('resources.txt')
		digitos, error = parseCuenta(lineas)
		self.assertEqual(range(1, 10), digitos)

	def test_checksum_cuenta(self):
		digitos = [3, 4, 5, 8, 8, 2, 8, 6, 5]
		self.assertTrue(checksum_cuenta(digitos))

	def test_checksum_cuenta_false(self):
		digitos = [1, 4, 5, 8, 8, 2, 8, 6, 5]
		self.assertFalse(checksum_cuenta(digitos))

	def test_parse_err(self):
		lineas = get_lineas('test-data/case3/1234_678_-ILL')
		digitos, error = parseCuenta(lineas)
		self.assertEqual(error, ERR_ILL)

	def test_report_account_parse(self):
		lineas = get_lineas('test-data/case3/1234_678_-ILL')
		digitos, error = parseCuenta(lineas)
		s = formatear_cuenta(digitos, error)
		self.assertEqual("1234?678? ILL", s)		

	def test_report_account_parse_ok(self):
		lineas = get_lineas('test-data/case3/000000051')
		digitos, error = parseCuenta(lineas)
		s = formatear_cuenta(digitos, error)
		self.assertEqual("000000051", s)

	def test_report_account_parse_err(self):
		lineas = get_lineas('test-data/case3/000000052-ERR')
		digitos, error = parseCuenta(lineas)
		s = formatear_cuenta(digitos, error)
		self.assertEqual("000000052 ERR", s)

	def test_fix_digit1(self):
		m = (
			(" ", " ", " "),
			(" ", " ", " "),
			(" ", " ", "|"))
		lista_numeros = fixDigit(m)
		self.assertEqual(lista_numeros, [1])

	def test_fix_digit2(self):
		m = (
			(" ", "_", " "),
			("|", "_", "|"),
			("|", "_", "|"))
		lista_numeros = fixDigit(m)
		self.assertEqual(lista_numeros, [0,6])

	def test_correction1(self):
		lineas = get_lineas('test-data/case4/000000051')
		digitos, error = parseCuenta(lineas)
		s = formatear_cuenta(digitos, error)
		self.assertEqual("000000051", s)








if __name__ == '__main__':
    unittest.main()