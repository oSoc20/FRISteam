package entities;

import java.util.Objects;

/**
 * Title entity that contains english and dutch titles
 */
public class Title {
    private String englishTitle;
    private String dutchTitle;

    public Title(String englishTitle, String dutchTitle) {
        this.englishTitle = englishTitle;
        this.dutchTitle = dutchTitle;
    }

    public String getEnglishTitle() {
        return englishTitle;
    }

    public String getDutchTitle() {
        return dutchTitle;
    }

    @Override
    public String toString() {
        return "Title{" +
                "englishTitle=" + englishTitle +
                ",dutchTitle=" + dutchTitle +
                '}';
    }

    public String toStringCSV() {
        return "\"" + englishTitle + "\"" +
                ",\"" + dutchTitle + "\"";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Title)) return false;
        Title title = (Title) o;
        return Objects.equals(englishTitle, title.englishTitle) &&
                Objects.equals(dutchTitle, title.dutchTitle);
    }

    @Override
    public int hashCode() {
        return Objects.hash(englishTitle, dutchTitle);
    }
}
