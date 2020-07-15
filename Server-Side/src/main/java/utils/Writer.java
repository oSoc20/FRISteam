package utils;

import entities.Project;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.List;

/**
 * Class to write data to a file
 */
public class Writer {
    //European countries use ";" as
    //CSV separator because "," is their digit separator
    private static final String CSV_SEPARATOR = ",";

    private Writer(){}

    /**
     * Method to write a List of Projects to a CSV file
     *
     * @param projects a list of Projects
     */
    public static void writeToCSV(List<Project> projects){
        try(
                BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("projects.csv"), StandardCharsets.UTF_8))
        ) {
            bw.write(headings());
            bw.newLine();

            projects.forEach(project -> {
                try {
                    bw.write(project.toStringCSV());
                    bw.newLine();
                } catch (IOException e) {
                    e.printStackTrace();
                }

            });
            bw.flush();

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    /**
     * Creates the titles for the columns of the CSV projects file
     *
     * @return a String with the titles comma separated
     */
    private static String headings() {
        StringBuilder header = new StringBuilder();
        header.append("project_id");
        header.append(CSV_SEPARATOR);
        header.append("english_title");
        header.append(CSV_SEPARATOR);
        header.append("dutch_title");
        header.append(CSV_SEPARATOR);
        header.append("english_keywords");
        header.append(CSV_SEPARATOR);
        header.append("dutch_keywords");
        header.append(CSV_SEPARATOR);
        header.append("abstract_id");
        header.append(CSV_SEPARATOR);
        header.append("english_abstract");
        header.append(CSV_SEPARATOR);
        header.append("dutch_abstract");
        header.append(CSV_SEPARATOR);
        header.append("data_provider_id");
        header.append(CSV_SEPARATOR);
        header.append("data_provider_name");
        header.append(CSV_SEPARATOR);

        return header.toString();
    }
}
