__author__ = 'Craig'
import os
from datetime import datetime


def populate():
    john = User.objects.create_user('john', 'john@john.com', 'johnpassword')

    john_profile = add_user_profile(john, 'www.john.com',
                                    'profile_images/john.jpg')

    dave = User.objects.create_user('dave', 'dave@dave.com', 'davepassword')

    dave_profile = add_user_profile(dave, 'www.dave.com', 'profile_images/dave.jpg')

    chris = User.objects.create_user('chris', 'chris@chris.com', 'chrispassword')

    chris_profile = add_user_profile(chris, 'www.chrischris.com',
                                     'profile_images/chris.jpg')

    ##########################################THE GARAGE################################################################
    garage_bar = add_bar(john, 'The Garage', '490 Sauchiehall St', 'The Garage is a music venue and nightclub located '
                                                                   'at 490 Sauchiehall Street in Glasgow which opened '
                                                                   'in 1994. It is Scotlands largest nightclub.', 3)

    garage_review = add_review(chris, garage_bar, 3, 4, 3, 3,
                               'OMG I like ttly <3 the Garage bn goin evryday since I ws 14 lol!!!!')

    garage_categories = add_category(garage_bar, True, True, False, False, True, True, True, False, False, False,
                                     True, True, False)

    garage_photo = add_photo(garage_bar, '/uploads/garage.jpg')

    garage_news = add_event(garage_bar, 'Monday Nights bring you: 3 Rooms / 2 DJs / And YOU! G2: Andy R hosts Space'
                                        ' Invader and brings the widest selection of musical genres to the Garage each '
                                        'week! Lasers and giant Space Invaders illuminate the dance floor as you throw '
                                        'your shapes and get MWI.', 'The Garage is known for Live bands and Comedy '
                                                                    'shows but weve set out hand to many an event in '
                                                                    'the past including fashion shows, awards '
                                                                    'ceremonies, conferences and product launches.')

    ##############################################CAMPUS################################################################
    campus_bar = add_bar(john, 'Campus', '332 Sauchiehall St', 'Glasgows First Frat house - Campus has a bigger '
                                                               'and better new home.... Open 7 nights a week.', 3)

    campus_review = add_review(chris, campus_bar, 3, 4, 3, 3,
                               'Thoroughly enjoyed coming here for my 13th Birthday')

    campus_categories = add_category(campus_bar, True, False, False, False, False, True, False, True, False, True,
                                     True, False, True)

    garage_photo = add_photo(campus_bar, '/uploads/campus.jpg')

    garage_news = add_event(campus_bar, 'Campus is a students union for non-students. We were recently shut down because'
                                        ' someone chewed someones ear off but we will be reopening soon in a new home!',
                                        'Campus will be opening in our new home soon! Watch this space if you still need'
                                        'your dj cammy fix!')

    #######################################THE GUU######################################################################
    GUU_bar = add_bar(john, 'GUU', 'University Avenue', 'Glasgow University Union (GUU) is one of the largest and oldest'
                                                        ' students unions in the UK, serving students and alumni of the '
                                                        'University of Glasgow since 1885', 5)

    GUU_review = add_review(chris, GUU_bar, 5, 5, 5, 5,
                               'Excellent craic, many pints and the atmosphere is stupendous')

    GUU_categories = add_category(GUU_bar, True, True, True, True, False, True, False, True, False, True,
                                     False, True, False)

    GUU_photo = add_photo(GUU_bar, '/uploads/GUU.jpg')

    GUU_news = add_event(GUU_bar, 'Whether you are a current student, a life member, a member of the public enquiring'
                                  ' about venue hire, or even just visiting, you should find the information you are '
                                  'looking for here. If not, please do not hesitate to contact us.',
                                  'Daft Friday, commonly referred to as D*** F*****, is a simply stunning event, '
                                  'celebrating its 106th year in December 2014. '
                                  'Held in honour of GUUs President, this end-of-term ball is a celebration like'
                                  ' none other.')

    ########################################################QMU#########################################################
    QMU_bar = add_bar(john, 'QMU', '22 University Gardens', 'The Queen Margaret Union (QMU) is one of two students '
                                                            'unions at the University of Glasgow, Scotland. Founded in'
                                                            ' 1890, it caters for the social and cultural needs of its'
                                                            ' members by providing a range of services including,'
                                                            ' entertainments, catering, shop facilities, bars and '
                                                            'games.', 2)

    QMU_review = add_review(chris, QMU_bar, 2, 2, 1, 3,
                            'Not as good as the union down the road')

    QMU_categories = add_category(QMU_bar, False, True, False, True, False, True, False, True, False, False,
                                     False, True, True)

    QMU_photo = add_photo(QMU_bar, '/uploads/QMU.jpg')

    QMU_news = add_event(QMU_bar, 'Joining the QM Union is dead easy, very worthwhile, and while you are a student it is'
                                  ' also completely free.',
                                  'Spring Break is on its way, and what better way to celebrate than a night out at the'
                                  ' QMU. And this year we bring you...Wild, Wild West END! Hipsters vs Cowboys!'
                                  'Love beanies or a Stetson? Love big black glasses or a piercing gaze? Love converse'
                                  ' or kicks? Are you a fan of the Mo or....well, if you like Moustaches this whole'
                                  ' event is for you!! Entry only 3/4 pounds Members/Non with all sorts of cowboy and '
                                  'hipster games taking place from 9pm.')

    ####################################################################################################################

