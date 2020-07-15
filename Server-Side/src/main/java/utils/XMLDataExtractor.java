package utils;

import entities.Abstract;
import entities.DataProvider;
import entities.Title;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class XMLDataExtractor {
    private static final Logger LOGGER = Logger.getLogger(XMLDataExtractor.class.getSimpleName());

    private XMLDataExtractor(){}

    /**
     * Extract repeating collection of data from an API response
     *
     * @param text the String from the SOAP API xml response
     * @return a List of String containing the repeating data
     */
    public static List<String> getListFromXmlData (String text, String startLimit, String endLimit){
        ArrayList<String> result = new ArrayList<>();

        Matcher matcher = getMatcher(text, startLimit, endLimit);

        while (matcher.find()){
            result.add(matcher.group(1));
        }

        return result;
    }

    /**
     * Get all keywords for a project from the API response
     *
     * @param text the String from the SOAP API xml response
     * @param startLimit the upper limit to where to find the data
     * @param endLimit the lower limit to where to find the data
     * @return a List with all keywords for a language
     */
    public static List<String> getKeywords(String text, String startLimit, String endLimit) {
        ArrayList<String> keywords = new ArrayList<>();
        Matcher matcher = getMatcher(text, startLimit, endLimit);

        while (matcher.find()){
            String keyword = matcher.group(1).replace(",", ";");
            keywords.add(keyword);
        }
        return keywords;
    }

    /**
     * Get the title from xml soap response
     *
     * @param text the xml response as String
     * @param startLimit the upper limit to where to find the data
     * @param endLimit the lower limit to where to find the data
     * @return a Title
     */
    public static Title getTitle(String text, String startLimit, String endLimit){
        Matcher matcher = getMatcher(text, startLimit, endLimit);
        if (matcher.find()){
            return new Title(
                    getDataByLocale(matcher.group(1), "en"),
                    getDataByLocale(matcher.group(1), "nl")
            );
        }
        return null;
    }

    /**
     *
     * @param text the String from the SOAP API xml response
     * @return null -> not access yet to this data
     */
    public static String getDoi(String text, String startLimit, String endLimit) {
        Matcher matcher = getMatcher(text, startLimit, endLimit);

        if (matcher.find()){
            return matcher.group(1);
        }
        return null;
    }

    /**
     * Extract the english and dutch abstracts from a SOAP API response
     *
     * @param startLimit the upper limit to where to find the data
     * @param endLimit the lower limit to where to find the data
     * @param text the String from the SOAP API xml response
     * @return an Abstract object containing the abstracts in english and dutch
     */
    public static Abstract getAbstract(String text, String startLimit, String endLimit){
        Matcher matcher = getMatcher(text, startLimit, endLimit);
        if (matcher.find()){
            return new Abstract(
                    getAbstractId(matcher.group(1)),
                    getDataByLocale(matcher.group(1), "en"),
                    getDataByLocale(matcher.group(1), "nl")
            );
        }
        return null;
    }

    /**
     * Get the UUID from an xml response
     *
     * @param xmlString the String from the SOAP API xml response
     * @return return the UUID
     */
    public static UUID getUUID(String xmlString){
        Matcher matcher = getMatcher(xmlString, "uuid=\"", "\"");
        if (matcher.find()){
            return UUID.fromString(matcher.group(1));
        }
        else return null;
    }

    /**
     * Get required data provider's information

     * @param text the String from the SOAP API xml response
     * @return a DataProvider object containing the required data provider information
     */
    public static DataProvider getDataProvider(String text) {
        return new DataProvider(
                getProviderId(text),
                getProviderName(text)
        );
    }

    /**
     * Get a data provider's name
     *
     * @param text the String from the SOAP API xml response
     * @return return the name of a data provider
     */
    private static String getProviderName(String text) {
        Matcher matcher = getMatcher(text, "<fris:dataProvider>", "</fris:dataProvider>");

        if (matcher.find()){
            return matcher.group(1);
        }
        else return null;
    }

    /**
     * Get a data provider's ID
     *
     * @param text the String from the SOAP API xml response
     * @return return the ID of a data provider
     */
    private static String getProviderId(String text) {
        Matcher matcher = getMatcher(text, "<fris:dataProviderId>", "</fris:dataProviderId>");

        if (matcher.find()){
            return matcher.group(1);
        }
        else return null;
    }

    /**
     * Extract an abstract for a language from a SOAP API response
     *
     * @param text the String from the SOAP API xml response
     * @param locale the language of the abstract needed
     * @return a String with the dutch abstract
     */
    private static String getDataByLocale(String text, String locale) {
        Matcher matcher = getMatcher(text, "fris:text locale=\""+locale+"\">", "</fris:text>");
        if (matcher.find()){
            return matcher.group(1);
        }

        else {
            LOGGER.severe(() -> String.format("No %s abstract found", locale));
            return null;
        }
    }

    /**
     * Extract an abstract's ID from a SOAP API response
     *
     * @param text a String containing the XML response from SOAP
     * @return the int ID of the abstracts
     */
    private static int getAbstractId(String text) {
        Matcher matcher = getMatcher(text, "id=\"", "\"");

        if (matcher.find()){
            return Integer.parseInt(matcher.group(1));
        }

        else{
            LOGGER.severe("No id found");
            return 0;
        }
    }

    /**
     * Create a matcher to use during the data extraction
     *
     * @param text a String containing the XML response from SOAP
     * @param startLimit the upper limit from which we want data to be extracted
     * @param endLimit the lower limit from which we want data to be extracted
     * @return a Matcher
     */
    private static Matcher getMatcher(String text, String startLimit, String endLimit) {
        String regex = Pattern.quote(startLimit) + "(.*?)" + Pattern.quote(endLimit);
        Pattern pattern = Pattern.compile(regex);
        return pattern.matcher(text);
    }
}
