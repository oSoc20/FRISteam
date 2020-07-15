package entities;

import java.util.List;
import java.util.UUID;

/**
 * Project entity that contains all publication's core data for data analysis
 */
public class Project {
    private UUID id;
    private List<String> englishKeywords;
    private List<String> dutchKeywords;
    private Abstract projectAbstract;
    private DataProvider dataProvider;
    private Title title;

    public Project(){}

    public Project(UUID id, Title title, List<String> englishKeywords, List<String> dutchKeywords, Abstract projectAbstract, DataProvider dataProvider) {
        this.id = id;
        this.englishKeywords = englishKeywords;
        this.dutchKeywords = dutchKeywords;
        this.projectAbstract = projectAbstract;
        this.dataProvider = dataProvider;
        this.title = title;
    }

    public UUID getId() {
        return id;
    }

    public Title getTitle() {
        return title;
    }

    public List<String> getEnglishKeywords() {
        return englishKeywords;
    }

    public List<String> getDutchKeywords() {
        return dutchKeywords;
    }

    public Abstract getAbstract() {
        return projectAbstract;
    }

    public DataProvider getDataProvider() {
        return dataProvider;
    }

    public boolean isEmpty(){
        return id == null;
    }

    public String toStringCSV(){
        return id +
                "," + title.toStringCSV() +
                "," + separateValuesWithSemicolon(englishKeywords) +
                "," + separateValuesWithSemicolon(dutchKeywords) +
                "," + projectAbstract.toStringCSV() +
                "," + dataProvider.toStringCSV();
    }

    private StringBuilder separateValuesWithSemicolon(List<String> values) {
        StringBuilder result = new StringBuilder();

        values.forEach(v -> result.append(v).append(";"));

        return result;
    }

    @Override
    public String toString() {
        return "project{" +
                "uuid=" + id +
                "title="+ title +
                ", englishKeywords=" + englishKeywords +
                ", dutchKeywords=" + dutchKeywords +
                ", projectAbstract=" + projectAbstract +
                ", dataProvider='" + dataProvider + '\'' +
                '}';
    }
}
