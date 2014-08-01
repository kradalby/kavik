from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.consultants.views',
    url(r'^maillist/$', 'maillist', name='maillist'),
    url(r'^vcf/$', 'vcf', name='vcf'),
    url(r'^maillist/(?P<team_id>[0-9]{2}|(tl))/$', 'maillist', name='maillist'),
)
