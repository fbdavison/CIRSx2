from django.shortcuts import render
from .models import Document, Curations


def reference_papers(request):
    rsch = Document.objects.filter(doctyp_num=2).order_by('title')
    #rsch = Document.objects
    context = {'rsch': rsch}
    return render(request, 'reference_papers.html', context)


def bibliographies(request):
    bib = Document.objects.filter(doctyp_num=1).order_by('title')
    context = {'bib': bib}
    return render(request, 'bibliographies.html', context)


def curation(request):
    cur = Curations.objects.filter(cur_name='Video Curration')
    cat = cur.distinct('cat_name')
    subcat = cur.filter(subcat_name__isnull=False).distinct('subcat_name')
    lst = Document.objects.filter(curr_num__cur_name='Video Curration')
    context = {'cat': cat, 'cur': cur, 'lst': lst}
    return render(request, 'curation.html', context)
