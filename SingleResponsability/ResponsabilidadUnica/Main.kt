
fun main() {
    val employee1 = Employee(
        ID = 1,
        name = "Pedro Alonso",
        hoursWorked = 40,
        salary = 40.0
    )
    
    println(employee1.calculatePay())
    println(employee1.reportHours())
    employee1.saveEmployee()


    val employee2 = Employee(
        ID = 2,
        name = "Fernando",
        hoursWorked = 35,
        salary = 35.0
    )

    val employeeFacade = EmployeeFacade()
    println(employeeFacade.reportHopurs(employee2))
    println("Salary: ${employeeFacade.calculatePay(employee2)}")
    employeeFacade.employeeSaver(employee2)
}