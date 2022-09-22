# Notas de clase para Linux

La preguntas básicas que nos hariamos al enfrentarnos a una terminal en un sistema operativo basado en Linux, se van a responder a continuación

### ¿Dónde estoy?

La pregunta va enfocada a saber en que carpeta del sistema operativo estamos.

La forma más fácil de saberlo es con `pwd`, este comando retornará la ruta donde me encuentro actualmente.

### ¿Cómo me muevo?

Saber donde estoy no es suficiente hasta ahora, también debemos saber hacia donde puedo moverme, pero no puedo moverme sin conocer las rutas,
para lograr esto, me enfoco en conocer las carpetas y archivos disponibles en mi ruta actual, puedo escribir `ls`, y esto listará los archivos en mi directorio actual.

Si quiero conocer también los archivos ocultos puedoe escribir `ls -a`, o si quiero que mis archivos vean como listas, puedo escribir `ls -l`.

En este punto ya conozco las rutas, pero ¿cómo me muevo hacia otro lugares? usamos el comando `cd` acompañado de la ruta a la que quiero acceder, es decir, suponiendo que en mi ruta actual
existe una subcarpeta llamada `horario/`,  y quiero acceder o entrar en ella, debo escribir `cd horario/`.

Pero ¿Que pasa si me quiero devolver? Sólo debo escribir `cd ..` y estaré en la carpeta raiz de mi carpeta actual.

Ya sabemos donde estoy, como listo los archivos y carpetas, y como me muevo por linux.

### ¿Cómo construyo algo?

Ahora que sé moverme y listar mis archivos en linux, debo entrar en modo creador.

Para construir una carpeta uso `mkdir` más el nombre de la carpeta, es decir, si quiero crear una carpeta llamada `myDirectory`, el comando sería `mkdir myDirectory`

Con esto, ya podría entrar a esta carpeta y crear un primer archivo llamado `holaMundo`, para esto, utilizo el comando `touch holaMundo.txt`, en este caso, al sistema operativo se le debe específicar la 
extensión del archivo, que para este ejemplo sera un texto plano con formato `.txt`.

Para editar el archivo que construimos, podemos usar diferentes interfaces, como `vim` o `nano`, para este caso usaremos `nano` y entramos al archivo escribiendo `nano holaMundo.txt`. Para salir de nano, sólo debemos escribir `CRTL+X`, si deseas guardar los cambios, presionas `y`, en caso contrario, presionas `n`.

## Ya estás listo con lo básico

##### Si quieres actualizar tu sistema operativo, con Ubuntu, puedes usar:
`sudo apt-get update` y luego `sudo apt-get upgrade`.
