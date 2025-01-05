import yfinance as yf

indian_etfs = {
    "ICICI Prudential Bluechip Fund": "ICICINIFTY.NS",  # Bluechip ETF
    "HDFC Top 100 Fund": "HDFCNIFETF.NS",  # Nifty ETF
    "UTI Nifty Index Fund": "UTINIFTY50.NS",  # Nifty Index ETF
    "SBI Bluechip Fund": "SBINIF50.NS",  # Bluechip ETF
    "Axis Bluechip Fund": "AXISNIFTY.NS",  # Nifty 50 ETF
    "Franklin India Bluechip Fund": "FRANKLININDIA.NS",  # Nifty ETF
    "Mirae Asset Large Cap Fund": "MIRAEETF.NS",  # Large Cap ETF
    "Kotak Standard Multicap Fund": "KOTAKNIFTY.NS",  # Nifty ETF
    "Reliance Large Cap Fund": "NIFTYBEES.NS",  # Nifty 50 ETF
    "Birla Sun Life Frontline Equity Fund": "BIRLANIFTY.NS",  # Frontline ETF
    "IDFC Nifty Fund": "IDFCNIFTY.NS",  # Nifty ETF
    "DSP BlackRock Top 100 Equity Fund": "DSPNIFTY100.NS",  # Nifty 100 ETF
    "HDFC Balanced Advantage Fund": "HDFCBALANCED.NS",  # Balanced ETF
    "ICICI Prudential Equity & Debt Fund": "ICICIETF.NS",  # Equity ETF
    "L&T India Value Fund": "LTVALUEETF.NS",  # Value Fund ETF
    "Kotak Tax Saver Fund": "KOTAKTAXETF.NS",  # Tax Saver ETF
    "Tata Equity P/E Fund": "TATAEQUITYETF.NS",  # P/E Ratio Fund ETF
    "UTI Equity Fund": "UTIEQUITYETF.NS",  # Equity ETF
    "Invesco India Growth Fund": "INVESCOETF.NS",  # Growth Fund ETF
    "Sundaram Select Focus Fund": "SUNDARAMSELECTETF.NS",  # Focus ETF
    "Franklin India Equity Fund": "FRANKLINEQUITYETF.NS",  # Equity ETF
    "Mirae Asset Emerging Bluechip Fund": "MIRAEEMERGEBLUEETF.NS",  # Emerging Bluechip ETF
    "Canara Robeco Bluechip Equity Fund": "CANARABLUECHIPETF.NS",  # Bluechip ETF
    "Axis Long Term Equity Fund": "AXISLONGETF.NS",  # Long-Term ETF
    "SBI Small Cap Fund": "SBISMALLCAPETF.NS",  # Small Cap ETF
    "HDFC Hybrid Equity Fund": "HDFCHYBRIDETF.NS",  # Hybrid Equity ETF
    "ICICI Prudential Growth Fund": "ICICIGROWETF.NS",  # Growth Fund ETF
    "L&T India Growth Fund": "LTINDIAGROWETF.NS",  # Growth Fund ETF
    "Birla Sun Life Equity Fund": "BIRLASUNEQUITYETF.NS",  # Equity Fund ETF
    "Tata Small Cap Fund": "TATASMALLCAPETF.NS",  # Small Cap ETF
    "DSP BlackRock Equity Fund": "DSPEQUITYETF.NS",  # Equity ETF
    "Nippon India Growth Fund": "NIPPONINDIAGROWETF.NS",  # Growth ETF
    "Franklin India High Growth Companies Fund": "FRANKLINHIGHGROWTHEETF.NS",  # High Growth ETF
    "Mirae Asset India Equity Fund": "MIRAEINDIAEQUITYETF.NS",  # India Equity ETF
    "HDFC Small Cap Fund": "HDFCSMALLCAPETF.NS",  # Small Cap ETF
    "UTI Small Cap Fund": "UTISMALLCAPETF.NS",  # Small Cap ETF
    "ICICI Prudential Nifty Next 50 Index Fund": "ICICINIFTYNEXT50.NS",  # Next 50 ETF
    "Kotak Nifty ETF": "KOTAKNIFTYNEXT50.NS",  # Nifty Next 50 ETF
    "Reliance ETF Nifty 50": "RELIANCEETF.NS",  # Nifty 50 ETF
    "Aditya Birla Sun Life Nifty 50 ETF": "ABSLNIFTY50ETF.NS",  # Nifty 50 ETF
    "Tata Nifty 50 ETF": "TATANIFTY50ETF.NS",  # Nifty 50 ETF
    "Franklin India Nifty 50 ETF": "FRANKLININDIAETF.NS",  # Nifty 50 ETF
    "ICICI Prudential Sensex ETF": "ICICISENSEXETF.NS",  # Sensex ETF
    "Mirae Asset Nifty 50 ETF": "MIRAEASSETNIFTY50ETF.NS",  # Nifty 50 ETF
    "HDFC Nifty ETF": "HDFCNIFTYETF.NS",  # Nifty ETF
    "SBI Nifty ETF": "SBINIFTYETF.NS",  # Nifty ETF
    "Aditya Birla Sun Life Nifty 50 Index Fund": "BIRLAFNIFTY50ETF.NS",  # Nifty ETF
    "Axis Nifty 50 ETF": "AXISNIFTY50ETF.NS",  # Nifty ETF
    "L&T Nifty ETF": "LTNIFTYETF.NS",  # Nifty ETF
    "Kotak Nifty 50 ETF": "KOTAKNIFTY50ETF.NS",  # Nifty ETF
    "Nippon India Nifty 50 ETF": "NIPPONINDIANIFTY50ETF.NS",  # Nifty 50 ETF
    "Canara Robeco Nifty 50 ETF": "CANARANIFTY50ETF.NS",  # Nifty 50 ETF
    "Sundaram Nifty 50 ETF": "SUNDARANNIFTY50ETF.NS",  # Nifty 50 ETF
    "Franklin India Nifty 50 Index Fund": "FRANKLININDIANIFTY50ETF.NS",  # Nifty 50 ETF
    "Mirae Asset Nifty Next 50 ETF": "MIRAEASSETNIFTYNEXT50ETF.NS",  # Next 50 ETF
    "ICICI Prudential Nifty 50 ETF": "ICICINIFTY50ETF.NS",  # Nifty 50 ETF
    "Tata Nifty Next 50 ETF": "TATANIFTYNEXT50ETF.NS",  # Next 50 ETF
    "Aditya Birla Sun Life Nifty Next 50 ETF": "BIRLANIFTYNEXT50ETF.NS",  # Next 50 ETF
    "HDFC Nifty Next 50 ETF": "HDFCNIFTYNEXT50ETF.NS",  # Next 50 ETF
    "Axis Nifty Next 50 ETF": "AXISNIFTYNEXT50ETF.NS",  # Next 50 ETF
    "Reliance Nifty Next 50 ETF": "NIPPONINDIANIFTYNEXT50ETF.NS",  # Next 50 ETF
    "L&T Nifty Next 50 ETF": "LTNIFTYNEXT50ETF.NS",  # Next 50 ETF
    "SBI Nifty Next 50 ETF": "SBINIFTYNEXT50ETF.NS",  # Next 50 ETF
    "Kotak Nifty Next 50 ETF": "KOTAKNIFTYNEXT50ETF.NS",  # Next 50 ETF
    "Franklin India Nifty Next 50 ETF": "FRANKLININDIANIFTYNEXT50ETF.NS",  # Next 50 ETF
    "Tata Nifty Next 50 Index Fund": "TATANIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "HDFC Nifty Next 50 Index Fund": "HDFCNIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "ICICI Prudential Nifty Next 50 Index Fund": "ICICINIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Mirae Asset Nifty Next 50 Index Fund": "MIRAEASSETNIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "UTI Nifty Next 50 Index Fund": "UTINIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Aditya Birla Sun Life Nifty Next 50 Index Fund": "ADITYABIRLANIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Kotak Nifty Next 50 Index Fund": "KOTAKNIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Reliance Nifty Next 50 Index Fund": "RELIANCENIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Sundaram Nifty Next 50 Index Fund": "SUNDARAMNIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Canara Robeco Nifty Next 50 Index Fund": "CANARAROBECONIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Franklin India Nifty Next 50 Index Fund": "FRANKLININDIANIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "SBI Nifty Next 50 Index Fund": "SBINIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "L&T Nifty Next 50 Index Fund": "LTNIFTYNEXT50INDEXETF.NS",  # Next 50 ETF
    "Nippon India Nifty Next 50 Index Fund": "NIPPONINDIANIFTYNEXT50INDEXETF.NS"  # Next 50 ETF
}


# List of ETF symbols
etf_symbols = list(indian_etfs.values())

# Fetch data for each ETF
for symbol in etf_symbols:
    try:
        etf = yf.Ticker(symbol)
        etf_info = etf.info
        print(f"{symbol}: {etf_info['shortName']} - {etf_info['regularMarketPrice']}")
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
