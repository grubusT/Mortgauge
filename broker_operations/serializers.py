from rest_framework import serializers
from .models import (
    InterviewScript, ScriptSection, Client, Application, 
    Document, Task, Reminder, User
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class ClientSerializer(serializers.ModelSerializer):
    application_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = '__all__'
    
    def get_application_count(self, obj):
        return obj.applications.count()

class ApplicationSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    
    class Meta:
        model = Document
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name', read_only=True)
    
    class Meta:
        model = Reminder
        fields = '__all__'

class ScriptSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptSection
        fields = '__all__'

class InterviewScriptSerializer(serializers.ModelSerializer):
    sections = ScriptSectionSerializer(many=True, read_only=True)
    
    class Meta:
        model = InterviewScript
        fields = '__all__'

class InterviewScriptCreateSerializer(serializers.ModelSerializer):
    sections = ScriptSectionSerializer(many=True)

    class Meta:
        model = InterviewScript
        fields = '__all__'

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        script = InterviewScript.objects.create(**validated_data)
        
        for section_data in sections_data:
            section = ScriptSection.objects.create(**section_data)
            script.sections.add(section)
        
        return script
