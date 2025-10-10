Class Employee (
    private val ID : Int,
    private val name : String,
    private val hoursWorked : Int,
    private val salary : double
) {
    fun calculatePay() : Double {
        val ordinaryHours = regularHours()
        return (hoursWorked * ordinaryHours).toDouble() 
    }


    fun reportHours(): String {
        val ordinaryHours = regularHours()
        return "Employee $name has worked $ordinaryHours hours"
    }



    fun saveEmployee(){
        print ("Saving employee $name to database...)
    }

    private fun regularHours() : Int{
        return if (hoursWorked > 35) 35 else hoursWorked
    }
}