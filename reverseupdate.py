from twitter import *
import json
import psycopg2

conn = psycopg2.connect(database = "aws", user = "milanmenezes", password = "nightfury", host = "milan-aws.crbk9i7trzoq.ap-south-1.rds.amazonaws.com", port = "5432")
api = Api(consumer_key='QBSJiqeISh3g98v4En482W0rU',
                      consumer_secret='x8Wgr1RIF5b6sR14wkuNIZvNOTslCBkrRKUBLCSCBT6Od0oM0S',
                      access_token_key='518104135-N40eShH1AonSJ4Ca0STFbw8ht9VbyCSoeHw8tJig',

                      access_token_secret='gvJewbmkt3PhNg24WU6ITitsAyMVHex3VgcWYV4BJbTWr')

q="q=%23VIVOIPL&result_type=recent&since=2018-01-01&count=100"
try:
	c = conn.cursor()
	c.execute("Select min(ID) from DATASTORE;")
	tid=c.fetchone()[0]-1
	c.close()

	res = api.GetSearch(raw_query=q+"&max_id="+str(tid), return_json=True)
	temp=res["statuses"]
	i=0
	tid=0
	while(i<150):
		print "Call no:",i
		i+=1
		c = conn.cursor()
		for t in temp:
			media=False
			tid=t["id"]
			userid=t["user"]["id"]
			username=t["user"]["screen_name"].replace("'","''")
			if "extended_entities" in t:
				if "media" in t["extended_entities"]:
					if t["extended_entities"]["media"]:
						media=True
			text=t["text"].replace("'","''")
			created=t["created_at"]

			retweet=t["retweet_count"]
			fav=t["favorite_count"]
			loc=t["user"]["location"].replace("'","''")
			
			# c.execute("Insert into DATASTORE values (?,?,?,?,?,?,?,?);",(tid, userid, username, media, text, retweet, fav, loc,))
			c.execute("Insert into DATASTORE values ("+str(tid)+", "+str(userid)+", '"+username.encode("utf-8")+"', "+str(media)+", '"+text.encode("utf-8")+"', "+str(retweet)+", "+str(fav)+", '"+loc.encode("utf-8")+"', TIMESTAMP '"+created.encode("utf-8")+"' );")
			conn.commit()
		# c = conn.cursor()
		c.execute("Select min(ID) from DATASTORE;")
		tid=c.fetchone()[0]-1
		c.close()
		res = api.GetSearch(raw_query=q+"&max_id="+str(tid), return_json=True)
		print tid
		temp=res["statuses"]
		if not temp:
			break
except:
	print "Error"
finally:
	conn.close()
print "Successfull"
