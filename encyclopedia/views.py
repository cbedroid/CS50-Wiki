import re
import random
import markdown2
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from . import util


def referred_message(req, url, msg, level="success"):
    """Handle referred message  when a view is redirect

    Arguments:
        req [dict] -- redirect request object
        url [str]  --  referred url
        msg [str]  -- message to display
        level[str] -- message level. default: success
    """
    referred_url = req.META.get("HTTP_REFERER")
    if referred_url and url in referred_url:
        # dynamically creating message with specified level
        msg_type = getattr(messages, level, None)
        if msg_type:
            msg_type(req, msg)


def index(request):
    context = {"entries": util.list_entries()}
    return render(request, "encyclopedia/index.html", context)


def wiki_entry(request, title):
    """ Base wiki view to view all available entries"""
    context = {}
    entry_list = util.list_entries()

    # Filter the title  with case-insensitive search
    title = title.strip()
    wiki = [entry for entry in entry_list if title.lower() in entry.lower()]

    if not wiki or wiki is None:
        return redirect("notfound")

    # get Entry by its title
    entry = util.get_entry(wiki[0])
    context["title"] = title
    context["entry"] = markdown2.markdown(entry).strip()
    return render(request, "encyclopedia/base_entry.html", context)


def wiki_search(request, search):
    """Wiki  side search bar

    Arguments:
        request {obj} -- Django request
        search {str} --  Name of entry to search for

    Returns:
        [Django view] -- rendered view template   'search/'
    """
    search = request.GET.get("search")
    if not search:
        return redirect("notfound")

    return wiki_entry(request, title=search)


def handler_save(request, **kwargs):
    """Save Entry

    Arguments:
        request {obj} -- Django request

    Returns:
        [Django redirect] -- redirect view   'index/' or 'wiki/<title>'
    """
    # This view handle saving new and edit entries
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # Save entry
    title = kwargs.get("title", "")
    content = kwargs.get("content", "")
    if content and title:
        title = re.sub(r"\s", "_", title.strip())
        entry = util.save_entry(title.strip(), str(content).strip())
        referred_message(request, "edit", f"{title} was updated successfully")
        return redirect("wiki_entry", title=title)

    return redirect("notfound")


def update_entry(request, title=""):
    """Update Wiki entry

    Arguments:
        request {obj} -- Django request
        title {str} -- Name of Wiki entry to update

    Returns:
        [Django view] -- rendered view template 'edit-entry/'
    """

    context = {"config": "create"}
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        submit = request.POST.get("submit")
        hidden = request.POST.get("config")

        if submit is None:
            if "create" in hidden:
                return redirect(index)
            else:
                return redirect(reverse("wiki_entry", kwargs={"title": title}))

        elif not title or not content:
            # redirect user to the same page to make changes
            messages.warn(
                request, f" You must add a title and content to create entry!"
            )

            return render(request, "encyclopedia/create_edit_entry.html", context)
        # Save the entry
        action = "created" if "edit" in hidden else "updated"
        messages.success(request, f" Your entry was {action} successfully!")
        print("\n\nTitle", title)
        return handler_save(request, title=title, content=content)

    else:  # GET request
        if title:
            entry = util.get_entry(title)
            if not entry or entry is None:
                return redirect("notfound")
            context["entry"] = entry
            context["config"] = "edit"

        # convert entry from html to Markdown
        context.update(
            {
                "title": title,
                "unavailable_entry": util.list_entries(),
            }
        )
    return render(request, "encyclopedia/create_edit_entry.html", context)


def random_entry(request):
    """Random Wiki entry

    Arguments:
        request {obj} -- Django request

        Returns:
            [Django view] -- rendered view template   'delete-entry/'
    """

    entry_list = util.list_entries()
    if entry_list:
        rand_entry = random.choices(entry_list)[0]
        return HttpResponseRedirect(reverse("wiki_entry", args=(rand_entry,)))

    messages.error(request, f"Opp... Something went wrong!")
    return redirect(index)


def delete_entry(request, title):
    """Delete Wiki entry

    Arguments:
        request {obj} -- Django request
        title {str} -- Name of entry to detete

    Returns:
        [Django view] -- rendered view template   'delete-entry/'
    """

    context = {}
    if request.method == "POST":
        deletion = request.POST.get("deletion")

        if title:
            if deletion == "yes":
                util.delete_entry(title)
                # Message here
                messages.error(request, f"{title} was deleted.")
                return redirect("index")
            else:
                messages.warning(request, f"Deleting was cancel {title}.")
                return redirect("wiki_entry", title=title)

    context["title"] = title
    return render(request, "encyclopedia/delete_entry.html", context)


def notFound(request):
    return render(request, "encyclopedia/notfound.html")