class HourReporter {
    fun reportHopurs(employee : Employee) : Int {
        val ordinaryHours = regularHours(employee)
        val nonOrdinaryHours = employee.hoursWorked - ordinaryHours
        return "Employee ${employee.name} has worked $ordinaryHours hours"
    }

    private fun regularHours(employee  :Employee) : Int {
        return if (employee.hoursWorked > 40) 40 else employee.hoursWorked

    }





}