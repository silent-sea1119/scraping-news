from pymongo import MongoClient

conn = MongoClient("www.polypite.com",27017)
db = conn.spidernews
my_set = db.pencilenews
my_set.insert_one({'category': 'none',
 'newsContent': '铅笔道获悉，工业互联网公司博拉科技完成数千万元A轮融资，投资方为戈壁创投。本轮融资主要用于产品研发和市场推广。博拉科技成立于2014年，面向汽车及零部件、机械加工、纺织、五金等离散制造行业，为中小型工业制造企业提供云MES产品服务，同时为中大型企业提供企业级、区域级与行业级的工业互联网平台解决方案。',
 'newsSource': '铅笔道',
 'newsTitle': '工业互联网公司“博拉科技”获戈壁创投数千万元A轮融资',
 'publishDate': '2019-03-07 08:39:52'})


