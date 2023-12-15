# tests/test_uganda_data.py
import unittest
from uganda_data_python.uganda_data import UgandaData

class TestUgandaData(unittest.TestCase):
    def setUp(self):

        self.api_key = '8|huYvAStlh1WafnG9LLHHLYRkOye5yg8jFHOLH9au19a40fc1'
        self.uganda_data = UgandaData(self.api_key)

    def test_fetch_districts(self):
        districts = self.uganda_data.fetch_districts()
        self.assertIsInstance(districts, dict)
         # Check if the 'data' key is present in the dictionary
        self.assertIn('data', districts)

    # def test_fetch_district(self):
    #     districts = self.uganda_data.fetch_districts()
    #     if districts:
    #         district_uuid = districts[0].get('uuid')
    #         district_info = self.uganda_data.fetch_district(district_uuid)
    #         self.assertIsInstance(district_info, dict)
    #         self.assertEqual(district_info.get('uuid'), district_uuid)

    # def test_fetch_district_county(self):
    #     districts = self.uganda_data.fetch_districts()
    #     if districts:
    #         district_uuid = districts[0].get('uuid')
    #         county_info = self.uganda_data.fetch_district_county(district_uuid)
    #         self.assertIsInstance(county_info, dict)
    #         # Add assertions based on your API response structure

    # # Add more test cases for other methods

if __name__ == '__main__':
    unittest.main()
