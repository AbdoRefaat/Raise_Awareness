import tkinter as tk
import winsound
import os

current_folder = os.path.dirname(os.path.abspath(__file__))

# home
window = tk.Tk()
window.title("My Digital Friend for Raising Awareness")
window.configure(bg= "white")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")
window.minsize(1500,650)
icon_path = os.path.join(current_folder, "images", "my_icon.ico")
window.iconbitmap(icon_path)
user_greeting = tk.Label(window, text= "Welcome to our program!💖", font=("Segoe UI Emoji", 25), bg= "white")
user_greeting.pack(pady= 10, padx= 20)

def play_sound(filename):
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)

# مسارات الأصوات
about_us_sound_path = os.path.join(current_folder, "sounds", "about_us.wav")
awareness_sound_path = os.path.join(current_folder, "sounds", "awareness.wav")
proplem_solving_sound_path = os.path.join(current_folder, "sounds", "proplem_solving.wav")
tips_sound_path = os.path.join(current_folder, "sounds", "tips.wav")
password_sound_path = os.path.join(current_folder, "sounds", "password.wav")

# دوال الأصوات
def about_us_sound():
    play_sound(about_us_sound_path)
def awareness_sound():
    play_sound(awareness_sound_path)
def proplem_solving_sound():
    play_sound(proplem_solving_sound_path)
def tips_sound():
    play_sound(tips_sound_path)
def password_sound():
    play_sound(password_sound_path)

# sound button....
# about us
sound_about_us_button = tk.Button(window, text= "listen", width=12, height=4, command= about_us_sound)
# awareness
sound_awareness_button = tk.Button(window, text= "listen", width=12, height=4, command= awareness_sound)
# proplem solving
sound_proplem_solving_button = tk.Button(window, text= "listen", width=12, height=4, command= proplem_solving_sound)
# tips
sound_tips_button = tk.Button(window, text= "listen", width=12, height=4, command= tips_sound)
# password 
sound_password_button = tk.Button(window, text= "listen", width=12, height=4, command= password_sound)

