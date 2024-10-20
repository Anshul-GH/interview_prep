from unittest import TestCase


class Guru:
    def __init__(self, endpoint: str = 'https://query.wikidata.org/sparql'):
        self.endpoint = endpoint

    def ask(self, question: str):
        pass


class TestGuru(TestCase):

    def test_ask(self):
        guru: Guru = Guru()
        # note these values may change a little as time moves on
        self.assertEqual('68', guru.ask('how old is Tony Blair'))
        self.assertEqual('75', guru.ask('how old is trump'))
        self.assertEqual('8908081', guru.ask('what is the population of London'))
        self.assertEqual('2175601', guru.ask('what is the population of Paris'))