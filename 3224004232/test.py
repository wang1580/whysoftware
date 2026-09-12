import unittest
from main import get_simhash, hamming_distance, calc_similarity

class TestSimHash(unittest.TestCase):
    def test_same_text(self):
        text1 = "软件工程是一门重要的学科"
        text2 = "软件工程是一门重要的学科"
        hash1 = get_simhash(text1)
        hash2 = get_simhash(text2)
        dist = hamming_distance(hash1, hash2)
        sim = calc_similarity(dist)
        self.assertEqual(sim, 1.0)

    def test_different_text(self):
        text1 = "软件工程是一门重要的学科"
        text2 = "今天天气很好适合出门散步"
        hash1 = get_simhash(text1)
        hash2 = get_simhash(text2)
        dist = hamming_distance(hash1, hash2)
        sim = calc_similarity(dist)
        self.assertLess(sim, 0.5)

if __name__ == '__main__':
    unittest.main()
