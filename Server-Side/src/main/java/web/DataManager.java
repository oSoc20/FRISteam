package web;

import data.SoapRepository;
import entities.Project;

import java.util.List;

/**
 * WIP
 */
public class DataManager {

    public static List<Project> getProjects(int number){
        return SoapRepository.getProjects(number);
    }
}
