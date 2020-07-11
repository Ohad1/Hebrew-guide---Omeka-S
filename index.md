
מדריך זה נוצר במסגרת פרוייקט [בקורס מדעי הרוח הדיגיטליים](https://www.cs.bgu.ac.il/~tdh202/Main), בהנחיית דר' יעל נצר, המחלקה למדעי המחשב, אוניברסיטת בן גוריון. 
מטרת המדריך היא להנגיש חלקים מרכזיים במדריך הרחב של OMEKA על מנת לאפשר לחסרי ניסיון והיכרות עם אומקה למידה והתנסות מהירה עם הפלטפורמה.

## התחברות והורדה של OMEKA S ל RECLAIM HOSTING
היכנסו -ל [reclaimhosting](https://reclaimhosting.com), ליחצו על products->shared hosting  והירשמו לשרת במסלול "personal".
![Image of hosting](resources/shir/hosting-1-05.jpg)

לאחר ההרשמה יש להיכנס ל client Area בעזרת מייל משתמש וססמא שהזנתם בעת ההרשמה:
![Image of hosting2](resources/shir/client erea hoasting.jpg)

זה דף הבית בכניסה:
![Image of hosting3](resources/shir/home client.jpg)

כעת, המנוי האישי מאפשר לכם דומיין יחיד, יש ליצור אותו לפני ההתקנה של OMEKA S :
1.  היכנסו ל domains-> Register a New Domain:
![Image of domain1](resources/shir/domain-1-01.jpg)

2. יש להכניס שם עבור הכתובת הרצויה וללחוץ על check Availability במידה והכתובת פנויה יתאפשר לכם ללחוץ על "continue" :
![Image of domain2](resources/shir/domain-2.jpg)

3. יש לפעול בהמשך ע"פי ההוראות הבסיסיות. בסיום התהליך תוכלו לראות את הדומיין שיצרתם ב "Active Domain" בדף הבית.
![Image of domain1](resources/shir/domain-3.jpg)

כעת, ניתן להתקין את OMEKA S :

1. כנסו ל "Cpanel" מדף הבית:	
![Image of cpanel1](resources/shir/home client- cpanel-02.jpg)

2. לחצו על "All Applications":
![Image of install1](resources/shir/install-1.jpg)

3. חפשו את "OMEKA S" (קל בעזרת ctrl+f) ולחצו:
![Image of install2](resources/shir/install-2.jpg)

4. יש ללחוץ על "install this application":
![Image of install3](resources/shir/install-3.jpg)

5. כעת יש לבחור דומיין עבור ההתקנה של אומקה, שם לאתר של אומקה, שם משתמש, מייל וססמא שישמשו את המנהל (אתם) בכניסה לOMEKA S  (החלונות הרלוונטים מסומנים בתמונה המצורפת). בסיום יש ללחוץ על "install" ולהמתין:
![Image of install5](resources/shir/install-4-03.jpg)

6. בסיום ההתקנה יופיעו שלושה קישורים (מסומנים) השני מביניהם יוביל להתחברות ל "admin dashboard" ותוכלו להתחיל לעבוד עם OMEKA S :
![Image of install6](resources/shir/install-5-04.jpg)

7. בכניסה ל"admin dashboard" תתבקשו להזין את המשתמש והססמא שהזנתם בהתקנה, ותוכלו להיכנס לOMEKA S :
![Image of install7](resources/shir/install-6.jpg)
![Image of install7a](resources/shir/install-7.jpg)


## הוספת מודולים (modules) ותבניות אתר (themes) ל OMEKA S 
OMEKA S מאפשר להתקין הרחבות שמאפשרות כלים נוספים לעבודה או לתצוגה באתר. ההרחבות זמינות בקישור הבא [https://omeka.org/s/modules/](https://omeka.org/s/modules/)  . כמו כן, יש מספר תבניות אפשריות לאתר שזמינות להורדה בקישור [https://omeka.org/s/themes/](https://omeka.org/s/themes/) . תהליך ההתקנה דומה פרט למיקום קבצי ההתקנה.
1. כנסו ל "Cpanel" ולחצו על "Terminal":
![Image of modulel](resources/shir/module-1.jpg)

2. בעת ההתקנה של אומקה נוצרה תיקייה בשרת בשם של הדומיין, המכילה תיקיה בשם "modules" ותיקיה בשם "themes". ניתן לראות אותה ואת כל הקבצים והתיקיות שלכם בשרת ע"י כניסה ל "file manager":
![Image of modulel-2](resources/shir/module-1-2.jpg)
![Image of module3](resources/shir/module-3.jpg)

3. כעת בחלון הטרמינל יש לנווט לתיקיה הרצויה, "themes" עבור התקנה של תבנית אתר ו "modules" עבור התקנה של כלים. ניתן לעשות זאת  באמצעות 2 פקודות cd  עם השמות הרלוונטים של התיקיה של הדומיין ואז התיקיה הרצויה:
```markdown
cd yourDomainForOmeka
cd modules
```
![Image of module2](resources/shir/module-2.jpg)

לאחר מכן יופיע ה path מעל חלון הterminal (מסומן בצהוב).

4. השתמשו בפקודת  "wget  link_to_module_download" כדי להוריד את ההתוסף הרצוי לתיקיה :
![Image of module4](resources/shir/module-4.jpg)

5. השתמשו בפקודת  "unzip name_of_downloaded_file" כדי להוריד את הכיווץ :
![Image of module5](resources/shir/module-5.jpg)

6. כעת היכנסו ל "admin dashboard" ב OMEKA S ולחצו על "Modules":
![Image of module6](resources/shir/module-6.jpg)

7. במידה והתקנתם "theme"  אין צורך בפעולות נוספות, הוא זמין לכם. במידה והתקנתם "module" יש ללחוץ "install". החל מאותו הרגע הוא זמין לשימוש.
![Image of module7](resources/shir/module-7.jpg)

* התהליך של התקנת "theme" זהה פרט לעובדה שעליכם לשים לב שאתם בתיקייה המתאימה.לאחר פקודת "unzip" אין צורך בפעולות נוספות.



## תרגום של [glossary] (https://omeka.org/s/docs/user-manual/glossary/) מתוך ה"user manual" של OMEKA S




## תרגום של: https://omeka.org/s/docs/user-manual/content/resource-template/




## הסבר על בניית קבצי CSV לעבודה עם המודול CSV-IMPORT 




## תרגום של: https://omeka.org/s/docs/user-manual/modules/csvimport/





## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/omerdv/Hebrew-guide---Omeka-S/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

עברית עברית

עברית english עומר

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```


For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/omerdv/Hebrew-guide---Omeka-S/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
