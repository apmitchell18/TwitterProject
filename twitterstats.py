import requests
import json

session = requests.Session()
auth = ('3leDE2ntHuugshR21ttrFI15f', 'JMHllBED2S6TDagavjMtYSC40f0fZiUS6B59TRfvc0mmDmNADI', '935370608635994112-BVZR2BMaznoWLgFfOBKzk8suJC519t1', '2hgcwV0ZeJ7QXQeT0xGIoakTJPpKuhv9rwOv3BWs3M5MZ')
r = requests.get('https://api.twitter.com/1.1/search/tweets.json', auth=auth)
print(r)
