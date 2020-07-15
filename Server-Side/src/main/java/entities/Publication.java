package entities;

import java.util.List;
import java.util.UUID;

/**
 * Publication entity that contains all publication's core data for data analysis
 */
public class Publication {
    private UUID id;
    private List<String> englishKeywords;
    private List<String> dutchKeywords;
    private Abstract projectAbstract;
    private DataProvider dataProvider;
    private Title title;
    private String doi;

    public Publication(){}

    public Publication(UUID id, List<String> englishKeywords, List<String> dutchKeywords, Abstract projectAbstract, DataProvider dataProvider, Title title, String doi) {
        this.id = id;
        this.englishKeywords = englishKeywords;
        this.dutchKeywords = dutchKeywords;
        this.projectAbstract = projectAbstract;
        this.dataProvider = dataProvider;
        this.title = title;
        this.doi = doi;
    }

    public UUID getId() {
        return id;
    }

    public List<String> getEnglishKeywords() {
        return englishKeywords;
    }

    public List<String> getDutchKeywords() {
        return dutchKeywords;
    }

    public Abstract getProjectAbstract() {
        return projectAbstract;
    }

    public DataProvider getDataProvider() {
        return dataProvider;
    }

    public Title getTitle() {
        return title;
    }

    public String getDoi() {
        return doi;
    }

    @Override
    public String toString() {
        return "publication{" +
                "uuid=" + id +
                ", englishKeywords=" + englishKeywords +
                ", dutchKeywords=" + dutchKeywords +
                ", publicationAbstract=" + projectAbstract +
                ", dataProvider=" + dataProvider +
                ", title=" + title +
                ", doi='" + doi + '\'' +
                '}';
    }

    public String toStringCSV(){
        return id +
                "," + title.toStringCSV() +
                "," + separateValuesWithSemicolon(englishKeywords) +
                "," + separateValuesWithSemicolon(dutchKeywords) +
                "," + projectAbstract.toStringCSV() +
                "," + dataProvider.toStringCSV() +
                "," + doi;
    }

    private StringBuilder separateValuesWithSemicolon(List<String> values) {
        StringBuilder result = new StringBuilder();

        values.forEach(v -> result.append(v).append(";"));

        return result;
    }

    public boolean isEmpty() {
        return id == null;
    }
}
