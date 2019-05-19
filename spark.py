from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession
# import spark.implicits._
from mpapp.rates import *
from pyspark.sql import Row
from pyspark.sql.types import *
#from pyspark.sql.types import StructType


spark = SparkSession.builder.appName('rates').getOrCreate()
data = spark.read.csv("C:/Users/renin prince/Desktop/ML/RecommenderSystems_PyData_2016-master/newchanged.csv",inferSchema=True,header=True)
# datas = spark.read.csv("C:/Users/renin prince/Desktop/ML/RecommenderSystems_PyData_2016-master/rates.csv",inferSchema=True,header=True)
#data1 = spark.read.csv("C:/Users/renin prince/Desktop/Maps/Maps/rates.csv",inferSchema=True,header=True)
Train_data, Test_data = data.randomSplit([0.8,0.2])
als =ALS(maxIter=10,regParam=0.01,userCol='Users',itemCol='Places',ratingCol='Ratings')
model = als.fit(Train_data)
prediction = model.transform(Test_data)
evaluator = RegressionEvaluator(metricName='rmse',labelCol='Ratings',predictionCol='prediction')
rmse = evaluator.evaluate(prediction)
print(rmse)
op = []

def predictor(process):
    U = process
    #det = db.Mapsapp_user.find_one({"first":tofind[-1]})
    #one = (det['first'])
    single_user = data.filter(data['Users']==U).select(['Users','Places','Ratings'])
    #single_user = data1.filter(data1['Users']==one).select(['Users','Places','Ratings'])

    recomendation = model.transform(single_user)
    k = recomendation.count()
    ratings = []
    places = []
    for i in range(k):
        ratings.append(recomendation.collect()[i][3])
        places.append(recomendation.collect()[i][1])
    print(ratings)
    def sort_list(ratings, places):
        pred_values = zip(ratings, places)
        z = [x for _, x in sorted(pred_values)]
        return z
    pred = str(sort_list(ratings, places)[-1])
    P = ['art galleries','dance clubs','juice bars','restaurants','museums','resorts'
     ,'parks','beaches','theaters','religious institutions']
    pls = P[int(pred)]
    op.append(str(U))
    op.append(pls)
    print('Predicted place for ' + 'User '+str(U)+' is: '+ pls)
    print('RMSE: ' + str(rmse))

def predictor1(process1):
    #sort_list(Ratings,us,pl)
    schema = StructType([StructField('Users', IntegerType()),
                 StructField('Places', IntegerType()),
                 StructField('Ratings', IntegerType())
                ])
    det = spark.createDataFrame(dataset, schema)
    #det = spark.createDataFrame(dataset)
    # det = spark.createDataFrame(Row(**x) for x in dataset).show(truncate=False)
    dett = det.select(['Users','Places','Ratings'])
    print(dett)
    unionDF = data.unionAll(dett)
    Train_data, Test_data = dett.randomSplit([0.8,0.2])
    als =ALS(maxIter=10,regParam=0.01,userCol='Users',itemCol='Places',ratingCol='Ratings')
    model = als.fit(Train_data)
    U = process1
    #det = db.Mapsapp_user.find_one({"first":tofind[-1]})
    #one = (det['first'])
    single_user = data.filter(data['Users']==U).select(['Users','Places','Ratings'])
    #single_user = data1.filter(data1['Users']==one).select(['Users','Places','Ratings'])

    recomendation = model.transform(single_user)
    k = recomendation.count()
    ratings = []
    places = []
    for i in range(k):
        ratings.append(recomendation.collect()[i][3])
        places.append(recomendation.collect()[i][1])
    print(ratings)
    def sort_list(ratings, places):
        pred_values = zip(ratings, places)
        z = [x for _, x in sorted(pred_values)]
        return z
    pred = str(sort_list(ratings, places)[-1])
    P = ['art galleries','dance clubs','juice bars','restaurants','museums','resorts'
     ,'parks','beaches','theaters','religious institutions']
    pls = P[int(pred)]
    op.append(str(U))
    op.append(pls)
    print('Predicted place for ' + 'User '+str(U)+' is: '+ pls)
