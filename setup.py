from setuptools import setup

setup(
   name='tvFeed4bt',
   version='1.0',
   description='Live Tradingview Feed for Backtrader without webhook',
   url='https://github.com/backtraders/tvFeed4bt',
   license='MIT',
   packages=['tvFeed4bt'],
   install_requires=['backtrader','flask'],
)
