from django.urls import path
from OpenGovCore.views import *
from django.conf.urls import include

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('members/',Members.as_view(),name='members'),
    path('members/name/<member>/',MemberDetail.as_view(),name='member_det'),
    path('members/house/<house>/<name>/',MemberInfo.as_view(),name="member_name"),
    path('members/term/<term>/',MemebersByTerm.as_view(),name='members_term'),
    path('members/session/<session>/',MembersBySession.as_view(),name='members_session'),
    path('members/house/<house>/',MembersByHouse.as_view(),name="members_house"),
    path('members/house/<house>/party/<party>/',MembersByParty.as_view(),name="members_party"),
    path('members/house/<house>/state/<state>/',MembersByState.as_view(),name="members_state"),
    path('members/house/<house>/constituency/<constituency>/',MembersByConstituency.as_view(),name="members_const"),
    path('questions/',All_Questions.as_view(),name='all_questions'),
    path('questions/house/<house>/',QuestionsByHouse.as_view(),name='questions_house'),
    path('questions/year/<year>/',QuestionsByYear.as_view(),name='questions_year'),
    path('questions/type/<type>/',QuestionsByType.as_view(),name='questions_type'),
    path('questions/ministry/<ministry>/',QuestionsByMinistry.as_view(),name='questions_ministry'),
    path('questions/member/<member>/',QuestionsByMember.as_view(),name='questions_member'),
    path('debates/',All_Debates.as_view(),name='all_debates'),
    path('debates/year/<year>/',DebatesByYear.as_view(),name='debates_year'),
    path('debates/member/<member>/',DebatesByMember.as_view(),name='debates_member'),
    path('debates/type/<type>/',DebatesByType.as_view(),name='debates_type'),
    path('debates/house/<house>/',DebatesByHouse.as_view(),name='debates_house'),
    path('bills/',A_Bill.as_view(),name='all_bills'),
    path('bills/year/<year>/',BillsByYear.as_view(),name='bills_year'),
    path('bills/type/<type>/',BillsByType.as_view(),name='bills_type'),
    path('bills/status/<status>/',BillsByStatus.as_view(),name='bills_status'),
]