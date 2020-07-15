package utils;

import entities.DataProvider;
import entities.Publication;
import entities.Title;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.*;
import java.util.Scanner;

import static org.junit.jupiter.api.Assertions.*;

class PublicationsDataExtractorTest {
    private static final String DIR_NAME = "./src/test/resources/";
    private static final String FILE_NAME = "xml-string-publication-data.txt";
    private Publication publication;

    @BeforeEach
    void setUp() {
        File f = new File(DIR_NAME, FILE_NAME);
        try (Scanner in = new Scanner(new FileInputStream(f))){
            StringBuilder sb = new StringBuilder();
            while (in.hasNextLine()){
                sb.append(in.nextLine());
            }
            publication = PublicationsDataExtractor.getPublicationData(sb.toString()).get(0);

        } catch (FileNotFoundException e) {
            fail(e.getMessage());
        }
    }

    @Test
    void getPublicationData() {
        assertFalse(publication.isEmpty());
    }

    @Test
    void getPublicationUUID(){
        assertEquals("85dbe745-772d-472e-b5fa-3e6d36f966d4", publication.getId().toString());
    }

    @Test
    void getPublicationKeywords(){
        assertTrue(publication.getEnglishKeywords().isEmpty());
        assertTrue(publication.getDutchKeywords().isEmpty());
    }

    @Test
    void getPublicationAbstract(){
        assertNull(publication.getProjectAbstract());
    }

    @Test
    void getPublicationDataProvider(){
        DataProvider dp = new DataProvider("c:irua:157601", "UAntwerpen");
        assertEquals(dp, publication.getDataProvider());
    }

    @Test
    void getPublicationTitle(){
        Title t = new Title("Intervention for reducing epilepsy-associated stigma", null);

        assertEquals(t, publication.getTitle());
    }

    @Test
    void getPublicationDoi(){
        assertNull(publication.getDoi());
    }
}