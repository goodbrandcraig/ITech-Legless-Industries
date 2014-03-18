from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

import datetime
now = datetime.datetime.now() #for getting current datetime

from the_watering_hole.forms import UserForm, UserProfileForm, BarForm, ImageForm, CategoryForm, ReviewForm, EventForm
from the_watering_hole.models import Bar, Review, Photo, Category, UserProfile, User, Event


def index(request):  # Request the context of the request.
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL bars currently stored.
    # Order the bars by name
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    bar_list = Bar.objects.order_by('name')
    event_list = Event.objects.order_by('bar')
    context_dict = {'Bars': bar_list}
    context_dict['Events'] = event_list

    # Render the response and send it back!
    return render_to_response('the_watering_hole/index.html', context_dict, context)


def sorted_index(request, category):
    context = RequestContext(request)

    bars = Category.objects.all()

    matching_bars = []
    matching_bar_objs = []

    for bar in bars:
        if getattr(bar, category):
            matching_bars.append(bar)

    for bar in matching_bars:
        bar = Bar.objects.get(name=bar)
        matching_bar_objs.append(bar)



    template_context = {'matching_bars': matching_bars}

    template_context['category'] = category

    template_context['matching_bar_objs'] = matching_bar_objs

    print matching_bar_objs

    return render_to_response('the_watering_hole/sorted_index.html', template_context, context)


def bar_page(request, bar_name_url):
     # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the bar name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    bar_name = bar_name_url.replace('_', ' ')

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the bar passed by the user.
    context_dict = {'bar_name': bar_name}

    try:
        # Can we find a bar with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        bar = Bar.objects.get(name=bar_name)

        # Retrieve all of the associated reviews
        # Note that filter returns >= 1 model instance.
        reviews = Review.objects.filter(bar=bar)

        review_overall = 0
        overall_booze = 0
        overall_bucks= 0
        overall_barstaff = 0
        overall_beats = 0
        review_count = 0

        #get all of the overall reviews, calculate the averages for each review category and send to template
        for review in reviews:
            review_overall = review_overall + review.get_overall()
            overall_booze = overall_booze + review.get_booze()
            overall_bucks = overall_bucks + review.get_bucks()
            overall_barstaff = overall_barstaff + review.get_barstaff()
            overall_beats = overall_beats + review.get_beats()
            review_count = review_count + 1

        if review_count != 0:
            review_overall = int(round(float(review_overall)/float(review_count)))
            overall_booze = int(round(float(overall_booze/float(review_count))))
            overall_bucks = int(round(float(overall_bucks)/float(review_count)))
            overall_barstaff = int(round(float(overall_barstaff)/float(review_count)))
            overall_beats = int(round(float(overall_beats)/float(review_count)))



        bar.overall_rating = review_overall
        bar.save()

        #retrieve associated photo
        photo = Photo.objects.get(bar=bar)

        #retrieve categories
        categories = Category.objects.get(bar=bar)

        #retreive events
        events = Event.objects.get(bar=bar)

        # Adds our results list to the template context under name pages.
        context_dict['reviews'] = reviews
        # We also add the bar object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['bar'] = bar
        # also add photo object
        context_dict['photo'] = photo
        # and category object
        context_dict['categories'] = categories
        #and events objects
        context_dict['events'] = events
        #and the overall scores
        context_dict['overall'] = review_overall
        context_dict['bucks'] = overall_bucks
        context_dict['beats'] = overall_beats
        context_dict['booze'] = overall_booze
        context_dict['barstaff'] = overall_barstaff
        #and the number of reviews
        context_dict['no_of_reviews'] = review_count

    except Bar.DoesNotExist:
        # We get here if we didn't find the specified bar.
        # Don't do anything - the template displays the "no bar" message for us.
        pass

    # Render the response and send it back!
    return render_to_response('the_watering_hole/bar_page.html', context_dict, context)

@login_required
def like_review(request):
    context = RequestContext(request)
    review_id = None
    if request.method == 'GET':
        print 'get'
        review_id = request.GET['review_id']

    likes = 0
    if review_id:
        review = Review.objects.get(id=int(review_id))
        if review:
            likes = review.likes + 1
            review.likes = likes
            review.save()

    return HttpResponse(likes)


def profile_page(request, username):
    # Get the context from the request.
    context = RequestContext(request)

    user_name = request.user

    user = User.objects.get(username=user_name)

    user_profile = UserProfile.objects.get(user=user_name)

     # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the bar passed by the user.
    context_dict = {'user_name': user_name}

    context_dict['user_profile'] = user_profile


    bars = Bar.objects.all()

    user_uploaded_bars = []

    for bar in bars:
        if bar.owner.username == username:
            user_uploaded_bars.append(bar)

    context_dict['user_uploaded_bars'] = user_uploaded_bars

    return render_to_response('the_watering_hole/profile.html', context_dict, context)


