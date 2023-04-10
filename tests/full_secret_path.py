import unittest

from ..filter_plugins.full_secret_path import full_secret_path

class TestFullSecretPath(unittest.TestCase):
    def test_full_secret_path(self):
        current_path = ['alpha', 'bravo']
        test_cases = [
            {'extra_path': '', 'result': '/alpha/bravo'},
            {'extra_path': '.', 'result': '/alpha/bravo'},
            {'extra_path': '/', 'result': '/'},
            {'extra_path': '//', 'result': '/'},
            {'extra_path': '//.', 'result': '/'},
            {'extra_path': '/.', 'result': '/'},
            {'extra_path': '/./', 'result': '/'},
            {'extra_path': '/./.', 'result': '/'},
            {'extra_path': '/././', 'result': '/'},
            {'extra_path': './', 'result': '/alpha/bravo/'},
            {'extra_path': './.', 'result': '/alpha/bravo'},
            {'extra_path': '././', 'result': '/alpha/bravo/'},
            {'extra_path': '././.', 'result': '/alpha/bravo'},
            {'extra_path': './././', 'result': '/alpha/bravo/'},
            {'extra_path': 'charlie', 'result': '/alpha/bravo/charlie'},
            {'extra_path': 'charlie/delta', 'result': '/alpha/bravo/charlie/delta'},
            {'extra_path': 'charlie/delta/echo', 'result': '/alpha/bravo/charlie/delta/echo'},
            {'extra_path': 'charlie/delta/echo/', 'result': '/alpha/bravo/charlie/delta/echo/'},
            {'extra_path': 'charlie/delta/echo/.', 'result': '/alpha/bravo/charlie/delta/echo'},
        ]

        for test_case in test_cases:
            with self.subTest(extra_path=test_case["extra_path"], expected_result=test_case["result"]):
                self.assertEqual(
                    full_secret_path(
                            test_case['extra_path'],
                            current_path
                    ),
                    test_case['result'],
                    msg="Failed for the following test case: " + str(test_case)
                )

if __name__ == '__main__':
    unittest.main()
