################### req / res
request.data
request.method
return Response(data) # response
status.HTTP_400_BAD_REQUEST

############################### serializers
# Serializer
##| ModelSerializer  # default fields repr, create and update
##| HyperlinkedModel #same as Model but link instead of pk

Serializer: #similar to django forms
    CharField(read_only=True, required=False, allow_blank=True, max_lengtg=100)
    ChoiceField(choices=['red', 'gree', 'blue'], default='red')

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.save()
        return instance


HyperlinkedModelSerializer # class Meta with model/fields


user_serialized = UserSerializer(data=user_data)
user_serialized.is_valid()
user_serialized.validated_data
user_serialized.save()

################### permissions

IsAuthenticated
permissions_classes = [IsAuthenticatedOrReadOnly,]
#### Custom: ex -> only author can edit the resource
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


################## views & viewsets: function based / class based / mixins / generic class based
## fbv | cbv + mixins
### APIView
#### | GenericAPIView
#### | ListAPIView/RetrieveAPIView/ListCreateAPIView/RetrieveUpdateDestroyAPIView

VIEWS: BASED ON HANDLES LIKE GET OR PUT
VIEWSETS: BASED ON OPERATIONS LIKE retrieve or update


# function based: @api_view([...])

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        return Response(UserSerializer(User.objects.all(), many=True).data)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data) # PUT: UserSerializer(myUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=...)
        return Response(serializer.errors, status=...)


# class based   : APIView # methods enabled by implementing get, post, put, delete
def get(self, request, pk): #same as request.method GET in fbv
def put(self, request, pk): #same as request.method POST/PUT in fbv

# class based   : GenericApiView # same as APIView + pagination/filtering/etc

# mixins: Add specific functionallity to ApiView/GenericApiView: 
##RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, CreateModelMixin: retrieve, update, destroy, list, create 
def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)


# generic class based: ListCreateAPIView, RetrieveUpdateDestroyAPIView

# viewset for reading: ReadOnlyModelViewSet instead of RetrieveModelMixin/ListModelMixin or ListAPIView/RetrieveAPIView
#                      ModelViewset instead of the generic class based ones

HOW TO ADD CUSTOM ENDPOINT TO VIEWSETS?
@action(detail=True, methods=['GET',])
def hightlight(self, request, *args, **kwargs):
    return Response(CustomSerializerThing(...))


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]
#################### routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='user') #binding viewsets

path('', include(router.urls))
path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

# pagination
REST_FRAMEWORK = [
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
]

################## TODO: check the api guide
# https://www.django-rest-framework.org/api-guide/requests/
