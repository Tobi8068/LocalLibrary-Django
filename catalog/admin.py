from django.contrib import admin
from .models import Book, Author, BookInstance, Genre, Language;
# Register your models here.

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')

  inlines = [BooksInstanceInline]

  def display_genre(self):
    """Create a string for the Genre. This is required to display genre in Admin."""
    return ', '.join(genre.name for genre in self.genre.all()[:3])
  pass
admin.site.register(Book, BookAdmin)

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_birth')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
  pass
admin.site.register(Author, AuthorAdmin)

# admin.site.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  list_filter = ('status', 'due_back')
  fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
  pass
admin.site.register(BookInstance, BookInstanceAdmin)

admin.site.register(Genre)

admin.site.register(Language)

