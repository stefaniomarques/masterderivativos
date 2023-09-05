import QuantLib as ql

# Option parameters
option_type = ql.Option.Call
underlying_price = 100.0
strike_price = 105.0
expiry_date = ql.Date(30, 6, 2023)
day_count = ql.Actual365Fixed()
# Market data
risk_free_rate = 0.05
dividend_rate = 0.0
volatility = 0.20

# Create the option and set the pricing engine
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(expiry_date)
option = ql.VanillaOption(payoff, exercise)

# Set up the market data handle
calculation_date = expiry_date - ql.Period(1, ql.Days)
ql.Settings.instance().evaluationDate = calculation_date
underlying = ql.SimpleQuote(underlying_price)
risk_free_curve = ql.FlatForward(calculation_date, risk_free_rate, day_count)
dividend_curve = ql.FlatForward(calculation_date, dividend_rate, day_count)
volatility_handle = ql.BlackConstantVol(calculation_date, ql.TARGET(), volatility, day_count)

process = ql.BlackScholesMertonProcess(ql.QuoteHandle(underlying),
                                       ql.YieldTermStructureHandle(risk_free_curve),
                                       ql.YieldTermStructureHandle(dividend_curve),
                                       ql.BlackVolTermStructureHandle(volatility_handle))

# Set the pricing engine
option.setPricingEngine(ql.AnalyticEuropeanEngine(process))

# Calculate and print the option price
option_price = option.NPV()
print("Option Price: ", option_price)