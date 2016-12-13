#Pickle
pd.to_pickle(testDF, 'testDF')
#Unpickle
testDF = pd.read_pickle('Pickled_DFs/testDF')