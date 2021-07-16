import random
from app import db
from app.models import User


def generateOnline():
    seed = random.randint(0, 1)
    if seed == 0:
        return False
    return True


def generateAge():
    return random.randint(16, 55)


def generateParamaters():
    paramaters = [
                'love',
                'instagood',
                'fashion',
                'photooftheday',
                'beautiful',
                'art',
                'photography',
                'happy',
                'picoftheday',
                'cute',
                'follow',
                'tbt',
                'followme',
                'nature',
                'like4like',
                'travel',
                'instagram',
                'style',
                'repost',
                'summer',
                'instadaily',
                'selfie',
                'me',
                'friends',
                'fitness',
                'girl',
                'food',
                'fun',
                'beauty',
                'instalike',
                'smile',
                'family',
                'photo',
                'life',
                'likeforlike',
                'music',
                'ootd',
                'follow4follow',
                'makeup',
                'amazing',
                'igers',
                'nofilter',
                'dog',
                'model',
                'sunset',
                'beach',
                'instamood',
                'foodporn',
                'motivation',
                'followforfollow',
                'design',
                'lifestyle',
                'sky',
                'l4l',
                'f4f',
                '일상',
                'cat',
                'handmade',
                'hair',
                'vscocam',
                'bestoftheday',
                'vsco',
                'funny',
                'dogsofinstagram',
                'drawing',
                'artist',
                'gym',
                'flowers',
                'baby',
                'wedding',
                'girls',
                'instapic',
                'pretty',
                'likeforlikes',
                'photographer',
                'instafood',
                'party',
                'inspiration',
                'lol',
                'cool',
                'workout',
                'likeforfollow',
                'swag',
                'fit',
                'healthy',
                'yummy',
                'blackandwhite',
                'foodie',
                'moda',
                'home',
                'christmas',
                'black',
                'memes',
                'holiday',
                'pink',
                'sea',
                'landscape',
                'blue',
                'london',
                'winter'
                ]
    user_paramaters = ''
    for i in range(5):
        user_paramaters += f'{paramaters[random.randrange(0, len(paramaters))]},'
    return user_paramaters[:-1]


