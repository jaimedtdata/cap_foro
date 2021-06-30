from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=40,null=True, blank=True)
    lastname = models.CharField(max_length=40,null=True, blank=True)
    document = models.CharField(max_length=20,null=True, blank=True)
    #created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.firstname + " " + self.lastname
 
    class Meta:
        ordering = ['created']
         
    class Meta:  
        db_table = "user_member"

"""
Forum 
forum_id, forum_name,forum_type, forum_description"

"Users
user_ id,
user_name,
user_mobile,
user_email,
user_usemame,
user_password,
user_address"

"Registartions
 Attributes of Registartions are registration_id,registration_user_id,registration_name, registration_type,registration_number, registration_date,registration_description"

"Posts :
 post_id,post_user_id,post_title,post_type, post_description"

"Replies :
 replies_id, replies_user_id,replies_title, replies_type,replies_description"

"Polls Entity : Attributes of Polls are poll_id,poll_name, pon_type, poll_description"
https://github.com/mdn/django-diy-blog/blob/master/blog/models.py
"""