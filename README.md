
# بسترو اشرسلیبن - Bistro Aschersleben

تطبيق جوال لمطعم Bistro Aschersleben للطلبات والتوصيل.

## نبذة عن المشروع

تطبيق Bistro Aschersleben مبني باستخدام Flet، وهي مكتبة Python تتيح بناء تطبيقات متعددة المنصات (Android / iOS / Web) بسهولة.

يتيح التطبيق للزبائن:
- تصفح قائمة الطعام
- تقديم الطلبات للتوصيل أو الاستلام من المطعم
- الدفع عبر الإنترنت أو عند الاستلام
- إنشاء حسابات شخصية وحفظ العناوين المفضلة

## الميزات الرئيسية

1. **الحساب الشخصي**
   - تسجيل الدخول / إنشاء حساب
   - عرض سجل الطلبات
   - إدارة العناوين المحفوظة

2. **المنيو**
   - عرض قائمة الطعام بالصور والأسعار
   - تخصيص الطلب (الإضافات والحجم)
   - إضافة إلى عربة التسوق

3. **الطلب والدفع**
   - خيارات التوصيل للمنزل أو الاستلام من المطعم
   - طرق دفع متعددة (نقداً، بطاقة، دفع إلكتروني)
   - تتبع حالة الطلب

4. **العروض والكوبونات**
   - عرض العروض الحالية
   - تطبيق كوبونات الخصم

## التثبيت والتشغيل

1. تأكد من تثبيت Python (الإصدار 3.7 أو أعلى) على جهازك

2. قم بتثبيت Flet:
   ```
   pip install flet
   ```

3. قم بتشغيل التطبيق:
   ```
   python src/main.py
   ```

## تجربة التطبيق

يمكنك تجربة التطبيق بالبيانات التالية:
- البريد الإلكتروني: test@example.com
- كلمة المرور: password

## بناء التطبيق للأجهزة المحمولة

للأندرويد:
```
flet build apk
```

للـ iOS (يتطلب جهاز Mac):
```
flet build ios
```
