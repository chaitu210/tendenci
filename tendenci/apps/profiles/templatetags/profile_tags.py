from django.contrib.auth.models import User
from django.template import Library
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import six


register = Library()


@register.inclusion_tag("profiles/top_nav_items.html", takes_context=True)
def profile_current_app(context, user, profile=None):
    context.update({
        "app_object": profile,
        "user": user
    })
    return context


@register.inclusion_tag("profiles/nav.html", takes_context=True)
def users_nav(context, user_current, user_this=None):
    if user_this:
        try:
            profile_this = user_this.profile
        except:
            profile_this = None
    else:
        profile_this = None
    context.update({
        "user_current":user_current,
        "user_this": user_this,
        "nav_object": profile_this,
        "profile":profile_this
    })

    return context


@register.inclusion_tag("profiles/options.html", takes_context=True)
def users_options(context, user_current, user_this):
    if user_this:
        try:
            profile_this = user_this.profile
        except:
            profile_this = None
    else:
        profile_this = None
    context.update({
        "user_current":user_current,
        "user_this": user_this,
        "profile":profile_this
    })
    return context


@register.inclusion_tag("profiles/search-form.html", takes_context=True)
def profile_search(context):
    return context


@register.inclusion_tag("profiles/meta.html", takes_context=True)
def profile_meta(context, detail_view=None):
    context.update({
        "detail_view":detail_view,
    })
    return context


@register.inclusion_tag("profiles/similar_profile_items.html", takes_context=True)
def similar_profile_items(context, users):
    context.update({
        "users": users,
    })
    return context


@register.inclusion_tag("profiles/merge_detail.html", takes_context=True)
def merge_detail(context, profile):
    context.update({
        "profile": profile,
    })
    return context


@register.simple_tag
def gravatar(user, size=settings.GAVATAR_DEFAULT_SIZE, **kwargs):
    try:
        url = user.profile.get_gravatar_url(size=size)
    except:
        return ''

    context = dict(kwargs, **{
        'user': user,
        'url': url,
        'alt': six.text_type(user),
        'size': size,
    })
    return render_to_string('profiles/gravatar_tag.html', context)