# text....
# about us
about_us_text = """بسم الله الرحمن الرحيم
السلام عليكم ورحمة الله وبركاته

هذا البرنامج تم تصميمه للمساهمة في حل مشاكل الشباب على الإنترنت، مثل التنمّر وما يشابهه من سلبيات الاستخدام الخاطئ.

محتويات البرنامج:

الصفحة الرئيسية
صفحة التوعية
صفحة حل المشاكل
صفحة نصائح للنجاة من مساوئ الإنترنت"""
# awareness
awareness_text = """ما هي التوعية الرقمية؟
التوعية الرقمية تعني فهم المخاطر التي قد تواجهنا عند استخدام الإنترنت، وكيفية التعامل معها بشكل صحيح وآمن.

لماذا التوعية مهمة؟
لأن الإنترنت مليء بالمعلومات، لكنه أيضًا مليء بالمشاكل مثل التنمّر الإلكتروني، سرقة البيانات، ونشر الأخبار الكاذبة.

كيف نحمي أنفسنا؟
لا تشارك معلوماتك الشخصية مع الغرباء.
إذا تعرضت للتنمّر، أخبر شخصًا تثق به فورًا.
تأكد دائمًا من صحة الأخبار قبل مشاركتها.
استخدم كلمات مرور قوية ولا تعطيها لأحد."""
# proplem solving
proplem_solving_text = """المشكلة 1: التنمّر الإلكتروني
الكثير من الشباب يتعرضون لتعليقات جارحة أو تهديدات عبر الإنترنت.
الحل: لا ترد على المتنمّر، واحفظ الأدلة (سكرين شوت)، ثم بلّغ شخصًا تثق به أو المسؤولين عن الموقع.

المشكلة 2: إدمان الإنترنت
بعض الشباب يقضون ساعات طويلة أمام الشاشات مما يؤثر على صحتهم ودراستهم.
الحل: ضع جدولًا لوقتك، وحدد ساعات محددة لاستخدام الإنترنت، واستبدلها بأنشطة أخرى مثل الرياضة أو القراءة.

المشكلة 3: الاحتيال وسرقة المعلومات
بعض المواقع أو الأشخاص يحاولون خداعك للحصول على بياناتك الشخصية.
الحل: لا تشارك كلمات السر أو بياناتك مع أي شخص، ولا تضغط على روابط مشبوهة."""
# tips
tips_text = """نصائح للنجاة من مساوئ الإنترنت:

1. لا تشارك معلوماتك الشخصية أو كلمات السر مع أي شخص.

2. إذا تعرضت للتنمر الإلكتروني، لا ترد بنفس الأسلوب، واحتفظ بالأدلة وأخبر شخصًا تثق به.

3. تجنب الدخول إلى المواقع المشبوهة أو الضغط على الروابط الغريبة.

4. خصص وقتًا محدد لاستخدام الإنترنت، ولا تجعله يسيطر على حياتك اليومية.

5. تعامل مع الآخرين بلطف واحترام، فأنت لا تعرف من يجلس خلف الشاشة.

6. استعن ببرامج الحماية (مثل مضاد الفيروسات) لتأمين جهازك.

7. تذكر دائمًا أن الإنترنت أداة للتعلم والتطوير، وليس للإساءة أو إضاعة الوقت."""
# password
password_text = """نصائح لإنشاء كلمة مرور قوية وآمنة:

1.استخدم طول كلمة مرور مناسب: من 12 حرفًا فأكثر.

2.اجمع بين الحروف الكبيرة والصغيرة، الأرقام، والرموز الخاصة.

3.تجنب استخدام معلومات شخصية مثل اسمك، تاريخ ميلادك، أو أسماء أفراد العائلة.

4.لا تستخدم كلمات شائعة أو متوقعة مثل "password" أو "123456".

5.استخدم عبارات مرور طويلة (Passphrase) من كلمات عشوائية يمكن تذكرها بسهولة.

5.لكل موقع أو حساب، استخدم كلمة مرور مختلفة لتقليل المخاطر عند الاختراق.

7.فكر في استخدام مدير كلمات المرور (Password Manager) لتخزين كلمات المرور بأمان وتوليد كلمات قوية.

8.غيّر كلمات المرور المهمة دوريًا، خاصة إذا شعرت بأي تهديد أو خرق أمني.

9.لا تشارك كلمة المرور مع أي شخص، ولا تكتبها في أماكن غير آمنة.

10.فعّل دائمًا المصادقة الثنائية (2FA) إذا كانت متاحة، لزيادة الأمان."""

# labels.....
# about us
about_us_label = tk.Label(window, text= about_us_text, font= ("Arial", 15), bg= "white")
# awareness
awareness_label = tk.Label(window, text= awareness_text, font= ("Arial", 15), bg= "lightblue")
# proplem solving
proplem_solving_label = tk.Label(window, text= proplem_solving_text, font= ("Arial", 15), bg= "#D4C7E0")
# tips
tips_label = tk.Label(window, text= tips_text, font= ("Arial", 15), bg= "#69A3AD")
# password
password_label = tk.Label(window, text= password_text, font= ("Arial", 14), bg= "#DA9CAC")

# EmergencyStop
# button to stop all sounds
# important for functions

# button
stop = tk.Button(window, text="Stop", width=9, height=4,command=lambda: winsound.PlaySound(None, winsound.SND_PURGE))

# functions.....

# about us
def on_about_us_pressed():
    window.title("about us")
    window.configure(bg="white")
    icon_path = os.path.join(current_folder, "images", "home_icon.ico")
    window.iconbitmap(icon_path)
    about_us_label.pack(pady= 20, padx= 20)
    awareness_label.pack_forget()
    proplem_solving_label.pack_forget()
    tips_label.pack_forget()
    sound_about_us_button.pack(side= "right", anchor= "n", padx= 40)
    stop.pack(side= "left", anchor= "n", padx= 80)
    sound_awareness_button.pack_forget()
    sound_proplem_solving_button.pack_forget()
    sound_tips_button.pack_forget()
    password_label.pack_forget()
    sound_password_button.pack_forget()

