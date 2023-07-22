import pickle
import unicodedata
l=pickle.load(open(r"C:\Users\Lenovo\PycharmProjects\car price predictor2\LinearRegressionModel.pkl",'rb'))
t1= unicodedata.normalize('NFC',l)#normalization