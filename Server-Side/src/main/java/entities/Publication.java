package entities;

import com.fasterxml.jackson.annotation.JsonIgnore;

import java.util.List;
import java.util.UUID;

/**
 * Publication entity that contains all publication's core data for data analysis
 */
public class Publication {
    private UUID id;
    private List<String> englishKeywords;
    private List<String> dutchKeywords;
    private Abstract publicationAbstract;
    private DataProvider dataProvider;
    private Title title;
    private String doi;

    public Publication(){}

    public Publication(UUID id, List<String> englishKeywords, List<String> dutchKeywords, Abstract publicationAbstract, DataProvider dataProvider, Title title, String doi) {
        this.id = id;
        this.englishKeywords = englishKeywords;
        this.dutchKeywords = dutchKeywords;
        this.publicationAbstract = publicationAbstract;
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

    public Abstract getAbstract() {
        return publicationAbstract;
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
                ", publicationAbstract=" + publicationAbstract +
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
                "," + publicationAbstract.toStringCSV() +
                "," + dataProvider.toStringCSV() +
                "," + doi;
    }

    private StringBuilder separateValuesWithSemicolon(List<String> values) {
        StringBuilder result = new StringBuilder();

        values.forEach(v -> result.append(v).append(";"));

        return result;
    }

    @JsonIgnore
    public boolean isEmpty() {
        return id == null;
    }
}
