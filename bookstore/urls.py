from django.conf.urls import url
from . import views 



app_name = "bookstore"
urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^software/$', views.software_view, name="software"),
	url(r'^hardware/$', views.hardware_view, name="hardware"),
	url(r'^programming/$', views.programming_view, name="programming"),
	url(r'^networking/$', views.networking_view, name="networking"),
	url(r'^others/$', views.other_view, name="others"),
	url(r'^lecture_note/$', views.lecture_note_view, name="lecture_note"),
	url(r'^software/(?P<softslug>.*)/$', views.software_view_detail, name="software_detail"),
	url(r'^hardware/(?P<hardslug>.*)/$', views.hardware_view_detail, name="hardware_detail"),
	url(r'^networking/(?P<networkslug>.*)/$', views.network_view_detail, name="network_detail"),
	url(r'^programming/(?P<programslug>.*)/$', views.programming_view_detail, name="programming_detail"),
	url(r'^lecture_note/(?P<lectureslug>.*)/$', views.lectures_view_detail, name="lectures_detail"),
	url(r'^others/(?P<otherslug>.*)/$', views.others_view_detail, name="others_detail"),
	#url(r'^register/$', views.register, name="register")
	#url(r'^(?P<question_id>[0-9]+)/votes/$', views.votes, name="votes"),

]
