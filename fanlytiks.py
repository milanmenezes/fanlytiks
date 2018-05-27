from flask import Flask, render_template, request, send_from_directory
import requests
import psycopg2

app = Flask(__name__)


@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def index():
	conn = psycopg2.connect(database = "aws", user = "milanmenezes", password = "nightfury", host = "milan-aws.crbk9i7trzoq.ap-south-1.rds.amazonaws.com", port = "5432")
	#general info
	info={}
	cur = conn.cursor()
	cur.execute("select count(*) from datastore;")
	info["tcount"]=cur.fetchone()[0]
	cur.close()
	cur = conn.cursor()
	cur.execute("select count(*) from (select distinct userid from datastore) as a;")
	info["ucount"]=cur.fetchone()[0]
	cur.close()
	cur = conn.cursor()
	cur.execute("select count(*) from datastore where media")
	info["mcount"]=cur.fetchone()[0]
	cur.close()

	#latest tweets
	cur = conn.cursor()
	cur.execute("select distinct ttime, twtext from datastore order by ttime desc limit 10;")
	latest=cur.fetchall()
	# return str(latest)
	# print cur
	latest=[(unicode(a[0]),unicode(a[1], "utf8").encode("utf-8")) for a in latest]
	cur.close()

	#tweets with most retweets
	cur = conn.cursor()
	cur.execute("Select max(retweet) as r, twtext FROM datastore group by twtext order by r desc limit 10;")
	retweet=cur.fetchall()
	cur.close()

	#tweets with most favourites
	cur = conn.cursor()
	cur.execute("Select max(favourite) as r, twtext FROM datastore group by twtext order by r desc limit 10;")
	favourite=cur.fetchall()
	cur.close()

	#tweets per day
	cur = conn.cursor()
	cur.execute("select to_char(ttime,'DD') as day, count(to_char(ttime,'DD')) as tweets from datastore group by day;")
	tpd=cur.fetchall()
	cur.close()

	x=['x']
	y=['tweets']
	for i in tpd:
		x.append(eval(i[0]))
		y.append(int(i[1]))
	tpd=[x,y]
	# return str(data)
	return render_template("index.html",info=info,tpd=tpd,latest=latest,retweet=retweet, favourite=favourite)



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)