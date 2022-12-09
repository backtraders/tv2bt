# tv2bt

This is forked out of tv2bt main package by Dave-Vallance which was created to bridges Tradingview alerts to backtrader. For a full overview and gentle introduction to Deve-Vallance tv2bt please see: https://backtest-rookies.com/2019/11/22/tv2bt-tradingview-to-backtrader-module/

This has been created for Tradingview live feed for Backtrader without using webhook

Backtrader provides link to tradingview feed for backtrader using webhook. Tradingview webhook example in python is also available on github @tv2bt. However, two problems have restricted use of webhook for backtrader feed.
1. accessibility of local computer from tradingview server. What URL should be used as webhook. Flask running on local computer cannot be accessed using Local IPs. You may need to use tunneling software.
2. Web hook on tradingview is available on subscription only

## Installation
Note: Developed for Python 3.x only.

Download and run `python setup.py install develop` or `python3 setup.py install develop`

A simple Flask server used to receive the webhooks from Tradingview is reused without modifying. There is no need to configure some port forwarding on your router to the machine running the datafeed. 

## Testing  
Run example.py for testing the script. 
