def get(self, request, *args, **kwargs):
    user = get_object_or_404(User, id=kwargs['id'])
    if request.user.is_authenticated:
        if user.id != request.user.id:
            messages.error(request, gettext('You do not have rights to change another user.'))
            return redirect('users')
        else:
            form = UpdateUserForm(request)
            return render(request, 'users/update.html', context={"form": form, "user": user})
    messages.error(request, gettext('You do not have rights to change another user.'))
    return redirect('users')


def post(self, request, *args, **kwargs):
    user = get_object_or_404(User, id=kwargs['id'])
    form = UpdateUserForm(request.POST or None)
    print(form.is_valid())
    if user.id == request.user.id and request.user.is_authenticated and form.is_valid():
        form.save()
        messages.success(request, gettext('User successfully updated'))
        print('Пони')
        redirect('users')
    else:
        print("Хуита")
        return render(request, 'users/update.html', context={"form": form, "user": user})