def add_user(name, email, password):
    u = User.objects.get_or_create(username=name, email=email, password=password)
    print 'adding user: ' + name
    return u[0]


def add_user_profile(user, website, picture):
    p = UserProfile.objects.get_or_create(user=user, website=website, picture=picture)
    print 'adding profile for: ' + str(user)
    return p[0]


def add_bar(owner, name, address, bio, overall_rating):
    b = Bar.objects.get_or_create(owner=owner, name=name, address=address, bio=bio, overall_rating=overall_rating)
    print 'adding bar: ' + name
    return b[0]


def add_review(poster, bar,  booze, beats, barstaff, bucks, text_review):
    print 'adding review: ' + text_review
    r = Review.objects.get_or_create(poster=poster, bar=bar, booze=booze, beats=beats, barstaff=barstaff,
                                     bucks=bucks, overall=((booze+beats+barstaff+bucks)/4), likes=0, favourites=0,
                                     date_posted=datetime.now(), text_review=text_review)
    return r[0]


def add_category(bar, food, big_screen, beer_garden, real_ale, whisky_collection,children_welcome, pets_welcome,
                 dartboard, pool_tables, games_machines, historic, wi_fi, function_room):
    c = Category.objects.get_or_create(bar=bar, food=food, big_screen=big_screen, beer_garden=beer_garden,
                                       real_ale=real_ale, whisky_collection=whisky_collection,
                                       children_welcome=children_welcome, pets_welcome=pets_welcome, dartboard=dartboard,
                                       pool_tables=pool_tables, games_machines=games_machines, historic=historic,
                                       wi_fi=wi_fi, function_room=function_room)
    print 'adding categories for: ' + str(bar)
    return c[0]


def add_event(bar, events, news):
    e = Event.objects.get_or_create(bar=bar, events=events, news=news)
    print 'adding events for: ' + str(bar)
    return e[0]


def add_photo(bar, image):
    p = Photo.objects.get_or_create(bar=bar, image=image)
    print 'adding photo: ' + bar.name
    return p[0]

if __name__ == '__main__':
    print "Starting Watering Hole population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'legless_industries_project.settings')
    from the_watering_hole.models import User, UserProfile, Bar, Review, Category, Event, Photo
    populate()

#d.maxwell.1@research.gla.ac.uk