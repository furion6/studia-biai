import requests
url = 'http://127.0.0.1:5000/gatherInfo'
urlimpl = 'http://127.0.0.1:5000/isImplemented'
urllearn = 'http://127.0.0.1:5000/relearn'
urlcheckn = 'http://127.0.0.1:5000/checkN'
data = """{
  "data": 
  [
  {
  	"label":"cat",
  	"urls":["https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png",
 		 "https://ichef.bbci.co.uk/news/1024/cpsprodpb/83D7/production/_111515733_gettyimages-1208779325.jpg",
 		 "https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg"
 		 ]
  },
  {
  	"label":"dog",
  	"urls":[
  	"https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg",
  	"https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-1100x628.jpg",
  	"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg",
  	"https://www.dw.com/image/49202627_303.jpg",
  	"https://cdn.mos.cms.futurecdn.net/JzqhuEDTRfCZKMKHUxPySB.jpg",
  	"https://media.apnarm.net.au/media/images/2020/03/18/v3imagesbin1084acc28c79e2b71b023d2b3b765223-of8z3fhc4ieuw4lm0u2_t1880.jpg",
  	"https://toppng.com/uploads/preview/happy-dog-png-dogs-labradors-11563057164unft9mx3kl.png"
  	] 
   },
   {
   	"label":"pillow",
   	"urls":[
   	"https://media.sheridanoutlet.com.au/catalog/product/cache/1/image/1200x/17f82f742ffe127f42dca9de82fb58b1/1/7/1700x1700_fresh-loft-pillow-white.jpg?impolicy=original",
   	"https://www.serta.com/sites/ssb/serta.com/uploads/2019/Transition/Accessory-images/serta-pillow-PremireLoft5-no-seal.png",
   	"https://b3h2.scene7.com/is/image/BedBathandBeyond/15364655025932m?$690$&wid=690&hei=690",
   	"https://images.crateandbarrel.com/is/image/Crate/DownAltPillowInsert16inchSHS16/?$web_zoom$&190411135006&wid=450&hei=450"
   	]
   }
   
 ]
}"""

datacheck  = """{
  "data": 
  [
  {
  	"label":"cat",
  	"url":"https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png"
 		 
  },
  {
  	"label":"dog",
  	"url":"https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg"
  	
   },
   {
   	"label":"pillow",
   	"url":
   	"https://media.sheridanoutlet.com.au/catalog/product/cache/1/image/1200x/17f82f742ffe127f42dca9de82fb58b1/1/7/1700x1700_fresh-loft-pillow-white.jpg?impolicy=original"
   },
   {
   	"label":"lamp",
   	"url":"https://cb2.scene7.com/is/image/CB2/SnakeTableLampSHF19/?$web_zoom$&190430165808&wid=450&hei=450"
   },
   {
   	"label":"car",
   	"url":"https://www.cartrack.pl/sites/default/files/car.jpg"
   } 
 ]
}"""

data2 = '''{
  "data": 
  [
  {
  	"label":"cat",
  	"url":"https://images.contentstack.io/v3/assets/bltf589e66bcaecd79c/blt45f3665fae20fbc4/5e45e5a2b498df0d57200b9a/Window-anatomy-feature.jpg?format=pjpg&auto=webp"
 		 
  }
  ]
}'''
#response = requests.get(urlimpl, data=data2)
response = requests.post(urllearn)
#response = requests.get(urlcheckn, data=data2)
#response = requests.get(urlcheckn,data=datacheck)
print(response.content)





