__author__ = 'Craig'
import os
from datetime import datetime


def populate():
    john = add_user('john', 'john@john.com', 'johnpassword')

    john_profile = add_user_profile(john, 'www.john.com',
                                    '/media/profile_images/988341_10201581831484988_1056121486_n.jpg')

    chris = add_user('chris', 'chris@chris.com', 'chrispassword')

    chris_profile = add_user_profile(chris, 'www.chrischris.com',
                                     '/media/profile_images/988609_543226820336_2091969694_n.jpg')

    garage_bar = add_bar(john, 'The Garage', '490 Sauchiehall St', 'The Garage is a music venue and nightclub located '
                                                                   'at 490 Sauchiehall Street in Glasgow which opened '
                                                                   'in 1994. It is Scotlands largest nightclub.')

    garage_review = add_review(john, garage_bar, 3, 4, 3, 3,
                               'OMG I like ttly <3 the Garage bn goin evryday since I ws 14 lol!!!!')

    garage_review_comment = add_comment(chris, garage_review, 'omg bbz ure so ttly right lololol!!!1!')

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


def add_user(name, email, password):
    u = User.objects.get_or_create(username=name, email=email, password=password)
    print 'adding user: ' + name
    return u[0]


def add_user_profile(user, website, picture):
    p = UserProfile.objects.get_or_create(user=user, website=website, picture=picture)
    print 'adding profile for: ' + str(user)
    return p[0]


def add_bar(owner, name, address, bio):
   # print type(owner)
   # print type(name)
   # print type(address)
   # print type(bio)
    b = Bar.objects.get_or_create(owner=owner, name=name, address=address, bio=bio)
    print 'adding bar: ' + name
    return b[0]


def add_review(poster, bar,  booze, beats, barstaff, bucks, text_review):
    print 'adding review: ' + text_review
    r = Review.objects.get_or_create(poster=poster, bar=bar, booze=booze, beats=beats, barstaff=barstaff,
                                     bucks=bucks, overall=((booze+beats+barstaff+bucks)/4), likes=0, favourites=0,
                                     date_posted=datetime.now(), text_review=text_review)
    return r[0]


def add_comment(poster, review, text_comment):
    print 'adding comment: ' + text_comment
    c = Comment.objects.get_or_create(poster=poster, review=review, text_comment=text_comment,
                                      date_posted=datetime.now(), likes=0)
    return c[0]


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
    from the_watering_hole.models import User, UserProfile, Bar, Review, Comment, Category, Event, Photo
    populate()

#d.maxwell.1@research.gla.ac.uk