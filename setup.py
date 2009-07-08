try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name = "django-tel",
      author = "Aaron Maxwell",
      url = "http://hilomath.com/software/django-tel",
      version = '0.1',
      packages = ['tel'],
      package_dir = {'': 'src'},
      # distutils complain about these, anyone know an easy way to silence it?
      zip_safe = True,
)
