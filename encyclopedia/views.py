import markdown2
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from . import util


def index(request):
    context = {"entries": util.list_entries()}
    return render(request, "encyclopedia/index.html", context)


def wiki_search(request, search):
    search = request.GET.get("search")
    print("SEARCH", search)
    if not search:
        return redirect("notfound")

    print("Search", search)
    return wiki_entry(request, title=search)


def wiki_entry(request, title):
    context = {}
    entry_list = util.list_entries()

    # Filter the title  with case-insensitive search
    wiki = [entry for entry in entry_list if title.lower() in entry.lower()]

    if not wiki or wiki is None:
        return redirect("notfound")

    # get Entry by its title
    entry = util.get_entry(wiki[0])
    context["title"] = title
    context["entry"] = markdown2.markdown(entry).strip()
    return render(request, "encyclopedia/base_entry.html", context)


def delete_entry(request, title):
    context = {}

    if request.method == "POST":
        deletion = request.POST.get("deletion")
        for k, v in request.POST.items():
            print(f"DELETION items:{k}: {v}")
        print("DELETION", deletion)

        if title:
            if deletion == "yes":
                util.delete_entry(title)
                # Message here
                messages.error(request, f"{title} was deleted.")
                return redirect("index")
            else:
                return redirect("wiki_entry", title=title)
    # title = request.GET.get("title")
    print("Deleting title:", title)

    context["title"] = title
    return render(request, "encyclopedia/delete_entry.html", context)


def edit_entry(request, title):
    # This view handle creating and saving entries
    context = {}
    entry = util.get_entry(title)
    if not entry or entry is None:
        return redirect("notfound")

    # convert entry from html to Markdown
    context["title"] = title
    context["entry"] = entry
    context["config"] = "edit"
    return render(request, "encyclopedia/create_edit_entry.html", context)


def create_entry(request):
    context = {}

    context["config"] = "create"
    context["title"] = ""
    context["entry"] = ""

    return render(request, "encyclopedia/create_edit_entry.html", context)


def save_entry(request):
    # This view handle saving new and edit entries

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print("title", title)
        print("content", content)
        # Save entry
        if content and title:
            print("CONTENT:", content)
            entry = util.save_entry(title, str(content).strip())
            return redirect(reverse("wiki_entry", kwargs={"title": title}))
    return redirect("notfound")


def notFound(request):
    return render(request, "encyclopedia/notfound.html")