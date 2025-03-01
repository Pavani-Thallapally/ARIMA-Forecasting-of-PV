**Aggregator-based-risk-model** \\

Resources and extra documentation for the manuscript "An Aggregator Based Market Modelling with an Impact of Risk under Uncertainty". The model follows a 3 stage approach 

1. Training model 
2. Market model
3. Risk Analysis model

Each of these three levels code are given in the folder and can be executed sequentially as follows
   
1. Training model 

The training model based on historical data of solar and wind output power. 

ARIMA forecasting is executed in 'Arima 20h.py' and 'WT1-11h.py'. 

Number of predicted data points are reduced to 5 scenarios using k-means clustering algorithm as in 'K-means clustering (1).py'.
 
2. Market model

In Market model a bi-level mathematical formulation is modelled in GAMS software as in 'DG_Latin.gms' and 'BS_Latin.gms'.

3. Risk Analysis model

In Risk analysis VaR and CVaR risk parameters are calculated for the above model as in 'AG1-CVaR (1).py' and 'AG2-CVaR.py'.
 
 Results with tables and plots are shown in 'Results and Tables.pdf'.

