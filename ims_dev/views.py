from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.conf import settings
from django.contrib.auth import views as auth_views
from re import match
try:
    adminName = settings.SITE_ADMIN[0]
except AttributeError:
    adminName=''
try:
    adminEmail = settings.SITE_ADMIN[1]
except AttributeError:
    adminEmail=''
try:
    siteVersion = settings.SITE_VERSION
except AttributeError:
    siteVersion=''
try:
    imsVersion = settings.IMS_VERSION
except AttributeError:
    imsVersion=''

def get_session_messages(request):
    if 'errorMessage' in request.session:
        errorMessage = request.session['errorMessage']
        errorMessage = errorMessage.replace('\n','<br />')
    else:
        errorMessage = ''
    request.session['errorMessage'] = ''
    if 'warningMessage' in request.session:
        warningMessage = request.session['warningMessage']
        warningMessage = warningMessage.replace('\n','<br />')
    else:
        warningMessage = ''
    request.session['warningMessage'] = ''
    if 'infoMessage' in request.session:
        infoMessage = request.session['infoMessage']
        infoMessage = infoMessage.replace('\n','<br />')
    else:
        infoMessage = ''
    request.session['infoMessage'] = ''
    return errorMessage, warningMessage, infoMessage

def home(request):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    return render(request,'base/base.html',{'nav_home':1,
                                            'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})

def redcross_help(request):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    return render(request,'base/redcross_help.html',{'nav_help':1,
                                                     'errorMessage':errorMessage,
                                                     'warningMessage':warningMessage,
                                                     'infoMessage':infoMessage,
                                                     'adminName':adminName,
                                                     'adminEmail':adminEmail,
                                                     'siteVersion':siteVersion,
                                                     'imsVersion':imsVersion,})

def handler404(request):
    warningMessage = '''Oops! It looks like you might be lost.<br />
                    The requested page<br />
                    <span id="url-text">"%s"</span><br />
                    doesn't exist on this site.<br />
                    The site admin has been informed of the problem.<br />
                    Try one of these links to find what you're looking for<br />
                    ''' % request.build_absolute_uri()
    response = render_to_response('404.html', {'warningMessage':warningMessage},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
 
def handler500(request):
    errorMessage = '''Uh oh! It looks like there was some kind of server error!<br />
    Sorry about that.<br />
    The site admin has been informed of the problem.<br /><br />
    Please use the menu bar at the top to continue using the site.'''
    response = render_to_response('500.html',{'errorMessage':errorMessage},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
 
def handler400(request):
    errorMessage = '''Hmm! There was something suspicious about that last request.<br />
    Please try again.<br />
    The site admin has been informed of the problem.<br /><br />
    Please use the menu bar at the top to continue using the site.'''
    response = render_to_response('400.html', {'errorMessage':errorMessage},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response

def logout(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    template_response = auth_views.logout(request, *args, **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        return template_response
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                'adminName':adminName,
                                'adminEmail':adminEmail,
                                'siteVersion':siteVersion,
                                'imsVersion':imsVersion,})
    return template_response

def login(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    template_response = auth_views.login(request, *args, **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        return template_response
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})
    return template_response

def password_change(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    post_change_redirect = request.GET.get('next',None)
    kwargs['post_change_redirect'] = post_change_redirect
    template_response = auth_views.password_change(request, *args, **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        request.session['infoMessage'] = 'Successfully changed password'
        return template_response
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})
    return template_response

def password_change_done(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    template_response = auth_views.password_change_done(request, *args, 
                                                        **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        return template_response
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})
    return template_response

def password_reset(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    template_response = auth_views.password_reset(request, *args, **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        return template_response
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})
    return template_response

def password_reset_done(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    template_response = auth_views.password_reset_done(request, *args, **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        return template_response
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})
    return template_response

def password_reset_confirm(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    post_reset_redirect = settings.LOGIN_URL
    kwargs['post_reset_redirect'] = post_reset_redirect
    template_response = auth_views.password_reset_confirm(request, *args, **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        request.session['infoMessage'] = 'Successfully changed password'
        return template_response
    if match('unsuccessful',template_response.context_data['title']):
        request.session['errorMessage'] = template_response.context_data['title']
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})
    return template_response

def password_reset_complete(request, *args, **kwargs):
    errorMessage, warningMessage, infoMessage = get_session_messages(request)
    template_response = auth_views.password_reset_complete(request, *args, **kwargs)
    if template_response.status_code == 302:
        # if we redirect, no need to change the response data
        return template_response
    template_response.context_data.update({
                                           'errorMessage':errorMessage,
                                            'warningMessage':warningMessage,
                                            'infoMessage':infoMessage,
                                            'adminName':adminName,
                                            'adminEmail':adminEmail,
                                            'siteVersion':siteVersion,
                                            'imsVersion':imsVersion,})
    return template_response