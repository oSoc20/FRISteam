package utils;

import entities.Abstract;
import entities.DataProvider;
import entities.Project;
import entities.Title;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

import static org.junit.jupiter.api.Assertions.*;

class ProjectDataExtractorTest {
    private static final String DIR_NAME = "./src/test/resources/";
    private static final String FILE_NAME = "xml-string-project-data.txt";
    private Project project;


    @BeforeEach
    void setUp() {
        File f = new File(DIR_NAME, FILE_NAME);
        try (Scanner in = new Scanner(new FileInputStream(f))){
            StringBuilder sb = new StringBuilder();
            while (in.hasNextLine()){
                sb.append(in.nextLine());
            }
            project = ProjectDataExtractor.getProjectData(sb.toString()).get(0);

        } catch (FileNotFoundException e) {
            fail(e.getMessage());
        }
    }

    @Test
    void getProjectData() {
        assertFalse(project.isEmpty());
    }

    @Test
    void getProjectId(){
        assertEquals("6fa0f7de-4502-4995-92ae-5467e49df1b3", project.getId().toString());
    }

    @Test
    void getProjectKeywords(){
        ArrayList<String> englishKeywords = new ArrayList<>();
        englishKeywords.add("Ion channels");
        englishKeywords.add("Positive allosteric modulators");
        englishKeywords.add("Crystallography");

        assertEquals(englishKeywords, project.getEnglishKeywords());
        assertTrue(project.getDutchKeywords().isEmpty());
    }

    @Test
    void getProjectDataProvider(){
        DataProvider dp = new DataProvider("54937891", "KULeuven");

        assertEquals(dp, project.getDataProvider());
    }

    @Test
    void getProjectTitle(){
        Title t = new Title("Structure-based discovery of positive allosteric modulators of the alpha7 nicotinic ecetylcholine receptor as cognition enhancers.", "Structuur-gebaseerde ontwikkeling van positieve allostere modulatoren van de alpha7 nicotine acetylcholine receptor met klinische toepassing als cognitie verbeteraars.");

        assertEquals(t, project.getTitle());
    }

    @Test
    void getProjectAbstract(){
        // abstract formatting issues are solved by data cleaning
        Abstract a = new Abstract(148096734, "", "");

        assertEquals(a, project.getAbstract());
    }
}