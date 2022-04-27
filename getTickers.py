from matplotlib import ticker
from finviz.screener import Screener

def get_tickers():
    filters = ['cap_mega', 'geo_usa']  # Shows mega-cap US companies
    stock_list = Screener(filters=filters, order='ticker')
    ticker_list = []

    # Export the screener results to .csv
    #stock_list.to_csv("stock.csv")

    # Create a SQLite database
    #stock_list.to_sqlite("stock.sqlite3")

    # Add more filters
    stock_list.add(filters=['fa_div_pos', 'fa_debteq_u1', 'fa_eps5years_pos', 'fa_epsqoq_pos', 'fa_epsyoy_pos', 'fa_epsyoy1_pos', 'fa_estltgrowth_pos', 'fa_netmargin_pos', 'fa_ltdebteq_u1', 'fa_quickratio_o1'])  # Show stocks with high dividend yield

    # Print the table into the console
    #print(stock_list)

    for stock in stock_list[:3]:  # Adds first two stocks from screen to ticker list
        ticker_list.append(stock['Ticker'])
    
    return ticker_list