from django.shortcuts import render

def home(req):
    return render( req,"index.html")

def about(req):
    return render( req,"about.html")

def news(req):
    return render( req,"news.html")

def contact(req):
    return render( req,"contact.html")

def admins(req):
    return render( req,"admin/index.html")

def Admin_edit(req):
    return render(req,"admin/pages/edit/basic_editfile.html")

def Admin_add(req):
    return render(req,"admin/pages/forms/basic_elements.html")

def Admin_view(req):
    return render(req,"admin/pages/tables/basic-table.html")
