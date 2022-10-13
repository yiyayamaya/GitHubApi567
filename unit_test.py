from unittest import mock
import unittest
import test


class TestReq(unittest.TestCase):
    @mock.patch("test.get")
    def test_request_01(self,mock_get):
        mock_get.return_value='can not find user'
        self.assertEqual(test.get("yiyayamaya123123"), 'can not find user')

    # def test_request_02(self):
    #     res = """Repo: CS-546_FinalProject_Covid_Get_Free_Food Number of commits: 22"
    #     Repo: leetcode-company-wise-problems-2022 Number of commits: 30
    #     Repo: mit-deep-learning Number of commits: 30"""
    #     test.get = mock.Mock(return_value=res)
    #
    #     self.assertEqual(test.get("ChaseWangPluviophile"),res)
    #


if __name__ == '__main__':
    unittest.main()
