import unittest
import subprocess
import re
import green

HOSTNAME="68.183.37.68"
PORT="22"

class TestSum(unittest.TestCase):

    def test_succcess(self):
        result = subprocess.run(["./isup", f"{HOSTNAME}", f"{PORT}"], capture_output=True)
        command_succceed = ( str(result.stderr).find("succeeded") > 0 )

        self.assertEqual(command_succceed, True)

if __name__ == '__main__':
    unittest.main()
