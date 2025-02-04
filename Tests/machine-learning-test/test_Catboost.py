import numpy as np
import unittest
from pysnippets.models.Catboost import CatBoostModel  # Updated import

class TestCatBoostModel(unittest.TestCase):
    def setUp(self):
        self.model = CatBoostModel()
        self.X = np.random.rand(100, 10)
        self.y = np.random.rand(100)

    def test_fit_predict(self):
        self.model.fit(self.X, self.y)
        predictions = self.model.predict(self.X)
        self.assertEqual(predictions.shape, (100,))

    def test_score(self):
        self.model.fit(self.X, self.y)
        score = self.model.score(self.X, self.y)
        self.assertIsInstance(score, float)

if __name__ == '__main__':
    unittest.main()