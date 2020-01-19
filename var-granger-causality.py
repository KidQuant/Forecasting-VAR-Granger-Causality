import pandas as pd
import numpy as np
import quandl
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

quandl.ApiConfig.api_key = 'tJKSQn1pHLbyo1mu1wYn'

gold = quandl.get('LBMA/GOLD')
silver = quandl.get('LBMA/SILVER')
oil = quandl.get('CHRIS/ICE_G6')
dollar = quandl.get('CHRIS/ICE_DX1')
dow_jones = quandl.get('BCB/UDJIAD1')
treasury = quandl.get('FRED/DGS10')

