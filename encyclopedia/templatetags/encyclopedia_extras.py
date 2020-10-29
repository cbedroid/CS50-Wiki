import random
from django import template


register = template.Library()


@register.filter("randomEntry")
def randomEntry(entries, *args):
    """Random wiki Entries
    Arguments:
        entries {list} -- list of entries
    """
    # NOTE: There seem to be something wrong with Django's random
    #      string inside anchor tags... So we will build our on filter tag here
    print("Entries", entries)
    print("Args", args)
    if entries:
        random_entry = random.choice(entries)
        print("Random_Entry", random_entry)
        return random_entry
