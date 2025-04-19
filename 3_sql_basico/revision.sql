#reto 1
# 1. **Contar el número total de usuarios registrados.**
   select * from usuarios;
   select count(distinct username) AS cantidad_de_usuarios
   from usuarios;
# No cumple con el requisito, username no es asegurado como un campo unico e irrepetible, lo que implica que
# puede existir más de un usuario con el mismo nombre. pista: preguntar o asegurar datos unicos e irrepetibles
# o en su defecto obtener los numeros para justificar


#reto 2
#**Mostrar los nombres de los usuarios y el número de publicaciones que han realizado, ordenados de mayor a menor número de publicaciones.**
select username, count(*) as numero_de_publicaciones
from usuarios
group by username
order by numero_de_publicaciones desc;
#No cumple con el requisito. La tabla usuarios contiene información de los usuarios, no de sus publicaciones.

#reto 3
#3. **Encontrar el número total de mensajes intercambiados en todas las salas de chat.**
select * from chatrooms;
select sum(total_messages_counter) as total_de_mensajes_enviados
from chatrooms;
# Primera linea innecesaria. Serviría una mejor presentación de los datos.

#reto 4
#4. **Encontrar el usuario que ha realizado más mensajes en total en todas las salas de chat.**
select usuarios._id, usuarios.username, chatrooms.total_messages_counter
from usuarios
inner join chatrooms on chatrooms.creator_id = usuarios._id
where chatrooms.total_messages_counter = (
	select max(total_messages_counter)
    from chatrooms
    );
#No cumple con el requisito. Se busca al usuario que ha realizado más mensajes, no al que haya creado más chatrooms.

#reto 5
#5. **Encontrar las áreas de envío que tienen al menos una publicación asociada.**
select * from publicaciones;
select * from publicaciones
where shipping_area_id is not Null;
#Falta mejor presentasión de los datos.

#6. **Contar el número total de publicaciones que están disponibles para envío.**
select * from publicaciones;

select count(*) as disponible_envio 
from publicaciones
where shipping_available !=0;
#distinto de 0 y Null agregar 
#Primer linea innecesaria.

#7. **Encontrar el número total de publicaciones para cada categoría.**
select categories, count(*) AS publicaciones_por_categoria 
from publicaciones
group by categories;
#Se solicita resultados, tomando en cuenta que categories puede ser tuplas y se requiere su analisis individual

#8. **Encontrar las áreas de envío con el mayor número de publicaciones asociadas.**
select * from publicaciones;
select shipping_area_id, count(*) as areas_de_envio
from publicaciones
group by shipping_area_id;
#primer linea innecesaria. Se están contabilizando las áreas de envio nulas.

#9. **Encontrar las publicaciones que no han sido actualizadas desde hace más de un mes.**
select * from publicaciones
order by last_update desc
#no se está localizando ni filtrando a las publicaciones

#10. **Calcular la longitud promedio de los mensajes intercambiados en todas las salas de chat.**
select * from chatrooms;
select avg(total_messages_length) as longitud_promedio
from chatrooms;
#primer linea innecesaria, falta presentación