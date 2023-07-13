from django.contrib import admin
from .models import Projects
from .models import Post
from .models import Projects_en
from .models import Post_en
from .models import TecSkills
from .models import ContactData
from .models import ProSkills
from .models import ProSkills_en

admin.site.register(Projects)
admin.site.register(Post)
admin.site.register(Projects_en)
admin.site.register(Post_en)
admin.site.register(TecSkills)
admin.site.register(ContactData)
admin.site.register(ProSkills)
admin.site.register(ProSkills_en)
