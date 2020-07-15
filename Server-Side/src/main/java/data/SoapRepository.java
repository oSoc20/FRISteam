package data;

import entities.Project;
import entities.Publication;
import utils.ProjectDataExtractor;
import utils.PublicationsDataExtractor;

import javax.net.ssl.HttpsURLConnection;
import java.io.*;
import java.net.URL;
import java.util.*;
import java.util.logging.Logger;

/**
 * A class to send request to the FRIS SOAP API
 */
public class SoapRepository {
    private static final String URL_FRIS_PROJECTS = "https://frisr4.researchportal.be/ws/ProjectServiceFRIS?wsdl";
    private static final String URL_FRIS_PUBLICATIONS = "https://frisr4.researchportal.be/ws/ResearchOutputServiceFRIS?wsdl";
    private static final String CONTENT_TYPE = "text/xml;charset=UTF-8";
    private static final Logger LOGGER = Logger.getLogger(SoapRepository.class.getSimpleName());


    private SoapRepository() {
        // empty
    }

    /**
     * Get publications data from SOAP API
     *
     * @param number the number of publications to get
     * @return a List of the requested publications' data
     */
    public static List<Publication> getPublications(int number){
        LOGGER.info("requesting publications");
        final String XML = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:fris=\"http://fris.ewi.be/\" xmlns:crit=\"http://fris.ewi.be/criteria\">\n" +
                "<soapenv:Header/>" +
                "<soapenv:Body>" +
                "<fris:getResearchOutput>" +
                "<criteria>" +
                "<crit:window>" +
                "<crit:pageSize>" +number+ "</crit:pageSize>" +
                "</crit:window>" +
                "</criteria>" +
                "</fris:getResearchOutput>" +
                "</soapenv:Body>" +
                "</soapenv:Envelope>";
        try {
            HttpsURLConnection connection = getHttpsURLConnection(URL_FRIS_PUBLICATIONS);
            writeAndCloseOutputstream(XML, connection);
            String responseStatus = connection.getResponseMessage();
            LOGGER.info(responseStatus);

            return getPublications(connection);

        } catch (IOException e) {
            LOGGER.severe(Arrays.toString(e.getStackTrace()));
            return Collections.singletonList(new Publication());
        }
    }

    /**
     * Method to build a List of publications from the SOAP response
     *
     * @param connection the connection to the SOAP API
     * @return a list of Publication
     * @throws IOException throws if something fails for BufferedReader
     */
    private static List<Publication> getPublications(HttpsURLConnection connection) throws IOException{

        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();
        while ((inputLine = in.readLine()) != null){
            response.append(inputLine);
        }
        in.close();

        return new ArrayList<>(
                PublicationsDataExtractor.getPublicationData(response.toString())
        );
    }

    /**
     * This method will return a project data identified by a UUID
     *
     * @param uuid the id as String identifying a project
     * @return a Project
     */
    public static Project getProject(String uuid){
        return getProject(UUID.fromString(uuid));
    }

    /**
     * This method will return a project data identified by a UUID
     *
     * @param uuid the id as UUID identifying a project
     * @return a Project
     */
    public static Project getProject(UUID uuid){
        final String XML = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:fris=\"http://fris.ewi.be/\" xmlns:crit=\"http://fris.ewi.be/criteria\"><soapenv:Header/><soapenv:Body><fris:getProjects>" +
                "<criteria>" +
                "<crit:uuids>" +
                "<crit:identifier>"+uuid+"</crit:identifier>" +
                "</crit:uuids>" +
                "</criteria>"+
                "</fris:getProjects></soapenv:Body></soapenv:Envelope>";

        try {
            HttpsURLConnection connection = getHttpsURLConnection(URL_FRIS_PROJECTS);
            writeAndCloseOutputstream(XML, connection);
            String responseStatus = connection.getResponseMessage();
            LOGGER.info(responseStatus);

            return getProjects(connection).get(0);

        } catch (IOException e) {
            LOGGER.severe(Arrays.toString(e.getStackTrace()));
            return new Project();
        }

    }

    /**
     * Get a publication searching by its uuid
     *
     * @param uuid the uuid of a publication
     * @return a Publication
     */
    public static Publication getPublication(UUID uuid) {
        final String XML = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:fris=\"http://fris.ewi.be/\" xmlns:crit=\"http://fris.ewi.be/criteria\">" +
                "<soapenv:Header/>" +
                "<soapenv:Body>" +
                "<fris:getResearchOutput>" +
                "<crit:uuids>" +
                "<crit:identifier>"+uuid+"</crit:identifier>" +
                "</crit:uuids>" +
                "</fris:getResearchOutput>" +
                "</soapenv:Body>" +
                "</soapenv:Envelope>";
        try {
            HttpsURLConnection connection = getHttpsURLConnection(URL_FRIS_PUBLICATIONS);
            writeAndCloseOutputstream(XML, connection);
            String responseStatus = connection.getResponseMessage();
            LOGGER.info(responseStatus);

            return getPublications(connection).get(0);

        } catch (IOException e) {
            LOGGER.severe(Arrays.toString(e.getStackTrace()));
            return new Publication();
        }
    }

    /**
     * This method will return all the projects data.
     *
     * @param number the number of project to fetch from the SOAP API
     */
    public static List<Project> getProjects(int number){
        final String XML = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:fris=\"http://fris.ewi.be/\" xmlns:crit=\"http://fris.ewi.be/criteria\"><soapenv:Header/><soapenv:Body><fris:getProjects>" +
                "<criteria>" +
                "<crit:window>" +
                "<crit:pageSize>"+number+"</crit:pageSize>" +
                "</crit:window>" +
                "</criteria>"+
                "</fris:getProjects></soapenv:Body></soapenv:Envelope>";
        try {
            HttpsURLConnection connection = getHttpsURLConnection(URL_FRIS_PROJECTS);
            writeAndCloseOutputstream(XML, connection);
            String responseStatus = connection.getResponseMessage();
            LOGGER.info(responseStatus);

            return getProjects(connection);

        } catch (IOException e) {
            LOGGER.severe(Arrays.toString(e.getStackTrace()));
            return Collections.singletonList(new Project());
        }
    }

    /**
     * Method to get all projects from the SOAP API response
     *
     * @param connection the connection to the SOAP API
     * @return a List of all the projects
     * @throws IOException in case of BufferReader errors
     */
    private static List<Project> getProjects(HttpsURLConnection connection) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();
        while ((inputLine = in.readLine()) != null){
            response.append(inputLine);
        }
        in.close();

        return new ArrayList<>(
                ProjectDataExtractor.getProjectData(response.toString())
        );
    }

    /**
     * Method to write the response from the API
     *
     * @param xml the xml in string format from the SOAP API response
     * @param connection the connection to the API
     * @throws IOException in case of DataOutputStream errors
     */
    private static void writeAndCloseOutputstream(String xml, HttpsURLConnection connection) throws IOException {
        DataOutputStream dos = new DataOutputStream(connection.getOutputStream());
        dos.writeBytes(xml);
        dos.flush();
        dos.close();
    }

    /**
     * Method to get the connection from the SOAP API
     *
     * @return the connection to the API
     * @throws IOException in case of HttpsURLConnection errors
     */
    private static HttpsURLConnection getHttpsURLConnection(String frisUrl) throws IOException {
        URL url = new URL(frisUrl);
        HttpsURLConnection connection = (HttpsURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Content-Type", CONTENT_TYPE);
        connection.setDoOutput(true);
        return connection;
    }
}
