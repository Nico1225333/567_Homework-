import unittest
from unittest.mock import patch, Mock
from github_api import get_repositories


class TestGitHub(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_repositories(self, mock_get):
        repos = Mock()
        repos.status_code = 200
        repos.json.return_value = [
            {"name": "Triangle"},
            {"name": "Homework"}
        ]
        repos.links = {}

        triangle = Mock()
        triangle.status_code = 200
        triangle.json.return_value = [{"sha": "a"}, {"sha": "b"}]
        triangle.links = {}

        homework = Mock()
        homework.status_code = 200
        homework.json.return_value = [{"sha": "c"}]
        homework.links = {}

        mock_get.side_effect = [repos, triangle, homework]

        result = get_repositories("testuser")

        self.assertEqual(result, [("Triangle", 2), ("Homework", 1)])
        self.assertEqual(mock_get.call_count, 3)

    @patch("github_api.requests.get")
    def test_no_repositories(self, mock_get):
        response = Mock()
        response.status_code = 200
        response.json.return_value = []
        response.links = {}
        mock_get.return_value = response

        self.assertEqual(get_repositories("testuser"), [])
        mock_get.assert_called_once()

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
        self.assertEqual(mock_get.call_count, 2)

    @patch("github_api.requests.get")
    def test_blank_username(self, mock_get):
        with self.assertRaises(ValueError):
            get_repositories("")

        mock_get.assert_not_called()

    @patch("github_api.requests.get")
    def test_invalid_input(self, mock_get):
        with self.assertRaises(ValueError):
            get_repositories(123)

        mock_get.assert_not_called()


if __name__ == "__main__":
    unittest.main()
