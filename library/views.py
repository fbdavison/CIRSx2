from django.shortcuts import render
from django.db import connection
from .models import Document, CurationCategory, HealersHelpers


def curr_sql():
    sql = 'select lcc.cat_name, ld.title, ld.doc_path from library_document ld left join library_document_cat_num ldcn on ld.id = ldcn.document_id left join library_curationcategory lcc on ldcn.curationcategory_id = lcc.id left join library_curations lc on lcc.cur_num_id = lc.id where lc.id = 1 order by lcc.cat_order'
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

def resource_library(request):
    title = 'Resource Library'
    rsch = Document.objects.filter(doctyp_num=2).order_by('title')
    context = {'rsch': rsch, 'title': title}
    return render(request, 'resource-library.html', context)

def bibliographies(request):
    title = 'Bibliographies'
    bib = Document.objects.filter(doctyp_num=1).order_by('title')
    context = {'bib': bib, 'title': title}
    return render(request, 'bibliographies.html', context)

def curation(request):
    lst = curr_sql()
    context = {'lst': lst}
    return render(request, 'curation.html', context)

def healers(request):
    title = 'Healers and Helpers'
    heal = HealersHelpers.objects.order_by('vid_order')
    context = {'heal': heal, 'title': title}
    return render(request, 'healers-helpers.html', context)

def video_library(request):
    title = 'Video Library'
    vid = Document.objects.filter(doctyp_num=3).order_by('title')
    context = {'title': title, 'vid': vid}
    return render(request, 'video-library.html', context)