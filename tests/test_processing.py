import unittest
from unittest.mock import patch, mock_open
import json
from data_processing.processing import format_json, process_data

class TestProcessing(unittest.TestCase):
    def setUp(self):
        # init config
        self.test_data = [
            {
                "name": "Recipe1",
                "ingredients": "1 cup chilies\n1 tbsp olive oil\nSalt and pepper to taste",
                "url": "http://example.com/recipe1",
                "image": "http://example.com/images/recipe1.jpg",
                "cookTime": "PT10M",
                "recipeYield": "4",
                "datePublished": "2021-01-01",
                "prepTime": "PT20M",
                "description": "A simple and delicious recipe for using chilies."
            },
            {
                "name": "Recipe2",
                "ingredients": "2 cups water\n1 cup rice\nSalt to taste",
                "url": "http://example.com/recipe2",
                "image": "http://example.com/images/recipe2.jpg",
                "cookTime": "PT20M",
                "recipeYield": "2",
                "datePublished": "2021-02-01",
                "prepTime": "PT5M",
                "description": "An easy recipe for plain rice."
            }
        ]

        # Transform JSON to match with the JSON file downloaded
        self.json_test_data = '\n'.join(json.dumps(recipe) for recipe in self.test_data)


    def test_format_json(self):

        with patch('builtins.open', mock_open(read_data=self.json_test_data)) as mock_file:
            # Testa se a função 'format_json' carrega corretamente os dados de um arquivo JSON
            expected_data = self.test_data
            result = format_json('dummy_file.json')
            self.assertEqual(result, expected_data)
            mock_file.assert_called_once_with('dummy_file.json', 'r')


    @patch('data_processing.processing.time_to_minutes')
    @patch('data_processing.processing.min_distance_to_chili')
    @patch('data_processing.processing.calculate_difficulty')
    def test_process_data(self, mock_calculate_difficulty, mock_min_distance_to_chili, mock_time_to_minutes):

        with patch('builtins.open', mock_open(read_data=self.json_test_data)) as mock_file:

            # Config mocks
            mock_min_distance_to_chili.side_effect = lambda ingredient: 0 if "chilies" in ingredient else 2
            mock_time_to_minutes.side_effect = lambda x: 20 if "PT20M" in x else 30  # Ajuste conforme necessário
            mock_calculate_difficulty.side_effect = lambda row: "Easy" if row.get('total_time', 0) <= 30 else "Medium"

            filtered_recipes, average_times_filtered = process_data('dummy_file.json')

            #verify
            self.assertEqual(len(filtered_recipes), 1)  # Apenas uma receita tem 'chilies'
            self.assertEqual(filtered_recipes.iloc[0]['difficulty'], 'Easy')
            self.assertTrue('Easy' in average_times_filtered['difficulty'].values)


if __name__ == '__main__':
    unittest.main()
