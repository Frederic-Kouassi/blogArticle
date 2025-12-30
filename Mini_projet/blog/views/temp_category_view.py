class AdminCategoryView(View):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect('login')
        
        categories = Category.objects.all().order_by('-id')
        return render(request, "admin_categories.html", {
            "categories": categories,
            "active_tab": "categories"
        })

    def post(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect('login')
            
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            # Handle manual icon field if separate from form or just let form save it if added to Meta fields
            # Assuming CategoryForm is updated or we handle it manually
            if 'icon' in request.POST:
                 category.icon = request.POST['icon']
            category.save()
            messages.success(request, "Category created successfully")
        else:
            messages.error(request, "Error creating category")
            
        return redirect("admin_categories")
