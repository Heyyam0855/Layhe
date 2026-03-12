from django.shortcuts import render

def test_view(request):
    """Test səhifəsi"""
    return render(request, 'test.html')