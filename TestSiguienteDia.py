import unittest
from SiguienteDia import SiguienteDia


class TestSiguienteDia(unittest.TestCase):

    def test_31_dias_mes(self):
        nextt = SiguienteDia()
        self.assertEqual("Fecha valida", nextt.comprobarFecha31(31,10,2014))
    def test_30_dias_mes(self):
        nextt = SiguienteDia()
        self.assertEqual("Fecha valida", nextt.comprobarFecha30(30,4,2014))
    def test_29_dias_mes(self):
        nextt = SiguienteDia()
        self.assertEqual("Fecha valida bisiesto", nextt.comprobarFecha_febrero(29,2,2016))
    def test_28_dias_mes(self):
        nextt = SiguienteDia()
        self.assertEqual("Fecha valida normal", nextt.comprobarFecha_febrero(28,2,2014))    

if __name__ == "__main__":
    unittest.main()
