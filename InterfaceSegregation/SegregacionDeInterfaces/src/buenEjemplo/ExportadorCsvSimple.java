package buenEjemplo;

public class ExportadorCsvSimple  implements CsvExportable {
    @Override
    public void exportCsv(String data){
        System.out.print(data);
    }
    
}
