
class EmployeeFacade {
    val payCalculator = PayCalculater()
    val hourReporter = HourReporter()
    val employeeSaver = EmployeeSaver()

    fun calculatePay(employee : Employee) {
        payCalculator.calculatePay(employee)
    }

    fun reportHours(employee : Employee) {
        hourReporter.reportHopurs(employee)
    }

    fun employeeSaver(employee : Employee) {
        employeeSaver.saveEmployee(employee)
    }

}