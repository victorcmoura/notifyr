import setuptools

with open('README.md', 'r') as readme:
  long_description = readme.read()

setuptools.setup(
      name='notifyr',
      version='1.1',
      description='Object notification tool that implements observer design pattern at runtime',
      url='https://github.com/victorcmoura/notifyr',
      author='Victor Moura',
      author_email='victor_cmoura@hotmail.com',
      license='GPL-3.0',
      packages=setuptools.find_packages(),
      zip_safe=False,
      long_description_content_type="text/markdown",
      long_description=long_description
)
