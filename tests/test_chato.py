import unittest

import Chato
from Chato import _Chato, chato


class TestChatoLib(unittest.TestCase):
    def test_chato_singleton(self):
        chato = Chato.getInstance()
        self.assertIsNotNone(chato)
        self.assertIsInstance(chato, _Chato)

    def test_enable_disable(self):
        # Should Post
        Chato.getInstance().enable()
        self.assertTrue(Chato.getInstance().enabled)
        # Should Disable
        Chato.getInstance().disable()
        self.assertFalse(Chato.getInstance().enabled)

    def test_post_chato_in_slack(self):
        Chato.getInstance().enable()
        chato("From test_post_chato_in_slack", '', 'ops')

    def test_post_chato_when_disabled(self):
        Chato.getInstance().disable()
        Chato.getInstance().chato("Should be disabled", '', 'ops')
