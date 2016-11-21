import numpy as np
import graphlab, random
from graphlab import aggregate as agg

train_data = graphlab.SFrame(data="FILE_PATH/rating_final.csv")
#Train Model
graphlab_model = graphlab.recommender.create(train_data, user_id='userID', item_id='placeID', target='rating')

#Make Recommendations:
graphlab_recomm = graphlab_model.recommend()
#graphlab_recomm.print_rows(num_rows=45)

graphlab_recomm.remove_columns(['score','rank']) 
graphlab_recomm.groupby(key_columns='userID', operations = {
	'placeIDs' : agg.CONCAT('placeID')
	})
df = graphlab_recomm.to_dataframe().set_index('userID')
recommendations = {}

for key, row in df.itertuples():
	recommendations.setdefault(key, []).append(row)

print "Enter user ID : "
current_user = raw_input()

if current_user not in recommendations:
	print "User does not exist!"
	exit()

print "Your surprise me option is :" + str(random.sample(recommendations[current_user],1)[0])