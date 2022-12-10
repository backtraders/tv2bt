# tvFeed4bt

This is forked out of tv2bt main package by Dave-Vallance which was created to bridges Tradingview alerts to backtrader. For a full overview and gentle introduction to Deve-Vallance tv2bt please see: https://backtest-rookies.com/2019/11/22/tv2bt-tradingview-to-backtrader-module/

This has been created for Tradingview live feed for Backtrader without using webhook

Backtrader provides link to tradingview live feed for backtrader using webhook. Tradingview webhook example in python is also available on github @tv2bt. However, two problems have restricted use of webhook for backtrader feed.
1. accessibility of local computer from tradingview server. What URL should be used as webhook? remains the question in the mind of users. Flask running on local computer cannot be accessed using Local IPs. You may need to use tunneling software and many fail to do so.
2. Web hook on tradingview is available on subscription only. Can you by-pass tradingview subscription for live feed.

The forked code from Dave-Vallance is not modified, but have been used along with code developed and added to the package as feed.py. This code also demonstrate that feed of any api or broker can be used in backtrader using tv2bt module without any need for modification.

For implementation of tradingview live data without subscription and tunnel ngrok software, entire python code of tv2bt module by Dave-Vallance without any modification and another code feed.py is used to fetch data from tradingview and providing to the waiting flask server of tv2bt module.
In webhook, data was push by trading view to your IP, however, here we pull the data to computer from tradingview and push it to flaskserver for futher processing. This technique saves energy to recode entire code to create feed code of backtrader.

## Book
In case you are new to python or struggling to use backtrader, you may refer : [Teach Yourself Python Backtrader: Step by Step Backtesting Implementation for Non-programmers](https://www.amazon.com/Teach-Yourself-Python-Backtrader-non-programmers/dp/B09RFYCJ3P).

## Installation
Note: Developed for Python 3.x only.

Download and run `python setup.py install develop` or `python3 setup.py install develop`

A simple Flask server used to receive the webhooks from Tradingview is reused without modifying. There is no need to configure some port forwarding on your router to the machine running the datafeed. 

## Testing  
Run example_strategy.py for testing the script. Make sure that the symbol name in example_strategy and feed.py are same. Presently, BTCUSDT has been configured.
