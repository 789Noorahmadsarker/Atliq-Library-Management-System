# ===========================================================================

#   Goal of this task:
#       Let Celina catalog books separately from other items, with the
#       author's name included.
#
#   How it works:
#       A Book is a LibraryItem with one extra fact: the author.
#       Because of inheritance, a Book can be borrowed and returned exactly
#       like any library item, with no extra code needed.
# ===========================================================================

class Book(LibraryItem):
    """A library item that also records the name of its author."""

    def __init__(self, title, author):
        super().__init__(title)     # Reuse the setup from LibraryItem (title, is_borrowed)
        self.author = author        # The extra detail that only books have


# ---------------------------------------------------------------------------
# Try it out: create a book and display its details
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("TASK 2  |  Book: title and author")
print("=" * 60)

book = Book("The Magic Of Thinking Big", "David Schwartz")
print(f"Title: {book.title}, Author: {book.author}")


# ===========================================================================
# Sample Output:
# Title: The Magic Of Thinking Big, Author: David Schwartz
