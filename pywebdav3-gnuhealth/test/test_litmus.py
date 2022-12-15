import re
import os
import sys
import time
import shutil
import tarfile
import tempfile
import unittest
import subprocess

testdir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(testdir, '..'))

import pywebdav.server.server

# Run davserver
user = 'test'
password = 'pass'
port = 38028


class Test(unittest.TestCase):
    def setUp(self):

        self.rundir = tempfile.mkdtemp()
        self._ensure_litmus()

    def _ensure_litmus(self):

        litmus_dist = os.path.join(testdir, 'litmus-0.13')
        self.litmus = os.path.join(litmus_dist, 'litmus')
        if not os.path.exists(self.litmus):
            print('Compiling litmus test suite')

            if os.path.exists(litmus_dist):
                shutil.rmtree(litmus_dist)
            with tarfile.open(litmus_dist + '.tar.gz') as tf:
                def is_within_directory(directory, target):
                    
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                
                    tar.extractall(path, members, numeric_owner=numeric_owner) 
                    
                
                safe_extract(tf, path=testdir)
            ret = subprocess.call(['sh', './configure'], cwd=litmus_dist)
            # assert ret == 0
            ret = subprocess.call(['make'], cwd=litmus_dist)
            # assert ret == 0
            litmus = os.path.join(litmus_dist, 'litmus')
            # assert os.path.exists(litmus)

    def tearDown(self):
        print("Cleaning up tempdir")
        shutil.rmtree(self.rundir)

    def test_run_litmus(self):

        result = []
        proc = None
        try:
            print('Starting davserver')
            davserver_cmd = [sys.executable, os.path.join(testdir, '..', 'pywebdav', 'server', 'server.py'), '-D',
                             self.rundir, '-u', user, '-p', password, '-H', 'localhost', '--port', str(port)]
            self.davserver_proc = subprocess.Popen(davserver_cmd)
            # Ensure davserver has time to startup
            time.sleep(1)

            # Run Litmus
            print('Running litmus')
            try:
                ret = subprocess.call([self.litmus, 'http://localhost:%d' % port, user, password])
                results = subprocess.check_output([self.litmus, 'http://localhost:%d' % port, user, password])
            except subprocess.CalledProcessError as ex:
                results = ex.output
            lines = results.decode().split('\n')
            assert len(lines), "No litmus output"
            for line in lines:
                line = line.split('\r')[-1]
                result.append(line)
                if len(re.findall('^ *\d+\.', line)):
                    assert line.endswith('pass'), line

        finally:
            print('\n'.join(result))

            print('Stopping davserver')
            self.davserver_proc.kill()


    def test_run_litmus_noauth(self):

        result = []
        proc = None
        try:
            print('Starting davserver')
            davserver_cmd = [sys.executable, os.path.join(testdir, '..', 'pywebdav', 'server', 'server.py'), '-D',
                             self.rundir, '-n', '-H', 'localhost', '--port', str(port)]
            self.davserver_proc = subprocess.Popen(davserver_cmd)
            # Ensure davserver has time to startup
            time.sleep(1)

            # Run Litmus
            print('Running litmus')
            try:
                ret = subprocess.call([self.litmus, 'http://localhost:%d' % port])
                results = subprocess.check_output([self.litmus, 'http://localhost:%d' % port])
            except subprocess.CalledProcessError as ex:
                results = ex.output
            lines = results.decode().split('\n')
            assert len(lines), "No litmus output"
            for line in lines:
                line = line.split('\r')[-1]
                result.append(line)
                if len(re.findall('^ *\d+\.', line)):
                    assert line.endswith('pass'), line

        finally:
            print('\n'.join(result))

            print('Stopping davserver')
            self.davserver_proc.kill()
