#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from code_source import get_lineas, parseCuenta, checksum_cuenta

class KataBankTest(unittest.TestCase):
	"""docstring for Kata"""

	def test_parse_cuenta(self):
		lineas = get_lineas('resources.txt')
		self.assertEqual(range(1, 10), parseCuenta(lineas))

	def test_checksum_cuenta(self):
		digitos = [3, 4, 5, 8, 8, 2, 8, 6, 5]
		self.assertTrue(checksum_cuenta(digitos))

	def test_checksum_cuenta_false(self):
		digitos = [1, 4, 5, 8, 8, 2, 8, 6, 5]
		self.assertFalse(checksum_cuenta(digitos))

if __name__ == '__main__':
    unittest.main()