def edit_bar(request, bar_name_url):
    context = RequestContext(request)

    bar = bar_name_url.replace('_', ' ')

    bar_to_edit = Bar.objects.get(name=bar)
    event_to_edit = Event.objects.get(bar=bar_to_edit)

    context_dict = {'bar_to_edit': bar_to_edit}
    context_dict['bar_to_edit'] = bar_to_edit
    context_dict['bar_url'] = bar_name_url

    bar_form = BarForm(instance=bar_to_edit)
    event_form = EventForm(instance=event_to_edit)

    if request.method == 'POST':
        bar_form = BarForm(request.POST, instance=bar_to_edit)
        event_form = EventForm(request.POST, instance=event_to_edit)

        if bar_form.is_valid() and event_form.is_valid():
            bar_form.save()
            event_form.save()


        else:
            print bar_form.errors

    return render_to_response('the_watering_hole/edit_bar.html', {'event_form': event_form, 'bar_form': bar_form,
                                                                  'context_dict':context_dict}, context)



def about(request):
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('the_watering_hole/about.html')


def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
        'the_watering_hole/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
        context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/the_watering_hole/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Watering Hole account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('the_watering_hole/login.html', {}, context)


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/the_watering_hole/')


def add_bar(request):
    #check user is logged in before allowing them to add a bar
    if request.user.is_authenticated():
        # Get the context from the request.
        context = RequestContext(request)

        # A boolean value for telling the template whether the creation was successful.
        # Set to False initially. Code changes value to True when creation succeeds.
        created = False

        # A HTTP POST?
        if request.method == 'POST':
            bar_form = BarForm(request.POST)
            image_form = ImageForm(request.POST, request.FILES)
            category_form = CategoryForm(request.POST)
            events_form = EventForm(request.POST)

             # Have we been provided with a valid form?
            if bar_form.is_valid():
                # Save the new category to the database.
                bar = bar_form.save(commit=False)
                bar.owner = request.user
                bar = bar_form.save()

                # Now sort out the photo instance.
                # Since we need to set the bar attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                photo = image_form.save(commit=False)
                photo.bar = bar

                # And now the categories instance
                category = category_form.save(commit=False)
                category.bar = bar

                # And now the events instance
                event = events_form.save(commit=False)
                event.bar = bar

                # Did the user provide a bar picture?
                # If so, we need to get it from the input form and put it in the photo model.
                if 'picture' in request.FILES:
                    photo.image = request.FILES['picture']

                # Now we save the photo model instance.
                photo.save()

                #and the Category instance
                category.save()

                #and the event instance
                event.save()

                # Update our variable to tell the template creation was successful.
                created = True

                # Now call the index() view.
                # The user will be shown the homepage.
                return index(request)

            else:
                # The supplied form contained errors - just print them to the terminal.
                print bar_form.errors, image_form.errors, category_form.errors, events_form.errors
        else:
            # If the request was not a POST, display the form to enter details.
            bar_form = BarForm()
            image_form = ImageForm()
            category_form = CategoryForm()
            events_form = EventForm()

            # Bad form (or form details), no form supplied...
            # Render the form with error messages (if any).
            return render_to_response('the_watering_hole/add_bar.html', {'bar_form': bar_form, 'image_form': image_form,
                                                                         'category_form': category_form, 'event_form':
                                                                         events_form, 'created': created}, context)

    else:
        return HttpResponse("You are not logged in.")


def add_review(request, bar_name_url):
     #check user is logged in before allowing them to add a bar
    if request.user.is_authenticated():
        # Get the context from the request.
        context = RequestContext(request)

        bar_name = bar_name_url.replace('_', ' ')

        bar = Bar.objects.get(name=bar_name)

        bar_name_url_slash = bar_name_url +'/'

        context_dict = {'bar_name': bar_name}
        context_dict['bar_name'] = bar_name
        context_dict['bar_name_url_slash'] = bar_name_url_slash

        # A boolean value for telling the template whether the creation was successful.
        # Set to False initially. Code changes value to True when creation succeeds.
        created = False

        # A HTTP POST?
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)

             # Have we been provided with a valid form?
            if review_form.is_valid():
                # Save the new review to the database.
                review = review_form.save(commit=False)
                review.poster = request.user
                review.date_posted = now.strftime("%Y-%m-%d %H:%M")
                review.overall = (review.barstaff+review.beats+review.booze+review.bucks)/4
                review.bar = bar

                review = review_form.save()

                # Update our variable to tell the template review was successful.
                created = True

            # Now call the bar_page() view.
                # The user will be shown the bar page again with the new review.
                return bar_page(request, bar_name_url)

            else:
                # The supplied form contained errors - just print them to the terminal.
                print review_form.errors

        else:
            # If the request was not a POST, display the form to enter details.
            review_form = ReviewForm()

            # Bad form (or form details), no form supplied...
            # Render the form with error messages (if any).
            return render_to_response('the_watering_hole/review_bar.html', {'review_form': review_form,
                                                                            'created': created,
                                                                            'context_dict': context_dict}, context)
    else:
        return HttpResponse("You are not logged in.")

