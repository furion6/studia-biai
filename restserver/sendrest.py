import requests
url = 'http://15.236.208.227:8133/gatherInfo'
urlimpl = 'http://15.236.208.227:8133/isImplemented'
urllearn = 'http://15.236.208.227:8133/relearn'
urlcheckn = 'http://15.236.208.227:8133/checkN'
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

datacheck  = """[
{"label":"dog","url":"https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg"},{"label":"dog","url":"https://upload.wikimedia.org/wikipedia/commons/d/d9/Collage_of_Nine_Dogs.jpg"},{"label":"dog","url":"https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12234558/Chinook-On-White-03.jpg"},{"label":"dog","url":"https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/09/dog-landing-hero-lg.jpg?bust=1536935129&width=1080"},{"label":"dog","url":"https://www.sciencemag.org/sites/default/files/styles/article_main_large/public/dogs_1280p_0.jpg?itok=cnRk0HYq"},{"label":"dog","url":"https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"},{"label":"dog","url":"https://post.medicalnewstoday.com/wp-content/uploads/sites/3/2020/02/322868_1100-1100x628.jpg"},{"label":"dog","url":"https://www.sciencealert.com/images/2020-03/processed/010-pomeranian_1024.jpg"},{"label":"dog","url":"https://www.washingtonian.com/wp-content/uploads/2018/10/marcus-wallis-471438-unsplash-2048x1536.jpg"},{"label":"dog","url":"https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/slideshows/dog_breed_health_issues_slideshow/1800x1200_dog_breed_health_issues_slideshow.jpg"},{"label":"dog","url":"https://cdn.mos.cms.futurecdn.net/JzqhuEDTRfCZKMKHUxPySB.jpg"},{"label":"dog","url":"https://ichef.bbci.co.uk/wwfeatures/live/976_549/images/live/p0/7z/n7/p07zn7p7.jpg"},{"label":"dog","url":"https://cdn.mos.cms.futurecdn.net/QjuZKXnkLQgsYsL98uhL9X-1200-80.jpg"},{"label":"dog","url":"https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/13000046/Boerboel-On-White-01.jpg"},{"label":"dog","url":"https://images.theconversation.com/files/319375/original/file-20200309-118956-1cqvm6j.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=1200.0&fit=crop"},{"label":"dog","url":"https://si.wsj.net/public/resources/images/B3-EU419_201908_GR_20190822110317.jpg"},{"label":"dog","url":"https://www.guidedogs.org/wp-content/uploads/2019/11/website-donate-mobile.jpg"}]"""

data2 = '''{
  "data": 
  [
  {
  	"label":"cat",
  	"url":"https://images.contentstack.io/v3/assets/bltf589e66bcaecd79c/blt45f3665fae20fbc4/5e45e5a2b498df0d57200b9a/Window-anatomy-feature.jpg?format=pjpg&auto=webp"
 		 
  }
  ]
}'''
data3 = '''{
  "label":"car"
}'''
#response = requests.get(urlimpl, data=data3)
#response = requests.post(urllearn)
#response = requests.get(urlcheckn, data=data2)
response = requests.post(urlcheckn,data=datacheck)
print(response.content)





