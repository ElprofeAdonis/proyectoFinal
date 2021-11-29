# proyectoFinal
en este proycte esta ilustrado con un api de la vida real


Tipo de trabajo: individual
 

Proyecto Final
 
Objetivo: Demostrar las habilidades de resolución de problemas del mundo real abstrayendo e implementando soluciones mediante el desarrollo de RESTful APIs como complemento de una solución completa bajo un esquema de separación de tareas en paradigma: Frontend/Backend.

Requisitos
•	Almacenamiento con MySQL
•	Flask de Python como plataforma de desarrollo
•	Flask’JWT’extended
•	Flask’SQLAlchemy
•	Es funcional a la hora de probar la solución a través de un cliente HTTP.
•	Se utilizan los apropiados códigos de estado HTTP para cada respuesta.
•	Tiene claridad de sintaxis.
•	

Enunciado

Se desea crear la base de datos para administrar un parqueo público. En este escenario, se cuenta con el típico parqueo que tiene una cantidad específica de campos y estos se alquilan por un monto determinado por hora.
En esta tabla se debe por almacenar User donde se almacene el registro de los usuarios que se login, cuenta con, id, public_id, name, password, admin.
En una tabla se debe poder almacenar la información general del parqueo. Esta tabla solo tendrá un registro, pero debe manejar los detalles el parqueo como: id, nombre del lugar, cedula Jurica, dueño, dirección, ano de creación, email, teléfono, cumple con los requisitos, parqueo id.
El parqueo esta hecho de una forma que el dueño puede cambiar la distribución de los campos, por lo que la cantidad de campos de un tipo o de otro, puede variar y es definida por el dueño del parqueo. Cuando un espacio este siendo utilizado se debe conocer la placa del vehículo que está en el espacio [se recomienda crear una tabla TipoEspacio que tenga el id, nombre cliente, descripción, placa, precio por hora, registro id, 


 

información del campo con el número de placa proporcionada y se genera un registro de factura que tenga el número del espacio utilizado (con lo que se puede saber el tipo de espacio y por ende el precio por hora) y la fecha y hora de ingreso (con el tipo de dato datetime se pueden almacenar ambos en un solo campo). Quedan pendientes por llenar la fecha y hora de salida, el monto total y en caso de que el cliente solicite la factura con nombre, el nombre completo del cliente. Esta información se ingresará cuando el cliente llegue a sacar el vehículo del parqueo.
Para el monto total se debe poder calcular la diferencia en horas entre la fecha de ingreso y la fecha de salida y multiplicar esta cantidad por el montoPorHora determinado para el espacio del parqueo que fue utilizado.

Se recomienda generar una tabla Factura que tenga los campos (id factura, num_espacio, placa, fechaIngreso, fechaSalida, montoTotal, cliente).


1.	Se indica a continuación cada una de las operaciones que deber realizar
a.	Creación de una base de datos llamada ParqueoPublico. Esta base de datos deberá tener las tablas necesarias para almacenar de forma correcta la información indicada en el enunciado. Se sugieren las siguientes tablas:
i.	User
ii.	Información?Parqueo
iii.	TipoEspacio
iv.	Factura.

Con este  proyecto lo que se pretende es el  parqueo las personas que tengan pensado utilizar este servicio, puedan registrarse y poder generar un token, para disfrutar de los servicios tengo 5 dueños, y  que al momento de imprimir la factura salga el nombre del dueño de turno de ese día,  lo mismo con lo del espacio que si las personas al momento de registrarse,  puedas disponer de un lugar en especifico en el parqueo pero siempre y cuando ellos mismos puedan identificar  si esta disponible o no y esto se trabajara por un  método que sea boolean, y al momento de imprimir la factura se pueda detallar datos en especifico que el dueño considere necesario para poder detallar en la factura 
