"""
API Test Skriptləri - BRO-EN Backend

Bu skript backend API-nin düzgün işlədiyini yoxlayır.
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"


def test_api():
    print("=" * 60)
    print("BRO-EN Backend API Test")
    print("=" * 60)
    
    tests = [
        ("Şirkət məlumatları", f"{BASE_URL}/api/core/company/"),
        ("Xidmətlər", f"{BASE_URL}/api/core/services/"),
        ("Komanda", f"{BASE_URL}/api/core/team/"),
        ("FAQ", f"{BASE_URL}/api/core/faq/"),
        ("Ana səhifə məlumatları", f"{BASE_URL}/api/core/company-info/"),
        ("Test kateqoriyaları", f"{BASE_URL}/api/tests/categories/"),
        ("Testlər", f"{BASE_URL}/api/tests/"),
        ("Məşhur testlər", f"{BASE_URL}/api/tests/popular/"),
        ("Qiymət cədvəli", f"{BASE_URL}/api/tests/prices/"),
        ("Test paketləri", f"{BASE_URL}/api/tests/packages/"),
        ("Əlaqə məlumatları", f"{BASE_URL}/api/contact/info/"),
        ("Sosial media", f"{BASE_URL}/api/contact/social/"),
    ]
    
    print("\n🧪 API Endpoint Testləri:\n")
    
    for name, url in tests:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {name}: OK ({response.status_code})")
            else:
                print(f"❌ {name}: FAILED ({response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"❌ {name}: ERROR - {str(e)}")
    
    print("\n" + "=" * 60)
    print("📧 Form Test:")
    print("=" * 60)
    
    # Contact form test
    contact_data = {
        "first_name": "Test",
        "last_name": "User",
        "phone": "+994501234567",
        "email": "test@example.com",
        "subject": "Test mesajı",
        "message": "Bu bir test mesajıdır"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/contact/form-submit/",
            json=contact_data,
            timeout=5
        )
        if response.status_code == 201:
            print(f"✅ Əlaqə formu: OK ({response.status_code})")
            print(f"   Mesaj: {response.json().get('message')}")
        else:
            print(f"❌ Əlaqə formu: FAILED ({response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"❌ Əlaqə formu: ERROR - {str(e)}")
    
    print("\n" + "=" * 60)
    print("✨ Test tamamlandı!")
    print("=" * 60)


if __name__ == "__main__":
    test_api()