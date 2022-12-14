# Final Project - Python Course - Coderhouse

## MVT Project – Python Framework Django

The project is named MVT due to the software design pattern for developing web applications Django is based on: MVT (Model-View-Template) architecture. 
To run this project, you will only have to have Python and Django installed.
To install Django type in the terminal:
•	Pip install Django
The directories we will need are configured in settings.py to work without issues on your computer, since only relative paths were used.

**The structure: MVT and AppMVT

The main project MVT has an app named AppMVT, to which the user is directly routed once the first page of the project is accessed. 
Main page  127.0.0.1:800 when accessed it, gets redirect to 127.0.0.1:800/AppMVT.

The template worked on was taken from Bootstrap and modified to meet the project proposal.
Reference link: Freelancer - One Page Theme - Start Bootstrap

AppMVT has:
•	A main page with brief information about the project and URLs redirecting the user to the author social medias.
•	3 models: “Courses”, “Languages” and “Contact”.
•	An about session with introduction to the author.

1.	Class Courses:

This session is accessed through the path http://127.0.0.1:8000/AppMVT/cursos/. 
The objects stored in the DB are rendered in the template and it shows a list of courses. 
At the bottom of the list of courses there is a button to add more courses in the DB. 
The button redirects the user to the path http://127.0.0.1:8000/AppMVT/addcursos/
Here the user can add courses following the structure of the model Courses (name, instituicion, start_date).
![image](https://user-images.githubusercontent.com/108837573/189411295-90b999ed-90dd-4e03-a1f8-e2666d71b23e.png)
When clicking to send the data, the user is redirected back to http://127.0.0.1:8000/AppMVT/cursos/ 
where the new course added can be seen in the bottom of the list.

2.	Class “Languages”:
This session is accesses through the path http://127.0.0.1:8000/AppMVT/lenguajes/ .
The objects stored in the DB are retrieved through a search form, in which the user needs to write a programming language name and a brief text taken  from DB associated to that language will appear. 
![image](https://user-images.githubusercontent.com/108837573/189411598-e94f4f23-90eb-476b-ba5d-2992292a4e63.png)
The search form has the method “GET” and  is case-sensitive, accepting only languages written with the first capital letter and if any language has 
capital letters in the middle in its presentation, such as JavaScript, the capital letter also needs to be written. If there is a typo,  not meeting the requirements or the object is not found in the database, a message will appear stating no language was identified. 
If the form is submitted without any data, a message will show stating no data was entered. 


In case the language the user is searching is not in the DB, the user can insert it through the button "No encuentro mi lenguaje". 
This button will redirect the user to the path http://127.0.0.1:8000/AppMVT/ayuda/ where there is a form to insert the missing language in the DB.
![image](https://user-images.githubusercontent.com/108837573/189411932-2828ff6a-5fa0-4915-b5ef-5b04d19742db.png)



3.	Class “Contact”:
This session is accessed through the path http://127.0.0.1:8000/AppMVT/contacto .
The contact form works as the method “POST” and will send user data to the DB where it will be stored. 
![image](https://user-images.githubusercontent.com/108837573/189413547-af290ff7-7017-4a11-88ce-d7a86a7d56ba.png)


4.	The about session is only a session to test the image file and how it displays in the template. The image can be replaced with your own information.
Remember to change all the information in the footer related to the author as well.

---------------------------------------------------------------- Español -------------------------------------------------
# Proyecto Final - Curso Python - Coderhouse 

## Proyecto MVT - Python Framework Django 

El proyecto se llama MVT debido al patrón de diseño de software para el desarrollo de aplicaciones web en el que django se basa: Arquitectura MVT 
(Model-View-Template).  Para ejecutar este proyecto, solo tendrás que tener python y Django instalados. Para instalar Django tipo en el terminal: 
• Pip install Django 

Los directorios que necesitaremos están configurados en settings.py para que funcionen sin problemas en tu ordenador, ya que solo se utilizaron rutas 
relativas. 

**La estructura: MVT y AppMVT

El proyecto principal MVT tiene una aplicación llamada AppMVT, a la que se enruta directamente al usuario una vez que se accede a la primera página del proyecto.
La página principal 127.0.0.1:800 cuando se accede a ella, se redirige a 127.0.0.1:800/AppMVT.  La plantilla trabajada fue tomada de Bootstrap y modificada 
para cumplir con la propuesta del proyecto. Enlace de referencia: Freelancer - One Page Theme - Start Bootstrap.
AppMVT tiene: 

• Una página principal con información breve sobre el proyecto y URLs redirigiendo al usuario a las redes sociales del autor. 
• 3 modelos: "Cursos", "Idiomas" y "Contacto". 
• Una sesión sobre con introducción al autor.  

1. Clase "Cursos": 

Se accede a esta sesión a través del camino http://127.0.0.1:8000/AppMVT/cursos/.  
Los objetos almacenados en la base de datos se representan en la plantilla y muestra una lista de cursos. 

En la parte inferior de la lista de cursos hay un botón para agregar más cursos en la base de datos. 
El botón redirige al usuario a la ruta http://127.0.0.1:8000/AppMVT/addcursos/
Aquí el usuario puede agregar cursos siguiendo la estructura de los Cursos modelo (nombre, institución, start_date).
Al hacer clic para enviar los datos, el usuario es redirigido de nuevo a http://127.0.0.1:8000/AppMVT/cursos/ 
donde el nuevo curso agregado se puede ver en la parte inferior de la lista.

2. Clase "Lenguajes": 

A esta sesión se accede a través de la ruta http://127.0.0.1:8000/AppMVT/lenguajes/. 
Los objetos almacenados en la base de datos se recuperan a través de un formulario de búsqueda, en el que el usuario debe escribir un nombre de lenguaje de programación y aparecerá un breve texto tomado de la base de datos asociada a ese lenguaje.

El formulario de búsqueda tiene el método "GET" y distingue entre mayúsculas y minúsculas, aceptando solo idiomas escritos con la primera letra mayúscula y si algún idioma tiene letras mayúsculas en el medio de su presentación, como JavaScript, la letra mayúscula también debe escribirse. Si hay un error tipográfico, no cumple con los requisitos o el objeto no se encuentra en la base de datos, aparecerá un mensaje que indica que no se identificó ningún lenguaje. Si el formulario se envía sin ningún dato, se mostrará un mensaje que indica que no se ingresaron datos.   

En caso de que el idioma que el usuario está buscando no esté en la base de datos, el usuario puede insertarlo a través del botón "No encuentro mi lenguaje". 
Este botón redirigirá al usuario a la ruta http://127.0.0.1:8000/AppMVT/ayuda/ donde hay un formulario para insertar el idioma que falta en la base de datos.

3. Clase "Contacto": 

Se accede a esta sesión a través de la ruta http://127.0.0.1:8000/AppMVT/contacto. 
El formulario de contacto funciona como el método "POST" y enviará los datos del usuario a la base de datos donde se almacenarán.   

4. La sesión acerca de es solo una sesión para probar el archivo de imagen y cómo se muestra en la plantilla.
La imagen puede ser reemplazada con su propia información. Recuerde cambiar toda la información en el pie de página relacionada con el autor también.



