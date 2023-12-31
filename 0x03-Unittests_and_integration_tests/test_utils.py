#!/usr/bin/env python3
'''Module task for test'''

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest import mock
from utils import get_json

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test that a KeyError is raised for the respective inputs """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test that utils.get_json returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """

    def test_memoize(self):
        """ Test that when calling a_property twice, the correct result
        is returned but a_method is only called once using
        assert_called_once
        """

        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
class TestGetJson(unittest.TestCase):

    @patch('requests.get')
    def test_get_json(self, mock_get):
        # Set up fixtures
        test_url1 = "http://example.com"
        test_payload1 = {"payload": True}
        test_url2 = "http://holberton.io"
        test_payload2 = {"payload": False}

        # Set up mock response
        mock_response = Mock()
        mock_response.json.return_value = test_payload1

        # Test get_json with test_url1 and test_payload1
        mock_get.return_value = mock_response
        result1 = get_json(test_url1)
        self.assertEqual(result1, test_payload1)
        mock_get.assert_called_once_with(test_url1)

        # Set up mock response
        mock_response = Mock()
        mock_response.json.return_value = test_payload2

        # Test get_json with test_url2 and test_payload2
        mock_get.return_value = mock_response
        result2 = get_json(test_url2)
        self.assertEqual(result2, test_payload2)
        mock_get.assert_called_once_with(test_url2)

class TestGithubOrgClient(unittest.TestCase):

    def setUp(self):
        # Set up fixtures
        self.org_name = "my_org"
        self.client = GithubOrgClient(self.org_name)
        self.repo_list = ["repo1", "repo2", "repo3"]
        self.repo_license_list = [{"name": "repo1", "license": {"name": "apache-2.0"}},
                                  {"name": "repo2", "license": None},
                                  {"name": "repo3", "license": {"name": "mit"}}]

    def test_public_repos(self):
        # Test public_repos method
        repos = self.client.public_repos()
        self.assertEqual(len(repos), len(self.repo_list))
        for repo in repos:
            self.assertIn(repo["name"], self.repo_list)

    def test_public_repos_with_license(self):
        # Test public_repos method with license argument
        repos = self.client.public_repos(license="apache-2.0")
        expected_repos = [repo for repo in self.repo_license_list if repo["license"] and repo["license"]["name"] == "apache-2.0"]
        self.assertEqual(len(repos), len(expected_repos))
        for repo in repos:
            self.assertIn(repo["name"], [r["name"] for r in expected_repos])
if __name__ == "__main__":
    unittest.main()
