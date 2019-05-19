
us = []
pl = []
Ratings = []
dataset = []
def rating(Holiday,Languages,Nathis,Time,Soqu,relationship,Preference,Foodie,Stress,un):

    art_galleries = 0
    dance_clubs = 0
    juice_bars = 0
    restaurants = 0
    museums = 0
    resorts = 0
    parks = 0
    beaches = 0
    theaters = 0
    religious_institutions = 0
    if Holiday == 1:
        art_galleries += 0.3
    elif Holiday == 2:
        dance_clubs += 0.3
    elif Holiday == 3:
        juice_bars += 0.3
    elif Holiday == 4:
        restaurants += 0.3
    elif Holiday == 5:
        museums += 0.3
    elif Holiday == 6:
        resorts += 0.3
    elif Holiday == 7:
        parks += 0.3
    elif Holiday == 8:
        beaches += 0.3
    elif Holiday == 9:
        theaters += 0.3
    else:
        religious_institutions += 0.3

    if Languages == 1:
        religious_institutions += 0.3
        art_galleries += 0.3
        museums += 0.3

    elif Languages == 2:
        dance_clubs += 0.3
        resorts += 0.3
        restaurants += 0.3
        theaters += 0.3

    elif Languages == 3:
        religious_institutions += 0.3
        art_galleries += 0.3
        museums += 0.3
        parks += 0.3

    elif Languages == 4:
        dance_clubs += 0.3
        resorts += 0.3
        restaurants += 0.3
        theaters += 0.3
        art_galleries += 0.3

    if Nathis == 1:
        religious_institutions += 0.3
        parks += 0.3
        resorts += 0.3
        beaches += 0.3

    elif Nathis == 2:
        art_galleries += 0.3
        religious_institutions += 0.3
        museums += 0.3

    if Time == 1:
        beaches += 0.3
        parks += 0.3
        religious_institutions += 0.3
        art_galleries += 0.3
        museums += 0.3
        theaters += 0.3
        juice_bars += 0.3

    elif Time == 2:
        dance_clubs += 0.3
        resorts += 0.3
        restaurants += 0.3


    elif Time == 3:
        religious_institutions += 0.3
        resorts += 0.3

    if Soqu == 1:
        dance_clubs += 0.3
        resorts += 0.3
        restaurants += 0.3
        theaters += 0.3
        juice_bars += 0.3

    elif Soqu == 2:
        beaches += 0.3
        parks += 0.3
        religious_institutions += 0.3
        art_galleries += 0.3
        museums += 0.3

    if relationship == 1:
        religious_institutions += 0.3
        art_galleries += 0.3
        museums += 0.3
        beaches += 0.3
        parks += 0.3
        resorts += 0.3
        restaurants += 0.3
        theaters += 0.3
        juice_bars += 0.3

    elif relationship == 2:
        beaches += 0.3
        parks += 0.3
        dance_clubs += 0.3
        resorts += 0.3
        restaurants += 0.3
        theaters += 0.3
        juice_bars += 0.3

    if Foodie == 1:
        restaurants += 0.3
        resorts += 0.3

    elif Foodie == 2:
        dance_clubs += 0.3
        juice_bars += 0.3

    if Stress == 1:
       religious_institutions += 0.3
       beaches += 0.3

    elif Stress == 2:
        art_galleries += 0.3
        museums += 0.3
    #print(art_galleries,dance_clubs,juice_bars,restaurants,museums,resorts,parks,beaches,theaters,religious_institutions)
    #Ratings.append('Ratings')
    Ratings.append(int(art_galleries))
    Ratings.append(int(dance_clubs))
    Ratings.append(int(juice_bars))
    Ratings.append(int(restaurants))
    Ratings.append(int(museums))
    Ratings.append(int(resorts))
    Ratings.append(int(parks))
    Ratings.append(int(beaches))
    Ratings.append(int(theaters))
    Ratings.append(int(religious_institutions))


    for i in range(len(Ratings)):
        u = ''
        for i in range(len(un)):
            u = u + str(ord(un[i]))
        j =  (int(u)%len(u))

        us.append(982)

    for i in range(len(Ratings)):
        pl.append(i)

def sort_list(Ratings,us,pl):
    for i in range(len(Ratings)):
        dataset.append({'Users': us[i], 'Places': pl[i], 'Ratings':Ratings[i]})
    #pred_values = zip(Ratings,us,pl)
    #z = [x for _, x in sorted(pred_values)]
    print(dataset)
    return dataset

# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName('rates').getOrCreate()
# sc = SQLContext(spark)
# def sparktest():
#     rt = []
#     for i in range(10):
#         rt.append(i)
#     ut = []
#     o = 'goawaydont'
#     for i in range(10):
#         ut.append(1234)
#     tt = [0.8999999999999999, 0.6, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 1.2, 0.8999999999999999, 1.2, 0.8999999999999999, 1.5]
#     #d = [{'name': ut, 'age': rt}]
#     d = []
#     for i in range(len(ut)):
#         d.append({'Users': ut[i], 'Places': rt[i], 'Ratings':tt[i]})
#
#     det = spark.createDataFrame(d)
#     dett = det.select(['Users','Places','Ratings'])
#
#     rrt = []
#     for i in range(10):
#         rrt.append(i)
#     uut = []
#     oo = 'goawaydont'
#     for i in range(10):
#         uut.append(12345)
#     ttt = [0.8999999999999999, 0.6, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 1.2, 0.8999999999999999, 1.2, 0.8999999999999999, 1.5]
#     #d = [{'name': ut, 'age': rt}]
#     dd = []
#     for i in range(len(uut)):
#         dd.append({'Users': uut[i], 'Places': rrt[i], 'Ratings':ttt[i]})
#
#     dettt = spark.createDataFrame(dd)
#     detttt = dettt.select(['Users','Places','Ratings'])
#
#     unionDF = dett.unionAll(detttt)
#     print(unionDF)
