
class PayCalculater {
    fun calculatePay(employee : Employee) : Double {
        val ordinaryHours = rehularHours(employee)
        val nonOrdinaryHours = employee.hoursWorked - ordinaryHours
        return (ordinaryHours * employee.salary) + (nonOrdinaryHours * 1.5)
    }

    private fun regularHours( employee : Employee) : Int {
        return if (employee.hoursWorked > 35) 35 else employee.hoursWorked
    }

    


}