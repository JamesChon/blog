# Mini Challenge 2

## Basic user navitation and interation

### Acceptance Criteria
1. Your web application must have a home page, which explains the purpose of the app (high level).
2. Your web application must have an about page, including a short blurb or bio about yourself or your finctional character.
3. Your web application must, at a minimum, allow users to view a list of posts.
3.1. Your users should be able to click a link on the navbar to go to your list of posts.
4. Your web application must, at a minimum, allow users to view a detail page for any given post they select.
4.1. It is recommended to do this through an anchor tag in list.html
5. Your web application must, in addition to the previous point, implement full CRUD support for the Post model.
5.1. You should have templates and urlpatterns for 'PostCreateView', 'PostUpdateView', and 'PostDeleteView'.
6. Test your project, you should be able to perform all CRUD(S) operations on your Post model.





from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        'draft': 'A post that is not ready to be published',
        'published': 'A post available for all to see',
        'archived': 'An older post available in the archive only'
    }
    Status = apps.get_model('posts', 'Status')
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [migrations.RunPython(populate_status)]