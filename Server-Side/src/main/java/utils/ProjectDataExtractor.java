package utils;

import entities.Abstract;
import entities.DataProvider;
import entities.Project;
import entities.Title;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Utility class for data extraction from SOAP API xml responses
 */
public class ProjectDataExtractor {
    private static final Logger LOGGER = Logger.getLogger(ProjectDataExtractor.class.getSimpleName());

    private ProjectDataExtractor(){}

    /**
     * This method will create a List of Projects containing all the data extracted from the API response
     *
     * @param xmlString the String response of the SOAP API
     * @return a List of Projects
     */
    public static List<Project> getProjectData (String xmlString){
        ArrayList<Project> projects = new ArrayList<>();

        ArrayList<String> projectsDataString = new ArrayList<>(
                XMLDataExtractor.getListFromXmlData(xmlString, "<fris:project ", "</fris:project>")
        );

        projectsDataString.forEach(s -> projects.add(new Project(
                getProjectUUID(s),
                getTitle(s),
                getKeywords(s, "en"),
                getKeywords(s, "nl"),
                getAbstract(s),
                getDataProvider(s)
                )
        ));

        return projects;
    }

    /**
     * Get title of a project
     *
     * @param text the String from the SOAP API xml response
     * @return the title of the project
     */
    private static Title getTitle(String text){
        return XMLDataExtractor.getTitle(text, "<fris:name id=", "</fris:name>");
    }

    /**
     * Get all keywords for a project from the API response
     *
     * @param text the String from the SOAP API xml response
     * @param language the language of the abstract needed
     * @return a List with all keywords for a language
     */
    private static List<String> getKeywords(String text, String language) {

        return XMLDataExtractor.getKeywords(text, "<fris:keyword locale=\""+language+"\">", "</fris:keyword>");
    }

    /**
     * Get required data provider's information
     *
     * @param text the String from the SOAP API xml response
     * @return a DataProvider object containing the required data provider information
     */
    private static DataProvider getDataProvider(String text) {
        return XMLDataExtractor.getDataProvider(text);
    }

    /**
     * Get the UUID of a project
     *
     * @param text the String from the SOAP API xml response
     * @return return the UUID of a project
     */
    private static UUID getProjectUUID(String text) {
        return XMLDataExtractor.getUUID(text);
    }

    /**
     * Extract the english and dutch abstracts from a SOAP API response
     *
     * @param text the String from the SOAP API xml response
     * @return an Abstract object containing the abstracts of a project in english and dutch
     */
    private static Abstract getAbstract(String text){
        return XMLDataExtractor.getAbstract(text, "<fris:projectAbstract ", "</fris:projectAbstract>");
    }
}
