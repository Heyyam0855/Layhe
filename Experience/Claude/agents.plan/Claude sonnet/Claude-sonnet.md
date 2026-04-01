# MVC və Digər Bənzər Arxitektura Pattern-ləri

## MVC (Model-View-Controller)
- **Model** – Məlumatları və biznes məntiqi idarə edir
- **View** – İstifadəçi interfeysi (UI) göstərir
- **Controller** – Model və View arasında vasitəçilik edir

---

## Bənzər Arxitektura Pattern-ləri

### MVP (Model-View-Presenter)
- **Model** – Məlumat təbəqəsi
- **View** – UI təbəqəsi (passiv)
- **Presenter** – Məntiqi idarə edir, View-u yeniləyir

### MVVM (Model-View-ViewModel)
- **Model** – Məlumat təbəqəsi
- **View** – UI təbəqəsi
- **ViewModel** – View üçün məlumatları hazırlayır (Data Binding)

### MVA (Model-View-Adapter)
- **Adapter** – Model ilə View arasında körpü rolunu oynayır

### VIPER
- **View** – UI
- **Interactor** – Biznes məntiqi
- **Presenter** – UI məntiqi
- **Entity** – Model obyektləri
- **Router** – Naviqasiya

### MVI (Model-View-Intent)
- **Model** – Vəziyyət (State)
- **View** – UI
- **Intent** – İstifadəçi hərəkətləri

---

## Açar Sözlər Cədvəli

| Pattern | Əsas Komponentlər | İstifadə Sahəsi |
|---------|-------------------|-----------------|
| MVC | Model, View, Controller | Web (Laravel, Rails) |
| MVP | Model, View, Presenter | Android, WinForms |
| MVVM | Model, View, ViewModel | WPF, Angular, Vue |
| VIPER | View, Interactor, Presenter, Entity, Router | iOS |
| MVI | Model, View, Intent | React, Redux |

---

## Ümumi Açar Sözlər
- `Separation of Concerns` – Vəzifələrin ayrılması
- `Data Binding` – Məlumat bağlama
- `Business Logic` – Biznes məntiqi
- `UI Layer` – İnterfeys təbəqəsi
- `State Management` – Vəziyyət idarəetməsi
- `Design Pattern` – Dizayn nümunəsi
- `Architecture` – Arxitektura