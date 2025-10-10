namespace TiposdePolimorfismo.Genericos
{
    public class Caja<T>
    {
        private T contenido;

        public void guardar(T item){
            contenido = item;
        }

        public T abrir()
        {
            return contenido;
        }


    }
}