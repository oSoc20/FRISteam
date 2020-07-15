package entities;

import java.util.Objects;

/**
 * Abstract entity that contains its id and english and dutch version
 */
public class Abstract {
    private int id;
    private String enAbstract;
    private String nlAbstract;

    public Abstract(int id, String enAbstract, String nlAbstract) {
        this.id = id;
        this.enAbstract = removeUselessCharacters(enAbstract);
        this.nlAbstract = removeUselessCharacters(nlAbstract);
    }

    public int getId() {
        return id;
    }

    public String getEnglishAbstract() {
        return enAbstract;
    }

    public String getDutchAbstract() {
        return nlAbstract;
    }

    @Override
    public String toString() {
        return "Abstract{" +
                "id=" + id +
                ", enAbstract='" + enAbstract + '\'' +
                ", nlAbstract='" + nlAbstract + '\'' +
                '}';
    }

    public String toStringCSV() {
        return id +
                ",\"" + enAbstract + "\"" +
                ",\"" + nlAbstract + "\"";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Abstract)) return false;
        Abstract that = (Abstract) o;
        return id == that.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    private String removeUselessCharacters(String text){

        if (text != null)
            return text.replace("\"", "");
        else return null;
    }
}
