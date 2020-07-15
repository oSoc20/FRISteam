import data.SoapRepository;
import entities.Project;
import io.vertx.core.Vertx;
import utils.Writer;
import web.MainVerticle;

import java.util.ArrayList;

/**
 * Class to launch the program
 */
public class Program {

    public static void main(String[] args) { new Program().run();}

    /**
     * It will run a Vertx http server
     */
    private void run() {
        Vertx vertx = Vertx.vertx();
        vertx.deployVerticle(new MainVerticle());
    }

    /**
     * It will write the data received from the SOAP API request to a CSV file
     *
     * @param numberOfProjects the number of projects to receive from the SOAP API
     */
    private void writeCSVWithProjectsData(int numberOfProjects){
        ArrayList<Project> projects = new ArrayList<>(SoapRepository.getProjects(numberOfProjects));
        Writer.writeToCSV(projects);
    }
}
