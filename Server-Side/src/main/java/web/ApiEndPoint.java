package web;

import io.vertx.ext.web.Router;

/**
 * Class to create endpoints for a http server
 */
public class ApiEndPoint {
    private final DataRoutes dataRoutes = new DataRoutes();

    /**
     * Create routes for the API
     *
     * @param router a router {@link Router}
     */
    void installRoutes(Router router){

        /*
         * Route to test API responses
         */
        router.get("/api/test").handler(dataRoutes::returnTestResponse);

        /*
         * Get a number N of projects as JSON
         */
        router.get("/api/projects/size/:number").handler(dataRoutes::getProjects);

        /*
         * Get a project from its UUID as JSON
         */
        router.get("/api/projects/:uuid").handler(dataRoutes::getProject);

        /*
         * Get a number N of publications as JSON
         */
        router.get("/api/publications/size/:number").handler(dataRoutes::getPublications);

        /*
         * Get a publication from its UUID as JSON
         */
        router.get("/api/publications/:uuid").handler(dataRoutes::getPublication);

        /*
         * Get a number N of projects as XML
         */
        router.get("/api/projects/xml/size/:number").handler(dataRoutes::getProjectsAsXml);

        /*
         * Get a project from its UUID as XML
         */
        router.get("/api/projects/xml/:uuid").handler(dataRoutes::getProjectAsXml);

        /*
         * Get a number N of publications as XML
         */
        router.get("/api/publications/xml/size/:number").handler(dataRoutes::getPublicationsAsXml);

        /*
         * Get a publication from its UUID as XML
         */
        router.get("/api/publications/xml/:uuid").handler(dataRoutes::getPublicationAsXml);
    }
}
