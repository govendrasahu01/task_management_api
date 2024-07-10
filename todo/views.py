from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import generics,viewsets,status

# viewset-----------------------------
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = task_serializer
    
    @action(detail=True, methods=['PATCH','GET'])
    def complete(self,request,pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        
        return Response({'status':"Task is marked as complete"})


# class based --------------------

# Create your views here.
# class index(generics.ListCreateAPIView, generics.CreateAPIView):
#     queryset = Task.objects.all().order_by('-id')
#     serializer_class = task_serializer
    
# class del_update(generics.DestroyAPIView,generics.UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = task_serializer
        

# class create(generics.CreateAPIView):
#     serializer_class = task_serializer



# function based ----------------

# @api_view(['GET'])
# def index(request):
#     all_tasks = Task.objects.all().order_by('-id')
#     ser_data = task_serializer(all_tasks,many = True)
    
#     return Response({'data':ser_data.data})


# @api_view(['POST'])
# def create(request):
#     data = request.data
    
#     ser_data= task_serializer(data = data)
    
#     if not ser_data.is_valid():
#         return Response({"Status":'403',"message":ser_data.errors})

#     ser_data.save()
#     return Response({'status':"200", "message":"new Task added!"})

