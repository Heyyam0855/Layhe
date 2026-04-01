# HTTP Response Status Codes

HTTP cavab status kodları, serverin müştəriyə göndərdiyi cavabın vəziyyətini göstərən üç rəqəmli kodlardır.

## 1xx - İnformasiya Cavabları (Informational Responses)

- **100 Continue**: Müştəri sorğusuna davam edə bilər
- **101 Switching Protocols**: Server protokolu dəyişir
- **102 Processing**: Server sorğunu emal edir (WebDAV)
- **103 Early Hints**: Server resursları əvvəlcədən yükləmək üçün məlumat göndərir

## 2xx - Uğurlu Cavablar (Successful Responses)

- **200 OK**: Sorğu uğurla yerinə yetirildi
- **201 Created**: Yeni resurs yaradıldı
- **202 Accepted**: Sorğu qəbul edildi, lakin hələ emal edilməyib
- **203 Non-Authoritative Information**: Meta-məlumat orijinal serverdən deyil
- **204 No Content**: Sorğu uğurlu oldu, lakin qaytarılacaq məzmun yoxdur
- **205 Reset Content**: Müştəri sənəd görünüşünü sıfırlamalıdır
- **206 Partial Content**: Yalnız məzmunun bir hissəsi göndərilir

## 3xx - Yönləndirmə Mesajları (Redirection Messages)

- **300 Multiple Choices**: Sorğu üçün birdən çox seçim mövcuddur
- **301 Moved Permanently**: Resurs daimi olaraq yeni URL-ə köçürülüb
- **302 Found**: Resurs müvəqqəti olaraq başqa URL-də yerləşir
- **303 See Other**: Cavab başqa URL-də tapıla bilər
- **304 Not Modified**: Resurs dəyişməyib, keş istifadə edilə bilər
- **307 Temporary Redirect**: Müvəqqəti yönləndirmə (metod dəyişməz)
- **308 Permanent Redirect**: Daimi yönləndirmə (metod dəyişməz)

## 4xx - Müştəri Xətaları (Client Errors)

- **400 Bad Request**: Yanlış sorğu sintaksisi
- **401 Unauthorized**: Autentifikasiya tələb olunur
- **402 Payment Required**: Ödəniş tələb olunur (gələcək istifadə üçün)
- **403 Forbidden**: Server sorğunu rədd edir
- **404 Not Found**: Resurs tapılmadı
- **405 Method Not Allowed**: HTTP metodu dəstəklənmir
- **406 Not Acceptable**: Server müştərinin qəbul edə biləcəyi məzmun yarada bilmir
- **407 Proxy Authentication Required**: Proxy autentifikasiyası tələb olunur
- **408 Request Timeout**: Sorğu vaxtı keçdi
- **409 Conflict**: Sorğu resursun cari vəziyyəti ilə ziddiyyət təşkil edir
- **410 Gone**: Resurs artıq mövcud deyil
- **411 Length Required**: Content-Length header tələb olunur
- **412 Precondition Failed**: Şərt yerinə yetirilmədi
- **413 Payload Too Large**: Sorğu çox böyükdür
- **414 URI Too Long**: URL çox uzundur
- **415 Unsupported Media Type**: Media tipi dəstəklənmir
- **416 Range Not Satisfiable**: Tələb olunan range ödənilə bilməz
- **417 Expectation Failed**: Expect header ödənilə bilməz
- **418 I'm a teapot**: Server çaydan dəmləməyi rədd edir (zarafat kodu)
- **422 Unprocessable Entity**: Sorğu düzgündür, lakin emal edilə bilmir
- **429 Too Many Requests**: Çox sayda sorğu göndərilib

## 5xx - Server Xətaları (Server Errors)

- **500 Internal Server Error**: Serverdə daxili xəta baş verdi
- **501 Not Implemented**: Server funksiyanı dəstəkləmir
- **502 Bad Gateway**: Gateway yanlış cavab aldı
- **503 Service Unavailable**: Server müvəqqəti olaraq əlçatan deyil
- **504 Gateway Timeout**: Gateway vaxtı keçdi
- **505 HTTP Version Not Supported**: HTTP versiyası dəstəklənmir
- **511 Network Authentication Required**: Şəbəkə autentifikasiyası tələb olunur

## Ən Çox İstifadə Olunan Kodlar

### Müştəri tərəfi:
- **200**: Hər şey qaydasındadır
- **404**: Səhifə tapılmadı
- **401/403**: Giriş qadağandır

### Server tərəfi:
- **500**: Server xətası
- **503**: Xidmət əlçatan deyil

## Flask-da Status Kod Qaytarma

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/success')
def success():
    return jsonify({"message": "Uğurlu"}), 200

@app.route('/not-found')
def not_found():
    return jsonify({"error": "Tapılmadı"}), 404

@app.route('/server-error')
def server_error():
    return jsonify({"error": "Server xətası"}), 500
```
