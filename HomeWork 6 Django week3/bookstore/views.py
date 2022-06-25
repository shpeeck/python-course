from django.shortcuts import render, redirect, Http404
from django.http import HttpRequest, HttpResponse
from .models import Books, Autors
from .forms import PostForm


books = [
    {'id': 1, 'title': 'Fluent Python','released_year': 2015, 'description': 'Python’s simplicity lets you become productive quickly, but this often means you aren’t using everything it has to offer. With this hands-on guide, you’ll learn how to write effective, idiomatic Python code by leveraging its best—and possibly most neglected—features. Author Luciano Ramalho takes you through Python’s core language features and libraries, and shows you how to make your code shorter, faster, and more readable at the same time.', 'author_id': 1}, 
    {'id': 2, 'title': 'Programming Python','released_year': 2006, 'description': 'Already the industry standard for Python users, ProgrammingPython from OReilly just got even better. This third edition has been updated toreflect current best practices andthe abundance of changes introduced by the latest version of thelanguage, Python 2.5', 'author_id': 3}, 
    {'id': 3, 'title': 'Learning Python','released_year': 2015, 'description': 'Portable, powerful, and a breeze to use, Python is ideal for both standalone programs and scripting applications. With this hands-on book, you can master the fundamentals of the core Python language quickly and efficiently, whether youre new to programming or just new to Python. Once you finish, you will know enough about the language to use it in any application domain you choose.', 'author_id': 3}, 
    {'id': 5, 'title': 'Regular Expression Pocket Reference','released_year': 2007, 'description': 'This handy little book offers programmers a complete overview of the syntax and semantics of regular expressions that are at the heart of every text-processing application. Ideal as a quick reference, Regular Expression Pocket Reference covers the regular expression APIs for Perl 5.8, Ruby (including some upcoming 1.9 features), Java, PHP, .NET and C#, Python, vi, JavaScript, and the PCRE regular expression libraries.', 'author_id': 2}, 
    {'id': 4, 'title': 'Meeting Mastery','released_year': 2016, 'description': 'Meeting problems are solvable. With this book, you’ll learn how to use meetings to achieve your goals. You’ll become a persuasive meeting facilitator. You’ll walk out of meetings with clear decisions, focused action items, and the confidence that you’ve gotten the most creative and innovative ideas from your team.', 'author_id': 2}]

authors = [{'id': 1, 'first_name': 'Luciano', 'last_name': 'Ramalho', 'age': 51 }, {'id': 2, 'first_name': 'Tony', 'last_name': 'Stubblebine', 'age': 55 }, {'id': 3, 'first_name': 'Mark', 'last_name': 'Lutz', 'age': 55 }]

def all(request):
    books = Books.objects.all()
    if request.method == "GET" and 'search' in request.GET:
        search = request.GET['search']
        books = books.filter(title__icontains=search)
    context = {'books': books}
    return render(request, 'bookstore/index.html', context=context)

def book(request, book_id):
    try:
        book = Books.objects.get(pk=book_id)
        autor = Autors.objects.get(pk=book.author_id)
        return render(request, 'bookstore/book.html', context={'book': book, 'autor': autor})
    except Books.DoesNotExist: 
        raise Http404(f"Not found book_id {book_id}")
    
def autor(request, autor_id):
    try:
        autor = Autors.objects.get(pk=autor_id)
        return render(request, 'bookstore/autor.html', context={'autor': autor})
    except Autors.DoesNotExist: 
        raise Http404(f"Not found autor_id {autor_id}")
        
def autors_books(request, autor_id):
    try:
        lst_books = Books.objects.filter(author_id=autor_id)
        return render(request, 'bookstore/autors-books.html', context={'lst_books': lst_books})
    except: 
        return HttpResponseNotFound('Not found')

def add_book(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'post_form': PostForm}
    return render(request, 'bookstore/add-book.html', context=context)
    





        
        
        
