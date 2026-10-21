# ===========================================================================
# ===========================================================================
#
#   Goal of this task:
#       Help Celina automate the borrowing and returning of library items.
#
#   How it works:
#       Every item has two facts (attributes):
#           title        - the name of the item
#           is_borrowed  - True if someone has it right now, otherwise False
#
#       and two actions (methods):
#           borrow_item()  - marks the item as borrowed
#           return_item()  - marks the item as returned
#
#       Both actions refuse to run when they make no sense:
#           - an item that is already borrowed cannot be borrowed again
#           - an item that is not borrowed cannot be returned
# ===========================================================================

class LibraryItem:
    """A general item in the library that can be borrowed and returned."""

    def __init__(self, title):
        # This runs automatically when a new item is created.
        self.title = title          # The name of the item
        self.is_borrowed = False    # Every new item starts on the shelf

    def borrow_item(self):
        """Mark the item as borrowed, unless it is already borrowed."""
        if self.is_borrowed:
            # Stop here and report the problem
            raise Exception(f"The item '{self.title}' is already borrowed.")
        self.is_borrowed = True
        print(f"{self.title} has been borrowed.")

    def return_item(self):
        """Mark the item as returned, unless it was never borrowed."""
        if not self.is_borrowed:
            # Stop here and report the problem
            raise Exception(f"The item '{self.title}' is not borrowed.")
        self.is_borrowed = False
        print(f"{self.title} has been returned.")


# ---------------------------------------------------------------------------
# Try it out: borrow and return a library item
# ---------------------------------------------------------------------------
print("=" * 60)
print("TASK 1  |  Library item: borrow and return")
print("=" * 60)

# Create one real item from the blueprint
library_item = LibraryItem("The Magic Of Thinking Big")
print(library_item.title)

library_item.borrow_item()    # Someone takes the item
library_item.return_item()    # The item is brought back
library_item.borrow_item()    # Someone takes it again (allowed, it is back on the shelf)

# Output:
# The Magic Of Thinking Big
# The Magic Of Thinking Big has been borrowed.
# The Magic Of Thinking Big has been returned.
# The Magic Of Thinking Big has been borrowed.
