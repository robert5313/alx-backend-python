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
        """ Test for the utils.get_json function to check result. """
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """ test class to tes utils.memoize """

    def test_memoize(self):
        """ Tests the function which occurs when calling a_property,
        the correct result is returned but a_result method """

        class TestClass:
            """ Test Classin which a memoize wrapping is done """

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
    @mock.patch('utils.requests.get')
    def test_get_json(self, mock_get):
        test_url = "http://example.com"
        test_payload = {"payload": True}
        
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        result = get_json(test_url)
        
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

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
