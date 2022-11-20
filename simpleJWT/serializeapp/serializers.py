from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,Student

class SnippetSerializer(serializers.ModelSerializer):
    
   #validator
    def start_with(value):
        if value[0].lower() == 'r':
            raise serializers.ValidationError('can not start with r')

    title = serializers.CharField(validators =[start_with])

    class Meta:
        model = Snippet
        fields = [ 'title','code','linenos','language','style']
   
    #fiel level validation
    def validate_title(self, value):
        if len(value) > 10:
            raise serializers.ValidationError('Title len must be under 10')
        return value
    #object level validation
    def validate(self, data): #example
        title = data.get('title')
        if title == 'javascript1':
            raise serializers.ValidationError('Can not be javascript')
        return data
    


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


#     def create(self, validated_data):
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
####################################################################################
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    student_id = serializers.CharField()
    year = serializers.IntegerField()
  
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.student_id = validated_data.get('student_id',instance.student_id)
        instance.year = validated_data.get('year',instance.year)
        instance.save()
        return instance