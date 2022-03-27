from audioop import avg
from multiprocessing import context
from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
from django.db.models import Sum,Avg,Min,Max,Count

# Create your views here.

def home(request):
      # student = Student.objects.get(pk=1)
      # student = Student.objects.last()
      # student = Student.objects.latest('pass_date')
      # student = Student.objects.earliest('pass_date')
      # student = Student.objects.create(name='shukumar',roll='120',city='dhaka',result=4,pass_date='2022-3-22')
      # student,created = Student.objects.get_or_create(name='raj',roll='121',city='dhaka',result=4,pass_date='2022-3-21')
      # student = Student.objects.filter(id=11).update(name= 'raj kumar')
      
      # oobjs= [ Student(name='karn',roll='123',city='jessor',result=4,pass_date='2022-3-23'),
      # Student(name='johor',roll='124',city='dhaka',result=3,pass_date='2022-3-22')
      # ]
      #  student= Student.objects.bulk_create(oobjs)

      # student= Student.objects.filter(id=12).delete()



      # student = Student.objects.filter(name__exact='shukumar')
      # student = Student.objects.filter(id__in=[4,10])
      # student = Student.objects.filter(name__contains='d')
      # student = Student.objects.filter(result__in=[4])
      # student = Student.objects.filter(result__gt=3)
      # student = Student.objects.filter(result__lt=4)
      # student = Student.objects.filter(result__lte=4)
      # student = Student.objects.filter(name__startswith ='a')
      # student = Student.objects.filter(pass_date__range =('2022-3-10','2022-3-22'))


      student = Student.objects.all()
      average = student.aggregate(Avg('result'))
      total = student.aggregate(Sum('result'))
      minimum = student.aggregate(Min('result'))
      maximim = student.aggregate(Max('result'))
      count = student.aggregate(Count('result'))

      context={'average':average, 'student':student,'total':total,'minimum':minimum,'maximum':maximim,'count':count}
      return render(request,'school/home.html',context)


      # student = Student.objects.all()


      # student = Student.objects.filter(result=4)
      # student = Student.objects.exclude(result=4)

      # student = Student.objects.order_by('name')
      # student = Student.objects.order_by('-name')
      # student = Student.objects.order_by('?')
     
     
     
      # student = Student.objects.order_by('id')[1:5]

      # student = Student.objects.values('name','city')

      # st = Student.objects.values_list('id','name', named=True)
      # tc = Teacher.objects.values_list('id','name', named=True)
      # student= tc.union(st)



      # st = Student.objects.values_list('name', named=True)
      # tc = Teacher.objects.values_list('name', named=True)
      # student= tc.intersection(st)


      # st = Student.objects.values_list('id','name', named=True)
      # tc = Teacher.objects.values_list('id','name', named=True)
      # student= tc.difference(st)



      #### AND OR OPERATORS  #######


      # student = Student.objects.filter(id=4) & Student.objects.filter(id=4)
      # student = Student.objects.filter(id=1,roll=101)
      # student = Student.objects.filter(Q(id=1)& Q(roll=101))