user = {'names': 
                ['Mary',
                'Patricia',
                'John',
                'Jennifer',
                'Michael',
                'Linda',
                'William',
                'Elizabeth',
                'David',
                'Barbara',
                'Richard',
                'Susan',
                'Joseph',
                'Jessica',
                'Thomas',
                'Sarah',
                'Charles',
                'Karen',
                'Christopher',
                'Nancy',
                'Daniel',
                'Lisa',
                'Matthew',
                'Betty',
                'Anthony',
                'Margaret',
                'Mark',
                'Sandra',
                'Donald',
                'Ashley',
                'Steven',
                'Kimberly',
                'Paul',
                'Emily',
                'Andrew',
                'Donna	',
                'Joshua',
                'Michell',
                'Kenneth',
                'Dorothy',
                'Kevin',
                'Carol',
                'Brian',
                'Amanda',
                'George',
                'Melissa',
                'Edward',
                'Deborah',
                'Ronald',
                'Stephanie',
                'Timothy',
                'Rebecca',
                'Jason',
                'Sharon',
                'Jeffrey',
                'Laura	',
                'Ryan',
                'Cynthia',
                'Jacob',
                'Kathleen',
                'Gary',
                'Amy',
                'Nicholas',
                'Shirley',
                'Eric',
                'Angela',
                'Jonathan',
                'Helen',
                'Stephen',
                'Anna',
                'Larry',
                'Brenda',
                'Justin',
                'Pamela',
                'Scott',
                'Nicole',
                'Brandon',
                'Emma',
                'Benjamin',
                'Samantha',
                'Samuel',
                'Katherine',
                'Gregory',
                'Christine',
                'Frank',
                'Debra',
                'Alexander',
                'Rachel',
                'Raymond',
                'Catherine',
                'Patrick',
                'Carolyn',
                'Jack',
                'Janet',
                'Dennis',
                'Ruth',
                'Jerry',
                'Maria'],
        'age': generateAge(),
        'online': generateOnline(),
        'location': [
                'New York, New York ',
                'Los Angeles, California ',
                'Chicago, Illinois ',
                'Houston, Texas ',
                'Phoenix, Arizona ',
                'Philadelphia, Pennsylvania ',
                'San Antonio, Texas ',
                'San Diego, California ',
                'Dallas, Texas ',
                'San Jose, California ',
                'Austin, Texas ',
                'Fort Worth, Texas',
                'Jacksonville, Florida ',
                'Columbus, Ohio ',
                'Charlotte, North Carolina ',
                'Indianapolis, Indiana ',
                'San Francisco, California ',
                'Seattle, Washington ',
                'Denver, Colorado ',
                'Washington, District of Columbi',
                'Boston, Massachusetts ',
                'El Paso, Texas ',
                'Nashville, Tennessee ',
                'Detroit, Michigan ',
                'Las Vegas, Nevada ',
                'Oklahoma City, Oklahoma ',
                'Portland, Oregon ',
                'Memphis, Tennessee ',
                'Louisville, Kentucky ',
                'Milwaukee, Wisconsin ',
                'Baltimore, Maryland',
                'Albuquerque, New Mexico ',
                'Tucson, Arizona ',
                'Fresno, California ',
                'Mesa, Arizona ',
                'Sacramento, California ',
                'Atlanta, Georgia ',
                'Kansas City, Missouri ',
                'Colorado Springs, Colorado',
                'Omaha, Nebraska ',
                'Raleigh, North Carolina ',
                'Miami, Florida ',
                'Long Beach, California ',
                'Virginia Beach, Virginia',
                'Minneapolis, Minnesota ',
                'Oakland, California ',
                'Tampa, Florida ',
                'Tulsa, Oklahoma ',
                'Arlington, Texas ',
                'Wichita, Kansas ',
                'New Orleans, Louisiana ',
                'Aurora, Colorado ',
                'Bakersfield, California ',
                'Cleveland, Ohio ',
                'Anaheim, California ',
                'Honolulu, Hawaii ',
                'Santa Ana, California ',
                'Riverside, California ',
                'Henderson, Nevada ',
                'Corpus Christi, Texas ',
                'Lexington, Kentucky ',
                'Stockton, California ',
                'Saint Paul, Minnesota ',
                'Cincinnati, Ohio ',
                'Pittsburgh, Pennsylvania ',
                'Greensboro, North Carolina ',
                'St. Louis, Missouri ',
                'Plano, Texas ',
                'Lincoln, Nebraska ',
                'Orlando, Florida ',
                'Anchorage, Alaska ',
                'Durham, North Carolina ',
                'Irvine, California ',
                'Newark, New Jersey ',
                'Chula Vista, California ',
                'Fort Wayne, Indiana ',
                'Toledo, Ohio ',
                'St. Petersburg, Florida ',
                'Chandler, Arizona ',
                'Laredo, Texas ',
                'Madison, Wisconsin ',
                'Jersey City, New Jersey ',
                'Scottsdale, Arizona ',
                'Lubbock, Texas ',
                'North Las Vegas, Nevada ',
                'Reno, Nevada ',
                'Gilbert, Arizona ',
                'Glendale, Arizona ',
                'Buffalo, New York ',
                'Winston–Salem, North Carolina ',
                'Chesapeake, Virginia ',
                'Norfolk, Virginia ',
                'Irving, Texas ',
                'Garland, Texas',
                'Fremont, California',
                'Richmond, Virginia',
                'Hialeah, Florida',
                'Boise, Idaho',
                'Spokane, Washington ',
                'Tacoma'
                        ],
        'email': '@gmail.com',
        'profile_image': ["https://avatarfiles.alphacoders.com/108/thumb-108917.png", "https://avatarfiles.alphacoders.com/707/thumb-70712.jpg", "https://avatarfiles.alphacoders.com/464/thumb-46432.jpg", "https://avatarfiles.alphacoders.com/765/thumb-76543.png", "https://avatarfiles.alphacoders.com/523/thumb-52325.jpg", "https://avatarfiles.alphacoders.com/105/thumb-105876.png", "https://avatarfiles.alphacoders.com/643/thumb-64385.png", "https://avatarfiles.alphacoders.com/468/thumb-46807.png", "https://avatarfiles.alphacoders.com/111/thumb-111799.png", "https://avatarfiles.alphacoders.com/500/thumb-50097.jpg", "https://avatarfiles.alphacoders.com/184/thumb-184197.jpg", "https://avatarfiles.alphacoders.com/110/thumb-110106.jpg", "https://avatarfiles.alphacoders.com/769/thumb-76959.jpg", "https://avatarfiles.alphacoders.com/123/thumb-123635.jpg", "https://avatarfiles.alphacoders.com/116/thumb-116236.png", "https://avatarfiles.alphacoders.com/105/thumb-105821.png", "https://avatarfiles.alphacoders.com/932/thumb-93221.jpg", "https://avatarfiles.alphacoders.com/921/thumb-92117.jpg", "https://avatarfiles.alphacoders.com/481/thumb-48130.jpg", "https://avatarfiles.alphacoders.com/475/thumb-47514.jpg", "https://avatarfiles.alphacoders.com/156/thumb-156141.png", "https://avatarfiles.alphacoders.com/129/thumb-129716.jpg", "https://avatarfiles.alphacoders.com/841/thumb-84190.png", "https://avatarfiles.alphacoders.com/176/thumb-176446.jpg", "https://avatarfiles.alphacoders.com/147/thumb-147517.jpg", "https://avatarfiles.alphacoders.com/141/thumb-141036.png", "https://avatarfiles.alphacoders.com/128/thumb-128800.png", "https://avatarfiles.alphacoders.com/128/thumb-128030.jpg", "https://avatarfiles.alphacoders.com/125/thumb-125117.png", "https://avatarfiles.alphacoders.com/124/thumb-124690.jpg", "https://avatarfiles.alphacoders.com/123/thumb-123591.png", "https://avatarfiles.alphacoders.com/122/thumb-122163.jpg", "https://avatarfiles.alphacoders.com/113/thumb-113880.png", "https://avatarfiles.alphacoders.com/107/thumb-107813.jpg", "https://avatarfiles.alphacoders.com/928/thumb-92848.png", "https://avatarfiles.alphacoders.com/895/thumb-89557.jpg", "https://avatarfiles.alphacoders.com/867/thumb-86735.png", "https://avatarfiles.alphacoders.com/835/thumb-83546.jpg", "https://avatarfiles.alphacoders.com/801/thumb-80146.jpg", "https://avatarfiles.alphacoders.com/682/thumb-68230.jpg", "https://avatarfiles.alphacoders.com/280/thumb-280593.png", "https://avatarfiles.alphacoders.com/232/thumb-232776.png", "https://avatarfiles.alphacoders.com/226/thumb-226297.png", "https://avatarfiles.alphacoders.com/225/thumb-225628.png", "https://avatarfiles.alphacoders.com/184/thumb-184741.jpg", "https://avatarfiles.alphacoders.com/174/thumb-174407.jpg", "https://avatarfiles.alphacoders.com/161/thumb-161657.jpg", "https://avatarfiles.alphacoders.com/161/thumb-161525.png", "https://avatarfiles.alphacoders.com/161/thumb-161188.png", "https://avatarfiles.alphacoders.com/155/thumb-155854.png", "https://avatarfiles.alphacoders.com/148/thumb-148760.jpg", "https://avatarfiles.alphacoders.com/128/thumb-128705.jpg", "https://avatarfiles.alphacoders.com/125/thumb-125727.jpg", "https://avatarfiles.alphacoders.com/124/thumb-124723.jpg", "https://avatarfiles.alphacoders.com/124/thumb-124548.jpg", "https://avatarfiles.alphacoders.com/124/thumb-124079.jpg", "https://avatarfiles.alphacoders.com/123/thumb-123795.png", "https://avatarfiles.alphacoders.com/123/thumb-123264.jpg", "https://avatarfiles.alphacoders.com/120/thumb-120702.jpg", "https://avatarfiles.alphacoders.com/106/thumb-106700.jpg","https://avatarfiles.alphacoders.com/105/thumb-105872.jpg", "https://avatarfiles.alphacoders.com/105/thumb-105378.png", "https://avatarfiles.alphacoders.com/104/thumb-104290.jpg", "https://avatarfiles.alphacoders.com/102/thumb-102105.jpg", "https://avatarfiles.alphacoders.com/929/thumb-92964.png", "https://avatarfiles.alphacoders.com/869/thumb-86903.jpg", "https://avatarfiles.alphacoders.com/854/thumb-85410.png", "https://avatarfiles.alphacoders.com/822/thumb-82201.jpg", "https://avatarfiles.alphacoders.com/793/thumb-79364.jpg", "https://avatarfiles.alphacoders.com/790/thumb-79019.png", "https://avatarfiles.alphacoders.com/685/thumb-68500.png", "https://avatarfiles.alphacoders.com/660/thumb-66006.png", "https://avatarfiles.alphacoders.com/629/thumb-62934.jpg", "https://avatarfiles.alphacoders.com/628/thumb-62852.png", "https://avatarfiles.alphacoders.com/582/thumb-58259.png", "https://avatarfiles.alphacoders.com/534/thumb-53498.jpg", "https://avatarfiles.alphacoders.com/488/thumb-48873.jpg", "https://avatarfiles.alphacoders.com/273/thumb-273760.jpg", "https://avatarfiles.alphacoders.com/269/thumb-269700.png", "https://avatarfiles.alphacoders.com/232/thumb-232598.png", "https://avatarfiles.alphacoders.com/226/thumb-226219.jpg", "https://avatarfiles.alphacoders.com/215/thumb-215049.png", "https://avatarfiles.alphacoders.com/208/thumb-208380.jpg", "https://avatarfiles.alphacoders.com/191/thumb-191643.png", "https://avatarfiles.alphacoders.com/188/thumb-188930.jpg", "https://avatarfiles.alphacoders.com/177/thumb-177358.png", "https://avatarfiles.alphacoders.com/173/thumb-173406.jpg", "https://avatarfiles.alphacoders.com/172/thumb-172528.png", "https://avatarfiles.alphacoders.com/170/thumb-170337.jpg", "https://avatarfiles.alphacoders.com/167/thumb-167289.jpg", "https://avatarfiles.alphacoders.com/167/thumb-167003.png", "https://avatarfiles.alphacoders.com/166/thumb-166610.png", "https://avatarfiles.alphacoders.com/165/thumb-165348.jpg", "https://avatarfiles.alphacoders.com/162/thumb-162123.png", "https://avatarfiles.alphacoders.com/161/thumb-161653.jpg", "https://avatarfiles.alphacoders.com/161/thumb-161507.jpg", "https://avatarfiles.alphacoders.com/161/thumb-161103.jpg", "https://avatarfiles.alphacoders.com/161/thumb-161101.png", "https://avatarfiles.alphacoders.com/160/thumb-160886.png", "https://avatarfiles.alphacoders.com/157/thumb-157334.jpg", "https://avatarfiles.alphacoders.com/156/thumb-156130.png", "https://avatarfiles.alphacoders.com/154/thumb-154087.jpg", "https://avatarfiles.alphacoders.com/151/thumb-151127.png", "https://avatarfiles.alphacoders.com/150/thumb-150429.jpg", "https://avatarfiles.alphacoders.com/150/thumb-150273.png", "https://avatarfiles.alphacoders.com/148/thumb-148921.png", "https://avatarfiles.alphacoders.com/146/thumb-146075.jpg", "https://avatarfiles.alphacoders.com/139/thumb-139953.png", "https://avatarfiles.alphacoders.com/139/thumb-139945.png", "https://avatarfiles.alphacoders.com/139/thumb-139523.jpg", "https://avatarfiles.alphacoders.com/129/thumb-129941.jpg", "https://avatarfiles.alphacoders.com/129/thumb-129735.jpg", "https://avatarfiles.alphacoders.com/128/thumb-128661.png", "https://avatarfiles.alphacoders.com/127/thumb-127411.png", "https://avatarfiles.alphacoders.com/125/thumb-125904.jpg", "https://avatarfiles.alphacoders.com/125/thumb-125091.jpg", "https://avatarfiles.alphacoders.com/124/thumb-124827.png", "https://avatarfiles.alphacoders.com/124/thumb-124822.png", "https://avatarfiles.alphacoders.com/124/thumb-124420.jpg", "https://avatarfiles.alphacoders.com/123/thumb-123638.jpg"],
        'paramaters': generateParamaters(),
}

for i in range(len(user['names'])):
    new_user = User(username=user['names'][i] + 'BOT')
    new_user.age = user['age']
    new_user.online = user['online']
    new_user.location = user['location'][i]
    new_user.email = new_user.username + user['email']
    new_user.profile_image = user['profile_image'][i]
    new_user.paramaters = user['paramaters']
    db.session.add(new_user)
    db.session.commit()