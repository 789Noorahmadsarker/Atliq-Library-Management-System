# ===========================================================================
# ===========================================================================
#
#   Goal:
#       Let Celina manage journals, where each issue is often requested by
#       staff for their research and development work.
#
#   How it works:
#       A Journal is a LibraryItem with one extra fact: the issue number.
#       This makes journals easy to locate by issue. Like a Book, it can be
#       borrowed and returned without any extra code.
# ===========================================================================
 
class Journal(LibraryItem):
    """A library item that also records the issue number of the journal."""
 
    def __init__(self, title, issue_number):
        super().__init__(title)             # Reuse the setup from LibraryItem
        self.issue_number = issue_number    # The extra detail that only journals have
 
 
# ---------------------------------------------------------------------------
# Try it out: create a journal and display its details
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("TASK 3  |  Journal: title and issue number")
print("=" * 60)
 
journal = Journal("Nature", 50)
print(f"Title: {journal.title}, Issue Number: {journal.issue_number}")
 
# Output:
# Title: Nature, Issue Number: 50
