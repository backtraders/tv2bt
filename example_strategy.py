import tvFeed4bt.config
import tvFeed4bt.feed
tvFeed4bt.config.PORT = 8123
import backtrader as bt
from datetime import datetime
from tvFeed4bt.tv_feed import TVFeed
symbol_name = "BTCUSDT"


class TVTest(bt.Strategy):
    '''
    Simple strat to test TV Feed.
    '''

    def __init__(self):

        self.data_info = dict()

        for i, d in enumerate(self.datas):

            self.data_info[d._name] = dict()
            self.data_info[d._name]['last bar'] = 0

    def next(self):

        print('='*80)
        print(' '*36,'NEXT')
        print('='*80)

        for i, d in enumerate(self.datas):

            dn = d._name
            dt = d.datetime.datetime()
            bar = len(d)

            # Check we have a new bar and are not repeating an old one.
            if bar > self.data_info[d._name]['last bar']:
                print('DATE   : {}'.format(dt))
                print('ASSET  : {}'.format(d._name))
                print('BAR    : {}'.format(bar))
                print('Open   : {}'.format(d.open[0]))
                print('High   : {}'.format(d.high[0]))
                print('Low    : {}'.format(d.low[0]))
                print('Close  : {}'.format(d.close[0]))
                print('Signal : {}'.format(d.signal[0]))
                print('-'*80)

                # Save the last bar processed
                self.data_info[d._name]['last bar'] = bar

    def notify_data(self, data, status, *args, **kwargs):
        print('DATA NOTIF: {}: {}'.format(data._getstatusname(status), ','.join(args)))

# Example Alerts
# --------------
# 1. DATA/OHLC
#    The ticker should be the same as you use for your broker to
#    make life easier. Don't blindly copy the Tradingview Ticker.
#    The rest of the string below should be copied in as it. Tradingview
#    will replace the values inside {{}} with the actual values.
'''
{'symbol':'[INSERT TICKER]', 'DT':'{{time}}', 'O':{{open}}, 'H':{{high}}, 'L':{{low}}, 'C':{{close}}, 'V':{{volume}}, 'action':0}
'''
# 2. SIGNAL OPNLY
#    Again use the same ticker as your broker unless you are adding more than one
#    Signal or data feed for a symbol. If so, you will need to create your own tickers
#    and process them accordingly in the strategy. I.e loop through all datas,
#    decide what to do and then create your order using the data feed that has the
#    correct ticker that the broker is expecting.
#    OHLC can be ommitted and will just appear as NaN
'''
{'symbol':'[INSERT TICKER]', 'action':1}
'''

print('='*80)
print('Starting Example Strategy')
print('All data feeds must have one bar of data before before you will see any output \n'
    'on the console. Please be patient...')
print('For instructions how to use, see:')
print('='*80)

debug = False

# Create an instance of cerebro
cerebro = bt.Cerebro()

# Get Data
data = TVFeed(dataname=symbol_name,  debug=debug)
# data2 = TVFeed(dataname='ETH/USD', debug=debug, kickstart=True)

# Add the data feeds
cerebro.adddata(data)
# cerebro.adddata(data2)


# Add our strategy
cerebro.addstrategy(TVTest)

# Run the strategy
cerebro.run()
