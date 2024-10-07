import unittest

from ..Account import Account

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        test_account = Account("Dariusz", "Januszewski")
        self.assertEqual(test_account.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(test_account.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(test_account.saldo, 0, "Saldo nie jest zerowe!")

    #tutaj proszę dodawać nowe testy