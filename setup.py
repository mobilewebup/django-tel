try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name = "django-tel",
      author = "Mobile Web Up",
      url = "http://mobilewebup.com",
      version = '0.3',
      packages = ['tel'],
      package_dir = {'': 'src'},
      # distutils complain about these, anyone know an easy way to silence it?
      zip_safe = True,
)
