# Generated by Django 3.1.7 on 2021-04-04 17:58

from django.db import migrations
from django.utils import timezone

def populate_db(appreg, ed):

    lorem = """At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas 
    molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. 
    Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod 
    maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus 
    saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus 
    maiores alias consequatur aut perferendis doloribus asperiores repellat. """

    Blog = appreg.get_model('blog', 'Blog')
    
    #First blog with comments
    blog1 = Blog(title="First Blog", author="First Blog Author", content=lorem, posted=timezone.now() - timezone.timedelta(minutes=15))
    blog1.save()

    b1comment1 = blog1.comment_set.create(commenter="John Jones", email="test@test.com", content="First comment on the 1st blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=15))
    b1comment1.save()

    b1comment2 = blog1.comment_set.create(commenter="John Jones", email="test@test.com", content="Second comment on the 1st blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=10))
    b1comment2.save()

    b1comment3 = blog1.comment_set.create(commenter="John Jones", email="test@test.com", content="Third comment on the 1st blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=5))
    b1comment3.save()

    b1comment4 = blog1.comment_set.create(commenter="John Jones", email="test@test.com", content="Fourth comment on the 1st blog " + lorem, posted=timezone.now())
    b1comment4.save()

    #Second blog and comments
    blog2 = Blog(title="Second Blog", author="Second Blog Author", content=lorem, posted=timezone.now() - timezone.timedelta(minutes=10))
    blog2.save()

    b2comment1 = blog2.comment_set.create(commenter="John Jones", email="test@test.com", content="First comment on the 2nd blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=15))
    b2comment1.save()

    b2comment2 = blog2.comment_set.create(commenter="John Jones", email="test@test.com", content="Second comment on the 2nd blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=10))
    b2comment2.save()

    b2comment3 = blog2.comment_set.create(commenter="John Jones", email="test@test.com", content="Third comment on the 2nd blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=5))
    b2comment3.save()

    b2comment4 = blog2.comment_set.create(commenter="John Jones", email="test@test.com", content="Fourth comment on the 2nd blog " + lorem, posted=timezone.now())
    b2comment4.save()

    #Third blog and comments
    blog3 = Blog(title="Third Blog", author="Third Blog Author", content=lorem, posted=timezone.now() - timezone.timedelta(minutes=5))
    blog3.save()

    b3comment1 = blog3.comment_set.create(commenter="John Jones", email="test@test.com", content="First comment on the 3rd blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=15))
    b3comment1.save()

    b3comment2 = blog3.comment_set.create(commenter="John Jones", email="test@test.com", content="Second comment on the 3rd blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=10))
    b3comment2.save()

    b3comment3 = blog3.comment_set.create(commenter="John Jones", email="test@test.com", content="Third comment on the 3rd blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=5))
    b3comment3.save()

    b3comment4 = blog3.comment_set.create(commenter="John Jones", email="test@test.com", content="Fourth comment on the 3rd blog " + lorem, posted=timezone.now())
    b3comment4.save()

    #Fourth blog and comments
    blog4 = Blog(title="Fourth Blog", author="Fourth Blog Author", content=lorem, posted=timezone.now())
    blog4.save()

    b4comment1 = blog4.comment_set.create(commenter="John Jones", email="test@test.com", content="First comment on the 4th blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=15))
    b4comment1.save()

    b4comment2 = blog4.comment_set.create(commenter="John Jones", email="test@test.com", content="Second comment on the 4th blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=10))
    b4comment2.save()

    b4comment3 = blog4.comment_set.create(commenter="John Jones", email="test@test.com", content="Third comment on the 4th blog " + lorem, posted=timezone.now() - timezone.timedelta(minutes=5))
    b4comment3.save()

    b4comment4 = blog4.comment_set.create(commenter="John Jones", email="test@test.com", content="Fourth comment on the 4th blog " + lorem, posted=timezone.now())
    b4comment4.save()

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]