# 1.awareness
def on_awareness_pressed():
    window.title("Awareness")
    window.configure(bg="lightblue")
    icon_path = os.path.join(current_folder, "images", "awareness.ico")
    window.iconbitmap(icon_path)
    awareness_label.pack(pady= 20, padx= 20)
    about_us_label.pack_forget()
    proplem_solving_label.pack_forget()
    tips_label.pack_forget()
    password_label.pack_forget()
    sound_awareness_button.pack(side= "right", anchor= "n", padx= 40)
    stop.pack(side= "left", anchor= "n", padx= 80)
    sound_about_us_button.pack_forget()
    sound_proplem_solving_button.pack_forget()
    sound_tips_button.pack_forget()
    sound_password_button.pack_forget()

# 2.proplem solving
def on_proplem_solving_pressed():
    window.title("Proplem Solving")
    window.configure(bg="#D4C7E0")
    icon_path = os.path.join(current_folder, "images", "proplem_solving.ico")
    window.iconbitmap(icon_path)
    proplem_solving_label.pack(pady= 20, padx= 20)
    about_us_label.pack_forget()
    awareness_label.pack_forget()
    tips_label.pack_forget()
    password_label.pack_forget()
    sound_proplem_solving_button.pack(side= "right", anchor= "n", padx= 40)
    stop.pack(side= "left", anchor= "n", padx= 80)
    sound_about_us_button.pack_forget()
    sound_awareness_button.pack_forget()
    sound_tips_button.pack_forget()
    sound_password_button.pack_forget()

# 3.tips
def on_tips_pressed():
    window.title("Tips")
    window.configure(bg="#69A3AD")
    icon_path = os.path.join(current_folder, "images", "tips.ico")
    window.iconbitmap(icon_path)
    tips_label.pack(pady= 20, padx= 20)
    about_us_label.pack_forget()
    awareness_label.pack_forget()
    proplem_solving_label.pack_forget()
    password_label.pack_forget()
    sound_tips_button.pack(side= "right", anchor= "n", padx= 40)
    stop.pack(side= "left", anchor= "n", padx= 80)
    sound_about_us_button.pack_forget()
    sound_awareness_button.pack_forget()
    sound_proplem_solving_button.pack_forget()
    sound_password_button.pack_forget()

# 4.password
def on_password_pressed():
    window.title("Password")
    window.configure(bg= "#DA9CAC")
    icon_path = os.path.join(current_folder, "images", "my_icon.ico")
    window.iconbitmap(icon_path)
    password_label.pack(pady= 20, padx= 20)
    about_us_label.pack_forget()
    awareness_label.pack_forget()
    proplem_solving_label.pack_forget()
    tips_label.pack_forget()
    sound_password_button.pack(side= "right", anchor= "n", padx= 40)
    stop.pack(side= "left", anchor= "n", padx= 80)
    sound_about_us_button.pack_forget()
    sound_awareness_button.pack_forget()
    sound_proplem_solving_button.pack_forget()
    sound_tips_button.pack_forget()

# 5.creat a password
# buttons......
# about us
about_us = tk.Button(window, text= "About Us", fg= "#2D7896", width= 9, height= 4, command=on_about_us_pressed)
# awareness
awareness = tk.Button(window, text= "Awareness", fg= "#2D7896", width= 9, height= 4, command= on_awareness_pressed)
# proplem solving
proplem_solving = tk.Button(window, text= "Proplem Solving", fg= "#2D7896", width= 13, height= 4, command= on_proplem_solving_pressed)
# tips
tips = tk.Button(window, text= "Tips", fg= "#2D7896", width= 9, height= 4, command= on_tips_pressed)
# good password
password = tk.Button(window, text= "password", fg= "#2D7896", width= 15, height= 4, command= on_password_pressed)
# result.....
# about us
about_us.pack(side= "left", anchor= "n", padx= 20, pady= 50)
# awareness
awareness.pack(side="left", anchor="n", padx=20, pady=50)
# proplem solving
proplem_solving.pack(side="left", anchor="n", padx=20, pady=50)
# tips
tips.pack(side="left", anchor="n", padx=20, pady=50)
# password
password.pack(side="left", anchor="n", padx=15, pady=50)

window.mainloop()