# Create setup.py file for uaimodal.py that requires socket
#

from setuptools import setup, find_packages

# setup(name='uaimodal', version='1.0', py_modules=['uaimodal'],long_description=open('README.md').read(), requires=['socket'])
# Setup file for uaimodal.py that requires socket and MediaItems.py and cv2
#
# setup(name='uaimodal', version='1.1', py_modules=['uaimodal'],long_description=open('README.md').read(), requires=['socket', 'MediaItems', 'cv2'])
setup(name='uaimodal', version='1.0.0', py_modules=['uaimodal'], packages=find_packages(), url="https://github.com/vltmedia/uaimodal"
      ,install_requires=["modal",
        ]
      )
