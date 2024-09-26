from django.shortcuts import render


def BaseNumber():
    # Options for bases to convert numbers
    options = []
    for base in range(2, 17):
        options.append(base)
    return options

def Convert(number, currentbase, futurebase):
    rests = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    currentbase = int(currentbase)
    futurebase = int(futurebase)
    inbase10 = int(number, currentbase)
    result = ""
    while inbase10 > 0:
        result += rests[inbase10 % futurebase]
        inbase10 = inbase10 // futurebase
    return result[::-1] or '0'


def home(request):
    try:
        options = BaseNumber()
        if request.method == "POST":
            number = request.POST.get("number")
            current_base = request.POST.get("current_base")
            future_base = request.POST.get("future_base")
            result = Convert(number, current_base, future_base)
            context = {"options": options, "result": result, "number": number, "first_base": current_base,
                       "second_base": future_base}
            return render(request, "home.html", context)
        return render(request, "home.html", {"options": options})
    except ValueError:
        errors_context = "Please go back in home page and introduce a valid number in valid bases!!!"
        return render(request, "error.html", {"errors_context": errors_context})
