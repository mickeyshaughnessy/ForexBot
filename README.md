# ForexBot
Contains code and data for machine learning-based forex trading strategy

Based on the initial analysis of the minute-by-minute and daily data for various
currency pairs, a classifier based on the previous n price movements performs poorly, ie
not significantly better than a random model. To further pursue classification based on previous n price movements would require better time resolution, ie ms data. 

The next version will use spectral data - FFT and Shannon entropy - to extract features and classify. 
