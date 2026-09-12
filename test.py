import unittest
from main import simhash, hamming_distance, calc_similarity

class TestSimHash(unittest.TestCase):
    def test_hash_same(self):
        text1 = "软件工程SimHash查重"
        text2 = "软件工程SimHash查重"
        h1 = simhash(text1)
        h2 = simhash(text2)
        d = hamming_distance(h1,h2)
        self.assertEqual(d,0)

    def test_hash_diff(self):
        t1 = "春天花开"
        t2 = "冬天下雪"
        h1 = simhash(t1)
        h2 = simhash(t2)
        d = hamming_distance(h1,h2)
        sim = calc_similarity(d)
        self.assertLess(sim,0.8)

if __name__ == '__main__':
    unittest.main()
