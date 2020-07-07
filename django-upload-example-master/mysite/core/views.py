from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import BookForm
from .models import Book
import os
a=0
b=0
from django.http import HttpResponse
class Home(TemplateView):
    template_name = 'home.html'


'''def upload(request):

    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
    out = 0
    if out==0:
        messages.info(request,'Malicious Content')
        return render('upload')
    else:
        messages.info(request,'Legit File')'''

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })
viruslist=[]

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            from django.contrib import messages
            import pandas as pd
            from sklearn.preprocessing import LabelEncoder
            l = LabelEncoder()
            from sklearn.neighbors import KNeighborsClassifier
            import os
            import hashlib
            # Loading dataset
            malware = pd.read_csv("C:\\Users\\hp\\Desktop\\project\\MalwareData.csv", sep="|")
            df = malware[["md5", 'legitimate,']]

            df['legitimate,'] = l.fit_transform(df['legitimate,'])
            length = df.shape[0]

            # User defined function for check value
            def check(df, md5):
                df = df.append({'md5': md5}, ignore_index=True)
                df['md5'] = l.fit_transform(df['md5'])
                train = df.iloc[:length, :]
                test = pd.DataFrame(df.iloc[length])
                test = test.transpose()['md5']
                x = train['md5']
                y = train['legitimate,']
                model = KNeighborsClassifier(n_neighbors=1).fit(x.values.reshape(-1, 1), y)
                # Predicting values
                pred = model.predict(test.values.reshape(-1, 1))
                return pred

            # create a foler(myfolder) in D drive and put the file in it
            global c
            c = 0
            def pred():
                    path = "C:\\Users\hp\\Desktop\\project\\xxx\\django-upload-example-master virus\\django-upload-example-master virus\\django-upload-example-master\\media\\books\\file\\"
                    import glob
                    list_of_files = glob.glob(path + '/*')  # * means all if need specific format then *.csv
                    if len(list_of_files)==0:
                        latest_file=list_of_files[0]
                    else:
                        latest_file = max(list_of_files, key=os.path.getctime)
                    md5 = hashlib.md5(open(latest_file, 'rb').read()).hexdigest()
                    print("File name",latest_file)
                    print("MD5", md5)
                    predict = check(df, md5)
                    if predict == [0.]:
                        messages.info(request, 'Legit File, continue..')
                        print("Legit File, continue..")

                        #return redirect('book_list')
                        #return render(request,'upload_book.html')
                    else:
                        global c
                        c += 1
                        print('c=', c)
                        messages.info(request,'Virus Found.. file not sent....')
                        print("Virus Found")
                        latest_file=latest_file.replace("C:\\Users\hp\\Desktop\\project\\xxx\\django-upload-example-master virus\\django-upload-example-master virus\\django-upload-example-master\\media\\books\\file\\","")
                        viruslist.append(latest_file)

            pred()
            print('a=', c)
            if c == 1:
                print('a1=', c)
                return redirect('dele')
            else:
                print('a2=', c)
                return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })
def dele(request):
    books = Book.objects.all()
    return render(request,'viruss.html',{'books':books})

def delete_book(request, pk):
     if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
     return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

def analyse(request,mylist=viruslist):
    import pandas as pd
    import os
    path = "C:\\Users\\hp\\Desktop\\project\\django-upload-example-master virus\\django-upload-example-master\\media\\books\\file\\"
    mylist = pd.Series(viruslist)
    import matplotlib.pyplot as plt

    for i in range(len(mylist)):
        mylist[i] = mylist[i].replace(".txt", "")
        mylist[i] = mylist[i].replace(".vba", "")
        mylist[i] = mylist[i].replace(".bat", "")
        mylist[i] = mylist[i].replace(".ext", "")
        end = mylist[i].find("_")
        if end == -1:
            mylist[i] = mylist[i][:]
        else:
            mylist[i] = mylist[i][:end]

    table = mylist.value_counts()
    plt.bar(table.index, table)
    plt.show()
    return render(request,'graph.html')

