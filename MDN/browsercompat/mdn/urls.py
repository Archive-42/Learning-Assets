"""URLs for MDN data importer."""
from django.conf.urls import patterns, url


mdn_urlpatterns = patterns(
    'mdn.views',
    url(r'^$', 'feature_page_list', name='feature_page_list'),
    url(r'^create$', 'feature_page_create', name='feature_page_create'),
    url(r'^search$', 'feature_page_url_search',
        name='feature_page_url_search'),
    url(r'^slug_search$', 'feature_page_slug_search',
        name='feature_page_slug_search'),
    url(r'^issues$', 'issues_summary', name='issues_summary'),
    url(r'^issues.csv$', 'issues_summary_csv', name='issues_summary_csv'),
    url(r'^issues/(?P<slug>.*).csv$', 'issues_detail_csv',
        name='issues_detail_csv'),
    url(r'^issues/(?P<slug>.*)$', 'issues_detail', name='issues_detail'),
    url(r'^(?P<pk>\d+)$', 'feature_page_detail', name='feature_page_detail'),
    url(r'^(?P<pk>\d+)\.json$', 'feature_page_json', name='feature_page_json'),
    url(r'^(?P<pk>\d+)/reset$', 'feature_page_reset',
        name='feature_page_reset'),
    url(r'^(?P<pk>\d+)/reparse$', 'feature_page_reparse',
        name='feature_page_reparse')
)
