from django.db import models

# Create your models here.

#内容，名字，时间
class Content(models.Model):
    content=models.TextField(db_column="content",null=False)#内容
    name=models.CharField(db_column='name',max_length=20,null=False)#姓名
    time=models.DateTimeField(auto_now_add=True)#自动添加时间
    class Meta:
        managed=True
        db_table='Content'
    def __str__(self):
        return '内容：%\t姓名：%s\t日期：%s' %(self.content,self.name,self.time)