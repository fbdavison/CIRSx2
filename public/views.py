from django.shortcuts import render
from library.models import Document
from .models import BOTY, ShoeyAwards, ResearchCommittee


def home(request):
    title = 'CIRSx: Leading the Way in Treating, Educating, and Serving Those with CIRS.'
    #Integrate Teachables and CTA
    context = {'title': title}
    return render(request, 'index.html', context)

def about(request):
    title = 'About Us'
    # Add to db and CTA
    context =  {'title': title}
    return render(request, 'about.html', context)

def boty(request):
    title = 'Book of the Year'
    boy = BOTY.objects.all().order_by('year')
    # Add CTA
    context = {'title': title, 'boy': boy}
    return render(request, 'book-of-the-year.html', context)

def institute(request):
    title = 'CIRSx Institute'
    #Integrate Teachables and CTA
    context = {'title': title}
    return render(request, 'cirsx-institute.html', context)

def conference(request):
    title = 'CIRSX | 2025 Conference Registration'
    # Add details to db and CTA
    context = {'title': title}
    return render(request, 'conference.html', context)

def research_lab(request):
    title = 'Research Lab'
    comm = ResearchCommittee.objects.filter(active=True).order_by('name')
    context = {'title': title, 'comm':comm}
    return render(request, 'research-lab.html', context)

def shoey_awards(request):
    title = 'Shoey Awards'
    award = ShoeyAwards.objects.all()
    # Add CTA
    context = {'title': title, 'award':award}
    return render(request, 'shoey-awards.html', context)

def conference_archives(request):
    title = 'Past Conferences'
    context = {'title': title}
    return render(request, 'archives.html', context)

def conference_exhibitors(request):
    title = 'Exhibitors'
    context = {'title': title}
    return render(request, 'conference-exhibitors.html', context)