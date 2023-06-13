### Resumen
Este repositorio contiene lo solicitado para la 3ra PreEntrega, y además algunos html y funcionalidades que pienso desarrollar para el proyecto final.

3ra PREENTREGA (buscar la rama con este nombre PREENTREGA-03_MATHIER):

- Generé el base.html del cual heredé luego en el resto de los template encabezados y demás. Este base.html tiene algo de código que usaré más adelante en el proyecto final, por lo que en esta preentrega no funcion (Ej: el carrito)

- Generé 3 clases en el models.py, las cuales son a modo de ejemplo y resumen de lo que voy a necesitar. 
    . Cliente: esta tabla registrará a clientes y sus datos personales
    . Producto: esta tabla registrará todos los productos disponibles así como la referencia de si no están en stock o promoción. A futuro reemplazaré esos registros por booleanos.
    . Pedido_Basico: esta tabla es a modo ejemplo para la 3ra entrega, ya que solamente permite registrar en un campo de texto el detalle del pedido, pero a futuro usare ids para referenciar a los productos en stock.

- Generé 3 formularios de carga de datos para las 3 clases generadas. Como aún no están relacionadas las tablas, se pueden probar en cualquier orden. La idea es poder cargar algunos clientes, productos y pedidos. Particularmente en la carga de pedidos sería bueno recordar la Fecha Entrega porque luego el formulario de búsqueda utiliza este dato como filtro.

- Generé 1 formulario de búsqueda para que el dueño del negocio pueda ver qué pedidos tiene para entregar cada día. Al filtrar por fecha le devuelve los pedidos cargados, el cliente y detalle.


