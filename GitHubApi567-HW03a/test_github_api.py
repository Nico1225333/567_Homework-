import unittest
from unittest.mock import patch, Mock
from github_api import get_repositories


class TestGitHub(unittest.TestCase):

    @patch("github_api.get_data")
    def test_repositories(self, mock_data):
        mock_data.side_effect = [
            [{"name": "Triangle"}, {"name": "Homework"}],
            [{"sha": "a"}, {"sha": "b"}],
            [{"sha": "c"}]
        ]

        result = get_repositories("testuser")

        self.assertEqual(result, [("Triangle", 2), ("Homework", 1)])

    @patch("github_api.get_data")
    def test_no_repositories(self, mock_data):
        mock_data.return_value = []

        self.assertEqual(get_repositories("testuser"), [])

    @patch("github_api.requests.get")
    def test_empty_repository(self, mock_get):
        repos = Mock()
        repos.status_code = 200
        repos.json.return_value = [{"name": "Empty"}]
        repos.links = {}

        commits = Mock()
        commits.status_code = 409
        commits.json.return_value = {
            "message": "Git Repository is empty."
        }

        mock_get.side_effect = [repos, commits]

        self.assertEqual(get_repositories("testuser"), [("Empty", 0)])

    def test_blank_username(self):
        with self.assertRaises(ValueError):
            get_repositories("")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            get_repositories(123)


if __name__ == "__main__":
    unittest.main()