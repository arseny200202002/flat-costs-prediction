from local_development.preprocess.data_preprocess import data_info
import unittest

class PreprocessTest(unittest.TestCase):
    def test_df_creation(self):

        df = data_info([[1, 2], [4, 5]], ['col1', 'col2'])
        print(df.info())
        print(df.columns)
