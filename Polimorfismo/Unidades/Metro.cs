namespace TiposdePolimorfismo.Unidades
{
    public class Metro
    {
        public double valor{ get; set; }

        public Metro(double valor)
        {
            this.valor = valor;
        }

        public static implicit operator double(Metro m)
        {
            return m.valor;
        }

        public static explicit operator Metro(double valor)
        {
            return new Metro(d);
        }

    }


}