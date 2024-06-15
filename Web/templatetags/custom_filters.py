from django import template

register = template.Library()

@register.filter
def get_youtube_video_id(url):
    if 'v=' in url:
        return url.split('v=')[-1]
    else:
        return url
