# Query String (Sorğu Sətri) Strukturu

Şəkildə URL-in sorğu parametrləri (query string) hissəsinin necə formalaşdığı göstərilir.
Nümunə URL: `https://www.domain.com/page?key1=value1&key2=value2`

Hissələrin izahı:

1.  **? (Sual işarəsi)** - *query string begins*
    *   Sorğu sətrinin başlanğıcını bildirir. Bu işarə URL-in əsas hissəsini (path) parametrlərdən ayırır.

2.  **key1** - *1st variable name*
    *   Birinci dəyişənin (və ya parametrin) adıdır.

3.  **= (Bərabərlik işarəsi)** - *value separator*
    *   Dəyər ayırıcısıdır. Dəyişənin adını (key) onun dəyərindən (value) ayırır.

4.  **value1** - *1st property value*
    *   Birinci dəyişənin aldığı dəyərdir.

5.  **& (Ampersand)** - *separator*
    *   Ayırıcıdır. Birdən çox parametr göndərilərsə, onları bir-birindən ayırmaq üçün istifadə olunur.

6.  **key2** - *2nd variable name*
    *   İkinci dəyişənin adıdır.

7.  **value2** - *2nd property value*
    *   İkinci dəyişənin dəyəridir.
