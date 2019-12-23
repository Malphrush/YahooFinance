from setuptools import setup

setup(
    name='PythonFinance',
    version='1.0',
    packages=['venv.Lib.site-packages.bs4', 'venv.Lib.site-packages.bs4.tests', 'venv.Lib.site-packages.bs4.builder',
              'venv.Lib.site-packages.pip', 'venv.Lib.site-packages.pip._vendor',
              'venv.Lib.site-packages.pip._vendor.idna', 'venv.Lib.site-packages.pip._vendor.pep517',
              'venv.Lib.site-packages.pip._vendor.pytoml', 'venv.Lib.site-packages.pip._vendor.certifi',
              'venv.Lib.site-packages.pip._vendor.chardet', 'venv.Lib.site-packages.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip._vendor.distlib', 'venv.Lib.site-packages.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip._vendor.msgpack', 'venv.Lib.site-packages.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip._vendor.urllib3.util', 'venv.Lib.site-packages.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip._vendor.colorama', 'venv.Lib.site-packages.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treebuilders', 'venv.Lib.site-packages.pip._vendor.progress',
              'venv.Lib.site-packages.pip._vendor.requests', 'venv.Lib.site-packages.pip._vendor.packaging',
              'venv.Lib.site-packages.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip._vendor.webencodings', 'venv.Lib.site-packages.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip._internal', 'venv.Lib.site-packages.pip._internal.cli',
              'venv.Lib.site-packages.pip._internal.req', 'venv.Lib.site-packages.pip._internal.vcs',
              'venv.Lib.site-packages.pip._internal.utils', 'venv.Lib.site-packages.pip._internal.models',
              'venv.Lib.site-packages.pip._internal.network', 'venv.Lib.site-packages.pip._internal.commands',
              'venv.Lib.site-packages.pip._internal.operations', 'venv.Lib.site-packages.pip._internal.distributions',
              'venv.Lib.site-packages.pip._internal.distributions.source', 'venv.Lib.site-packages.idna',
              'venv.Lib.site-packages.lxml', 'venv.Lib.site-packages.lxml.html', 'venv.Lib.site-packages.lxml.includes',
              'venv.Lib.site-packages.lxml.isoschematron', 'venv.Lib.site-packages.pytz',
              'venv.Lib.site-packages.numpy', 'venv.Lib.site-packages.numpy.ma',
              'venv.Lib.site-packages.numpy.ma.tests', 'venv.Lib.site-packages.numpy.doc',
              'venv.Lib.site-packages.numpy.fft', 'venv.Lib.site-packages.numpy.fft.tests',
              'venv.Lib.site-packages.numpy.lib', 'venv.Lib.site-packages.numpy.lib.tests',
              'venv.Lib.site-packages.numpy.core', 'venv.Lib.site-packages.numpy.core.tests',
              'venv.Lib.site-packages.numpy.f2py', 'venv.Lib.site-packages.numpy.f2py.tests',
              'venv.Lib.site-packages.numpy.tests', 'venv.Lib.site-packages.numpy.compat',
              'venv.Lib.site-packages.numpy.compat.tests', 'venv.Lib.site-packages.numpy.linalg',
              'venv.Lib.site-packages.numpy.linalg.tests', 'venv.Lib.site-packages.numpy.random',
              'venv.Lib.site-packages.numpy.random.tests', 'venv.Lib.site-packages.numpy.random.tests.data',
              'venv.Lib.site-packages.numpy.testing', 'venv.Lib.site-packages.numpy.testing.tests',
              'venv.Lib.site-packages.numpy.testing._private', 'venv.Lib.site-packages.numpy.distutils',
              'venv.Lib.site-packages.numpy.distutils.tests', 'venv.Lib.site-packages.numpy.distutils.command',
              'venv.Lib.site-packages.numpy.distutils.fcompiler', 'venv.Lib.site-packages.numpy.matrixlib',
              'venv.Lib.site-packages.numpy.matrixlib.tests', 'venv.Lib.site-packages.numpy.polynomial',
              'venv.Lib.site-packages.numpy.polynomial.tests', 'venv.Lib.site-packages.pandas',
              'venv.Lib.site-packages.pandas.io', 'venv.Lib.site-packages.pandas.io.sas',
              'venv.Lib.site-packages.pandas.io.json', 'venv.Lib.site-packages.pandas.io.excel',
              'venv.Lib.site-packages.pandas.io.formats', 'venv.Lib.site-packages.pandas.io.msgpack',
              'venv.Lib.site-packages.pandas.io.clipboard', 'venv.Lib.site-packages.pandas.api',
              'venv.Lib.site-packages.pandas.api.types', 'venv.Lib.site-packages.pandas.api.extensions',
              'venv.Lib.site-packages.pandas.core', 'venv.Lib.site-packages.pandas.core.ops',
              'venv.Lib.site-packages.pandas.core.util', 'venv.Lib.site-packages.pandas.core.tools',
              'venv.Lib.site-packages.pandas.core.arrays', 'venv.Lib.site-packages.pandas.core.dtypes',
              'venv.Lib.site-packages.pandas.core.sparse', 'venv.Lib.site-packages.pandas.core.groupby',
              'venv.Lib.site-packages.pandas.core.indexes', 'venv.Lib.site-packages.pandas.core.reshape',
              'venv.Lib.site-packages.pandas.core.internals', 'venv.Lib.site-packages.pandas.core.computation',
              'venv.Lib.site-packages.pandas.util', 'venv.Lib.site-packages.pandas._libs',
              'venv.Lib.site-packages.pandas._libs.tslibs', 'venv.Lib.site-packages.pandas.tests',
              'venv.Lib.site-packages.pandas.tests.io', 'venv.Lib.site-packages.pandas.tests.io.sas',
              'venv.Lib.site-packages.pandas.tests.io.json', 'venv.Lib.site-packages.pandas.tests.io.excel',
              'venv.Lib.site-packages.pandas.tests.io.parser', 'venv.Lib.site-packages.pandas.tests.io.formats',
              'venv.Lib.site-packages.pandas.tests.io.msgpack', 'venv.Lib.site-packages.pandas.tests.io.pytables',
              'venv.Lib.site-packages.pandas.tests.api', 'venv.Lib.site-packages.pandas.tests.util',
              'venv.Lib.site-packages.pandas.tests.frame', 'venv.Lib.site-packages.pandas.tests.tools',
              'venv.Lib.site-packages.pandas.tests.arrays', 'venv.Lib.site-packages.pandas.tests.arrays.sparse',
              'venv.Lib.site-packages.pandas.tests.arrays.interval',
              'venv.Lib.site-packages.pandas.tests.arrays.categorical', 'venv.Lib.site-packages.pandas.tests.config',
              'venv.Lib.site-packages.pandas.tests.dtypes', 'venv.Lib.site-packages.pandas.tests.dtypes.cast',
              'venv.Lib.site-packages.pandas.tests.scalar', 'venv.Lib.site-packages.pandas.tests.scalar.period',
              'venv.Lib.site-packages.pandas.tests.scalar.interval',
              'venv.Lib.site-packages.pandas.tests.scalar.timedelta',
              'venv.Lib.site-packages.pandas.tests.scalar.timestamp', 'venv.Lib.site-packages.pandas.tests.series',
              'venv.Lib.site-packages.pandas.tests.series.indexing', 'venv.Lib.site-packages.pandas.tests.sparse',
              'venv.Lib.site-packages.pandas.tests.sparse.frame', 'venv.Lib.site-packages.pandas.tests.sparse.series',
              'venv.Lib.site-packages.pandas.tests.tslibs', 'venv.Lib.site-packages.pandas.tests.window',
              'venv.Lib.site-packages.pandas.tests.generic', 'venv.Lib.site-packages.pandas.tests.groupby',
              'venv.Lib.site-packages.pandas.tests.groupby.aggregate', 'venv.Lib.site-packages.pandas.tests.indexes',
              'venv.Lib.site-packages.pandas.tests.indexes.multi', 'venv.Lib.site-packages.pandas.tests.indexes.period',
              'venv.Lib.site-packages.pandas.tests.indexes.interval',
              'venv.Lib.site-packages.pandas.tests.indexes.datetimes',
              'venv.Lib.site-packages.pandas.tests.indexes.timedeltas', 'venv.Lib.site-packages.pandas.tests.reshape',
              'venv.Lib.site-packages.pandas.tests.reshape.merge', 'venv.Lib.site-packages.pandas.tests.tseries',
              'venv.Lib.site-packages.pandas.tests.tseries.holiday',
              'venv.Lib.site-packages.pandas.tests.tseries.offsets',
              'venv.Lib.site-packages.pandas.tests.tseries.frequencies', 'venv.Lib.site-packages.pandas.tests.indexing',
              'venv.Lib.site-packages.pandas.tests.indexing.interval',
              'venv.Lib.site-packages.pandas.tests.indexing.multiindex', 'venv.Lib.site-packages.pandas.tests.plotting',
              'venv.Lib.site-packages.pandas.tests.resample', 'venv.Lib.site-packages.pandas.tests.extension',
              'venv.Lib.site-packages.pandas.tests.extension.base',
              'venv.Lib.site-packages.pandas.tests.extension.json',
              'venv.Lib.site-packages.pandas.tests.extension.list',
              'venv.Lib.site-packages.pandas.tests.extension.arrow',
              'venv.Lib.site-packages.pandas.tests.extension.decimal', 'venv.Lib.site-packages.pandas.tests.internals',
              'venv.Lib.site-packages.pandas.tests.arithmetic', 'venv.Lib.site-packages.pandas.tests.reductions',
              'venv.Lib.site-packages.pandas.tests.computation', 'venv.Lib.site-packages.pandas.arrays',
              'venv.Lib.site-packages.pandas.compat', 'venv.Lib.site-packages.pandas.compat.numpy',
              'venv.Lib.site-packages.pandas.errors', 'venv.Lib.site-packages.pandas._config',
              'venv.Lib.site-packages.pandas.tseries', 'venv.Lib.site-packages.pandas.plotting',
              'venv.Lib.site-packages.pandas.plotting._matplotlib', 'venv.Lib.site-packages.certifi',
              'venv.Lib.site-packages.chardet', 'venv.Lib.site-packages.chardet.cli', 'venv.Lib.site-packages.urllib3',
              'venv.Lib.site-packages.urllib3.util', 'venv.Lib.site-packages.urllib3.contrib',
              'venv.Lib.site-packages.urllib3.contrib._securetransport', 'venv.Lib.site-packages.urllib3.packages',
              'venv.Lib.site-packages.urllib3.packages.backports',
              'venv.Lib.site-packages.urllib3.packages.ssl_match_hostname', 'venv.Lib.site-packages.dateutil',
              'venv.Lib.site-packages.dateutil.tz', 'venv.Lib.site-packages.dateutil.parser',
              'venv.Lib.site-packages.dateutil.zoneinfo', 'venv.Lib.site-packages.requests',
              'venv.Lib.site-packages.soupsieve', 'venv.Lib.site-packages.matplotlib',
              'venv.Lib.site-packages.matplotlib.tri', 'venv.Lib.site-packages.matplotlib.axes',
              'venv.Lib.site-packages.matplotlib.cbook', 'venv.Lib.site-packages.matplotlib.style',
              'venv.Lib.site-packages.matplotlib.compat', 'venv.Lib.site-packages.matplotlib.testing',
              'venv.Lib.site-packages.matplotlib.testing.jpl_units', 'venv.Lib.site-packages.matplotlib.backends',
              'venv.Lib.site-packages.matplotlib.backends.qt_editor', 'venv.Lib.site-packages.matplotlib.sphinxext',
              'venv.Lib.site-packages.matplotlib.projections', 'venv.Lib.site-packages.mpl_toolkits.mplot3d',
              'venv.Lib.site-packages.mpl_toolkits.axes_grid', 'venv.Lib.site-packages.mpl_toolkits.axes_grid1',
              'venv.Lib.site-packages.mpl_toolkits.axisartist', 'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.idna',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.pytoml',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.certifi',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.chardet',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.distlib',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.msgpack',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.urllib3.util',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.colorama',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.lockfile',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.progress',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.requests',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.packaging',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.webencodings',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._internal',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._internal.req',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._internal.vcs',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._internal.utils',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._internal.models',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._internal.commands',
              'venv.Lib.site-packages.pip-10.0.1-py3.8.egg.pip._internal.operations', 'yahoofinance',
              'yahoofinance.graph', 'yahoofinance.query'],
    url='https://github.com/Malphrush/YahooFinance',
    license='MIT License',
    author='Henry Malphrus',
    author_email='',
    description='Program for getting and plotting historical stock data from Yahoo Finance'
)
