from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('front.views',
    # Main site patterns:
    url(r'^$', 'home', name='kew_default_home'),
    url(r'^home', 'home', name='kew_target_home'),
    url(r'^services', 'services', name='kew_services'),
    url(r'^clients', 'clients', name='kew_clients'),
    url(r'^details', 'details', name='kew_details'),
    url(r'^faq', 'faq', name='kew_faq'),
    url(r'^securelogin', 'securelogin', name='kew_securelogin'),
    url(r'^paypal', 'paypal', name='kew_paypal'),
    url(r'^contactindex', 'contactindex', name='kew_contact')
    # url(r'^kew_editing/', include('kew_editing.foo.urls')),
)

urlpatterns += patterns('',
	# Admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin:
    url(r'^admin/', include(admin.site.urls))
)
