## Books Site

### Purpose
This assignment is designed for you to practice creating models and relating them using one-to-many and many-to-many relationships.

###Answer:
1. How would we filter for all books with titles containing the word ‘Django’?
    - Book.objects.filter(title__contains="Django")
2. How would we filter for all books with tag ‘Fiction’?
    - Book.objects.filter(tags__name="Fiction")
3. How would we filter for all authors who have written books containing the word ‘Django’?
    - Author.objects.filter(book__title__contains='Django')