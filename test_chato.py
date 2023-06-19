import unittest
from unittest import mock

from . import Chato
from . import Notapi

class TestChatoLib(unittest.TestCase):
    def test_chato(self):
        self.assertIsNotNone(Chato.getInstance())

        # Should Post
        Chato.getInstance().enable()
        self.assertTrue(Chato.getInstance().enabled)
        # result = Chato.chato('Chato was tested', 'home.tests.test_chato', 'llau-systems')
        # self.assertEqual(result, 0) # 0 means SUCCESS``                                       
        
        # Should Disable
        Chato.getInstance().disable()
        self.assertFalse(Chato.getInstance().enabled)

class TestNotapi(unittest.TestCase):
    def test_napi(self):
        self.assertIsNotNone(Notapi)
    
    def test_is_domain_live(self):
        self.assertTrue(Notapi.is_domain_live('llau.systems'))

    def test_is_domain_live_invalid_input(self):
        self.assertFalse(Notapi.is_domain_live('this.should.not.exist'))

if __name__ == '__main__':
    unittest.main()